#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException


class Page(object):
    '''Base class for all Pages

    This class contains core methods that we want to use throughout the page
    objects. By inheritance these methods are accessible in other page objects.
    It is important not to include locators or site specific functions in this
    class. Generally the methods in this class are common across all project and
    don't change often.
    '''

    def __init__(self, testsetup):
        '''Constructor'''
        self.testsetup = testsetup
        self.base_url = testsetup.base_url
        self.selenium = testsetup.selenium

    def go_to_home_page(self):
        self.selenium.get(self.base_url)

    def go_to_page(self, url):
        self.selenium.get(self.base_url + url)

    @property
    def page_url(self):
        return self.selenium.current_url

    @property
    def page_title(self):
        WebDriverWait(self.selenium, 10).until(lambda s: self.selenium.title)
        return self.selenium.title

    def is_element_present(self, *locator):
        self.selenium.implicitly_wait(0)
        try:
            self.selenium.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            # set back to where you once belonged
            self.selenium.implicitly_wait(self.testsetup.default_implicit_wait)

    def is_element_visible(self, *locator):
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except NoSuchElementException, ElementNotVisibleException:
            return False
