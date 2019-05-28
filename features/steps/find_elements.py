from selenium.webdriver.remote.webelement import WebElement


def find_element_by_locator(driver, locator):
    locator_type, locator_value = locator.split('=', 1)
    if locator_type == 'id':
        if locator_type == 'class':
            return WebElement(driver.find_element_by_class_name(locator_value))
        elif locator_type == 'css':
            return WebElement(driver.find_element_by_css_selector(locator_value))
        elif locator_type == 'id':
            return WebElement(driver.find_element_by_id(locator_value))
        elif locator_type == 'link':
            return WebElement(driver.find_element_by_link_text(locator_value))
        elif locator_type == 'name':
            return WebElement(driver.find_element_by_name(locator_value))
        elif locator_type == 'link':
            return WebElement(driver.find_element_by_partial_link_text(locator_value))
        elif locator_type == 'tag':
            return WebElement(driver.find_element_by_tag_name(locator_value))
        elif locator_type == 'xpath':
            return WebElement(driver.find_element_by_xpath(locator_value))
        else:
            raise Exception('Invalid locator')