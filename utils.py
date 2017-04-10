from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def establish_database_connection(db_name):
    """Setup database connection and sqlalchemy interface."""
    db_url = 'mysql+mysqldb://root:password@localhost/' + db_name
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    return engine, Session
