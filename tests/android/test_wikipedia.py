import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from allure import step
from selene import be
from mobile_tests_lesson_13.model import app


@allure.step("Открываем страницу википедии")
def test_check_for_search_resuls_1():
    allure.dynamic.tag("Verify that first screen opened")
    if browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).matching(
        have.text("The Free Encyclopedia")):
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
    else:
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_card_header_title')).matching(
            have.text("Featured article")
        )

    allure.dynamic.tag("Verify that second screen opened")
    if browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).matching(
            have.text("New ways to explore")):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    allure.dynamic.tag("Verify that third screen opened")
    if browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).matching(
            have.text("Reading lists with sync")):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    allure.dynamic.tag("Verify that forth screen opened")
    if browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).matching(
            have.text("Send anonymous data")):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/acceptButton')).click()


