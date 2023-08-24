from fastapi import status, HTTPException
from sqlalchemy.exc import IntegrityError
from internal.custom_exception import ItemKeyValidationError
from datetime import datetime, time
from typing import Dict, Any
import ast
from internal.schema import Node, Edge
from collections import defaultdict
import datetime as dt


# FILTERING LOGIC CODE 간소화 함수
def filters_by_query(query, model, q):
    for attr, value in q.__dict__.items():
        if value:
            if isinstance(value, str):
                query = query.filter(getattr(model, attr).ilike(f"%{value}%"))
            elif isinstance(value, (int, bool)):
                query = query.filter(getattr(model, attr) == value)
    return query


## 뉴스ID 목록의 STRING을 ID 리스트로 변환
def extract_nid(nid_string : str):
    nid_list = ast.literal_eval(nid_string)
    nid_list = [int(nid) for nid in nid_list]
    return nid_list

# pid(int) -> press_name(str)
def convert_pid(pid : int):
    press_name = {
        32: '경향신문',
        5: '국민일보',
        20 : '동아일보',
        21 : '문화일보',
        81 : '서울신문',
        22 : '세계일보',
        23 : '조선일보',
        25 : '중앙일보',
        28 :'한겨레',
        469 : '한국일보'
    }

    return press_name[pid]

def group_articles(input_data):
#     grouped_articles = defaultdict(list)
#     for article in news_articles:
#         key = (article["main_word"], article["nc_id"])
#         grouped_articles[key].append(article["news"])
#
#
#     # 그룹화된 결과를 원하는 형태로 변환
#     output = []
#     for (main_word, nc_id), articles in grouped_articles.items():
#         eid = next(a["eid"] for a in news_articles if a["main_word"] == main_word and a["nc_id"] == nc_id)
#         datetime = next(a["datetime"] for a in news_articles if a["main_word"] == main_word and a["nc_id"] == nc_id)
#         output.append({
#             "eid": eid,  # 여기서 nid를 어떻게 설정할지에 따라 달라질 수 있습니다.
#             "nc_id": nc_id,
#             "main_word": main_word,
#             "datetime": datetime,
#             "articles": articles
#         })
#     return output

    grouped_output = defaultdict(list)

    for item in input_data:
        nc_id = item["nc_id"]
        eid = item["eid"]
        main_word = item["main_word"]
        datetime = item["datetime"]
        if len(item["sentiments"]) == 1:
            sentiment = item["sentiments"][0]  # Assuming there's only one sentiment in your example
            sentiment_dict = {
                "title": item["news"].title,
                "nid": item["news"].nid,
                "datetime" : item["news"].datetime.date(),
                "polarity": sentiment.polarity,
                "sid": sentiment.sid
            }
        else :
            sentiment_dict = {
                "title": item["news"].title,
                "nid": item["news"].nid,
                "polarity" : None,
                "datetime": item["news"].datetime.date(),
            }
        grouped_output[main_word].append(sentiment_dict)

    final_output = []
    for main_word, article_list in grouped_output.items():
        entry = {
            "eid" : eid,
            "main_word": main_word,
            "datetime": datetime,
            "nc_id": nc_id,
            "article": article_list
        }
        final_output.append(entry)
    return final_output


# 명시적 외래키 값 존재 확인
# 성능 최적화 또는 자세한 오류 처리와 같이 데이터를 삽입하기 전에 외래 키 값의 존재를 확인해야 하는 특정 요구 사항이 있는 경우
def get_referenced_table_and_fk(model):
    referenced_tables = {}
    for column in model.__table__.columns:
        if column.foreign_keys:
            for fk in column.foreign_keys:
                referenced_tables[column.name] = fk.column.table.name
    return referenced_tables


# get the item by primary key
def get_item_by_id(
                   model,
                   index: int,
                   db):
    try:
        item = db.query(model).get(index)
        if not item:
            raise ItemKeyValidationError(detail=("", index))
    finally:
        db.close()
    return item

# get_item_by_column
# column 이름과 value 값을 이용하여 filtering
def get_item_by_column(*,
                       model,
                       columns: Dict[str, Any],
                       mode: bool,
                       db):
    for column_name, value in columns.items() :
        if value:
            if column_name in model.__table__.columns:
                query = db.query(model).filter(getattr(model, column_name) == value)
                query = query.filter(model.valid)
    if mode:
        result = query.all()
    else: result = query
    return result

# GET
def get_list_of_item(*,
                     model,
                     skip: int | None = 0,
                     limit: int | None = 10,
                     q,
                     init_query: Any | None = None,
                     db,
                     ):
    if init_query is None:
        init_query = db.query(model)
    query = filters_by_query(init_query, model, q)
    if hasattr(model, 'update_datetime'):
        query = query.order_by(model.update_datetime.desc())
    elif hasattr(model, 'datetime'):
        query = query.order_by(model.datetime.desc())
    result = query.offset(skip).limit(limit).all()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    db.close()
    return result





