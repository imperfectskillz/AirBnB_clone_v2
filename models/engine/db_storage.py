#!/usr/bin/python3
"""DB Storage model"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Database storage

    Attributes:
            __engine: home base for the DB and its DBAPI
            __session: session of db-object interaction
    """
    __engine = None
    __session = None

    def __init__(self):
        """Constructor method"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                HBNB_MYSQL_USER,
                HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST,
                HBNB_MYSQL_DB),
            pool_pre_ping=True)
        if os.environ['HBNB_ENV'] == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects given a class name (if no class name, all objs)"""
        result = {}
        if cls:
            cls_objs = self.__session.query(cls).all()
        else:
            cls_objs = self.__session.query(User, State, City,
                                            Amenity, Place, Review).all()
        for obj in cls_objs:
            key = obj.__class__.__name__ + '.' + obj.id
            result[key] = obj
        return result

        def new(self, obj):
            """Add obj to current db session"""
            if obj:
                self.__session.add(obj)

        def save(self):
            """Commits changes to current db session"""
            self.__session.commit()

        def delete(self, obj=None):
            """Deletes obj from current db session"""
            if obj:
                self.__session.delete(obj)

        def reload(self):
            """Creates db session and creates all tables in db"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker
                                 (bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
