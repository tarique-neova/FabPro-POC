import string
import time
from random import random

import pytest
import logging
from lib import launch_browser, common_fixtures, utils
from locators import homepage,login
from conftest import parse_test_cases_testdata

@pytest.fixture(scope='module')
def pre_setup(request, launch_session):
    global driver
    driver = launch_session


@pytest.mark.usefixtures("pre_setup")
@pytest.mark.testjob
class TestJobTestCase(object):
    def test_verify_login_successful(self, request):
        logging.info("Verify User is Logging to Home page {}".format(request.node.name))
        assigned_drawing_heading_text = utils.get_element_text(driver, homepage.ASSIGNED_DRAWINGS, "")
        if assigned_drawing_heading_text == "Assigned Drawings":
            # status_id is 1 for Passed, 2 For Blocked, 4 for Retest and 5 for Failed
            common_fixtures.update_testrail(request.node.name, 1,
                                            "Login successfully")
        else:
            common_fixtures.update_testrail(request.node.name, 5,
                                            "Unable to login to application")
        assert assigned_drawing_heading_text == "Assigned Drawings", "Unable to login"

    def test_verfiy_create_job_successful(self, request):
        logging.info("Verify Job is Created Successfully")
        assigned_drawing_heading_text = utils.get_element_text(driver, homepage.ASSIGNED_DRAWINGS, "")
        assert assigned_drawing_heading_text == "Assigned Drawings", "Fabpro Page is not launched successfully"
        case_data = parse_test_cases_testdata('job_details')
        common_fixtures.create_new_job(driver, case_data)

        # if assigned_drawing_heading_text == "Assigned Drawings":
        #     common_fixtures.update_testrail(request.node.name, 1,
        #                                     "Job is Created successfully")
        # else:
        #     common_fixtures.update_testrail(request.node.name, 5,
        #                                     "Job is not created successfully")
        # assert assigned_drawing_heading_text == "Assigned Drawings", "Unable to login"

    def test_verfiy_job_info_update_successful(self, request):
        logging.info("Verify User is Logging to Home page ")
        assigned_drawing_heading_text = utils.get_element_text(driver, homepage.ASSIGNED_DRAWINGS, "")
        assert assigned_drawing_heading_text == "Assigned Drawings", "Fabpro Page is not launched successfully"
        case_data = parse_test_cases_testdata('job_details')
        common_fixtures.update_existing_job_info(driver, case_data)


    def test_verfiy_package_update_successful(self, request):
        logging.info("Verify User is Logging to Home page ")
        assigned_drawing_heading_text = utils.get_element_text(driver, homepage.ASSIGNED_DRAWINGS, "")
        assert assigned_drawing_heading_text == "Assigned Drawings", "Fabpro Page is not launched successfully"
        case_data = parse_test_cases_testdata('job_details')
        common_fixtures.update_existing_job_package(driver, case_data)
        


