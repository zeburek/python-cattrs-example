import logging
from typing import Type

import attr
from cattr import unstructure, structure
from requests import Session
from simplejson.errors import JSONDecodeError

logger = logging.getLogger("example." + __name__)


@attr.s
class Response:
    status = attr.ib()
    data = attr.ib()
    headers = attr.ib()

    def structure(self, t: Type) -> 'Response':
        self.data = structure(self.data, t)
        return self


class session(Session):
    session_token = None

    def request(
        self,
        method: str,
        url: str,
        host: str = None,
        use_auth_data: bool = True,
        **kwargs,
    ):
        kwargs["method"] = method
        if use_auth_data and self.session_token:
            kwargs['cookies'] = {"token": self.session_token}
        if host:
            if not str(url).startswith("/"):
                raise ValueError("URL path should start with /")
            kwargs["url"] = f"{host}{url}"
        else:
            kwargs["url"] = url
        if "__attrs_attrs__" in dir(kwargs.get("data")):
            kwargs['json'] = unstructure(kwargs.get("data"))
            del kwargs['data']
        logger.info(f"Request: {method} {kwargs['url']} data: {kwargs}")
        res = super().request(**kwargs)
        try:
            data = res.json()
            logger.info(f"Response: {method} {kwargs['url']} data: {data}")
        except JSONDecodeError:
            data = res.content
            if b"\0" not in data:
                data = res.text
                logger.info(f"Response: {method} {kwargs['url']} data: {data}")
        return Response(res.status_code, data, res.headers)
