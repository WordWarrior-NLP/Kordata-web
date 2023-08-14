from pydantic import BaseModel
from typing import List
from internal.custom_exception import InvalidDateFormatError
import datetime

class defaultClass(BaseModel):
    valid : bool
    created_at : datetime.datetime
    updated_at : datetime.datetime
    class Config:
        from_attributes = True

class NewsOut (defaultClass):
    nid : int
    pid : int
    title : str
    main_text : str
    summary : str
    reporter : str
    datetime : datetime.datetime
    section : int

class NewsQuery :
    def __init__(self,
                 datetime: str | None = None,
                 title: str | None = None,
                 pid: int | None = None,
                 nc_id: int | None = None):
        self.datetime = datetime
        self.title = title
        self.pid = pid
        self.nc_id = nc_id

class EventQuery :
    def __init__(self,
                 name: str | None = None,
                 datetime: str | None = None,
                 update_datetime: str | None = None,
                 ):
        self.datetime = datetime
        self.name = name
        self.updated_datetime = update_datetime

class EventOut(defaultClass):
    cid : int
    name : str
    datetime: datetime.date
    update_datetime : datetime.date
    nc_id : str


