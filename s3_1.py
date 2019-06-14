from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#import s3_functions as func



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
desired_cap = {
  "platformName": "Android",
  #"deviceName": "Android Emulator",
  #Redmi 4X
  #"deviceName": "7e25bb67d740",
  #Samsung S2
  #"deviceName": "001a38de4d76af",
  "deviceName": "emulator-5554",
  
  #emulator
  "udid": "emulator-5554",


  # #s3
  # "udid": "4df134143e934f4d",


  # #Redmi 4x
  # "udid": "7e25bb67d740",
  


  #mapy.cz
  "appPackage": "cz.seznam.mapy",
  "appWaitActivity": "cz.seznam.mapy.MapActivity",
  #"appWaitActivity": "cz.seznam.auth.app.SznAccountActivity",
  "app": "C:\\my\\auto\\mobile\\Mapy cz Cycling Hiking offline maps_v6.6.1_apkpure.com.apk",
  


  # #windy.com
  # "appPackage": "com.windyty.android",
  # "appWaitActivity": "com.windyty.android.MainActivity",
  # "app": "C:\\my\\auto\\mobile\\Windy com Wind Waves and Hurricanes Forecast_v18.0207_apkpure.com.apk",
  

  # #mujVlak
  # "appPackage": "cz.cd.mujvlak.an",
  # "appWaitActivity": "com.circlegate.cd.app.activity.TutorialActivity",
  # "app": "C:\\my\\auto\\mobile\\Můj vlak_v1.13.0_apkpure.com.apk",



  "autoGrantPermissions": "true",
  "unicodeKeyboard" : "true",
  "resetKeyboard" : "true"
}




driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
print('start wait')
driver.implicitly_wait(30)
print('end wait')


timeOut()



# #s3
# TouchAction(driver).press(x=460, y=853).move_to(x=258, y=856).release().perform()
# timeOut()     
# TouchAction(driver).press(x=482, y=781).move_to(x=296, y=773).release().perform() 
# timeOut()   
# TouchAction(driver).press(x=474, y=717).move_to(x=335, y=737).release().perform()
# timeOut()   
# TouchAction(driver).press(x=471, y=919).move_to(x=335, y=919).release().perform()
# timeOut()   
    



# #emu
# TouchAction(driver).press(x=753, y=1156).move_to(x=374, y=1185).release().perform()
# timeOut()   
# TouchAction(driver).press(x=606, y=1212).move_to(x=371, y=1201).release().perform()
# timeOut()  
# TouchAction(driver).press(x=614, y=1204).move_to(x=371, y=1209).release().perform()
# timeOut()  
# TouchAction(driver).press(x=701, y=1220).move_to(x=406, y=1225).release().perform()


# timeOut()
# elem = driver.find_element_by_id('cz.cd.mujvlak.an:id/button')
# user_name = elem.get_attribute('text')
# print(user_name)

# elem.click()


# #s3
# timeOut() 
# TouchAction(driver).press(x=61, y=914).move_to(x=144, y=908).release().perform()
# timeOut() 
# TouchAction(driver).tap(x=598, y=906).perform()
# timeOut() 



# #emu
# timeOut() 
# TouchAction(driver).tap(x=113, y=959).perform()
# timeOut()    
# TouchAction(driver).tap(x=805, y=1243).perform()
# timeOut()






# print('try found menu button')

contexts = driver.contexts
print(contexts)

current = driver.current_context
print(current)


	


# try:
#     elem = driver.find_element_by_id('cz.cd.mujvlak.an:id/base_activity_root')
#     #
#     #elem = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout')
#     #print ('found')


#     #elem = driver.find_element_by_id('cz.cd.mujvlak.an:id/action_bar')
#     #
#     #/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup

    

# except:    
#     print('not found')










# elem1 = driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Otevřít navigační menu"]')
# elem1.click()
# print('menu button clicked')


# timeOut(tick = 3.0)
# elem = driver.find_element_by_id('cz.seznam.mapy:id/goToMapButton')
# user_name = elem.get_attribute('text')
# print(user_name)

# elem.click()

# #TouchAction(driver).tap(x=242, y=708).perform()
# print('goToMapButton clicked')

# contexts = driver.contexts
# print(contexts)

# current = driver.current_context
# print(current)

# timeOut()
# print('after timeout')

# #first screen
# #elem = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout')
# elem = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout')


# #map screen
# #elem = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout')

# user_name = elem.get_attribute('text')
# print(type(user_name))
# print(user_name)



timeOut() 
elem = driver.find_element_by_id('cz.seznam.mapy:id/goToMapButton')
elem.click()
print('goToMapButton clicked')




timeOut()
contexts = driver.contexts
print(contexts)

current = driver.current_context
print(current)


try:
	timeOut() 
	elem = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout')
	print('found')
	user_name = elem.get_attribute('clickable')
	print(user_name)
except:
    print('not found')





# timeOut()
# elem = driver.find_element_by_id('cz.seznam.mapy:id/menuButton')
# timeOut()
# elem.click()
# print('menu clicked')




# try:
# 	timeOut()
# 	#cz.seznam.mapy:id/action_bar_root
# 	#cz.seznam.mapy:id/appWindowFragment
# 	elem = driver.find_element_by_id('cz.seznam.mapy:id/action_bar_root')
# 	print('found')
# 	user_name = elem.get_attribute('clickable')
# 	print(user_name)

# except:
#     print('not found')	







# #go to map
# timeOut(tick = 2.0)
# #func.goToMap()

# user_name = elem.get_attribute('text')
# print(type(user_name))
# print(user_name)
# elem = driver.find_element_by_id('cz.seznam.mapy:id/appWindowFragment')
	
# #cz.seznam.mapy:id/mainLayout

# #cz.seznam.mapy:id/menuButton
# #View.View
# #cz.seznam.mapy:id/appWindowFragment
# #View.ViewGroup
# #cz.seznam.mapy:id/appWindowFragment


# user_name = elem.get_attribute('text')
# print(type(user_name))
# print(user_name)
# elem.click()





# print('cz.seznam.mapy:id/menuButton')








# #elem = driver.find_element_by_id('cz.seznam.mapy:id/menuButton')
# elem = driver.find_element_by_id('cz.seznam.mapy:id/actionButtons')
# timeOut()
# user_name = elem.get_attribute('package')
# print(user_name)
# elem.click()
# print('menu clicked')



# #for emulator, doesn;t work
# elem = driver.find_element_by_id('cz.seznam.mapy:id/goToMapButton')
# elem.click()
# print("loaded ?")
# timeOut(tick = 2.0)
# print("loaded map ?")

# #elem = driver.find_element_by_id('cz.seznam.mapy:id/menuButton')
# TouchAction(driver).tap(x=87, y=1691).perform()
# try:
# 	#elem = driver.find_elements_by_accessibility_id('Menu')
# 	#cz.seznam.mapy:id/appWindowFragment
# 	#cz.seznam.mapy:id/actionButtons
# 	#cz.seznam.mapy:id/mainLayout
# 	#elem = driver.find_element_by_id('cz.seznam.mapy:id/menuButton')
# 	#elem = driver.find_element_by_id('cz.seznam.mapy:id/mainLayout')
# 	elem = driver.find_element_by_id('cz.seznam.mapy:id/userName')
# 	print (type(elem))
# 	print (len(elem), 'len list')
# 	print (elem)
# 	#elem.click()
# except:
# 	print ('ele not found')






#timeOut()
#elem = func.driver.find_element_by_id('cz.seznam.mapy:id/menuButton')
#elem = func.driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Menu"]')
#timeOut()
#elem.click()
#func.menu()
#elem = driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Menu"]')


# #go to map catalog
# func.goToCatalog()





#route planning
#menu
timeOut()
print ('loaded ?')
#func.menu()


# #search
# func.search_button()
# func.search_input('seznam')
# timeOut()
# func.scroll()





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
#func.login()

	

#cz.seznam.mapy:id/accountName


# handle_one_size = func.driver.get_window_size()
# print(handle_one_size)
