from faker import Faker

from api.types import BookingInfoType, BookingDatesType

faker = Faker()


def random_booking_info_type():
    return BookingInfoType(
        firstname=faker.first_name(),
        lastname=faker.last_name(),
        totalprice=faker.pyint(),
        depositpaid=True,
        bookingdates=BookingDatesType(
            checkin=faker.iso8601()[:10],
            checkout=faker.iso8601()[:10]
        ),
        additionalneeds=faker.word()
    )
