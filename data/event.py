import sqlalchemy
from .db_session import SqlAlchemyBase


class Event(SqlAlchemyBase):
    __tablename__ = 'events'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    region = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    image = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    info = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def get_list(self):
        return [self.id, self.region, self.title, self.address, self.image, self.info]
