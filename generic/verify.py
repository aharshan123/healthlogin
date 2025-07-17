

# def verify_title(etitle):
#     driver.implicitly_wait(10)
#     assert etitle == driver.title f"{driver.title} page not displayed"
#     print(f"{driver.title} page is displayed")


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def veriy_t(driver,t):
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_is(t))
    except:
        driver.save_screenshot(r'C:\Users\DELL\Desktop\pythonsel\testproject\heathmrs\healthmrs\Screenshots\failure.png')
        print("not displayed")


