import re
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from fastapi.exceptions import HTTPException
from typing import List, Any
from app.database import db_conn
from app.database.model import error_log


class SqlAlchemyOrm:
    def __init__(self):
        self._engine = db_conn.DBConn()
        self._db = self._engine.session_maker()
        self._get_engine = self._engine.get_engine()

    async def use_orm(self,
                                 selected_tags: [],
                                 tags_type: str
                                 ):
        if selected_tags is None:
            return False
        try:
            tb_rationale_map = error_log.ErrorLog
            selected_house = self._db.query(tb_rationale_map).filter(tb_rationale_map.clientIp.in_(selected_tags)) \
                .filter(tb_rationale_map.errorUrl == tags_type) \
                .all()

            response = []
            pattern = r'[\\,"]'
            for res in selected_house:
                display_message = re.sub(pattern, '', res.displayMessage)
                res.displayMessage = display_message
                response.append(res)

            return selected_house
        except SQLAlchemyError as e:
            raise HTTPException(500, "db connection error")
        except Exception as e:
            raise HTTPException(500, e.__class__.__name__)

    async def use_text_query(self, recommend_danji_list: [], recommend_pyeong_list: []):
        danji_list_string = ','.join(str(element) for element in recommend_danji_list)
        pyeong_list_string = ','.join(str(element) for element in recommend_pyeong_list)
        try:
            with self._get_engine.connect() as connection:
                query = f"""
                select * from recommend_rationale where `단지코드` in ({danji_list_string}) and `평형코드` in ({pyeong_list_string})
                """
                result = connection.execute(text(query))
                rows = result.fetchall()
                keys = result.keys()
                dict_result = [dict(zip(keys, row)) for row in rows]
                result.close()
                return dict_result
        except SQLAlchemyError as e:
            raise HTTPException(500, "db connection error")
        except Exception as e:
            raise HTTPException(500, e.__class__.__name__)

