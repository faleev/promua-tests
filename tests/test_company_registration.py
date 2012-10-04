#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Test cases for company registration on Prom.ua.'''

import pytest
from pages.promua_registration_page import RegistrationPage


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_that_company_registration_form_is_present_on_page(mozwebqa):

    page = RegistrationPage(mozwebqa)
    page.go_to_page('/join-now?path_id=txt.register')

    result = page.get_absent_elements()

    assert len(result) != 0, 'List of absent elements: {0}.'.format(', '.join(result))
