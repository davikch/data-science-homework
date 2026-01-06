import sys
from time import sleep

import sqlalchemy
from generate_data import generate_entry

# https://docs.sqlalchemy.org/en/20/core/engines.html#postgresql
engine = sqlalchemy.create_engine("postgresql://postgres@localhost/taxis", echo=True)

with sqlalchemy.orm.Session(engine) as session:
    if len(sys.argv) < 2:
        BATCH_SIZE = 100
    else:
        BATCH_SIZE = sys.argv[1]

    while True:
        batch = [generate_entry() for _ in range(BATCH_SIZE)]
        session.add_all(batch)
        session.commit()
        sleep(1)
