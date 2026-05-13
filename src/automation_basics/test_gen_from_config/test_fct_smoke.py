class TestFCTSmoke:
    def test_action(self, get_device, _func_name):
        method_ = getattr(get_device, _func_name)
        ret = method_()
        assert ret == _func_name
