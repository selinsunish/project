from sqlalchemy import create_engine
from sqlalchemy import sessionmaker,declarative_base
DATABASE_URL="sqlite:///./uploaded_files.db"
engine=create_engine(DATABASE_URL,connect_args={"check-same-thread":False})
sessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base=declarative_base()
