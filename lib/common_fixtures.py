import json
import logging
import random
import time
from datetime import datetime, timedelta
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
import conftest
from helper import constants
from lib import utils, testrail
from locators import login, job


def get_json_file_data():
    try:
        with open(constants.CONFIG_FILENAME, "r") as config_file:
            json_data = json.load(config_file)
        json_data = eval(json.dumps(json_data))
        username = json_data['credentials']['username']
        password = json_data['credentials']['password']
        testrail_project_name = json_data['testrail']['project_name']
        testrail_suite_name = json_data['testrail']['suite_name']
        testrail_username = json_data['testrail']['username']
        testrail_password = json_data['testrail']['password']
        testrail_url = json_data['testrail']['testrail_url']
        return username, password, testrail_project_name, testrail_suite_name, testrail_username, testrail_password, testrail_url
    except Exception as ex:
        logging.warning("Exception while getting data from json file: {} ".format(ex))


get_json_file_data()


def login_application(driver):
    try:
        username, password, _, _, _, _, _ = get_json_file_data()
        utils.wait_for_element_to_be_present_using_xpath(driver, login.MSUIT)
        driver.find_element_by_xpath(login.USERNAME).send_keys(username)
        driver.find_element_by_xpath(login.PASSWORD).send_keys(password)
        driver.find_element_by_xpath(login.LOGIN_BUTTON).click()
    except Exception as ex:
        logging.info("Got exception while login : {} ".format(ex))


def navigate_fabpro_homepage(driver):
    try:
        utils.wait_for_element_to_be_present_using_xpath(driver, login.FABPRO_IMAGE)
        driver.find_element_by_xpath(login.FABPRO_IMAGE).click()
    except Exception as ex:
        logging.info("Got exception while login : {} ".format(ex))


def verify_fabpro_homepage(driver):
    try:
        utils.wait_for_element_to_be_present_using_xpath(driver, login.FABPRO_IMAGE)
        driver.find_element_by_xpath(login.FABPRO_IMAGE).click()
    except Exception as ex:
        logging.info("Got exception while login : {} ".format(ex))


def create_new_job(driver, casedata):
    navigate_create_job(driver)
    logging.info("casedata job name {}".format(casedata['create_job_data']['job_name']))
    fill_data_job_info(driver, casedata['create_job_data'])
    click_next_button(driver)
    fill_cost_code(driver, casedata['create_job_data'])
    click_next_button(driver)
    fill_package_info(driver, casedata['create_job_data'])
    click_next_button(driver)
    fill_drawing_info(driver)
    click_next_button(driver)
    fill_item_info(driver)
    pass


def update_existing_job_info(driver, casedata):
    click_on_job_menu(driver)
    search_existing_job(driver, casedata['create_job_data'])
    update_data_job_info(driver, casedata['update_job_data'])
    click_next_button(driver)


def update_existing_job_package(driver, casedata):
    click_on_job_menu(driver)
    search_existing_job(driver, casedata['create_job_data'])
    click_next_button(driver)
    click_next_button(driver)
    update_data_package_info(driver, casedata['update_job_data'])
    click_next_button(driver)
    pass


# Job Related Functions:
def fill_data_job_info(driver, casedata):
    # Due Date Field

    float_mode = utils.get_element(driver, job.FLOAT_MODE)
    float_mode.click()

    # Job Site Address Field
    job_site_field = utils.get_element(driver, job.JOB_SITE)
    job_site_field.clear()
    job_site_field.send_keys(casedata['job_site'])

    # City Field
    city_field = utils.get_element(driver, job.CITY)
    city_field.send_keys(casedata['city'])
    city_field.send_keys(Keys.TAB)

    # State Field
    state_field = utils.get_element(driver, job.STATE)
    state_field.send_keys(casedata['state'])
    state_field.send_keys(Keys.TAB)

    # Zip Code Field
    zip_code_field = utils.get_element(driver, job.ZIP_CODE)
    zip_code_field.send_keys(casedata['zip_code'])

    budget_hours_field = utils.get_element(driver, job.BUDGET_HOURS)
    budget_hours_field.clear()
    budget_hours_field.send_keys(casedata['budget_hrs'])

    random_number = random.randint(1, 10000)
    job_name_field = utils.get_element(driver, job.JOB_NAME)
    job_name = "Fabpro_" + str(random_number)
    conftest.test_update_config("job_details", 'job_name', job_name)
    job_name_field.send_keys(job_name)

    # Job Number field
    job_number_field = utils.get_element(driver, job.JOB_NUMBER)
    job_number_field.send_keys(random_number)
    conftest.test_update_config("job_details", 'job_number', random_number)

    due_date_field = utils.get_element(driver, job.DUE_DATE)
    due_date_field.click()
    due_date_field.send_keys(get_due_date)

    time.sleep(5)


def fill_cost_code(driver, casedata):
    utils.sendkeys_element_without_click(driver, job.AREA, casedata['test_area'])
    utils.sendkeys_element_without_click(driver, job.DESCRIPTION, casedata['test_description'])
    utils.sendkeys_element_without_click(driver, job.BUDGET_HOURS, casedata["budget_hrs"])
    utils.sendkeys_element_without_click(driver, job.BUDGET_COST, casedata["budget_cost"])
    select = Select(driver.find_element_by_xpath(job.TYPE))
    # select by visible text
    select.select_by_visible_text('Mechanical')
    utils.sendkeys_element_without_click(driver, job.COST_CODE, ["cost_code"])

    utils.click_element_by_locator(driver, job.ADD_COST_CODE)
    time.sleep(10)


def fill_package_info(driver, casedata):
    utils.sendkeys_element_by_locator(driver, job.PACKG_NAME, casedata['package_name'])
    time.sleep(5)
    select1 = Select(driver.find_element_by_xpath(job.WORKFLOW))
    select1.select_by_visible_text('RL tests Flow Creation')
    time.sleep(3)
    # due date
    due_date_field = utils.get_element(driver, job.DUE_DATE)
    due_date_field.send_keys("06-27-2022")
    utils.click_element_by_locator(driver, job.UPLOAD_PACKAGE)
    time.sleep(5)
    utils.click_element_by_locator(driver, job.CANCEL_PACKAGE)
    time.sleep(3)
    utils.sendkeys_element_by_locator(driver, job.PACKG_NUMBER, casedata['package_number'])
    utils.sendkeys_element_by_locator(driver, job.DELIVERY_INSTRUCTION, casedata['delivery_instruction'])

    utils.get_element(driver, job.CHOOSEFILE).send_keys("/home/sheba/Documents/FabPro.pdf")
    utils.click_element_by_locator(driver, job.UPLOAD)
    time.sleep(10)


def fill_drawing_info(driver):
    utils.click_element_by_locator(driver, job.UPLOAD_DRAWING)
    select2 = Select(driver.find_element_by_xpath(job.SELECT_PACK))
    select2.select_by_index('1')
    utils.get_element(driver, job.CHOOSEDRAWNFILE).send_keys("/home/sheba/Documents/FabPro.pdf")
    time.sleep(3)
    utils.click_element_by_locator(driver, job.UPLOADDRAWNFILE)
    time.sleep(5)


def fill_item_info(driver):
    select2 = Select(driver.find_element_by_xpath(job.SELECT_PACKAGE))
    select2.select_by_index('1')
    time.sleep(5)


def update_data_job_info(driver, casedata):
    # Job Site Address Field
    job_site_field = utils.get_element(driver, job.JOB_SITE)
    job_site_field.clear()
    job_site_field.send_keys(casedata['job_site'])

    # City Field
    city_field = utils.get_element(driver, job.CITY)
    city_field.send_keys(casedata['city'])
    city_field.send_keys(Keys.TAB)

    # State Field
    state_field = utils.get_element(driver, job.STATE)
    state_field.send_keys(casedata['state'])
    state_field.send_keys(Keys.TAB)

    # Zip Code Field
    zip_code_field = utils.get_element(driver, job.ZIP_CODE)
    zip_code_field.send_keys(casedata['zip_code'])

    budget_hours_field = utils.get_element(driver, job.BUDGET_HOURS)
    budget_hours_field.clear()
    budget_hours_field.send_keys(casedata['budget_hrs'])


def update_data_package_info(driver, casedata):
    utils.sendkeys_element_by_locator(driver, job.PACKG_NAME, casedata['package_name'])
    time.sleep(5)


def navigate_create_job(driver):
    click_on_job_menu(driver)

    create_job_button = utils.get_element(driver, job.CREATE_JOB)
    create_job_button.click()


def click_on_job_menu(driver):
    job_menu = utils.get_element(driver, job.SELECT_JOB)
    job_menu.click()


def search_existing_job(driver, casedata):
    logging.info("Searching for existing job - {}".format(casedata['job_name']))
    utils.sendkeys_element_without_click(driver, job.SEARCH, casedata['job_name'])
    # logging.info()
    job_name = utils.get_element_text(driver, job.JOB_NAME_GET_FIRST_ROW)
    if job_name.strip() == (casedata['job_name']).strip():
        logging.info("Job Name successfully found")
        return True
    else:
        logging.error("No Job Name found")
        return False


def click_next_button(driver):
    next_button = utils.get_element(driver, job.NEXT)
    next_button.click()
    time.sleep(5)


# ----------- Functions for TestRail --->
def get_project_id(project_name):
    client = get_testrail_client()
    project_id = None
    projects = client.send_get('get_projects')
    for project in projects['projects']:
        if project['name'] == project_name:
            project_id = project['id']
            break
            # project_found_flag=True

    return project_id


def get_testrail_client():
    """Get the TestRail account credentials from the testrail. Env file"""

    # Get the TestRail Url
    _, _, _, _, testrail_username, testrail_password, testrail_url = get_json_file_data()
    testrail_url = testrail_url
    client = testrail.APIClient(testrail_url)
    # Get and set the TestRail User and Password
    client.user = testrail_username
    client.password = testrail_password

    return client


def get_run_id(client, test_run_name, project_name):
    run_id = None
    # client = get_testrail_client()
    project_id = get_project_id(project_name)

    try:
        test_runs = client.send_get('get_runs/%s' % project_id)

    except Exception:
        return None
    else:
        for test_run in test_runs['runs']:
            if test_run['name'] == test_run_name:
                run_id = test_run['id']
                break
        return run_id


def get_case_id(client, test_run_name, project_name):
    case_id = None
    # client = get_testrail_client()
    project_id = get_project_id(project_name)
    try:
        test_cases = client.send_get('get_cases/%s' % project_id)
    except Exception:
        return None
    else:
        for test_case in test_cases['cases']:
            if test_case['title'] == test_run_name:
                case_id = test_case['id']
                break
        return case_id


def update_testrail(test_case_name, result_flag, msg=""):
    """Update TestRail for a given run_id and case_id"""
    update_flag = False
    # Get the TestRail client account det,ails
    _, _, testrail_project_name, testrail_suitename, _, _, _ = get_json_file_data()
    client = get_testrail_client()
    case_id = get_case_id(client, test_case_name, testrail_project_name)
    run_id = get_run_id(client, testrail_suitename, testrail_project_name)
    status_id = result_flag
    if run_id is not None:
        try:
            client.send_post(
                'add_result_for_case/%s/%s' % (run_id, case_id),
                {'status_id': status_id, 'comment': msg})
        except Exception:
            return None
        else:
            logging.info('Updated test result for case: %s in test run: %s with msg:%s' % (case_id, run_id, msg))
    return update_flag


def get_status_id(result):
    status_id = None
    if result == "Passed":
        status_id = 1
    elif result == "Failed":
        status_id = 5
    elif result == "Blocked":
        status_id = 2
    elif result == "Retest":
        status_id = 4
    return status_id


def get_due_date():
    due_date = datetime.now() + timedelta(days=30)
    due_date = "%s-%s-%s" % (due_date.month, due_date.day, due_date.year)
    conftest.test_update_config("job_details", 'due_date', due_date)
    return due_date
