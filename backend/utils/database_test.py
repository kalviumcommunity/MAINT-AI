import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))

with engine.connect() as connection:
    result = connection.execute(text("SELECT current_database(), version();"))
    row = result.fetchone()

    print("Database:", row[0])
    print("Connection successful!")