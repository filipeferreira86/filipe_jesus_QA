from selenium.webdriver import Chrome


def before_scenario(context, scenario):
    d = Chrome()
    d.set_page_load_timeout(20000)
    context.driver = d
    context.scenario = scenario

def after_scenario(context, scenario):
    context.driver.quit()