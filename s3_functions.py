#from driver_init import driver
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys



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
  "deviceName": "Android Emulator",
  #"deviceName": "emulator-5554",
  "appPackage": "cz.seznam.mapy",
  "appWaitActivity": "cz.seznam.mapy.MapActivity",
  "app": "C:\\my\\auto\\mobile\\mapy-cz-6-5-2.apk",
  "autoGrantPermissions": "true",
  "unicodeKeyboard" : "true",
  "resetKeyboard" : "true"
}




driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
print('start wait')
driver.implicitly_wait(30)
print('end wait')








def timeOut(delay = 100000000, tick = 1):
	#default delay 3 s
	for i in range(int(delay * tick)):
	    pass


def menu():
	elem = driver.find_element_by_id('cz.seznam.mapy:id/menuButton')
	driver.implicitly_wait(10)
	timeOut()
	elem.click()
	print('menu clicked')


def goToMap():
	elem = driver.find_element_by_id('cz.seznam.mapy:id/goToMapButton')
	elem.click()
	#print('start wait')
	driver.implicitly_wait(10)
	#print('end wait')
	print('goToMapButton clicked')


def goToCatalog():
	elem = driver.find_element_by_id('cz.seznam.mapy:id/downloadMapsButton')
	elem.click()
	print('start wait')
	driver.implicitly_wait(10)
	print('end wait')


def relative_pos(x,y):
	x1 = x / driver.get_window_size()['width']
	y1 = y / driver.get_window_size()['height']
	return [x1, y1]



def login():
	timeOut()
	#TouchAction(driver).tap(x=410, y=562).perform()
	#TouchAction(driver).tap(x=driver.get_window_size()['width'] * 0.5694, y=driver.get_window_size()['height'] * 0.439).perform()

	elem = driver.find_element_by_id('cz.seznam.mapy:id/userName')
	elem.click()

	


	elem = driver.find_element_by_id('cz.seznam.mapy:id/webView')
	#print (elem.get_attribute('innerHTML'))
	contexts = driver.contexts
	print(contexts)

	current = driver.current_context
	print(current)



	#login
	timeOut(tick = 2.0)
	#TouchAction(driver).tap(x=168, y=668).perform()
	handle_one_size = driver.get_window_size()
	width = 0.233 * handle_one_size['width']
	height = 0.522 * handle_one_size['height']
	TouchAction(driver).tap(x=width, y=height).perform()



	timeOut(tick = 2.0)
	#"mapy"
	driver.press_keycode(41)
	driver.press_keycode(29)
	driver.press_keycode(44)
	driver.press_keycode(53)

	#"testing"
	driver.press_keycode(48)
	driver.press_keycode(33)
	driver.press_keycode(47)
	driver.press_keycode(48)
	driver.press_keycode(37)
	driver.press_keycode(42)
	driver.press_keycode(35)

	#"2"
	driver.press_keycode(9)

	#enter
	driver.press_keycode(66)




	timeOut(tick = 3.0)

	#"testing"
	driver.press_keycode(48)
	driver.press_keycode(33)
	driver.press_keycode(47)
	driver.press_keycode(48)
	driver.press_keycode(37)
	driver.press_keycode(42)
	driver.press_keycode(35)


	#"mapy"
	driver.press_keycode(41)
	driver.press_keycode(29)
	driver.press_keycode(44)
	driver.press_keycode(53)


	#enter
	driver.press_keycode(66)


	# elem = driver.find_element_by_id('cz.seznam.mapy:id/userName')
	# user_name = elem.get_attribute('text')

	# elem = driver.find_element_by_id('cz.seznam.mapy:id/accountName')
	# account_name = elem.get_attribute('text')


	# if user_name == 'mapytesting2' and account_name == 'mapytesting2@seznam.cz':
	# 	print ('Log in success')
	# else:
	#     print('Log in failed')		