import time
from typing import Iterator, Optional

import requests
from pydantic import TypeAdapter

from config import Config
from structures.messages import Message, SendMessageResponse
from structures.webhooks import SetWebhookResponse, WebhookRequest

from structures.updates import UpdatesResponse, UpdateData


class YoBot(object):
    """
    curl -X POST "https://yoai.yophone.com/api/pub/getUpdates" \
      -H "Content-Type: application/json" \
      -H "X-YoAI-API-Key: your YoAI api key" \
      -d '{}'
    """

    def get_client(self):
        if self._client:
            return self._client

        self._client = requests.Session()
        return self._client

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'X-YoAI-API-Key': self.token
        }

    def request(self, method, command, *args, **kwargs):
        kwargs.setdefault("allow_redirects", True)
        url = Config.BASE_API_URL + command
        kwargs.setdefault('headers', {})
        kwargs['headers'].update(self.get_headers())
        return self.get_client().request(method, url, *args, **kwargs)

    def __init__(self, token: str, debug: bool = False):
        self._client = None
        self.token = token
        self.debug = debug

    def get_updates(self) -> UpdatesResponse:
        result = self.request('get', self.get_updates.command)
        return TypeAdapter(UpdatesResponse).validate_json(result.text)

    get_updates.command = '/getUpdates'

    def send_message(self, message: Message) -> SendMessageResponse:
        result = self.request('post', self.send_message.command, data=message.__dict__)
        return TypeAdapter(SendMessageResponse).validate_json(result.text)

    send_message.command = '/sendMessage'

    def set_webhook(self, url) -> SetWebhookResponse:
        result = self.request('post', self.set_webhook.command, data=WebhookRequest(webhookURL=url).__dict__)
        if result.headers.get('Content-Type') != 'application/json':
            return SetWebhookResponse(
                code=result.status_code,
                text=result.text,
                success=False,
            )
        return TypeAdapter(SetWebhookResponse).validate_json(result.text)

    set_webhook.command = '/setWebhook'

    def updates_listener(self, interval: int) -> Iterator[Optional[UpdateData]]:
        """
        Method returns an iterator for bot updates. Yields UpdateData objects.
        If no updates the iterator will yield None. Make sure to check for iterated item to not be None.
        :param interval: wait in seconds for next updates request
        :return:
        """
        updates = None
        while True:
            if updates is not None:
                time.sleep(interval)

            updates = self.get_updates()
            if self.debug:
                print(updates)

            if not updates.data:
                # if no data Yield None to not interrupt the iterator
                yield None

            for update in (updates.data or []):
                yield update
