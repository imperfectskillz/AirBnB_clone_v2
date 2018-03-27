#!/usr/bin/python3
"""DB Storage model"""


from sqlalchemy import create_engine


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
            'mysql+mysqldb://{}:{}@HBNB_MYSQL_HOST' .format(
                HBNB_MYSQL_USER,
                HBNB_MYSQL_PWD,
                HBNB_MYSQL_DB),
            pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
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
