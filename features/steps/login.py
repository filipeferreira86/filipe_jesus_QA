from behave import *
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('that I am in the site "{site}"')
def step_impl(context, site):
    context.driver = Chrome()
    context.driver.set_page_load_timeout(20000)
    context.driver.get('https://uat.ormuco.com/login')


@when('I click at the button "{link}"')
def step_impl(context, link):
    element = find_element_by_locator(context.driver, link)
    element.click()


@when('I inform "{content}" in the field "{locator}"')
def step_impl(context, content, locator):
    element = find_element_by_locator(context.driver, locator)
    element.send_keys(content)


@when('I clear the field "{locator}"')
def step_impl(context, locator):
    element = find_element_by_locator(context.driver, locator)
    element.clear()


# Results


@then('the site should show the message "{msg}" in the field "{locator}"')
def step_impl(context, msg, locator):
    lbl = find_element_by_locator_wait(context.driver, locator)

    assert msg == lbl.text


def find_element_by_locator(d, locator):
    locator_type, locator_value = locator.split('=')
    if locator_type == 'class':
        return d.find_element_by_class_name(locator_value)
    elif locator_type == 'css':
        return d.find_element_by_css_selector(locator_value)
    elif locator_type == 'id':
        return d.find_element_by_id(locator_value)
    elif locator_type == 'link':
        return d.find_element_by_link_text(locator_value)
    elif locator_type == 'name':
        return d.find_element_by_name(locator_value)
    elif locator_type == 'partial_link':
        return d.find_element_by_partial_link_text(locator_value)
    elif locator_type == 'tag':
        return d.find_element_by_tag_name(locator_value)
    elif locator_type == 'xpath':
        return d.find_element_by_xpath(locator_value)
    else:
        raise Exception('Invalid locator')


def find_element_by_locator_wait(d, locator):
    locator_type, locator_value = locator.split('=')
    if locator_type == 'class':
        return WebDriverWait(d, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, locator_value)))
    elif locator_type == 'css':
        return WebDriverWait(d, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator_value)))
    elif locator_type == 'id':
        return WebDriverWait(d, 10).until(EC.element_to_be_clickable((By.ID, locator_value)))
    elif locator_type == 'link':
        return WebDriverWait(d, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, locator_value)))
    elif locator_type == 'name':
        return WebDriverWait(d, 10).until(EC.element_to_be_clickable((By.NAME, locator_value)))
    elif locator_type == 'partiallink':
        return WebDriverWait(d, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, locator_value)))
    elif locator_type == 'tag':
        return WebDriverWait(d, 10).until(EC.element_to_be_clickable((By.TAG_NAME, locator_value)))
    elif locator_type == 'xpath':
        return WebDriverWait(d, 10).until(EC.element_to_be_clickable((By.XPATH, locator_value)))
    else:
        raise Exception('Invalid locator')

