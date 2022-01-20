from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from config.log import Logging

load_dotenv()

BASE = declarative_base()
META = MetaData()

LOCAL_DAESHIN_DATABASE = os.environ.get('LOCAL_DAESHIN_DATABASE')
DAESHIN_ENGINE = create_engine(LOCAL_DAESHIN_DATABASE)
DAESHIN_SESSION = sessionmaker(bind=DAESHIN_ENGINE)
