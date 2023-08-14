from pydantic import BaseModel, validator
from typing import List
from custom_exception import InvalidDateFormatError
import datetime

class NewsOut (BaseModel):
    nid : int
    pid : int
    title : str
    main_text : str
    summary : str
    reporter : str
    datetime : datetime.datetime
    section : int
    valid : bool

    class Config:
        orm_mode = True


class EventOut(BaseModel):
    cid : int
    name : str
    datetime: datetime.date
    update_datetime : datetime.date
    nc_id : str
    valid : bool

    class Config:
        orm_mode = True



