from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from sqlalchemy import func
from sqlalchemy.orm import Session
from internal.crud import *
from model import Event, NewsCluster, News, Entity, Sentiment
from internal.schema import *

router = APIRouter(prefix="/api/graph", tags=["graph"])

@router.get("/{cid}/data", status_code=status.HTTP_200_OK)
async def get_graph_data(
        cid: int,
        db: Session = Depends(get_db)
):
    entity_data = (
        db.query(Entity.eid, Entity.nc_id, Entity.main_word, NewsCluster.cid, func.max(NewsCluster.datetime))
        .join(NewsCluster, Entity.nc_id == NewsCluster.nc_id)
        .filter(NewsCluster.cid == cid)
        .group_by(Entity.main_word)
        .all()
    )
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
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    if entity_data:
        print(entity_data[0])
        for entity in entity_data:
            eid = entity[0]
            nc_id = entity[1]
            main_word = entity[2]
            cid = entity[3]
            datetime = entity[4]
            if main_word not in existed_et:
                existed_et.append(main_word)
                entity_cnt += 1
                entity_attributes = {
                    'label': main_word,
                    'cluster': nc_id,
                    'datetime': datetime,
                }
                entity_node = Node(entity_cnt, 1, entity_attributes, end_date)
                output.append(entity_node)
                entity_key = entity_node.data['id']
                edge_id += 1
                entity_to_event = Edge(edge_id, entity_key, output[0].data['id'])
                output.append(entity_to_event)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    if news_data:
        for news in news_data:
            if news[1] not in existed_nw:
                existed_nw.append(news[1])
                news_cnt += 1
                news_attributes = {
                    'label': news[0][:10].replace('"', '') + "...",
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
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    return output
