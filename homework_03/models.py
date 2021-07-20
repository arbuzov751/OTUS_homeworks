"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
import asyncio
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    func,
    select,
)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import (
    declarative_base,
    relationship,
    joinedload,
    selectinload,
    sessionmaker,
)

SQLALCHEMY_CONN_URI = "postgresql+asyncpg://user:password@localhost/project"
engine = create_async_engine(SQLALCHEMY_CONN_URI, echo=True)
# PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"
# engine = create_async_engine(PG_CONN_URI, echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default="", server_default="")
    username = Column(String, nullable=False, default="", server_default="")
    email = Column(String, nullable=True, default="", server_default="")

    post = relationship("Post", back_populates="user")
    __mapper_args__ = {"eager_defaults": True}

    def __str__(self):
        return f"{self.__class__.__name__}" \
               f"(id={self.id}, name={self.name!r}, username={self.username!r})"

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, default="", server_default="")
    body = Column(String, nullable=False, default="", server_default="")

    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship("User", back_populates="post")

    def __str__(self):
        return f"{self.__class__.__name__}" \
               f"(id={self.id}, name={self.title!r}, parent_id={self.user_id})"

    def __repr__(self):
        return str(self)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def add(users, posts):
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        session: AsyncSession

        async with session.begin():
            for user in users:
                new_user = User(id=user['id'], name=user['name'], username=user['username'], email=user['email'])
                new_user.post = []
                for post in posts:
                    if post['userId'] == user['id']:
                        new_post = Post(id=post['id'], title=post['title'], body=post['body'])
                        new_user.post.append(new_post)
                session.add(new_user)



