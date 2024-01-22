import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

squile_file_name = "../database.sqlite"
# Esta variable nos permite obtener la ruta absoluta de la carpeta donde se encuentra el archivo database.py
base_dir = os.path.dirname(os.path.abspath(__file__))

database_url = f"sqlite:///{os.path.join(base_dir, squile_file_name)}"

engine = create_engine(database_url,echo = True)

Session = sessionmaker(bind=engine)

Base = declarative_base()