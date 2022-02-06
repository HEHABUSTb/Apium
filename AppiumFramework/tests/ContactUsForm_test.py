import logging
import pytest
from AppiumFramework.base.DriverClass import Driver, allure_step


@pytest.mark.All
def test_allure_report():
    allure_step('Check')
    logging.info('CHECK')
    driver = Driver()

    driver.getDriverMethod()
