
from logging import error, exception
from selenium.webdriver.common.by import By
import time
import os.path

class publitas_QA_slideshow:
   
    image_source = (By.CSS_SELECTOR,"div.current img")
    right_button = (By.XPATH, "//*[@id='react_root']/div/div[1]/button[2]")
    left_buttom = (By.XPATH, "//*[@id='react_root']/div/div[1]/button[1]")
    slide_counter = (By.XPATH,"//*[@id='react_root']/div/div[2]") #get the text 
    pic_display =(By.CSS_SELECTOR,'div.current')



    def __init__(self,driver):
        self.driver = driver




    def get_display_pic(self,driver):
        return driver.find_element(*publitas_QA_slideshow.pic_display)

    def get_button_right(self,driver):
        return driver.find_element(*publitas_QA_slideshow.right_button)

    def get_button_left(self,driver):
        return driver.find_element(*publitas_QA_slideshow.left_buttom)

    def get_count_slider(self,driver):
        return driver.find_element(*publitas_QA_slideshow.slide_counter)

    def get_image_source(self,driver):
        return driver.find_element(*publitas_QA_slideshow.image_source)


# check if the site opened with correct title
    def action_check_page_title(self):
        Title = self.driver.title
        assert Title == 'Publitas QA Challenge'
        
        time.sleep(2)
    

    def action_check_if_the_right_click_display_img(self):
        pictures = self.get_display_pic(self.driver)
        time.sleep(2)

        right_tbn = self.get_button_right(self.driver)

        ## if I don't know the num of images ##

        # i=0
        # while right_tbn.is_enabled():
        #     if pictures.is_displayed():
        #         assert pictures.get_attribute('aria-hidden') == 'false'
        #         i=i+1
        #         count_img = self.get_count_slider(self.driver).text
        #         if count_img == str(i)+" / 4":
        #             print(count_img)
        #             pass
        #         else:
        #             print('wrong counter under the slide',count_img)

        #         print('image display',i)
        #         right_tbn.click()
        #         time.sleep(2)
                
        #         pictures = self.get_display_pic(self.driver)
        #     else:
        #         print('not display')

        #  loop for click the right button to see all 4 images in the slideshow 
        i=0
        while i < 4:
            if pictures.is_displayed():
                assert pictures.get_attribute('aria-hidden') == 'false'
                # save the image source1
                image1_src = self.get_image_source(self.driver).get_attribute('src')
                print('image display',i,'\n the scource for image is:',image1_src)
                right_tbn.click()
                time.sleep(1)
                pictures = self.get_display_pic(self.driver)
                image2_src = self.get_image_source(self.driver).get_attribute('src')
                if image1_src == image2_src:
                    print('the first image still display and the click disabled')
                    break
                else:
                    continue
        

## checks if the left click is not changing the fisrt image in the slide 
    def action_check_if_the_left_click_display_img(self):

        time.sleep(2)

        left_tbn = self.get_button_left(self.driver)
        #  first need to click to ensure I have displayed image

        left_tbn.click()
        pictures = self.get_display_pic(self.driver)
        # the numger of images known as 4 and we check if extra  left  click have error with display img 
        i=0
        while i < 4:
            if pictures.is_displayed():
                assert pictures.get_attribute('aria-hidden') == 'false'
                # save the image source in para1
                image1_src = self.get_image_source(self.driver).get_attribute('src')
                print('image display',i,'\n the scource for image is:',image1_src)
                left_tbn.click()
                time.sleep(1)
                pictures = self.get_display_pic(self.driver)
                # save the next image in para2
                image2_src = self.get_image_source(self.driver).get_attribute('src')
                if image1_src == image2_src:
                    print('the first image still display and the click disabled')
                    break
                elif image1_src != image2_src: 
                    continue
                else:
                    raise Exception
                    
## checks the image counter text for first image and the last image
    def action_check_the_counter_txt_under_last_img(self):

# if I know that the text sould be from 1/4 to first image or  4/4 to last image

        count_img = self.get_count_slider(self.driver).text
        if count_img == '4 / 4' or count_img == '1 / 4':
            print(count_img)
            pass
        else:
            print('wrong counter under the slide',count_img)
            raise Exception

