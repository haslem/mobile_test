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
func.goToMap()
# elem = driver.find_element_by_id('cz.seznam.mapy:id/goToMapButton')
# elem.click()
# #print('start wait')
# driver.implicitly_wait(10)
# #print('end wait')
# print('goToMapButton clicked')




#go to map catalog
# elem = driver.find_element_by_id('cz.seznam.mapy:id/downloadMapsButton')
# elem.click()
# print('start wait')
# driver.implicitly_wait(10)
# print('end wait')




#route planning
#menu
elem = driver.find_element_by_id('cz.seznam.mapy:id/menuButton')
driver.implicitly_wait(10)
timeOut()
elem.click()
print('menu clicked')

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

timeOut()
TouchAction(driver).tap(x=410, y=562).perform()



elem = driver.find_element_by_id('cz.seznam.mapy:id/webView')
#print (elem.get_attribute('innerHTML'))
contexts = driver.contexts
print(contexts)

current = driver.current_context
print(current)


#login
timeOut(tick = 2.0)
TouchAction(driver).tap(x=210, y=643).perform()
timeOut(tick = 2.0)
TouchAction(driver).tap(x=568, y=1081).perform()
timeOut(tick = 2.0)
TouchAction(driver).tap(x=72, y=979).perform()
TouchAction(driver).tap(x=676, y=888).perform()
TouchAction(driver).tap(x=394, y=897).perform()
TouchAction(driver).tap(x=317, y=891).perform()
TouchAction(driver).tap(x=177, y=891).perform()
TouchAction(driver).tap(x=138, y=979).perform()
TouchAction(driver).tap(x=320, y=891).perform()
TouchAction(driver).tap(x=538, y=886).perform()
TouchAction(driver).tap(x=499, y=1073).perform()
TouchAction(driver).tap(x=356, y=985).perform()
TouchAction(driver).tap(x=111, y=798).perform()
TouchAction(driver).tap(x=662, y=1161).perform()



#pass
TouchAction(driver).tap(x=188, y=593).perform()
timeOut(tick = 2.0)
TouchAction(driver).tap(x=324, y=894).perform()
TouchAction(driver).tap(x=180, y=892).perform()
TouchAction(driver).tap(x=144, y=980).perform()
TouchAction(driver).tap(x=324, y=883).perform()
TouchAction(driver).tap(x=537, y=892).perform()
TouchAction(driver).tap(x=498, y=1077).perform()
timeOut(tick = 2.0)
TouchAction(driver).tap(x=354, y=980).perform()
TouchAction(driver).tap(x=568, y=1072).perform()
TouchAction(driver).tap(x=72, y=983).perform()
TouchAction(driver).tap(x=678, y=889).perform()
TouchAction(driver).tap(x=390, y=886).perform()
timeOut(tick = 2.0)
TouchAction(driver).tap(x=667, y=1166).perform()

#press login button
TouchAction(driver).tap(x=402, y=847).perform()




elem = driver.find_element_by_id('cz.seznam.mapy:id/userName')
user_name = elem.get_attribute('text')

elem = driver.find_element_by_id('cz.seznam.mapy:id/accountName')
account_name = elem.get_attribute('text')


if user_name == 'mapytesting2' and account_name == 'mapytesting2@seznam.cz':
	print ('Log in success')
else:
    print('Log in failed')	

#cz.seznam.mapy:id/accountName


handle_one_size = driver.get_window_size()
print(handle_one_size)
