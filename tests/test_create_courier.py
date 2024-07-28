import allure
import consts
from generators import generate_courier
from request_helper import make_request_courier 


class TestCreateCourier:

    @allure.title('Проверяем успешность создания курьера и корректность кода ответа')
    def test_create_new_courier(self):
        payload = generate_courier()

        response = make_request_courier(payload)
        data = response.json()

        assert response.status_code == 201
        assert data["ok"] == True

    @allure.title('Проверяем создание двух одинаковых курьеров')
    def test_create_double_couriers(self):
        payload = generate_courier()

        make_request_courier(payload)
        response = make_request_courier(payload)
        data = response.json()

        assert response.status_code == 409
        assert data["message"] == consts.login_already_exists

    @allure.title('Проверяем создание курьера с уже зарегистрированным логином')
    def test_double_courier_login(self):
        payload = generate_courier()
        payload["login"] = consts.correct_login

        response = make_request_courier(payload)
        data = response.json()

        assert response.status_code == 409
        assert data["message"] == consts.login_already_exists

    @allure.title('Проверяем создание курьера без нужного поля')
    def test_create_courier_without_required_field(self):
        payload = generate_courier()
        payload["password"] = None

        response = make_request_courier(payload)
        data = response.json()

        assert response.status_code == 400
        assert data["message"] == consts.not_enough_data_courier_create
