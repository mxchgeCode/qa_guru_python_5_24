import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from allure import step
from selene import be
from mobile_tests_lesson_13.model import app


# @allure.step("Открываем страницу википедии")
def test_open_wikipedia_app():
    primary_list = 'org.wikipedia.alpha:id/primaryTextView'
    forward_button = 'org.wikipedia.alpha:id/fragment_onboarding_forward_button'
    accept_button = 'org.wikipedia.alpha:id/acceptButton'

    with step("Verify that first screen opened"):
        assert browser.element((AppiumBy.ID, primary_list)).matching(
            have.text("The Free Encyclopedia"))
        if browser.element(
                (AppiumBy.ID, forward_button)).should(be.visible):
            browser.element(
                (AppiumBy.ID, forward_button)).click()

    with step("Verify that second screen opened"):
        browser.wait_until((AppiumBy.ID, primary_list))
        assert browser.element((AppiumBy.ID, primary_list)).matching(
            have.text("New ways to explore"))
        if browser.element(
                (AppiumBy.ID, forward_button)).should(be.visible):
            browser.element(
                (AppiumBy.ID, forward_button)).click()

    with step("Verify that third screen opened"):
        browser.wait_until((AppiumBy.ID, primary_list))
        assert browser.element((AppiumBy.ID, primary_list)).matching(
            have.text("Reading lists with sync"))
        if browser.element(
                (AppiumBy.ID, forward_button)).should(be.visible):
            browser.element(
                (AppiumBy.ID, forward_button)).click()

    with step("Verify that forth screen opened"):
        browser.wait_until((AppiumBy.ID, primary_list))
        assert browser.element((AppiumBy.ID, primary_list)).matching(
            have.text("Send anonymous data"))
        if browser.element(
                (AppiumBy.ID, accept_button)).should(be.visible):
            browser.element(
                (AppiumBy.ID, accept_button)).click()
