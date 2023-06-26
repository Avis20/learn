
from uuid import UUID

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.sql import text
from sqlalchemy import create_engine
from sqlalchemy.dialects import postgresql

import sqlparse

engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=engine)
session = Session()

stmt = '''
SELECT order_lines.id AS order_lines_id, order_lines.order_id AS order_lines_order_id, order_lines.sku AS order_lines_sku, order_lines.qty AS order_lines_qty 
FROM order_lines, allocations 
WHERE :param_1 = allocations.batch_id AND order_lines.id = allocations.order_line_id
'''

data = {'param_1': 75}


stmt = text(stmt)
stmt = stmt.bindparams(**data)
sql = stmt.compile(dialect=postgresql.dialect(),compile_kwargs={"literal_binds": True})
print(sql)

# print(sqlparse.format(str(sql), reindent=True))


# session.execute(stmt, data)
