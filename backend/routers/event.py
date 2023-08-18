from fastapi import APIRouter, Depends, status
from database import get_db
from sqlalchemy import func
from sqlalchemy.orm import Session,joinedload
from internal.crud import *
from model import Event, EventKeyword, NewsMainTitle
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
        for event in events_list:
            name = event.name
            event.name = name.split(",", 2)
    except NoResultFound :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
    finally:
        db.close()
    return events_list


@router.get("/title/list", response_model=List[EventWithMainTitle], status_code=status.HTTP_200_OK)
async def event_list(
        skip: int | None = 0,
        limit: int | None = 10,
        db: Session = Depends(get_db)
):
    try:
        result = db.query(Event, NewsMainTitle) \
            .join(NewsMainTitle, Event.cid == NewsMainTitle.cid) \
            .filter(Event.update_datetime == NewsMainTitle.datetime) \
            .order_by(Event.update_datetime.desc()) \
            .offset(skip).limit(limit).all()

        if result:
            events_title_list = [
                EventWithMainTitle(
                    cid=row.Event.cid,
                    name=row.Event.name.split(",", 2),
                    valid=row.Event.valid,
                    created_at=row.Event.created_at,
                    updated_at=row.Event.updated_at,
                    datetime=row.Event.datetime,
                    update_datetime=row.Event.update_datetime,
                    newest_main_title=row.NewsMainTitle.title
                )
                for row in result
            ]
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
    finally:
        db.close()

    return events_title_list


@router.get("/{cid}/keyword", status_code=status.HTTP_200_OK)
async def event_keyword_list(
        cid : int,
        q: NewsQuery = Depends(),
        db: Session = Depends(get_db)):
    query = get_item_by_column(model=EventKeyword, columns={'cid' : cid}, mode=False, db=db)
    return get_list_of_item(model=EventKeyword, q=q, init_query=query, db=db)

