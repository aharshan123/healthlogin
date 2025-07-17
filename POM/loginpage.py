class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.__username = "//input[@id = 'username']"
        self.__password = "//input[@id = 'password']"
        self.__registration_desk = "//li[. = 'Registration Desk']"
        self.__login = "//input[@value = 'Log In']"


    def login_(self,u, p):
        self.driver.find_element("xpath", self.__username).send_keys(u)
        self.driver.find_element("xpath", self.__password).send_keys(p)
        self.driver.find_element("xpath", self.__registration_desk).click()
        self.driver.find_element("xpath", self.__login).click()

    # def username(self, usn):
    #     self.driver.find_element("xpath", "//input[@id = 'username']").send_keys(usn)
    #
    # def password(self, pwd):
    #     self.driver.find_element("xpath", "//input[@id = 'password']").send_keys(pwd)
    #
    #
    # def registration_desk(self):
    #     self.driver.find_element("xpath", "//li[. = 'Registration Desk']").click()


    # def login(self):
    #     self.driver.find_element("xpath", "//input[@value = 'Log In']").click()


