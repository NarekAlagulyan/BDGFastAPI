import uuid

from fastapi import FastAPI, Depends
from sqlalchemy import select

from sqlalchemy.orm import Session
from models import User, Story, Comment

from typing import List

from db import get_db_session
from serializers import UserCreateSerializer, UserGetSerializer, StoryCreateSerializer, StoryGetSerializer

app = FastAPI()



@app.post('/users', response_model=UserGetSerializer)
def create_user(
        user_data: UserCreateSerializer,
        db_session: Session = Depends(get_db_session)
):
    user = User(
        username=user_data.username,
        password=user_data.password
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    return user


@app.get('/users', response_model=List[UserGetSerializer])
def get_users_list(db_session: Session = Depends(get_db_session)):
    query = (
        select(User)
    )
    users = db_session.scalars(query)

    return users



@app.post('/users/{user_id}/stories', response_model=StoryGetSerializer)
def create_story(
        user_id: int,
        story_data: StoryCreateSerializer,
        db_session: Session = Depends(get_db_session)
):
    story = Story(
        text=story_data.text,
        author_id=user_id,
        music=story_data.music
    )
    db_session.add(story)
    db_session.commit()
    db_session.refresh(story)

    return story



@app.get('/users/{user_id}/stories', response_model=List[StoryGetSerializer])
def get_user_stories_list(
        user_id: int,
        db_session: Session = Depends(get_db_session)
):
    query = (
        select(Story)
        .where(Story.author_id == user_id)
    )
    posts = db_session.scalars(query)
    print(posts)

    return posts