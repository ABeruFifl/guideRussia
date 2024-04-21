import sqlalchemy
from flask_login import UserMixin
from .db_session import SqlAlchemyBase


class Route(SqlAlchemyBase, UserMixin):
    __tablename__ = 'routes'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    region = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    duration = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    image = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    info = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    map_api = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def get_list(self):
        return [self.id, self.region, self.title, self.duration, self.image, self.info, self.map_api]
