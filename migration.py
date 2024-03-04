import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load env variables
load_dotenv()

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

candidates = pd.read_csv("data/sample.csv")

# create connection to the db
candidates_connection = create_engine(
    f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
)

# export the dataframe to the db
candidates.to_sql("candidates", candidates_connection, if_exists="replace", index=False)
