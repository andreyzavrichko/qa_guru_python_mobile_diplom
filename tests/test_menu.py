import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@allure.feature("More")
@allure.story("Menu")
@allure.severity(allure.severity_level.MINOR)
@allure.title("Check more button")
def test_more():
    with step('Skip onboarding page'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip')).click()
    with step('Tap more button'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/main_btn3')).click()
    with step('Tap view'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/text')).click()
    with step('Check view'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/alertTitle')).should(
            be.visible)


@allure.feature("Archive")
@allure.story("Menu")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Check archive button")
def test_archive():
    with step('Skip onboarding page'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip')).click()
    with step('Tap menu button'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/page_more')).click()
    with step('Tap archive button'):
        browser.element(
            (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                             'FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                             'android.widget.RelativeLayout/c.q.a.b/android.widget.ScrollView/android.widget.LinearLayout/'
                             'android.widget.GridView/android.widget.LinearLayout[1]/android.widget.TextView')).click()
    with step('Check archive'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/main_title')).should(
            be.visible)


@allure.feature("Trash")
@allure.story("Menu")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Check trash button")
def test_trash():
    with step('Skip onboarding page'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip')).click()
    with step('Tap menu button'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/page_more')).click()
    with step('Tap trash button'):
        browser.element(
            (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                             'FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                             'android.widget.RelativeLayout/c.q.a.b/android.widget.ScrollView/android.widget.LinearLayout/'
                             'android.widget.GridView/android.widget.LinearLayout[2]/android.widget.TextView')).click()
    with step('Check trash'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/main_title')).should(
            be.visible)


@allure.feature("Settings")
@allure.story("Menu")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Check settings button")
def test_settings():
    with step('Skip onboarding page'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip')).click()
    with step('Tap menu button'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/page_more')).click()
    with step('Tap settings button'):
        browser.element(
            (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                             'FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                             'android.widget.RelativeLayout/c.q.a.b/android.widget.ScrollView/android.widget.LinearLayout/'
                             'android.widget.GridView/android.widget.LinearLayout[3]/android.widget.TextView')).click()
    with step('Check settings'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/action_bar')).should(
            be.visible)


@allure.feature("Theme")
@allure.story("Menu")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Check theme button")
def test_theme():
    with step('Skip onboarding page'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip')).click()
    with step('Tap menu button'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/page_more')).click()
    with step('Tap theme button'):
        browser.element(
            (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                             'FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                             'android.widget.RelativeLayout/c.q.a.b/android.widget.ScrollView/android.widget.LinearLayout/'
                             'android.widget.GridView/android.widget.LinearLayout[4]/android.widget.TextView')).click()
    with step('Check theme'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/title_template')).should(
            be.visible)


@allure.feature("Tutorial")
@allure.story("Menu")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.title("Check tutorial button")
def test_tutorial():
    with step('Skip onboarding page'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip')).click()
    with step('Tap menu button'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/page_more')).click()
    with step('Tap tutorial button'):
        browser.element(
            (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                             'FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                             'android.widget.RelativeLayout/c.q.a.b/android.widget.ScrollView/android.widget.LinearLayout/'
                             'android.widget.GridView/android.widget.LinearLayout[5]/android.widget.TextView')).click()
    with step('Check tutorial'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/textTitle')).should(
            have.text("Welcome to ColorNote"))


@allure.feature("Menu")
@allure.story("Menu")
@allure.severity(allure.severity_level.MINOR)
@allure.title("Check menu")
def test_menu():
    with step('Skip onboarding page'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip')).click()
    with step('Tap menu button'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/page_more')).click()
    with step('Check menu'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/main_title')).should(
            be.visible)
