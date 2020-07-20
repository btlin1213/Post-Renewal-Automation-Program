import time
import random 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# TO BE FILLED BY USER 
LOGIN_NAME = "to_be_filled"
PW = "to_be_filled"
USERNAME = "to_be_filled"
JOB_TITLE_1 = "to_be_filled"
JOB_TITLE_2 = "to_be_filled"

# CONSTANTS FOR YEEYI.COM
LOGIN_LINK = "http://yeeyi.com/forum/index.php?app=member&act=login" 
USERNAME_BOX_ID = "telTxtLogin"
PW_BOX_ID = "passShow"
LOGIN_BUTTON_ID = "postBtn"
THREAD_ID = "thread_content"
LISTINGS_XPATH = "//ul[@class='xl']/li"
MAX_LIFT_THREAD = 15
LIFT_THREAD = "k_refresh"
COMMENTS_FILE = "comments.txt"
COMMENT_ID = "post_reply"
COMMENT_TEXT_ID = "postmessage"
SUBMIT_BUTTON_ID = "postsubmit"
LIFT_THREAD_RESULT_ID = "fctrl_k_refresh"
SUCCESS_CLASS_NAME = "alert_right"
ERROR_CLASS_NAME = "alert_error"
CLOSE_BUTTON_ID = "closebtn"

def main(): 
    # CONTAINERS
    to_update = []
    # LOGIN 
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(LOGIN_LINK)
    username_box = driver.find_element_by_id(USERNAME_BOX_ID)
    username_box.send_keys(LOGIN_NAME)
    pw_box = driver.find_element_by_id(PW_BOX_ID)
    pw_box.send_keys(PW)
    login_button = driver.find_element_by_id(LOGIN_BUTTON_ID)
    login_button.click()
    # wait 10 seconds or until alert appears
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    # accept alert
    driver.switch_to.alert.accept()

    # NAVIGATE TO PROFILE 
    # wait 10 seconds or until username pops up 
    username_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT,USERNAME)))
    username_link.click()
    # wait 10 seconds or until threads pop up
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, THREAD_ID)))
    all_listings = driver.find_elements_by_xpath(LISTINGS_XPATH)

    # ADD THE LISTINGS TO UPDATE
    for listing in all_listings:
        text = listing.text
        if RECEPTIONIST in text or "测屏" in text:
            to_update.append(listing)

    # CALCULATE LIFT THREAD PER LISTING
    lift_per_listing = MAX_LIFT_THREAD // len(to_update)

    profile_window = driver.window_handles[0]
    # UPDATE THE LISTINGS
    for listing in to_update:
        # click it to open the page
        listing_link = driver.find_element_by_link_text(listing.text)
        listing_link.click()
        time.sleep(5)
        listing_window = driver.window_handles[1]
        driver.switch_to.window(listing_window)

        # COMMENT
        comment_on_post(driver)

        # LIFT THREAD
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, LIFT_THREAD)))
        # spam that thread lifting button 
        lift_thread_button = driver.find_element_by_id(LIFT_THREAD)
        lift_thread_button.click() 
        count = 1
        # detect error
        # wait 10 seconds or until alert appears
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, LIFT_THREAD_RESULT_ID)))
        potential_error = driver.find_elements_by_class_name(ERROR_CLASS_NAME) 
        potential_success = driver.find_elements_by_class_name(SUCCESS_CLASS_NAME)
        
        if len(potential_success) > 0:
            while count < lift_per_listing: 
                lift_thread_button.click()
                count += 1
                WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, CLOSE_BUTTON_ID))) 
                close_button = driver.find_element_by_id(CLOSE_BUTTON_ID)
                close_button.click()
                time.sleep(2)
        elif len(potential_error) > 0:
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, CLOSE_BUTTON_ID))) 
            close_button = driver.find_element_by_id(CLOSE_BUTTON_ID)
            close_button.click()

        # SWITCH POST 
        driver.close()
        driver.switch_to.window(profile_window)
        # wait 120 seconds before moving onto next post
        time.sleep(120)
    
    driver.quit()

    
def comment_on_post(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, COMMENT_ID)))
    comment_link = driver.find_element_by_id(COMMENT_ID)
    comment_link.click()
    # enter text
    WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID, COMMENT_TEXT_ID)))
    textbox = driver.find_element_by_id(COMMENT_TEXT_ID)
    comment = random_line(COMMENTS_FILE)
    textbox.send_keys(comment)
    submit_button = driver.find_element_by_id(SUBMIT_BUTTON_ID)
    submit_button.click()

def random_line(fname):
    lines = open(fname, "r").read().splitlines()
    return random.choice(lines)

main()