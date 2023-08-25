from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from sqlalchemy.orm import Session,joinedload,load_only
from internal.crud import *
from model import Event, NewsCluster, News, Entity, Sentiment
from internal.schema import *

# TODO : GRAPH DATA
#    event - [clsuter] -news(entity 없음) - entity - news(있음) - sentiment
router = APIRouter(prefix="/api/graph", tags=["graph"])


@router.get("/{cid}/data", status_code=status.HTTP_200_OK)
async def get_graph_data(
        cid: int,
        db: Session = Depends(get_db)
):
    nc_ids = db.query(NewsCluster.nc_id).filter_by(cid=cid).all()
    nc_ids = [nc_id[0] for nc_id in nc_ids]
    news_data = db.query(News.title, News.nid, News.nc_id, News.datetime, Entity.main_word, Entity.datetime, Sentiment.polarity) \
        .join(Entity, (News.nid == Entity.nid)) \
        .outerjoin(Sentiment, (News.nid == Sentiment.nid)) \
        .filter(News.nc_id.in_(nc_ids)) \
        .all()

    output = []
    existed_nw = []
    existed_et = []
    edge_id = 0
    entity_cnt = -1
    news_cnt = -1

    event = get_item_by_id(Event,cid, db)
    end_date = event.update_datetime

    if event:
        event_attributes = {
            'label' : event.name,
        }
        event_node = Node(event.cid, 0, event_attributes, end_date)
        output.append(event_node)

    if news_data:
        for news in news_data:
            main_word = news[4]
            if main_word not in existed_et:
                existed_et.append(main_word)
                entity_cnt += 1
                entity_attributes = {
                    'label': main_word,
                    'cluster': news[2],
                    'datetime': news[5],
                }

                entity_node = Node(entity_cnt, 1, entity_attributes, end_date)
                output.append(entity_node)
                entity_key = entity_node.data['id']
                edge_id += 1
                entity_to_event = Edge(edge_id, entity_key, output[0].data['id'])
                output.append(entity_to_event)

    if news_data:
        for news in news_data:
            if news[1] not in existed_nw:
                existed_nw.append(news[1])
                news_cnt += 1
                news_attributes = {
                    'label': news[0].replace('"', '') + "...",
                    'cluster' : news[2],
                    'datetime': news[3].date(),
                }
                news_node = Node(news_cnt, 2, news_attributes, end_date)

                source = news_node.data['id']
                output.append(news_node)
            else :
                source = 'news_' + str(existed_nw.index(news[1]))
            news_to_entity_attr = {
                'polarity': news[6]
            }
            edge_id += 1
            target = "entity_" + str(existed_et.index(news[4]))
            news_to_entity = Edge(edge_id, source, target, news_to_entity_attr)
            output.append(news_to_entity)
    return output
