from sqlalchemy import Column, Text, Integer, Boolean, String, TIMESTAMP, Date, DateTime, DECIMAL, SmallInteger
from sqlalchemy import text, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Entity(Base):
    __tablename__ = "Entity"
    eid = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(30), nullable=False)
    label = Column(String(30), nullable=False)
    desc = Column(String(30), nullable=False)
    main_word = Column(Boolean, nullable=True, default=0)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    nc_id = Column(Integer, ForeignKey('NewsCluster.nc_id'), nullable=False)
    valid = Column(Boolean, nullable=False, default=1)
class Event(Base):
    __tablename__ = "Event"
    cid = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    valid = Column(Boolean, nullable=False, default=1)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    nc_id = Column(Text, nullable=False)

class EventKeyword(Base):
    __tablename__ = "EventKeyword"
    ck_id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    keyword = Column(String(20), nullable=False)
    cid = Column(Integer, ForeignKey('Event.cid'), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    valid = Column(Boolean, nullable=False, default=1)

class News(Base):
    __tablename__ = "News"
    nid = Column(Integer, nullable=False, primary_key=True)
    pid = Column(Integer, nullable=False)
    title = Column(Text, nullable=False)
    linkUrl = Column(Text, nullable=False)
    section = Column(SmallInteger, nullable=True, default=100)
    main_text = Column(Text, nullable=False)
    pre_main_text = Column(Text, nullable=False)
    summary = Column(Text, nullable=False)
    reporter = Column(String(30), nullable=True)
    datetime = Column(TIMESTAMP, nullable=False)
    strtime = Column(String(30), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    valid = Column(Boolean, nullable=False, default=1)
    photo = Column(Boolean, nullable=True)
    nc_id = Column(Integer, ForeignKey('NewsCluster.nc_id'), nullable=True)
    pre_title = Column(Text, nullable=False)

class NewsCluster(Base):
    __tablename__ = "NewsCluster"
    nc_id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    datetime = Column(DateTime, nullable=False)
    rank = Column(Integer, nullable=False)
    cid = Column(Integer, ForeignKey('Event.cid'), nullable=True)
    keyword = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    valid = Column(Boolean, nullable=False, default=1)

class NewsMainTitle(Base):
    __tablename__ = "NewsMainTitle"
    nt_id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    title = Column(Text, nullable=False)
    nc_id = Column(Integer, ForeignKey('NewsCluster.nc_id'), nullable=False)
    cid = Column(Integer, ForeignKey('Event.cid'), nullable=True)
    datetime = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    valid = Column(Boolean, nullable=False, default=1)


class NewsSocial(Base):
    __tablename__ = "NewsSocial"
    nid = Column(Integer, nullable=False, primary_key=True)
    pid = Column(Integer, nullable=False)
    title = Column(Text, nullable=False)
    linkUrl = Column(Text, nullable=False)
    section = Column(SmallInteger, nullable=True, default=102)
    main_text = Column(Text, nullable=False)
    pre_main_text = Column(Text, nullable=False)
    summary = Column(Text, nullable=False)
    reporter = Column(String(30), nullable=True)
    datetime = Column(TIMESTAMP, nullable=False)
    strtime = Column(String(30), nullable=False)
    photo = Column(Boolean, nullable=True)
    nc_id = Column(Integer, ForeignKey('NewsCluster.nc_id'), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    valid = Column(Boolean, nullable=False, default=1)

class Sentiment(Base):
    __tablename__ = 'Sentiment'
    sid = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    polarity = Column(DECIMAL, nullable=False)
    eid = Column(Integer, ForeignKey('Entity.eid'), nullable=False)
    nid = Column(Integer, ForeignKey('News.nid'), nullable=True)
    nc_id = Column(Integer, ForeignKey('NewsCluster.nc_id'), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False,
                        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    valid = Column(Boolean, nullable=False, default=1)

class Sentence(Base):
    __tablename__ = 'Sentence'
    sentence_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    polarity = Column(DECIMAL, nullable=False)
    eid = Column(Integer, ForeignKey('Entity.eid'), nullable=False)
    nid = Column(Integer, ForeignKey('News.nid'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False,
                        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    valid = Column(Boolean, nullable=False, default=1)
# ---------------------------------------------------------------------------------------