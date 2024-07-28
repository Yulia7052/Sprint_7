import allure
from request_helper import get_orders


class TestOrdersList:

    @allure.title('Проверка списка закаов')
    def test_create_order(self):
        response = get_orders()
        data = response.json()

        assert response.status_code == 200
        assert data["orders"] != None
