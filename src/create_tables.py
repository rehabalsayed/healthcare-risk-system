from database.database import engine
from database.models import Prediction
from database.database import Base
import database.models  

Base.metadata.create_all(bind=engine)

print("Tables created successfully")