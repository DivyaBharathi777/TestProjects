#!/usr/bin/python

from PageObject_About import *
from selenium import webdriver
from utilities_custom_usage import *

chrome_driver_path_used = '.\\chromedriver.exe'
delay_min = 3  # sec
delay_medium = 5  # sec
delay_max = 9  # sec


class Implementation:
    def __init__(self):
        pass

    def initialize_browser_setup(self, list_var):
        print('Invoking chrome browser')
        list_var.append(webdriver.Chrome(executable_path=chrome_driver_path_used))
        list_var[0].maximize_window()
        list_var.append('success')
        return True

    def open_About_page(self, list_var, url_about_page):
        print('Opening the url and about page and navigating to our-people ')
        web_driver = list_var[0]
        about_page = AboutPage(web_driver)
        about_page.method_launch_about_page_url(web_driver, url_about_page)
        list_var.append('success')
        return

    def search_for_a_person(self, list_var, person_name ):
        print('Searching for a person named ' +person_name+ ' and vaidating')
        web_driver = list_var[0]
        about_page = AboutPage(web_driver)
        about_page.method_search_a_person(web_driver, person_name)
        list_var.append('success')
        return

    def validate_profile(self, list_var, person_name):
        print('Validating person profile: ' +person_name)
        web_driver = list_var[0]
        about_page = AboutPage(web_driver)
        about_page.method_validate_profile_details(web_driver, person_name)
        list_var.append('success')
        return

    def sort_by_options(self, list_var, ):
        print('Sort by options and validate')
        web_driver = list_var[0]
        about_page = AboutPage(web_driver)
        about_page.method_sort_by_option(web_driver)
        list_var.append('success')
        return

    def final_verification(self, list_var, ):
        print('Performing final verification for each step pass or fail')
        chrome_web_driver = list_var[0]
        chrome_web_driver.close()
        chrome_web_driver.quit()
        compare_success = UtilitiesCustom()
        compare_success.method_utilities_compare_all_success_failure(list_var)
        return


impl_obj = Implementation()
