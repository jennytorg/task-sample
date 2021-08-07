from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

from pageObject_publitas.slideshow import publitas_QA_slideshow

from selenium.webdriver.common.keys import Keys


class Test_images_count_slideshow:

    @classmethod
    def setup_class(cls):
        global driver
        global slide_area
        
        driver = webdriver.Chrome(ChromeDriverManager().install())
        time.sleep(3)
        driver.get('http://challenge.publitas.com/qa.html')
        
        time.sleep(1)
        driver.maximize_window()
        driver.implicitly_wait(10)

        slide_area = publitas_QA_slideshow(driver)
        
    
    @classmethod
    def teardown_class(cls):
        driver.quit()
         
    # vefiry the correct page loaded (task = should pass)     
    def test_check_the_page_title(self):
        try:
            slide_area.action_check_page_title()
            
        except Exception as e:  
            print(e)
            pytest.fail(str(e))

# checkes if after the last click there are image (task = should fail)
    def test_click_right_arrow_and_check_image_displayed(self):
        try:
            slide_area.action_check_if_the_right_click_display_img()
            
        except Exception as e:
            print(e)
            driver.get_screenshot_as_file('C:/img.jpg')
            pytest.fail(str(e))

#  the slider limit should be from 1/4 to 4/4  ( task = should fail)
    def test_verify_the_counter_under_image_as_expected(self):
        try:
            slide_area.action_check_the_counter_txt_under_last_img()
            
        except Exception as e:
            print(e)
            pytest.fail(str(e))

#  verify that the first img not change when click (task = should pass)
   
# option 2 - run this test after login again with new browser session (than the code can be shorter)

    def test_click_left_arrow_and_check_image_displayed(self):
        try:
            slide_area.action_check_if_the_left_click_display_img()
            
        except Exception as e:
            print(e)
            pytest.fail(str(e))