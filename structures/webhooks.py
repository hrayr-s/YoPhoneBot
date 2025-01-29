from typing import Optional, Dict

from pydantic.dataclasses import dataclass

from structures.base import BaseResponseStructure


@dataclass
class SetWebhookResponse(BaseResponseStructure):
    data: Optional[Dict] = None
    message: Optional[str] = None


@dataclass
class WebhookRequest(object):
    webhookURL: str
