from fastapi import APIRouter, Depends, status
from database import get_db
from sqlalchemy.orm import Session
from internal.crud import *
from model import News
from internal.schema import *
from typing import List

router = APIRouter(prefix="/api/news", tags=["news"])

@router.get("/list", response_model=List[NewsOut], status_code=status.HTTP_200_OK)
async def get_all_news_list(
        skip: int | None = 0,
        limit: int | None = 10,
        q: NewsQuery = Depends(),
        db: Session = Depends(get_db)):
    return get_list_of_item(model=News, db=db, q=q,skip=skip, limit=limit,)


@router.get("/{nc_id}/list", response_model=List[NewsOut], status_code=status.HTTP_200_OK)
async def get_news_list(
        nc_id : int,
        skip: int | None = 0,
        limit: int | None = 10,
        q: NewsQuery = Depends(),
        db: Session = Depends(get_db)):
    q.nc_id = nc_id
    return get_list_of_item(model=News, db=db, q=q, skip=skip, limit=limit)



