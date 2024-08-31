import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@allure.feature("Note")
@allure.story("Main")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Check create note")
def test_create_note():
    with step('Skip onboarding page'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip')).click()
    with step('Create new note button'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/bottom_fab')).click()
    with step('Create new note'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/text')).click()
    with step('Type note'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/edit_note')).type("123456")
    with step('Exit'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/back_btn')).click()
    with step('Exit'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/back_btn')).click()
    with step('Check create note'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/title')).should(
            have.text("123456"))


@allure.feature("Checklist")
@allure.story("Main")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Check create check list")
def test_check_list():
    with step('Skip onboarding page'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip')).click()
    with step('Create new note button'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/bottom_fab')).click()
    with step('Create new checkbox'):
        browser.element(
            (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                             'FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.'
                             'LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.'
                             'LinearLayout[2]/android.widget.TextView')).click()
    with step('Add new item'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/text')).click()
    with step('Add title'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/edit')).type("New item")
    with step('Tap button OK'):
        browser.element((AppiumBy.ID, 'android:id/button1')).click()
    with step('Check create checklist'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/text')).should(
            be.visible)


@allure.feature("Note")
@allure.story("Main")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Check add note")
def test_add_note():
    with step('Skip onboarding page'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip')).click()
    with step('Add new note button'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/empty_text')).click()
    with step('Create new note'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/text')).click()
    with step('Type note'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/edit_note')).type("123456")
    with step('Exit'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/back_btn')).click()
    with step('Exit'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/back_btn')).click()
    with step('Check create note'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/title')).should(
            have.text("123456"))
