import sys
from time import sleep

import sqlalchemy
from generate_data import generate_entry
from get_env import PASSWORD, DB, USER
import models


if len(sys.argv) < 2:
    BATCH_SIZE = 100
else:
    BATCH_SIZE = int(sys.argv[1])

# https://docs.sqlalchemy.org/en/20/core/engines.html#postgresql
engine = sqlalchemy.create_engine(
    f"postgresql://{USER}:{PASSWORD}@localhost/{DB}"
)
models.Base.metadata.create_all(engine)

with sqlalchemy.orm.Session(engine) as session:
    while True:
        batch = [generate_entry() for _ in range(BATCH_SIZE)]
        session.add_all(batch)
        session.commit()
        sleep(1)
