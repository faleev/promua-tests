#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Test cases for company registration on Prom.ua.'''

import pytest
import random
import string
from pages.promua_registration_page import RegistrationPage


def get_random_string(size=10, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))


def get_random_email(base_email):
    return ''.join([base_email.split('@')[0], '+' + get_random_string(5) + '@', base_email.split('@')[1]])


def generate_form_data():
    '''Generate pseudo random data for filling form fields.

    For any particular cases values ​​of certain fields could be changed inside test case
    (e.g. for specifying promo code or wrong email).
    '''
    data = {}

    data['company_name'] = u'Company ' + get_random_string()
    data['first_name'] = u'First name ' + get_random_string()
    data['last_name'] = u'Last name ' + get_random_string()
    data['email'] = get_random_email('johndoe@example.com')
    data['password'] = get_random_string()
    # Promotion code is empty by default.
    data['promo_code'] = ''

    return data


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_that_company_registration_form_is_present_on_page(mozwebqa):

    page = RegistrationPage(mozwebqa)
    page.go_to_page('/join-now?path_id=txt.register')

    result = page.get_absent_elements()

    assert len(result) == 0, 'List of absent elements: {0}.'.format(', '.join(result))


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_form_submit_with_correct_data(mozwebqa):

    data = generate_form_data()

    page = RegistrationPage(mozwebqa)
    page.go_to_page('/join-now?path_id=txt.register')

    page.fill_registration_form(**data)
    account_page = page.submit_registration_form()

    assert data['company_name'] in account_page.page_title, 'Company name "{0}" is not in page title. Current title: {1}'.format(data['company_name'], account_page.page_title)

    actual_company_name = account_page.get_company_name_from_field
    expected_company_name = data['company_name']
    assert actual_company_name == expected_company_name, 'Incorrect company name in the field on account page. Actual company name: {0}. Expected company name: {1}'.format(actual_company_name, expected_company_name)

    actual_contact_person_name = account_page.get_contact_person_name_from_field
    expected_contact_person_name = data['first_name'] + ' ' + data['last_name']
    assert actual_contact_person_name == expected_contact_person_name, 'Incorrect contact person name in the field on account page. Actual person name: {0}. Expected person name: {1}'.format(actual_contact_person_name, expected_contact_person_name)


@pytest.mark.nondestructive
def test_form_submit_with_incorrect_promocode(mozwebqa):

    data = generate_form_data()
    data['promo_code'] = get_random_string()

    page = RegistrationPage(mozwebqa)
    page.go_to_page('/join-now?path_id=txt.register')

    page.fill_registration_form(**data)
    page.click_on_submit_button()

    promo_error_msg = page.get_promocode_error_message
    assert promo_error_msg == u'Неверный промо-код. Укажите верное значение или оставьте поле пустым.', 'Promotion code error message is incorrect.'


@pytest.mark.nondestructive
@pytest.mark.parametrize(('email', 'message'), [('', u'Это обязательное поле.'),
                                                ('johndoe[at]example.com', u'email адрес должен содержать один символ @'),
                                                ('@example.com', u'Неправильное имя пользователя в email адресе (часть адреса до символа @: )'),
                                                ('johndoe@', u'Неверная доменная часть email адреса (часть после символа @: )'),
                                                ('johndoe@example', u'Неверная доменная часть email адреса (часть после символа @: example)'),
                                               ])
def test_form_submit_with_incorrect_email_format(mozwebqa, email, message):

    data = generate_form_data()
    data['email'] = email

    page = RegistrationPage(mozwebqa)
    page.go_to_page('/join-now?path_id=txt.register')

    page.fill_registration_form(**data)
    page.click_on_submit_button()

    email_error_msg = page.get_email_error_message

    assert email_error_msg == message, u'Incorrect error message for empty email field. Message: {0}'.format(email_error_msg)


@pytest.mark.nondestructive
def test_password_field_length_validation(mozwebqa):

    data = generate_form_data()
    data['password'] = '12'

    page = RegistrationPage(mozwebqa)
    page.go_to_page('/join-now?path_id=txt.register')

    page.fill_registration_form(**data)
    page.click_on_submit_button()

    password_error_msg = page.get_password_error_message
    expected_password_error_msg = u'Количество символов должно быть от 3 до 100.'
    assert password_error_msg == expected_password_error_msg, 'Password validation error message is incorrect. Message: {0}'.format(password_error_msg)


@pytest.mark.nondestructive
def test_form_submit_without_eula_agreement(mozwebqa):

    data = generate_form_data()

    page = RegistrationPage(mozwebqa)
    page.go_to_page('/join-now?path_id=txt.register')

    page.fill_registration_form(**data)
    page.uncheck_eula_agreement_checkbox()
    page.click_on_submit_button()

    eula_error_msg = page.get_eula_error_message
    expected_eula_error_msg = u'Вы должны принять правила'

    assert eula_error_msg == expected_eula_error_msg, 'Incorrect EULA error message. Message: {0}'.format(eula_error_msg)


@pytest.mark.nondestructive
def test_that_impossible_submit_empty_form(mozwebqa):

    page = RegistrationPage(mozwebqa)
    page.go_to_page('/join-now?path_id=txt.register')
    title = page.page_title

    page.clean_registration_form()
    page.click_on_submit_button()

    current_url = page.page_url
    assert current_url == page.base_url + '/join-now?path_id=txt.register', 'Page URL has been changed after submit of the empty form.'

    current_title = page.page_title
    assert current_title == title, 'Page title has been changed after submit of empty form.'
