import logging

import pytest

from conftest import parse_test_cases_testdata
from lib import common_fixtures, utils
from locators import homepage


@pytest.fixture(scope='module')
def pre_setup(launch_session):
    global driver
    driver = launch_session


@pytest.mark.usefixtures("pre_setup")
@pytest.mark.testjob
class TestJobTestCase(object):
    def test_verify_msuite_portal_login(self, request):
        logging.info("Executing - Verify if user able to login successfully in MSuite homepage portal {}".format(
            request.node.name))
        assigned_drawing_heading_text = utils.get_element_text(driver, homepage.ASSIGNED_DRAWINGS, "")
        if assigned_drawing_heading_text == "Assigned Drawings":
            common_fixtures.update_testrail(request.node.name, 1,
                                            "Successfully logged in in MSuite Portal")
        else:
            common_fixtures.update_testrail(request.node.name, 5,
                                            "Error while logging in MSuite Portal. Please check")
        assert assigned_drawing_heading_text == "Assigned Drawings", "Unable to login"

    def test_verify_create_new_job(self, request):
        logging.info("Executing - Verify if user is able to create a new job successfully")
        assigned_drawing_heading_text = utils.get_element_text(driver, homepage.ASSIGNED_DRAWINGS, "")
        assert assigned_drawing_heading_text == "Assigned Drawings", "Fabpro Page is not launched successfully"
        case_data = parse_test_cases_testdata('job_details')
        common_fixtures.create_new_job(driver, case_data)
        case_data = parse_test_cases_testdata('job_details')
        if assigned_drawing_heading_text == "Assigned Drawings":
            common_fixtures.update_testrail(request.node.name, 1,
                                            "Job is Created successfully")
        else:
            common_fixtures.update_testrail(request.node.name, 5,
                                            "Job is not created successfully")
        assert assigned_drawing_heading_text == "Assigned Drawings", "Unable to login"


def test_verify_update_existing_job_info(self):
    logging.info("Executing - Verify if user is update the existing job info successfully")
    assigned_drawing_heading_text = utils.get_element_text(driver, homepage.ASSIGNED_DRAWINGS, "")
    assert assigned_drawing_heading_text == "Assigned Drawings", "Fabpro Page is not launched successfully"
    case_data = parse_test_cases_testdata('job_details')
    common_fixtures.update_existing_job_info(driver, case_data)


def test_verify_update_existing_job_package(self):
    logging.info("Executing - Verify if user is able to update the package details of existing job successfully")
    assigned_drawing_heading_text = utils.get_element_text(driver, homepage.ASSIGNED_DRAWINGS, "")
    assert assigned_drawing_heading_text == "Assigned Drawings", "Fabpro Page is not launched successfully"
    case_data = parse_test_cases_testdata('job_details')
    common_fixtures.update_existing_job_package(driver, case_data)
