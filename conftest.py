import time
import allure
import pytest
import logging
from allure_commons.types import AttachmentType
from AppiumFramework.base.DriverClass import Driver

driver = None


@pytest.fixture(scope='class')
def driver(request):
    global driver
    logging.info('driver fixture start working')
    driver = Driver().getDriverMethod()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    logging.info('Try to close driver')
    time.sleep(5)
    driver.quit()


@pytest.mark.hookwrapper
@pytest.mark.usefixtures('driver')
def pytest_runtest_makereport():
    # Automatically take screenshot when test fails and attach to allure report

    outcome = yield
    report = outcome.get_result()
    try:
        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                allure.attach(driver.get_screenshot_as_png(), name=file_name,
                              attachment_type=AttachmentType.PNG)
    except Exception as e:
        logging.info('Something got wrong in hookwrapper')

