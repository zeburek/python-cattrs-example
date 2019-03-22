from random import randint

import pytest

from api import random
from api.client import RestfulBookerClient
from api import types as t


class TestExample:

    @pytest.fixture(scope="session")
    def client(self):
        client = RestfulBookerClient("https://restful-booker.herokuapp.com")
        client.authorize("admin", "password123")
        return client

    def test_create_new_booking(self, client):
        data = random.random_booking_info_type()
        res = client.vr(client.create_booking(data), [200, 201])
        created: t.BookingType = res.structure(t.BookingType).data
        assert created.bookingid
        assert created.booking == data

    def test_new_booking_exists(self, client):
        data = random.random_booking_info_type()
        res = client.vr(client.create_booking(data), [200, 201])
        created: t.BookingType = res.structure(t.BookingType).data
        res = client.vr(client.get_booking(created.bookingid))
        exists: t.BookingInfoType = res.structure(t.BookingInfoType).data
        assert exists == data

    def test_update_booking(self, client):
        data = random.random_booking_info_type()
        res = client.vr(client.create_booking(data), [200, 201])
        created: t.BookingType = res.structure(t.BookingType).data
        data2 = random.random_booking_info_type()
        res = client.vr(client.update_booking(created.bookingid, data2))
        updated: t.BookingInfoType = res.structure(t.BookingInfoType).data
        assert updated == data2

    def test_not_existing_booking(self, client):
        res = client.get_booking(randint(10000, 99999))
        assert res.status == 404
