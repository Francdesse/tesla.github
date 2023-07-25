from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.application import Application


def browser_init(context, test_name):
    """
    :param context: Behave context
    """

    #CONNECTING TO CHROME
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    #CONNECTING TO FIREFOX
    context.driver = webdriver.Firefox()

    #CONNECTING TO SAFARI
    #context.driver = webdriver.Safari()

    #print(f"Test Name {test_name}")
    #### BROWSERSTACK ####
    # chrome_options = webdriver.ChromeOptions()
    # bstack_options = {
    #     "osVersion": 'Big Sur',
    #     "buildName": 'test',
    #     "sessionName": 'test_name'
    #                  }
    # chrome_options.set_capability('bstack:options', bstack_options)

    # # RUNNING ON WINDOWS 10 CHROME VER 114
    # desired_cap = {
    #     'bstack:options': {
    #         "os": "Windows",
    #         "osVersion": "10",
    #         "browserVersion": "latest",
    #         "local": "false",
    #         "seleniumVersion": "3.14.0",
    #     },
    #     "browserName": "Chrome",
    # }

    #RUNNING ON IOS CHROME
    # desired_cap = {
    #     'os': 'OS X',
    #     'osVersion': 'Big Sur',
    #     'browserName': 'Chrome',
    #     'browserVersion': 'latest',
    #     'sessionName': 'test_name'
    # }
    # bs_user = 'francyoudesse_ZgwiS3'
    # bs_key = '2wpdUvU3UwJTPzAvuqM2'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # #context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    # context.driver = webdriver.Remote(command_executor=url, options=chrome_options)
    # print(context.scenario.name)
    # context.driver.execute_script('browserstack_executor:{"action":"setSessionName", "arguments":{ "name":"' + context.scenario.name + '"}}')

    context.driver.maximize_window()

    context.driver.implicitly_wait(4)

    context.driver.wait = WebDriverWait(context.driver, 5)

    context.app = Application(context.driver)
def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        context.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments":{"status":"Failed", "reason": "Validation Failed"}}')
        print('\nStep failed: ', step)


# def after_step(context, step):
#     if step.status == 'failed':
#         print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
