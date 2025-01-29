from typing import Optional

from pydantic.dataclasses import dataclass


@dataclass
class Sender(object):
    id: str
    firstName: str
    lastName: str
    isBot: bool = False
    chanelId: Optional[str] = None
