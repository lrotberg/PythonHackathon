import allure
import pytest

import test.conftest as conf
import workflows.web_flows as wf
import test.users_ddt as ddt

from utilities.common_ops import get_data


@pytest.mark.usefixtures("init_web")
class Test_Web:
    def teardown_method(self):
        wf.logout()

    @allure.title("Test User Balance")
    @allure.description("This test should login to a user and then check its balance")
    @pytest.mark.parametrize(ddt.users_headers, ddt.users)
    @pytest.mark.order(1)
    def test_check_balance(self, username, password, expected_balance):
        wf.login(username, password)

        assert wf.get_str_balance() == expected_balance

    @allure.title("Test User Registration")
    @allure.description("This test should register a new user and then"
                        " verify that it's getting the get started modal")
    @pytest.mark.order(4)
    def test_register_user(self):
        expected_text = "Get Started with Real World App"
        conf.driver.get(get_data("url_web") + "/signup")
        wf.register("TempFN", "TempLN", "TEMPUN", "s3cret", "s3cret")
        wf.login("TEMPUN", "s3cret")

        actual_text = wf.get_modal_text()

        wf.finish_registration()

        assert actual_text == expected_text

    @allure.title("Test Send Money")
    @allure.description("This test should")
    @pytest.mark.order(3)
    def test_send_money(self):
        wf.login("Katharina_Bernier", "s3cret")
        conf.driver.implicitly_wait(2)

        balance_before = wf.get_number_balance()
        payment_amount = 10

        wf.navigate_to_new_transaction()
        conf.driver.implicitly_wait(2)

        wf.choose_contact(3)
        conf.driver.implicitly_wait(2)

        wf.send_payment(payment_amount, "For The Pizza")
        conf.driver.implicitly_wait(2)

        assert wf.get_number_balance() == balance_before - payment_amount

    @allure.title("Test Number of Notifications")
    @allure.description("This test should verify that there are the same amount of notifications"
                        " on the notifications list as there are in the bubble")
    @pytest.mark.order(2)
    def test_num_of_notifications(self):
        wf.login("Katharina_Bernier", "s3cret")
        conf.driver.implicitly_wait(2)

        wf.navigate_to_notifications()
        conf.driver.implicitly_wait(2)

        assert wf.get_notifications_list_length() == wf.get_notifications_number()
