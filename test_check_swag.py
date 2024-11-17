from pages.swag_labs import SwagLabs


def test_icon_presence(browser):
    demo = SwagLabs(browser)
    demo.visit()
    assert demo.exist_icon()
    assert demo.user_name()
    assert demo.password()




