# from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
# from selenium.webdriver.common.keys import Keys
import s3_functions as func



def timeOut(delay = 100000000, tick = 1):
	#default delay 3 s
	for i in range(int(delay * tick)):
	    pass


#func.connect()

func.all_elements()
#go to map
timeOut(tick = 2.0)
func.goToMap()



# #go to map catalog
# func.goToCatalog()
# timeOut()
# func.scroll()



func.all_elements()


#menu
timeOut(tick = 2.0)
func.menu()



#func.navigation()





# #search
# func.search_button()

# timeOut()
# func.search_input('seznam')








#login check
func.login()

	


#timeOut()
#func.menuMyMaps()
#timeOut(tick = 3)










#func.TC486()
#func.TC487()


handle_one_size = func.driver.get_window_size()
print(handle_one_size)
