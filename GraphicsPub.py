import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


#This has been tested using chrome, I have not tested it with any other web browser, be sure to consult slenium doc for more. 
browser = webdriver.Chrome('Driver path') """This is where you'll key in the drivever path where you installed the chromedriver for selenium.
                                             for information on this driver and download go to https://chromedriver.chromium.org/getting-started
                                             the path should look like 'C:\\user\\...\\chromdriver.exe'. For mac and unix based users remember it 
                                             should look like 'drive/user/.../chromedriver.exe'"""

#Grab best buy webpage
browser.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")
#TestBed
#browser.get("https://www.bestbuy.com/site/insignia-aaa-batteries-8-pack/5491600.p?skuId=5491600") #Use this to Test the program. It won't buy it, but should get u to the end. 
#Just remove the hashtage above, and place one in front of the actual RTX SKU page. 
buyButton = False

while not buyButton:
    try:
        #time.sleep(2)  
        """each time.sleep call is used to prevent code from loading before the webpage does.
           if you find that the code is executing before your page can load try increasing the sleep increment by
           1, I.E. time.sleep(3) instead of time.sleep(2). Remember if # proceeds the statement it will not be read.
           See python documentation for more."""
        
        #If this works the button is currently sold out
        addToCartButton = addButton = browser.find_element_by_class_name("btn-disabled")

        print('not in stock')
        

        #this refreshes the page 
        #time.sleep(1)      #Remove the hashtage before running if you're worried about the program getting flagged, shouldn't be a problem though. 
        
        browser.refresh()
    except:

        addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")

        print('The buy Button was clicked')
        addToCartBtn.click()
        #time.sleep(3)
        element = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))) #Trying something new. 
        """plsWaitBtn = browser.find_element_by_class_name("overlayTrigger")
        while plsWaitBtn == True:
            time.sleep(1)
        addToCartBtn.click()"""
        #time.sleep(2)
        buyButton=True

while buyButton == True:
    time.sleep(2)

    goTo = addButton = browser.find_element_by_class_name("go-to-cart-button")
    goTo.click()
    goTo=False

    time.sleep(2)

    CheckOut = addButton = browser.find_element_by_class_name("btn-primary")
    CheckOut.click()

    """Auto insert the username info and password, then click the checkout button."""
    time.sleep(1)

    AddUsername = browser.find_element_by_id('fld-e')
    AddUsername.click()

    AddUsername.send_keys("email") #Your email address should be listed here like "JMahoney@gmail.com" or whatever

    AddPassword = browser.find_element_by_id('fld-p1')
    AddPassword.click()

    AddPassword.send_keys("password")   #Same thing, your password should look like, "JayzTwoChains33"
    
    #These two send keys will automatically fill in your log in info and sign you to checkout. 

    SignIn = addButton = browser.find_element_by_class_name('cia-form__controls__submit')
    SignIn.click()
    break
    #If the program makes it to the end, Be sure to get down to placing your order ASAP, even with this, the odds are still stacked against you.
    #You just have a better chance now is all. Good luck and happy hunting. No this cannot be used to buy multiple in a drop, I designed it that way.
    #This code may only be moddified with the explicit consent of the author. 
