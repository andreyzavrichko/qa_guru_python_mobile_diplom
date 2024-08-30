from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


# def test_onboarding():
#     with step('First onboarding page'):
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/textTitle')).should(
#             have.text('Welcome to ColorNote'))
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start')).click()
#     with step('Second onboarding page'):
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/textTitle')).should(
#             have.text('Create a note'))
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_next')).click()
#     with step('Third onboarding page'):
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/textTitle')).should(
#             have.text('Choose a note type'))
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_next')).click()


# def test_create_note():
#     with step('Skip onboarding page'):
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip')).click()
#     with step('Create new note button'):
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/bottom_fab')).click()
#     with step('Create new note'):
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/text')).click()
#     with step('Type note'):
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/edit_note')).type("123456")
#     with step('Exit'):
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/back_btn')).click()
#     with step('Exit'):
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/back_btn')).click()
#     with step('Check create note'):
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/title')).should(
#             have.text("123456"))


# def test_check_list():
#     with step('Skip onboarding page'):
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip')).click()
#     with step('Create new note button'):
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/bottom_fab')).click()
#     with step('Create new checkbox'):
#         browser.element(
#             (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
#                              'FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.'
#                              'LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.'
#                              'LinearLayout[2]/android.widget.TextView')).click()
#     with step('Add new item'):
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/text')).click()
#     with step('Add title'):
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/edit')).type("New item")
#     with step('Tap button OK'):
#         browser.element((AppiumBy.ID, 'android:id/button1')).click()
#     with step('Check create checklist'):
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/text')).should(
#             be.visible)


# def test_calendar():
#     with step('Skip onboarding page'):
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip')).click()
#     with step('Tap calendar button'):
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/page_calendar')).click()
#     with step('Check calendar'):
#         browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/month_view')).should(
#             be.visible)


# void checkSearchTest() {
#         step("Allow access", () ->
#                 $(AppiumBy.id("com.android.permissioncontroller:id/permission_allow_button")).click());
#         step("Skip onboarding page", () ->
#                 $(AppiumBy.id("com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip")).click());
#         step("Tap search button", () ->
#                 $(AppiumBy.id("com.socialnmobile.dictapps.notepad.color.note:id/page_search")).click());
#         step("Check search", () -> {
#             $(AppiumBy.id("com.socialnmobile.dictapps.notepad.color.note:id/edit_search")).shouldBe(Condition.visible);
#         });
#     }

def test_search():
    with step('Skip onboarding page'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip')).click()
    with step('Tap calendar button'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/page_calendar')).click()
    with step('Check calendar'):
        browser.element((AppiumBy.ID, 'com.socialnmobile.dictapps.notepad.color.note:id/month_view')).should(
            be.visible)