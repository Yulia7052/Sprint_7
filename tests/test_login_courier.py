import allure
import consts
from request_helper import make_request_login


class TestLoginCourier:

    @allure.title('Проверка успешной авторизации существующего курьера')
    def test_authorization_succces(self):
        payload = {
            "login": consts.correct_login,
            "password": consts.correct_pass
        }

        response = make_request_login(payload)
        data = response.json()

        assert response.status_code == 200
        assert data["id"] == consts.courier_id

    @allure.title('Проверка отказа в авторизации из-за незаполненного логина')
    def test_not_authorization_without_login(self):
        payload = {
            "password": consts.correct_pass
        }

        response = make_request_login(payload)
        data = response.json()

        assert response.status_code == 400
        assert data["message"] == consts.not_enough_data_login

    @allure.title('Проверка отказа в авторизации из-за неправильного пароля')
    def test_authorization_wrong_password(self):
        payload = {
            "login": consts.correct_login,
            "password": consts.wrong_pass
        }

        response = make_request_login(payload)
        data = response.json()

        assert response.status_code == 404
        assert data["message"] == consts.account_not_exists

    @allure.title('Проверка отказа в авторизации из-за данных, под которыми не было регистрации')
    def test_authorization_not_exists_user(self):
        payload = {
            "login": consts.wrong_login,
            "password": consts.wrong_pass
        }

        response = make_request_login(payload)
        data = response.json()

        assert response.status_code == 404
        assert data["message"] == consts.account_not_exists

