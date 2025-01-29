from pydantic.dataclasses import dataclass
from typing import Any, Optional


@dataclass
class BaseResponseStructure(object):
    code: int
    success: bool
    text: Optional[str]
    data: Any
