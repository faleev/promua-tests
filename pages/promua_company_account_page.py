#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Page object for Prom.ua Registration page.'''

from pages.page import Page
from selenium.webdriver.common.by import By


class CompanyAccountPage(Page):

    _company_name_field_locator = (By.ID, 'name')
    _contact_person_field_locator = (By.ID, 'contact_person')

    @property
    def get_company_name_from_field(self):
        return self.selenium.find_element(*self._company_name_field_locator).get_attribute('value')

    @property
    def get_contact_person_name_from_field(self):
        return self.selenium.find_element(*self._contact_person_field_locator).get_attribute('value')
