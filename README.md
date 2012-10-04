Selenium test cases for prom.ua
===============================

This repository contains Selenium-based test cases for registration form on the [prom.ua](http://prom.ua) portal.
In future this suite could be extended by adding new cases for various functional areas.

## Before you begin

Before start using this cases you need to prepare your local environment. Everything what you need are Python and Firefox browser. In case you already have Python and `pip`, just run the next command in the console:
  
    sudo pip install -r requirements.txt

After that you environment will be ready for running Selenium tests from this repository.

## Running tests locally

This test cases developed for running on the local enfironment just for illustration abilities of the testing framework. To run test cases locally execute the next command in the console (make sure you already in the repository root):

    py.test --driver=firefox --baseurl=http://prom.ua
    
At the same way this suite can be run using Internet Explorer, Google Chrome, using Selenium server, etc. For more information about possible configurations, please read documentation.

## License

Some part of this software is licensed under the [MPL](http://www.mozilla.org/MPL/2.0/) 2.0.
Another part which not covered by MPL could be reused under GNU GPL.
