from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Sequence, String, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///localdb/todo_dev.db', echo=True)

Session = sessionmaker(bind=engine)
Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    name = Column(String(50))
    comments = relationship('Comment', back_populates='todo')

    def __repr__(self):
        return "<Todo ('%d', '%s')>" % (self.id, self.name)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def save(self):
        session = Session()
        session.add(self)
        session.commit()

    @classmethod
    def get_one(cls, id):
        session = Session()
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        session = Session()
        return session.query(cls).filter_by().all()

    @classmethod
    def put_one(cls, id, delta_payload):
        todo = cls.get_one(id)
        if todo:
            todo.name = delta_payload.get('name')
            todo.save()
        return todo

    @classmethod
    def post_one(cls, payload):
        todo = Todo()
        todo.name = payload.get('name')
        todo.save()
        return todo


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    message = Column(Text)
    todo_id = Column(Integer, ForeignKey('todos.id'))
    todo = relationship('Todo', back_populates='comments')

    def __repr__(self):
        return "<Comment ('%d', '%d', '%s')>" % (self.id, self.todo_id, self.message)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def save(self):
        session = Session()
        session.add(self)
        session.commit()
