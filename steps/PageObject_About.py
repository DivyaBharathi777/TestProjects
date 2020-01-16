#!/usr/bin/python

import time
from page_objects import PageObject, PageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

delay_time = 7

class AboutPage(PageObject):

    person_name = ''
    condition_check = PageElement(xpath="//button[text() = 'Continue']")
    condition_check2 = PageElement(xpath="//a[text() = 'Continue']")
    search_input = PageElement(xpath="//input[@name='search']")
    search_click = PageElement(xpath="//input[@name='search']/following::span/img")
    person_profile = PageElement(xpath="//h2[text() ='Chloe Allan']")
    profile_click = PageElement(xpath="//h2[text() ='Chloe Allan']/preceding-sibling::div/img")
    profile_check = PageElement(xpath="//h3[text() = 'Chloe Allan']")
    select_click = PageElement(xpath="//*[@class='jq-selectbox__trigger-arrow']")
    select_open = PageElement(xpath="//*[@class='jq-selectbox__dropdown']")
    team_list = PageElement(xpath="//h2[@class='team-item_title']")


    def method_launch_about_page_url(self, web_driver, url_about_page):

        #Launching the browser and navigating to the URL
        self.get(url_about_page)
        WebDriverWait(web_driver, delay_time).until(expected_conditions.title_contains('Our people'))

        #accept conditions and continue
        WebDriverWait(web_driver, delay_time).until(expected_conditions.visibility_of(self.condition_check))
        self.condition_check.click()
        WebDriverWait(web_driver, delay_time).until(expected_conditions.visibility_of(self.condition_check2))
        self.condition_check2.click()
        return

    def method_search_a_person(self, web_driver, person_name):

        #search for a person by clearing the input field and passing name
        WebDriverWait(web_driver, delay_time).until(expected_conditions.visibility_of(self.search_input))
        self.search_input.clear()
        self.search_input = person_name
        self.search_click.click()
        web_driver.refresh()
        web_driver.execute_script("window.scroll(0,400)")

        #validating the person data
        WebDriverWait(web_driver, delay_time).until(expected_conditions.visibility_of(self.person_profile))
        actual_name = self.person_profile.text
        if person_name != actual_name:
            raise Exception(' ******* Expected "' + person_name + '" is not matching with  ' + actual_name)
        else:
            print("Validation successful: Search result is as expected")
        return

    def method_validate_profile_details(self,web_driver,person_name):

        #open a person profile through search
        web_driver.refresh()
        WebDriverWait(web_driver, delay_time).until(expected_conditions.visibility_of(self.search_input))
        self.search_input.clear()
        WebDriverWait(web_driver, delay_time).until(expected_conditions.visibility_of(self.search_input))
        self.search_input = person_name
        self.search_click.click()

        #Click on the image link ofthe profile
        web_driver.execute_script("window.scroll(0,700)")
        WebDriverWait(web_driver, delay_time).until(expected_conditions.visibility_of(self.person_profile))
        self.profile_click.click()

        #Validate the profile data
        WebDriverWait(web_driver, delay_time).until(expected_conditions.visibility_of(self.profile_check))
        actual_title = self.profile_check.text
        if person_name != actual_title:
            raise Exception(' ******* Expected "' + person_name + '" is not matching with  ' + actual_title)
        else:
            print("Validation successful: Search result is as expected")
        web_driver.execute_script("window.history.go(-2)")
        return

    def scroll_end(self,web_driver):

        # scroll through dynamic page till the end
        lst_ht = web_driver.execute_script("return document.body.scrollHeight")
        while True:
            web_driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(0.3)
            nw_ht = web_driver.execute_script("return document.body.scrollHeight")
            if nw_ht == lst_ht:
                break
            lst_ht = nw_ht
        web_driver.execute_script("window.scroll(0,400)")
        return

    def method_sort_by_option(self,web_driver):

        self.asc_list = []
        self.desc_list = []
        self.mem_lis = []
        self.mem_list = []

        #get ordered list of people for validation
        WebDriverWait(web_driver, delay_time).until(expected_conditions.visibility_of(self.search_input))
        self.search_input.clear()
        self.scroll_end(web_driver)
        WebDriverWait(web_driver, delay_time).until(expected_conditions.visibility_of(self.team_list))
        self.team_lis = web_driver.find_elements_by_xpath("//h2[@class='team-item_title']")
        for self.mem in self.team_lis:
            self.mem_lis.append(self.mem.text)
        self.asc_list = self.mem_lis
        self.desc_list = self.mem_lis[::-1]

        # getting the sort by options
        WebDriverWait(web_driver, delay_time).until(expected_conditions.visibility_of(self.search_input))
        self.select_click.click()
        WebDriverWait(web_driver, delay_time).until(expected_conditions.visibility_of(self.select_open))
        self.dropdown_list = web_driver.find_elements_by_xpath("//div[@class='jq-selectbox__dropdown']/ul/li[contains(text(),'Sort')]")

        # iterate through two sort and validate
        for self.item in self.dropdown_list:
            order = self.item.text
            self.item.click()
            time.sleep(5) # time used as my home network is very slow
            WebDriverWait(web_driver, delay_time).until(expected_conditions.visibility_of(self.team_list))
            self.scroll_end(web_driver)

            WebDriverWait(web_driver, delay_time).until(expected_conditions.visibility_of(self.team_list))
            self.team_lis = web_driver.find_elements_by_xpath("//h2[@class='team-item_title']")
            for self.member in self.team_lis:
                self.mem_list.append(self.member.text)

            if (order == "Sort A-Z" and self.mem_list == self.asc_list):
                print("Success: sort of " + order + " is ordered as expected")
            elif (order == "Sort Z-A" and self.mem_list == self.desc_list):
                print("Success: sort of " + order + " is ordered as expected")
            else:
                print("Failure: sort of " + order + " is not Ordered as expected")
            self.mem_list[:] = []
            self.select_click.click()
            WebDriverWait(web_driver, delay_time).until(expected_conditions.visibility_of(self.select_open))

        return



