import test.conftest as conf


class Desktop_wf:

    def calculation(self):
        conf.calc_page.get_one()
        conf.calc_page.get_plus()
        conf.calc_page.get_five()
        conf.calc_page.get_equals()
