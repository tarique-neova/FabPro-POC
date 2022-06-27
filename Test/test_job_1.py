import time

import pytest
import logging
from lib import launch_browser, common_fixtures, utils
from locators import homepage,login
import random

@pytest.mark.testjob
def test_rail():

    # testrunid = common_fixtures.get_run_id("JobsDetails", "Fabpro")
    # testcaseid = common_fixtures.get_case_id("Verify if user is able to create a job successfully", "Fabpro")
    # common_fixtures.update_testrail(testcaseid,testrunid,True,"Failed")
    # testcaseid = common_fixtures.get_case_id("Verify if user is able to login in portal successfully", "Fabpro")
    # common_fixtures.update_testrail(testcaseid, testrunid, True, "Failed")
    # logging.info(testrunid)
    # logging.info(testcaseid)
    random_number = random.randint(1, 10000)
    logging.info(random_number)
