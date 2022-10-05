from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep

PHONE_NO_LIST = [""]
PHONE_NO = PHONE_NO_LIST[1]

schools = ["University of Cape Town", "UCT", "CPUT", "Cape Peninsula"]

chrome_path = "C:\Development\chromedriver_win32\chromedriver.exe"

service = Service(chrome_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://bumble.com/en/the-buzz/bumble-web-the-same-experience-without-your-phone")
driver.maximize_window()

sign_in = driver.find_element(By.CSS_SELECTOR, '[aria-label="Sign In"]')
sign_in.click()
sleep(2)
sign_in_cell = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[3]/div')
sign_in_cell.click()
sleep(2)
phone_no = driver.find_element(By.ID, "phone")
phone_no.send_keys(PHONE_NO)
phone_no.send_keys(Keys.ENTER)

sleep(30)

while True:
    try:
        like = driver.find_element(By.CSS_SELECTOR, ".encounters-action__icon [data-qa-icon-name='floating-action-yes']")
        education = driver.find_element(By.CSS_SELECTOR, ".encounters-story-profile__education")
        school_text = education.text
        s_year = int(school_text.split()[-1])
        school_check = [school for school in schools if (school.upper() in school_text.upper())]
        print(school_text)
        if isinstance(s_year, int) and s_year >= 2022 and bool(school_check) is True:
            like.click()
            sleep(1)
        else:
            pass_ = driver.find_element(By.CSS_SELECTOR, ".encounters-action__icon [data-qa-icon-name='floating-action-no']")
            pass_.click()
            sleep(1)

    except ValueError:
        try:
            pass_ = driver.find_element(By.CSS_SELECTOR, ".encounters-action__icon [data-qa-icon-name='floating-action-no']")
            pass_.click()
            sleep(1)
        except NoSuchElementException:
            print("Adjust your filters 1")
            break
    except NoSuchElementException:
        try:
            like = driver.find_element(By.CSS_SELECTOR, ".encounters-action__icon [data-qa-icon-name='floating-action-yes']")
            occupation = driver.find_element(By.CSS_SELECTOR, ".encounters-story-profile__occupation")
            job_text = occupation.text
            job_year = int(job_text.split()[-1])
            job_check = [job for job in schools if (job.upper() in job_text.upper())]
            print(job_text)
            if isinstance(job_year, int) and job_year >= 2022 and bool(job_check) is True:
                like.click()
                sleep(1)
            else:
                pass_ = driver.find_element(By.CSS_SELECTOR, ".encounters-action__icon [data-qa-icon-name='floating-action-no']")
                pass_.click()
                sleep(1)

        except ValueError:
            try:
                pass_ = driver.find_element(By.CSS_SELECTOR, ".encounters-action__icon [data-qa-icon-name='floating-action-no']")
                pass_.click()
                sleep(1)
            except NoSuchElementException:
                print("Adjust your filters 2")
                break

        except NoSuchElementException:
            try:
                pass_ = driver.find_element(By.CSS_SELECTOR, ".encounters-action__icon [data-qa-icon-name='floating-action-no']")
                pass_.click()
                sleep(1)
            except NoSuchElementException:
                print("Upgrade your plan")
                # driver.quit()
                break
    except ElementClickInterceptedException:
        print("You're out of Potentials")
        # driver.quit()
        break

    sleep(3)



