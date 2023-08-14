from fastapi import APIRouter, Depends, status
from database import get_db
from sqlalchemy.orm import Session
from internal.crud import *
from model import News
from internal.schema import *

router = APIRouter(prefix="/api/news", tags=["news"])

@router.get("/list", response_model=List[dict], status_code=status.HTTP_200_OK)
async def news_list(
        # skip: int | None = 0,
        # limit: int | None = 10,
        q: NewsQuery = Depends(), db: Session = Depends(get_db)):
    return get_list_of_item(model=News, db=db, q=q)


