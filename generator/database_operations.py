import sys
from time import sleep

import sqlalchemy
from generate_data import generate_entry
from get_env import PASSWORD, DB, USER
import models


if len(sys.argv) == 3:
    BATCH_SIZE = int(sys.argv[1])
    TIME_INTERVAL = int(sys.argv[2])
else:
    BATCH_SIZE = 100
    TIME_INTERVAL = 5

# https://docs.sqlalchemy.org/en/20/core/engines.html#postgresql
engine = sqlalchemy.create_engine(f"postgresql://{USER}:{PASSWORD}@db:5432/{DB}")
models.Base.metadata.create_all(engine)

with sqlalchemy.orm.Session(engine) as session:
    while True:
        batch = [generate_entry() for _ in range(BATCH_SIZE)]
        session.add_all(batch)
        session.commit()
        print(f"{BATCH_SIZE} entries added!")
        sleep(TIME_INTERVAL)
