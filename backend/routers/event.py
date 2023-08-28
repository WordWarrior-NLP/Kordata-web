from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from sqlalchemy.orm import Session,joinedload,load_only
from internal.crud import *
from model import Event, NewsMainTitle, NewsCluster, News
from internal.schema import *
from typing import List

router = APIRouter(prefix="/api/events", tags=["event"])

@router.get("/list", response_model=List[EventListOut], status_code=status.HTTP_200_OK)
async def get_event_list(
    skip: int | None = 0,
    limit: int | None = 25,
    q : EventQuery = Depends(),
    db: Session = Depends(get_db)
):
    try:
        events_list = get_list_of_item(model=Event, db=db, skip=skip, limit=limit, q=q)
        if events_list :
            for event in events_list:
                event.name = event.name.split(",", 2)

        else :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal server error : {e}")
    finally:
        db.close()
    return events_list

@router.get("/{cid}", response_model=EventOut, status_code=status.HTTP_200_OK)
async def get_event_list(
    cid : int,
    db: Session = Depends(get_db)
):
    try:
        event_data = get_item_by_id(model=Event, db=db, index=cid)
        if event_data:
            event_data.name = event_data.name.split(",", 2)
            result_dict = event_data.__dict__
            duration = event_data.update_datetime - event_data.datetime
            result_dict['days'] = duration.days
        else :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal server error : {e}")
    finally:
        db.close()
    return result_dict


@router.get("/{cid}/with_title", response_model=EventWithMainTitle, status_code=status.HTTP_200_OK)
async def event_list(
        cid : int,
        db: Session = Depends(get_db)
):
    try:
        result = db.query(Event) \
            .options(joinedload(Event.main_titles).load_only(NewsMainTitle.title, NewsMainTitle.nc_id, NewsMainTitle.datetime))\
            .filter(Event.cid == cid) \
            .options(load_only(Event.nc_id, Event.update_datetime, Event.datetime, Event.cid, Event.name)) \
            .first()
        if result:
            result.name = result.name.split(",", 2)
            result_dict = result.__dict__
            duration = result.update_datetime - result.datetime
            result_dict['days'] = duration.days

            return result_dict
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal server error:{e}")
    finally:
        db.close()


@router.get("/{cid}/main_title", response_model=List[MainTitleOut], status_code=status.HTTP_200_OK)
async def event_list(
        cid : int,
        db: Session = Depends(get_db)
):
    try:
        result = db.query(NewsMainTitle) \
            .filter(NewsMainTitle.cid == cid) \
            .options(load_only(NewsMainTitle.nc_id, NewsMainTitle.title, NewsMainTitle.datetime, NewsMainTitle.cid)) \
            .all()
        if result:
            return result
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal server error:{e}")
    finally:
        db.close()

# Event ID로 뉴스 조회
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
                for news in event["news"]:
                    news.pid = convert_pid(news.pid)
            return events_news_list
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal server error : {str(e)}")
    finally:
        db.close()


