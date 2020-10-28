from selenium import webdriver 
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options  
  
usr=input('Enter Email Id:')  
pwd=input('Enter Password:')  
  
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://www.reddit.com/login/') 
print ("Opened facebook") 
sleep(1) 
  
username_box = driver.find_element_by_css_selector("#loginUsername")
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1) 
  
password_box = driver.find_element_by_css_selector("#loginPassword")
password_box.send_keys(pwd) 
print ("Password entered") 
login_box = driver.find_element_by_css_selector("body > div > div > div.PageColumn.PageColumn__right > div > form > div.Onboarding__step.narrow > fieldset:nth-child(17) > button") 
login_box.click() 
  
print ("Done") 
input('Press anything to quit') 
driver.quit() 
print("Finished") 