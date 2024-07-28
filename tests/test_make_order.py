import allure
import pytest
from generators import generate_order
from request_helper import make_request_orders


class TestMakeOrder:

    @pytest.mark.parametrize(
        "payload",
        [
            generate_order(["BLACK"]),
            generate_order(["BLACK", "WHITE"]),
            generate_order(None),
        ]
    )
    @allure.title('Проверка создания заказа пользователем')
    def test_create_order(self, payload):
        response = make_request_orders(payload)
        data = response.json()

        assert response.status_code == 201
        assert data["track"] != None
