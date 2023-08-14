from fastapi import APIRouter, Depends, status
from database import get_db
from sqlalchemy.orm import Session
from internal.crud import *
from model import Event, EventKeyword
from internal.schema import *

router = APIRouter(prefix="/api/events", tags=["event"])

@router.get("/list", response_model=List[EventOut], status_code=status.HTTP_200_OK)
async def event_list(
        # skip: int | None = 0,
        # limit: int | None = 10,
        q: EventQuery = Depends(), db: Session = Depends(get_db)):
    return get_list_of_item(model=Event, db=db, q=q)

@router.get("/{cid}/keyword", status_code=status.HTTP_200_OK)
async def event_keyword_list(
        cid : int,
        skip: int | None = 0,
        limit: int | None = 10,
        q: NewsQuery = Depends(),
        db: Session = Depends(get_db)):
    query = get_item_by_column(model=EventKeyword, columns={'cid':cid}, mode=False, db=db)
    return get_list_of_item(model=EventKeyword, q=q, init_query=query, db=db)