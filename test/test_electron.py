import pytest
import workflows.electron_flows as wf


@pytest.mark.usefixtures("init_electron")
class Test_Electron:
    def test_01(self):
        wf.electron_test()

