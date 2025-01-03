from app.database.connection import Base, engine
from app.database.models import Document

if __name__ == "__main__":
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created!")