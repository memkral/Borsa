from pyvirtualdisplay  import Display
from selenium import webdriver

class screenshot():
    
    def ekrangoruntusu1():
        print("sa")
        with Display():
            print("display içindeyiiiim")
            browser = webdriver.Firefox()
        
            try:
                browser.get('http://www.google.com')
                print(browser.title)
                browser.save_screenshot("screenshot.png") # bu kısmı ben ekledim, bu kod selenium modülünün bir fonksiyonu. Bu kod o anda ki ekranın resmini kayıt ediyor.
        
            finally:
                browser.quit()
                
    def ekrangoruntusu2():
        print("ekrangoruntusu2 içindeyiiiim")
        browser = webdriver.Chrome()
    
        
        browser.get('http://www.google.com')
        print(browser.title)
        browser.save_screenshot("screenshot.png") # bu kısmı ben ekledim, bu kod selenium modülünün bir fonksiyonu. Bu kod o anda ki ekranın resmini kayıt ediyor.

            
          
