import time
link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_botton_add_is_displayed(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_class_name("btn-add-to-basket").is_displayed(), "Кнопка отсутствует"
