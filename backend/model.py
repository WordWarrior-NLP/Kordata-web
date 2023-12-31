from sqlalchemy import Column, Text, Integer, Boolean, String, TIMESTAMP, Date, DateTime, DECIMAL, SmallInteger
from sqlalchemy import text, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Entity(Base):
    __tablename__ = "entity"
    eid = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    word = Column(String(30), nullable=False)
    label = Column(String(30), nullable=False)
    desc = Column(String(20), nullable=False)
    main_word = Column(String(30), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    nc_id = Column(Integer, ForeignKey('news_cluster.nc_id'), nullable=False)
    nid = Column(Integer, ForeignKey('news.nid'), nullable=False)
    valid = Column(Boolean, nullable=False, default=1)
    datetime = Column(Date, nullable=False)



class Event(Base):
    __tablename__ = "event"
    cid = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    valid = Column(Boolean, nullable=False, default=1)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    nc_id = Column(Integer, nullable=False)
    datetime = Column(Date, nullable=False)
    update_datetime = Column(Date, nullable=True)



class News(Base):
    __tablename__ = "news"
    nid = Column(Integer, nullable=False, primary_key=True)
    pid = Column(Integer, nullable=False)
    title = Column(Text, nullable=False)
    linkUrl = Column(Text, nullable=False)
    section = Column(SmallInteger, nullable=True, default=100)
    main_text = Column(Text, nullable=False)
    pre_main_text = Column(Text, nullable=False)
    summary = Column(Text, nullable=False)
    reporter = Column(String(30), nullable=True)
    datetime = Column(DateTime, nullable=False)
    strtime = Column(String(30), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    valid = Column(Boolean, nullable=False, default=1)
    photo = Column(Boolean, nullable=True)
    nc_id = Column(Integer, ForeignKey('news_cluster.nc_id'), nullable=True)
    pre_title = Column(Text, nullable=False)




class NewsCluster(Base):
    __tablename__ = "news_cluster"
    nc_id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    datetime = Column(Date, nullable=False)
    rank = Column(Integer, nullable=False)
    cid = Column(Integer, ForeignKey('event.cid'), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    valid = Column(Boolean, nullable=False, default=1)
    nid = Column(Text, nullable=False)


class ClusterKeyword(Base):
    __tablename__ = "cluster_keyword"
    ck_id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    keyword = Column(String(30), nullable=False)
    nc_id = Column(Integer, ForeignKey('news_cluster.nc_id'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False,
                        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    valid = Column(Boolean, nullable=False, default=1)

class NewsMainTitle(Base):
    __tablename__ = "news_main_title"
    nt_id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    title = Column(Text, nullable=False)
    nc_id = Column(Integer, ForeignKey('news_cluster.nc_id'), nullable=False)
    cid = Column(Integer, ForeignKey('event.cid'), nullable=True)
    datetime = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    valid = Column(Boolean, nullable=False, default=1)


class NewsSocial(Base):
    __tablename__ = "news_social"
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
    # nc_id = Column(Integer, ForeignKey('news_cluster.nc_id'), nullable=True)
    nc_id = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    valid = Column(Boolean, nullable=False, default=1)

class Sentiment(Base):
    __tablename__ = 'sentiment'
    sid = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    polarity = Column(DECIMAL, nullable=False)
    eid = Column(Integer, ForeignKey('entity.eid'))  # set not null
    nid = Column(Integer, ForeignKey('news.nid'))    # set not null
    nc_id = Column(Integer, ForeignKey('news_cluster.nc_id'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False,
                        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    valid = Column(Boolean, nullable=False, default=1)
    datetime = Column(Date, nullable=False)


class Sentence(Base):
    __tablename__ = 'sentence'
    sentence_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    polarity = Column(DECIMAL, nullable=False)
    eid = Column(Integer, ForeignKey('entity.eid'))  # set not null
    nid = Column(Integer, ForeignKey('news.nid'))    # set not null
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False,
                        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    valid = Column(Boolean, nullable=False, default=1)
    datetime = Column(Date, nullable=False)



Entity.sentiments = relationship("Sentiment", back_populates="entity")
Entity.news= relationship("News", back_populates="entity")
Entity.news_cluster = relationship("NewsCluster", back_populates="entity")

News.news_cluster = relationship("NewsCluster", back_populates="news")
News.entity = relationship("Entity", back_populates="news")

NewsCluster.news = relationship("News", back_populates="news_cluster", order_by='news.columns.datetime.desc()')
NewsCluster.event = relationship("Event", back_populates="news_cluster")
NewsCluster.entity = relationship("Entity", back_populates="news_cluster")


Event.main_titles = relationship("NewsMainTitle", backref="event", order_by='news_main_title.columns.datetime.desc()')
Event.news_cluster = relationship("NewsCluster", back_populates="event")

Sentiment.entity = relationship("Entity", back_populates="sentiments")