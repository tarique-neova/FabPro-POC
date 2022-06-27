import json
import logging
from typing import Any

import pytest

from helper import constants
from lib import launch_browser, common_fixtures

import os

ROOTDIR = os.path.dirname(os.path.abspath(__file__))


__TEST_DATA = 'testdata'

TESTCASE_DIR = os.path.join(ROOTDIR, __TEST_DATA)
CASES_DIR = os.path.join(ROOTDIR, __TEST_DATA)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S',
                    filename=constants.LOG_FILENAME, filemode='w', force=True)


@pytest.fixture(scope="session")
def launch_session():
    global driver
    driver = launch_browser.launch_browser()
    driver.get('https://devlogin.msuite.tech/')
    common_fixtures.login_application(driver)
    common_fixtures.navigate_fabpro_homepage(driver)
    yield driver
    driver.quit()
    logging.info("Closed the browser")

def parse_test_cases_testdata(file_name: str) -> Any:
    with open(os.path.join(CASES_DIR, '{}.json'.format(file_name))) as case_file:
        case_data = json.load(case_file)
    return case_data

def test_update_config(file_name: str, key, value) -> Any:
    try:
        with open(os.path.join(CASES_DIR, '{}.json'.format(file_name))) as case_file:
            config_data = json.load(case_file)
            config_data['create_job_data'][key] = value
        with open(os.path.join(CASES_DIR, '{}.json'.format(file_name)), "w") as outfile:
            json.dump(config_data, outfile, indent=4)
    except Exception as e:
        raise
