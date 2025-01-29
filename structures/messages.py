from pydantic.dataclasses import dataclass

from structures.base import BaseResponseStructure
from structures.common import Sender


@dataclass
class Message(object):
    to: str
    text: str


@dataclass
class SendMessageData(object):
    id: int
    chatId: str
    sender: Sender
    text: str


@dataclass
class SendMessageResponse(BaseResponseStructure):
    data: SendMessageData
