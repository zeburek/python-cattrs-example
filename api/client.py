import inspect
import logging
from typing import overload

from api.requests import session, Response
from api.types import AuthType, BookingInfoType, AuthResponseType

logger = logging.getLogger("example." + __name__)


class RestfulBookerClient:

    _s = session()
    host = None

    def __init__(self, host):
        self.host = host

    def verify_response(self, res: Response, ok_status=200):
        func = inspect.stack()[1][3]
        if isinstance(ok_status, int):
            ok_status = [ok_status]
        if res.status not in ok_status:
            raise ValueError(f"Verified response: function {func} failed: "
                             f"server responded {res.status} "
                             f"with data: {res.data}")
        else:
            logger.info(
                f"Verified response: function {func} code {res.status}")
        return res

    vr = verify_response

    def authorize(self, username, password):
        res = self.login(AuthType(username, password)).structure(
            AuthResponseType)
        if res.status != 200:
            raise Exception("Unable to authorize using given credentials")
        self._s.session_token = res.data.token

    def login(self, data: AuthType = None, json=None):
        return self._s.post(self.host + "/auth", data=data, json=json)

    def create_booking(self, data: BookingInfoType = None, json=None):
        return self._s.post(self.host + "/booking", data=data, json=json)

    def update_booking(self, id: int, data: BookingInfoType = None, json=None):
        return self._s.put(self.host + f"/booking/{id}", data=data, json=json)

    def get_booking(self, id: int):
        return self._s.get(self.host + f"/booking/{id}")
