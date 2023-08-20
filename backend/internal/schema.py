from pydantic import BaseModel
from typing import List
from internal.custom_exception import InvalidDateFormatError
import datetime as dt

class defaultClass(BaseModel):
    class Config:
        from_attributes = True

class NewsOut (defaultClass):
    nid : int
    pid : int
    title : str
    summary : str
    reporter : str | None
    datetime : dt.datetime
    nc_id : int | None
    linkUrl : str

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
    name : List[str]
    datetime: dt.date
    update_datetime : dt.date
    nc_id : int

class MainTitleOut(defaultClass):
    title: str
    nc_id : int
    datetime : dt.date
    nt_id : int

class EventWithMainTitle(EventOut):
    main_titles : List[MainTitleOut]


class ClusterOut(defaultClass):
    cid : int
    nc_id : int
    datetime : dt.date
    rank : int

class NewsSidebar (defaultClass):
    nid: int
    pid: str
    title: str
    linkUrl : str

class EventWithNews(ClusterOut):
    news : List[NewsSidebar]