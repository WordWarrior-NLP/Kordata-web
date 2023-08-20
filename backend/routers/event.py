from fastapi import APIRouter, Depends, status
from database import get_db
from sqlalchemy.orm import Session,joinedload,load_only
from internal.crud import *
from model import Event, NewsMainTitle, NewsCluster, News
from internal.schema import *

router = APIRouter(prefix="/api/events", tags=["event"])

@router.get("/list", response_model=List[EventOut], status_code=status.HTTP_200_OK)
async def get_event_list(
    skip: int | None = 0,
    limit: int | None = 10,
    q : EventQuery = Depends(),
    db: Session = Depends(get_db)
):
    try:
        events_list = get_list_of_item(model=Event, db=db, skip=skip, limit=limit, q=q)
        if events_list :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        for event in events_list:
            event.name = event.name.split(",", 2)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal server error : {e}")
    finally:
        db.close()
    return events_list


@router.get("/with_title", response_model=List[EventWithMainTitle], status_code=status.HTTP_200_OK)
async def event_list(
        skip: int | None = 0,
        limit: int | None = 10,
        db: Session = Depends(get_db)
):
    try:
        result = db.query(Event) \
            .options(joinedload(Event.main_titles)
                     .load_only(NewsMainTitle.title, NewsMainTitle.nc_id, NewsMainTitle.datetime, )) \
            .order_by(Event.update_datetime.desc()) \
            .all()

        if result:
            events_title_list = [res._asdict() for res in result]
            for event in events_title_list:
                event["name"] = event["name"].split(",", 2)
            return events_title_list
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal server error : {e}")
    finally:
        db.close()

# Event ID로 뉴스 조회
# TODO q 없으면 전체 클러스터 기사 조회
#   q에 nc_id, datetime로 뉴스 클러스터 노드 클릭시 해당 클러스터에 속한 기사만 select
@router.get("/{cid}/news/", response_model=List[EventWithNews], status_code=status.HTTP_200_OK)
async def get_cluster_list(
        cid : int,
        db: Session = Depends(get_db)):
    try:
        results = db.query(NewsCluster) \
            .options(joinedload(NewsCluster.news)
                     .load_only(News.title, News.linkUrl, News.pid,))\
            .filter(NewsCluster.cid == cid) \
            .options(load_only(NewsCluster.nc_id, NewsCluster.rank, NewsCluster.datetime, NewsCluster.cid)) \
            .order_by(NewsCluster.datetime.desc())\
            .all()
        if results:
            events_news_list = [res.__dict__ for res in results]
            for event in events_news_list:
                for news in  event["news"]:
                    news.pid = convert_pid(news.pid)
            return events_news_list
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal server error : {e}")
    finally:
        db.close()


