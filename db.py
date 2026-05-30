from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from settings import DATABASE_URL


class Model(DeclarativeBase):
    metadata = MetaData(
        naming_convention={
            'ix': 'ix_%(column_0_label)s',
            'uq': 'uq_%(table_name)s_%(column_name)s',
            'ck': 'ck_%(table_name)s_%(constraint_name)s',
            'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s)',
            'pk': 'pk_%(table_name)s',
        }
    )


engine = create_engine(DATABASE_URL, echo=False)


Session = sessionmaker(engine)
def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()