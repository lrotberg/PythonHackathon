import allure

from test import conftest


class DB_Actions:

    @staticmethod
    @allure.step("Return list of users from DB")
    def get_list_of_new_users():
        query = "SELECT * FROM temp WHERE id=1"
        my_cursor = conftest.my_db.cursor()
        my_cursor.execute(query)
        my_result = my_cursor.fetchall()
        return my_result