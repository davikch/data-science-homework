import os
from dotenv import load_dotenv

load_dotenv(".env")

PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB = os.getenv("POSTGRES_DB")
USER = os.getenv("POSTGRES_USER", "postgres")
