import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from allure import step


@allure.step("Открываем страницу википедии")
def test_open_wikipedia_app():
    with step("Verify that first screen opened"):
        if browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).matching(
                have.text("The Free Encyclopedia")):
            browser.element(
                (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        else:
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_card_header_title')).matching(
                have.text("Featured article")
            )

    with step("Verify that second screen opened"):
        if browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).matching(
                have.text("New ways to explore")):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step("Verify that third screen opened"):
        if browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).matching(
                have.text("Reading lists with sync")):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step("Verify that forth screen opened"):
        if browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).matching(
                have.text("Send anonymous data")):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/acceptButton')).click()


