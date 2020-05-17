import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class test01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)

    def testTwt(self):
        self.driver.get("https://twitter.com")
        self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/a/div").click()
        self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/label/div/div[2]/div/input").send_keys("holajorgeee")
        self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[4]/span").click()
        twitter_verification_window = self.driver.current_window_handle
        self.driver.execute_script('''window.open("https://correotemporal.org/","_blank")''')
        temporal_email_window = [window for window in  self.driver.window_handles if window != twitter_verification_window] [0]
        self.driver.switch_to_window(temporal_email_window)
        emailText=''
        while emailText == '':
            print("Esperando a generar correo electronico")
            time.sleep(0.5)
            emailText= self.driver.find_element(By.XPATH,"//*[@id='emailtemporal']").get_attribute('value')

        self.driver.switch_to_window(twitter_verification_window)  #se vuelve a la ventana de login twiter
        self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/label/div/div[2]/div/input").send_keys(emailText)
        self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/div/span/span").click()
        self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/div/span/span").click()
        self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div[2]/div/div/div[4]/div/span/span")
        time.sleep(10)

    def tearDown(self):
            pass
if __name__ == '__main__':
    unittest.main()
