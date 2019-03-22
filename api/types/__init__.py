import attr


@attr.s
class AuthResponseType:
    token: str = attr.ib()


@attr.s
class AuthType:
    username: str = attr.ib()
    password: str = attr.ib()


@attr.s
class BookingDatesType:
    checkin: str = attr.ib()
    checkout: str = attr.ib()


@attr.s
class BookingInfoType:
    firstname: str = attr.ib()
    lastname: str = attr.ib()
    totalprice: int = attr.ib()
    depositpaid: bool = attr.ib()
    bookingdates: BookingDatesType = attr.ib()
    additionalneeds: str = attr.ib()


@attr.s
class BookingType:
    bookingid: int = attr.ib()
    booking: BookingInfoType = attr.ib()
