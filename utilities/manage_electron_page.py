import test.conftest as conf
from pages.electron_pages.api_demo_page import APIDemoPage


class ManageElectronPages:
    def init_electron_pages(self):
        conf.demo_page = APIDemoPage(conf.driver)
        globals()['demo_page'] = conf.demo_page

