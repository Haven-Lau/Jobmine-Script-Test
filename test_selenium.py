from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

USERNAME = ""
PASSWORD = ""
discipline_1 = "ENG-Computer"
discipline_2 = "ENG-Software"
discipline_3 = "MATH-Computer Science"
discipline_list = [discipline_1, discipline_2, discipline_3]

browser = webdriver.Firefox()

browser.get('https://jobmine.ccol.uwaterloo.ca/SS/signon.html')

element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "userid"))
    	)

userid = browser.find_element_by_name("userid")
userid.send_keys(USERNAME)

pwd = browser.find_element_by_name("pwd")
pwd.send_keys(PASSWORD)

loginbtn = browser.find_element_by_name("submit")
loginbtn.click()

time.sleep(1)

browser.get('https://jobmine.ccol.uwaterloo.ca/psp/SS/EMPLOYEE/WORK/c/UW_CO_STUDENTS.UW_CO_JOBSRCH.GBL?pslnkid=UW_CO_JOBSRCH_LINK&FolderPath=PORTAL_ROOT_OBJECT.UW_CO_JOBSRCH_LINK&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder')

browser.switch_to.frame(browser.find_element_by_id("ptifrmtgtframe"))

# Choose disciplines
for x in xrange(0,3):
    select_discipline = Select(browser.find_element_by_id('UW_CO_JOBSRCH_UW_CO_ADV_DISCP%d' % (x + 1)))
    select_discipline.select_by_visible_text(discipline_list[x])

searchbtn = browser.find_element_by_xpath('//*[@id="UW_CO_JOBSRCHDW_UW_CO_DW_SRCHBTN"]')
searchbtn.click()

element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "UW_CO_JOBTITLE_HL$1")))

for inc in xrange(0,4):
    jobtitle_id = 'UW_CO_JOBTITLE_HL$%d' % (inc)
    jobtitle = browser.find_element_by_id(jobtitle_id)
    time.sleep(1)
    jobtitle.click()

browser.switch_to_default_content()
