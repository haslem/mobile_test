# from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
# from selenium.webdriver.common.keys import Keys
import s3_functions as func



def timeOut(delay = 100000000, tick = 1):
	#default delay 3 s
	for i in range(int(delay * tick)):
	    pass





##real
# desired_cap = {
#   "deviceName": "4df134143e934f4d",
#   "platformName": "Android",
#   "app": "C:\\my\\auto\\mobile\\mapy-cz-6-5-2.apk"
# }


##emu
#somehow also works on real device
# desired_cap = {
#   "platformName": "Android",
#   "deviceName": "Android Emulator",
#   #"deviceName": "emulator-5554",
#   "appPackage": "cz.seznam.mapy",
#   "appWaitActivity": "cz.seznam.mapy.MapActivity",
#   "app": "C:\\my\\auto\\mobile\\mapy-cz-6-5-2.apk",
#   "autoGrantPermissions": "true"
# }




# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
# print('start wait')
# driver.implicitly_wait(30)
# print('end wait')




#go to map
#timeOut(tick = 2.0)
func.goToMap()



# #go to map catalog
# func.goToCatalog()





#route planning
#menu
#timeOut(tick = 2.0)
func.menu()
# elem = driver.find_element_by_id('cz.seznam.mapy:id/menuButton')
# driver.implicitly_wait(10)
# timeOut()
# elem.click()
# print('menu clicked')

# #route planing
# elem = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[3]')
# elem.click()



# #close navigation
# elem = driver.find_element_by_id('cz.seznam.mapy:id/closeButton')
# elem.click()


# try:
# 	elem = driver.find_element_by_id('cz.seznam.mapy:id/content')
# 	print ('Error menu')
# except:
# 	print ('menu dissapear ok')	











		

# #search
# elem = driver.find_element_by_id('cz.seznam.mapy:id/searchButton')
# elem.click()
# print('searchButton clicked')



# elem = driver.find_element_by_id('cz.seznam.mapy:id/input')
# driver.implicitly_wait(5)
# elem.send_keys('seznam')
# print(type(elem))
# driver.implicitly_wait(5)


# driver.execute_script('mobile: performEditorAction', {'action': 'search'})
# driver.implicitly_wait(5)




# #scroll
# scroll = TouchAction(driver)

# scroll.press(x=480, y=761).move_to(x=469, y=430).release().perform()
# print ('scrolled')





# #tap
# TouchAction(driver).tap(x=407, y=304).perform()






#drag and drop
# timeOut()
# dd = TouchAction(driver)
# dd.long_press(x=407, y=304).move_to(x=505, y=714).release().perform()
# dd.press('cz.seznam.mapy:id/routePlannerView').move_to(x=555, y=143).release().perform()







#cz.seznam.mapy:id/accountArrow
#	cz.seznam.mapy:id/searchButton

#login check
func.login()

	

#cz.seznam.mapy:id/accountName


handle_one_size = func.driver.get_window_size()
print(handle_one_size)
