from datetime import datetime
from typing import List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Model


class User(Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str]

    # Relationships
    stories: Mapped[List["Story"]] = relationship(back_populates="author")
    comments: Mapped[List["Comment"]] = relationship(back_populates="author")


class Story(Model):
    __tablename__ = "stories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    text: Mapped[str]
    date: Mapped[datetime] = mapped_column(default=datetime.now, index=True)
    music: Mapped[str | None]

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    # Relationships
    author: Mapped["User"] = relationship(back_populates="stories")
    comments: Mapped[List["Comment"]] = relationship(back_populates="story")


class Comment(Model):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    text: Mapped[str]
    date: Mapped[datetime] = mapped_column(default=datetime.now, index=True)

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    story_id: Mapped[int] = mapped_column(ForeignKey("stories.id"))

    # Adding back-populates to match User and Story expectations
    author: Mapped["User"] = relationship(back_populates="comments")
    story: Mapped["Story"] = relationship(back_populates="comments")