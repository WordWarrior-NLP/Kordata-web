from pydantic import BaseModel
from typing import List
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

class EventListOut(defaultClass):
    cid : int
    name : List[str]
    datetime: dt.date
    update_datetime : dt.date
    nc_id : int

class EventOut(EventListOut):
    days : int

class MainTitleOut(defaultClass):
    title: str
    nc_id : int
    datetime : dt.date
    nt_id : int
    cid: int

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

## graph node 클래스
class Node:
    def __init__(self, key, level, attributes, end_date):
        self.data = {}
        self.group = 'nodes'
        self.data['level'] = 3 - level
        self.set_id(key, level)
        self.set_attributes(attributes, end_date)

    def set_id(self, key, node_type):
        if node_type == 2:
            id =  f"news_{key}"
        elif node_type == 1:
            id =  f"entity_{key}"
        else :
            id = f"event_{key}"
        self.data['id'] = id

    def set_attributes(self, attributes, end_date):
        if "label" in attributes:
            self.data["label"] = attributes["label"]
        if "cluster" in attributes:
            self.data['cluster'] = attributes["cluster"]
        if "datetime" in attributes:
            self.data['datetime'] = attributes["datetime"]
            if end_date:
                duration = end_date - attributes['datetime']
                self.data['days'] = duration.days
                min_op = 0.3
                op = min(max(round(1 - duration.days / 10, 2), min_op), 1)
                self.data['opacity'] = op

class Edge:
    def __init__(self, key, source, target, attributes=None):
        self.group = 'edges'
        self.data = {}
        self.data['id'] = f"edge_{key}"
        self.data['source'] = source
        self.data['target'] = target
        self.set_attributes(attributes)

    def set_attributes(self, attributes=None):
        if attributes:
            if "polarity" in attributes:
                self.data['polarity'] = attributes["polarity"]


