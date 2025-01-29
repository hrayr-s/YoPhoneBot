from pydantic.dataclasses import dataclass
from typing import List, Optional

from structures.base import BaseResponseStructure
from structures.common import Sender


@dataclass
class UpdateData(object):
    id: int
    chatId: str
    text: str
    sender: Sender


@dataclass
class UpdatesResponse(BaseResponseStructure):
    data: Optional[List[UpdateData]] = None
    text: Optional[str] = None
