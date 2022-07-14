from databases import Database
from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    create_engine
)



DATABASE_URL="sqlite:///./blogs.db"

engine=create_engine(DATABASE_URL)
metadata=MetaData()

Article=Table(
    "article",
    metadata,
    Column('id',Integer,primary_key=True),
    Column('title',String(500)),
    Column('description',String(500))
    

)

User=Table(
    "user",
    metadata,
    Column('id',Integer,primary_key=True),
    Column('username',String(100)),
    Column('password',String(100))
    

)

database=Database(DATABASE_URL)
    
    
    
    


