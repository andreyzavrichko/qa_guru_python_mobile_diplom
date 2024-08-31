import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@allure.feature("Onboarding")
@allure.story("Onboarding")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Check onboarding")
def test_onboarding():
    with step('First onboarding page'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/textTitle')).should(
            have.text('Welcome to ColorNote'))
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start')).click()
    with step('Second onboarding page'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/textTitle')).should(
            have.text('Create a note'))
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_next')).click()
    with step('Third onboarding page'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/textTitle')).should(
            have.text('Choose a note type'))
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_next')).click()


@allure.feature("Calendar")
@allure.story("Calendar")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Check calendar")
def test_calendar():
    with step('Skip onboarding page'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip')).click()
    with step('Tap calendar button'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/page_calendar')).click()
    with step('Check calendar'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/month_view')).should(
            be.visible)


@allure.feature("Search")
@allure.story("Search")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Check search")
def test_search():
    with step('Skip onboarding page'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip')).click()
    with step('Tap search button'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/page_search')).click()
    with step('Check search'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/edit_search')).should(
            be.visible)


@allure.feature("Color")
@allure.story("Color")
@allure.severity(allure.severity_level.MINOR)
@allure.title("Check color")
def test_color():
    with step('Skip onboarding page'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip')).click()
    with step('Tap color button'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/main_btn1')).click()
    with step('Tap color'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/item_container')).click()
    with step('Check color'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/text_button_center')).should(
            be.visible)


@allure.feature("Sorting")
@allure.story("Sorting")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Check sorting")
def test_sort():
    with step('Skip onboarding page'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip')).click()
    with step('Tap sort button'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/text_button_center')).click()
    with step('Tap sort by modified time button'):
        browser.element(
            (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                             'FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/c.q.a.b/android.widget.'
                             'ListView/android.widget.LinearLayout[1]/android.widget.TextView')).click()
    with step('Check sort'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/empty_text')).should(
            have.text("Add note"))
