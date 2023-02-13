from logging.config import fileConfig
from sqlalchemy import engine_from_config
from app.Model.user_model import User
from app.Model.entry_model import Entry
from app.Model.competition_model import Competition
from app.database.database import Base
from sqlalchemy import pool
import os 
from dotenv import load_dotenv
from alembic import context

load_dotenv()

$(SQLALCHEMY_URL)s

#read .env file for alembic.ini
section = config.config_ini_section
DRIVER = os.getenv("DB_DRIVER")
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DATABASE = os.getenv("DB_DATABASE")
SQLALCHEMY_URL = f"{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
config.set_section_option(section, "sqlalchemy.url", SQLALCHEMY_URL)