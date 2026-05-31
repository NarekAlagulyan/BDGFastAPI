from pydantic import BaseModel as BaseSerializer


class UserCreateSerializer(BaseSerializer):
    username: str
    password: str


class UserGetSerializer(BaseSerializer):
    id: int
    username: str

    class Config:
        from_attributes = True


class StoryCreateSerializer(BaseSerializer):
    text: str
    music: str | None = None


class StoryGetSerializer(BaseSerializer):
    id: int
    text: str
    author_id: int

    class Config:
        from_attributes = True


class CommentCreateSerializer(BaseSerializer):
    text: str
    author_id: int
    post_id: int


class CommentGetSerializer(BaseSerializer):
    id: int
    text: str
    author_id: int
    post_id: int

    class Config:
        from_attributes = True
