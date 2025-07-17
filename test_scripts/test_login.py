from time import sleep
import pytest

from POM.loginpage import *
from generic.data import *
from generic.verify import *

@pytest.mark.regression
@pytest.mark.smoke
def test_login_v(launch):
    driver = launch
    veriy_t(driver,'Login')
    login_cred = usn_pwd()
    l = LoginPage(driver)
    l.login_(login_cred[0][0], login_cred[0][1])
    veriy_t(driver, 'Home')

@pytest.mark.regression
def test_login_ivu(launch):
    driver = launch
    veriy_t(driver,'Login')
    login_cred = usn_pwd()
    l = LoginPage(driver)
    l.login_(login_cred[1][0], login_cred[1][1])
    veriy_t(driver, 'Home')

@pytest.mark.regression
def test_login_ivp(launch):
    driver = launch
    veriy_t(driver,'Login')
    login_cred = usn_pwd()
    l = LoginPage(driver)
    l.login_(login_cred[2][0], login_cred[2][1])
    veriy_t(driver, 'Home')

@pytest.mark.regression
def test_login_inup(launch):
    driver = launch
    veriy_t(driver,'Login')
    login_cred = usn_pwd()
    l = LoginPage(driver)
    l.login_(login_cred[3][0], login_cred[3][1])
    veriy_t(driver, 'Home')
