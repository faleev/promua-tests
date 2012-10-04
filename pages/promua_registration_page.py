#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Page object for Prom.ua Registration page.'''

from pages.page import Page
from selenium.webdriver.common.by import By


class RegistrationPage(Page):

    _registration_form_fieldset_locator = (By.CSS_SELECTOR, '#registration_form > div > div > fieldset')

    _company_name_field_locator = (By.ID, 'company_name')
    _company_name_error_msg_locator = (By.ID, 'company_name_error')

    _first_name_field_locator = (By.ID, 'first_name')
    _first_name_error_msg_locator = (By.ID, 'first_name_error')

    _last_name_field_locator = (By.ID, 'last_name')
    _last_name_error_msg_locator = (By.ID, 'last_name_error')

    _email_field_locator = (By.ID, 'email')
    _email_field_error_msg_locator = (By.ID, 'email_error')
    _email_help_popup_locator = (By.CSS_SELECTOR, '#email_line .icon-help')

    _password_field_locator = (By.ID, 'password')
    _password_field_error_msg_locator = (By.ID, 'password_error')
    _password_help_popup_locator = (By.CSS_SELECTOR, '#password_line .icon-help')

    _agreement_checkbox_locator = (By.ID, 'agreement')
    _agreement_error_msg_locator = (By.ID, 'agreement_error')

    _promocode_link_locator = (By.LINK_TEXT, 'Промо-код')
    _promocode_field_locator = (By.ID, 'promotion')
    _promocode_error_msg_locator = (By.ID, 'promotion_error')

    _popup_layout_locator = (By.CSS_SELECTOR, '.b-popup_layout_with-closer')
    _popup_layout_close_btn_locator = (By.CSS_SELECTOR, '.b-popup__close')

    _registration_button_locator = (By.ID, 'register_button')

    def get_absent_elements(self):

        result = {}

        result['company_name'] = self.is_element_visible(*self._company_name_field_locator)
        result['first_name'] = self.is_element_visible(*self._first_name_field_locator)
        result['laft_name'] = self.is_element_visible(*self._last_name_field_locator)
        result['email'] = self.is_element_visible(*self._email_field_locator)
        result['password'] = self.is_element_visible(*self._password_field_locator)
        result['agreement'] = self.is_element_visible(*self._agreement_checkbox_locator)
        result['button'] = self.is_element_visible(*self._registration_button_locator)

        absent_elements = [key for key in result.iterkeys() if not result[key]]
        if absent_elements:
            return absent_elements
        else:
            return []
