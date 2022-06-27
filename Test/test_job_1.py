import logging
import random

import pytest


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
