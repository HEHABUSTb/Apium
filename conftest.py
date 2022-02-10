import time
import pytest
import logging
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
