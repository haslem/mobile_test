#from driver_init import driver
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.multi_action import MultiAction
import locators_mobile


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions as TouchActionSelenium


import threading


def s3():

	# if device == 'redmi4x':
	# 	ud_id = "7e25bb67d740"
	# 	port = 4000
	# else:
	# 	ud_id = "D1AGAD1762742739"
	# 	port = 4001	



	desired_cap = {
	  "platformName": "Android",
	  #"deviceName": "Android Emulator",
	  # #Redmi 4X
	  # "udid": "7e25bb67d740",
	  #Samsung S2
	  #"deviceName": "001a38de4d76af",
	  # #Samsung S6
	  # "udid": "02157df29b72ad22",
	  # #Samsung S6 by Wi-fi
	  # "udid": "192.168.0.138:5555",
	  "deviceName": "Android",
	  # #emulator
	  # "udid": "emulator-5554",
	  # # huawei
	  # "udid": "WTM9K17224913440",
	  # #s3
	  # "udid": "4df134143e934f4d",
	  # #LG small
	  # "udid": "LGD160aa16aa2",
	  # #Moto
	  #"udid": "ZH33C2676B",
	  #Redmi 4x
	  "udid": "7e25bb67d740",
	  # #Redmi 4x by WIFI
	  # "udid": "192.168.0.186:5555",
	  # #Huawei by WIFI
	  # "udid": "192.168.0.180:5555",
	  # #Huawei
	  # "udid": "W3D7N16C20008324",
	  # #Redmi 3S
	  # "udid": "c51d1c8b7d53",
	  #"udid": f"{ud_id}",
	  #  #Nokia
	  # "udid": "D1AGAD1762742739",
	  #  #Nokia by WIFI
	  # "udid": "192.168.0.142:5555",

	  #'browserName': 'Chrome',
	  
	  # #mapy.cz
	  # "appPackage": "cz.seznam.mapy",
	  # "appWaitActivity": "cz.seznam.mapy.MapActivity",
	  # "app": "C:\\my\\auto\\mobile\\Mapy_v6.10.0_apkpure.apk",

	  #windy maps
	  "appPackage": "cz.seznam.windymaps",
	  "appWaitActivity": "cz.seznam.mapy.MapActivity",
	  "app": "C:\\my\\auto\\mobile\\Windy Maps_v1.1.0_apkpure.com.apk",

	  
	  "autoGrantPermissions": "true",
	  "unicodeKeyboard" : "true",
	  "resetKeyboard" : "true",
	  "noReset" : "true"
	}


		
	print('launched')
	#driver = webdriver.Remote(f"http://localhost:{port}/wd/hub", desired_cap)
	driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
	#driver = webdriver.Remote("http://localhost:4000/wd/hub", desired_cap)
	print('start wait')
	#driver.get("http://www.mapy.cz");
	driver.implicitly_wait(30)
	print('end wait')



	def search_by_locator(locator: dict , key: str):
		if locator[key][0] == 'xpath':
			return driver.find_element_by_xpath(locator[key][1])
		else:
			return driver.find_element_by_id(locator[key][1])	



	class Menu(object):
		"""docstring for ClassName"""
		#def menuButton(self):
		def __init__(self):	
			self.elem = driver.find_element_by_id(locators_mobile.map_screen['menu']).click()
		
		# def menu(self):
		# 	self.elem = driver.find_element_by_id(locators_mobile.map_screen['menu']).click()

		def buttons(self):
			self.elem = driver.find_element_by_id('cz.seznam.mapy:id/content')
			TouchAction(driver).long_press(self.elem).move_to(x=100, y=100).release().perform()

			self.elements = driver.find_elements_by_class_name('android.widget.Button')
			return self.elements

		def offline_maps(self):
			self.all_buttons = self.buttons()
			for i in self.all_buttons:
				if i.get_attribute('text') == 'Offline maps':
					i.click()
					break

		def places_and_routes(self):
			self.all_buttons = self.buttons()
			for i in self.all_buttons:
				if i.get_attribute('text') == 'Places and routes':
					i.click()
					break
					

		def activities(self):
			self.all_buttons = self.buttons()
			for i in self.all_buttons:
				if i.get_attribute('text') == 'Activities':
					i.click()
					break
					


		def route_planning(self):
			self.all_buttons = self.buttons()
			for i in self.all_buttons:
				if i.get_attribute('text') == 'Route planning':
					i.click()
					break
					

		def trips_nearby(self):
			self.all_buttons = self.buttons()
			for i in self.all_buttons:
				if i.get_attribute('text') == 'Trips nearby':
					i.click()
					break


		def start_tracker(self):
			self.all_buttons = self.buttons()
			for i in self.all_buttons:
				if i.get_attribute('text') == 'Start Tracker':
					i.click()
					break
			
		def tracker_switch(self):
			self.all_buttons = self.buttons()
			self.elem = driver.find_element_by_id(locators_mobile.menu['tracker_switch']).click()			

		def report_problem(self):
			self.all_buttons = self.buttons()
			for i in self.all_buttons:
				if i.get_attribute('text') == 'Report a problem':
					i.click()
					break


		def first_aid(self):
			self.all_buttons = self.buttons()
			for i in self.all_buttons:
				if i.get_attribute('text') == 'First aid':
					i.click()
					break
					

		def about(self):
			self.all_buttons = self.buttons()
			for i in self.all_buttons:
				if i.get_attribute('text') == 'About Mapy.cz':
					i.click()
					break																								




	class Menu_windy(object):
		"""docstring for ClassName"""
		#def menuButton(self):
		def __init__(self):	
			self.elem = driver.find_element_by_id(locators_mobile.map_screen_windy['menu']).click()
		
		# def menu(self):
		# 	self.elem = driver.find_element_by_id(locators_mobile.map_screen['menu']).click()

		def buttons(self):
			# self.elem = driver.find_element_by_id('cz.seznam.windymaps:id/content')
			# TouchAction(driver).long_press(self.elem).move_to(x=100, y=100).release().perform()

			self.elements = driver.find_elements_by_class_name('android.widget.Button')
			return self.elements

		def offline_maps(self):
			self.all_buttons = self.buttons()
			for i in self.all_buttons:
				if i.get_attribute('text') == 'Offline maps':
					i.click()
					break

		def my_maps(self):
			self.all_buttons = self.buttons()
			for i in self.all_buttons:
				if i.get_attribute('text') == 'My maps':
					i.click()
					break
					

		def route_planning(self):
			self.all_buttons = self.buttons()
			for i in self.all_buttons:
				if i.get_attribute('text') == 'Route planning':
					i.click()
					break


		def report_problem(self):
			self.all_buttons = self.buttons()
			for i in self.all_buttons:
				if i.get_attribute('text') == 'Report a problem':
					i.click()
					break


		def first_aid(self):
			self.all_buttons = self.buttons()
			for i in self.all_buttons:
				if i.get_attribute('text') == 'First aid':
					i.click()
					break
					

		def about(self):
			self.all_buttons = self.buttons()
			for i in self.all_buttons:
				if i.get_attribute('text') == 'About':
					i.click()
					break	


		def login(self):
			self.elem = driver.find_element_by_id('cz.seznam.mapy:id/userName')
			self.account_name = self.elem.get_attribute('text')
			if self.account_name != 'Log in':
				print('Already logged in')
				return
			self.elem.click()
			timeOut(tick = 2.0)

		def logout(self):
			self.elem = driver.find_element_by_id('cz.seznam.mapy:id/userName').click()
			
			self.elem = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button').click()






	class LoginPage(object):
		def user_name(self, user_name):
			self.user_name = user_name
			self.elem = driver.find_element_by_id(locators_mobile.sign_in['email']).send_keys(user_name)

		def password(self, password):
			self.password = password
			self.elem = driver.find_element_by_id(locators_mobile.sign_in['password']).send_keys(password)

		def sign_in_button(self):
			self.elem = driver.find_element_by_xpath(locators_mobile.sign_in['sign_in']).click()	
									
		def check_login(self):
			self.elem = driver.find_element_by_id('cz.seznam.mapy:id/userName')
			self.user_name = self.elem.get_attribute('text')

			self.elem = driver.find_element_by_id('cz.seznam.mapy:id/accountName')
			self.account_name = self.elem.get_attribute('text')


			if self.user_name == 'mapytesting2' and self.account_name == 'mapytesting2@seznam.cz':
				print ('Log in')
			else:
			    print('Not log in')
	
	

	class SearchPage_windy(object):
		def category_search(self):
			self.elem = driver.find_element_by_xpath(locators_mobile.search_windy['category']).click()

		def clear_search(self):
			self.elem = driver.find_element_by_id(locators_mobile.search_windy['close_button']).click()


		def search_input(self, search_word, *args):
			self.elem = driver.find_element_by_id(locators_mobile.search_windy['search_input'])
			self.elem.send_keys(search_word)
			if len(args) == 0:
				driver.execute_script('mobile: performEditorAction', {'action': 'search'})
			else:
				self.elem = driver.find_element_by_xpath(locators_mobile.search_windy['naseptavac_result']).click()


		def history_search(self):
			try:
				#self.elem = driver.find_element_by_xpath(locators_mobile.search_windy['history_first_item'])
				self.elem = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView').click()

			except:
				print('no history')	


	class Tracker(object):
		def start(self):
			self.elem = driver.find_element_by_id(locators_mobile.tracker['start']).click()

		def tracker_button(self):
			self.elem = driver.find_element_by_id(locators_mobile.tracker['tracker_button']).click()

		def expand(self):
			self.elem = driver.find_element_by_id(locators_mobile.tracker['expand']).click()

		def discard(self):
			self.elem = driver.find_element_by_id(locators_mobile.tracker['discard']).click()

		def discard_discard(self):
			self.elem = driver.find_element_by_id(locators_mobile.tracker['discard_discard']).click()



	class Tracker_windy(object):
		def tracker_button(self):
			self.elem = driver.find_element_by_id(locators_mobile.tracker_windy['start_screen']).click()

		def start(self):
			self.elem = driver.find_element_by_id(locators_mobile.tracker_windy['start']).click()

		def expand(self):
			self.elem = driver.find_element_by_id(locators_mobile.tracker_windy['expand']).click()

		def discard(self):
			self.elem = driver.find_element_by_id(locators_mobile.tracker_windy['discard']).click()

		def discard_discard(self):
			self.elem = driver.find_element_by_id(locators_mobile.tracker_windy['discard_discard']).click()	


	class RoutePlanning_windy(object):
		"""docstring for RoutePlanning_windy"""
		def start(self):
			self.elem = search_by_locator(locators_mobile.planning_windy, 'start').click()

		def end(self):
			self.elem = search_by_locator(locators_mobile.planning_windy, 'end').click()	
	
		def search(self, search_word: str):
			self.elem = search_by_locator(locators_mobile.planning_windy, 'search')
			self.elem.send_keys(search_word)
			#enter
			driver.press_keycode(66)
			#chhose first result
			self.elem =driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]')
			self.elem.click()

		def my_location(self):
			self.elem = search_by_locator(locators_mobile.planning_windy, 'my_location').click()	


			




	def all_elements():
		elementsList = driver.find_elements_by_xpath("//*")
		print(type(elementsList), 'type of elemlist')
		print(len(elementsList), 'len of elementsList')

		return elementsList


	def timeOut(delay = 100000000, tick = 1):
		#default delay 3 s
		for i in range(int(delay * tick)):
		    pass


	def menu():
		elem = driver.find_element_by_id('cz.seznam.mapy:id/menuButton')
		#elem = driver.find_element_by_id('cz.seznam.mapy:id/mapStyleSwitch')
		print(elem.size, 'elem size')
		#elem = driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Menu"]')

		# elem = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout')

		# driver.implicitly_wait(10)
		
		# user_name = elem.get_attribute('text')
		# print(user_name, 'empty text attribute')

		timeOut()
		#print(type(elem))
		#print(dir(elem))
		elem.click()
		print('menu clicked')



	def menu_windy():
		elem = driver.find_element_by_id('cz.seznam.windymaps:id/menuButton').click()


	def goToMap():
		elem = driver.find_element_by_id('cz.seznam.mapy:id/goToMapButton')
		elem.click()
		#print('start wait')
		driver.implicitly_wait(10)
		#print('end wait')
		#TouchAction(driver).tap(x=242, y=708).perform()
		print('goToMapButton clicked')



	def goToCatalog():
		elem = driver.find_element_by_id('cz.seznam.mapy:id/downloadMapsButton')
		elem.click()
		print('start wait')
		driver.implicitly_wait(10)
		print('end wait')




	def relative_pos(x,y):
		# x1 = x / driver.get_window_size()['width']
		# y1 = y / driver.get_window_size()['height']

		x1 = x /1080
		y1 = y /1794
		return [x1, y1]


	def search_button():
		elem = driver.find_element_by_id('cz.seznam.mapy:id/searchButton')
		elem.click()
		print('searchButton clicked')


	def search_button_windy():
		elem = driver.find_element_by_id('cz.seznam.windymaps:id/searchButton')
		elem.click()
		print('searchButton clicked')	



	def search_input(search_word):

		#search_input('seznam')

		elem = driver.find_element_by_id('cz.seznam.mapy:id/input')
		driver.implicitly_wait(5)
		elem.send_keys(search_word)
		print(type(elem))
		driver.implicitly_wait(5)

		driver.execute_script('mobile: performEditorAction', {'action': 'search'})
		driver.implicitly_wait(5)



		#/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView
		#/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.view.View[1]

		elem = driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.view.View[*]')

		print(type(elem))
		print(len(elem))
		elem[0].click()


	def scroll():	
		scroll = TouchAction(driver)
		#scroll.press(x=480, y=761).move_to(x=469, y=430).release().perform()
		scroll.press(x = relative_pos(480,761)[0], y = relative_pos(480,761)[1]).move_to(x = relative_pos(469,430)[0], y = relative_pos(469,430)[1]).release().perform()
		print ('scrolled')


	def login():
		timeOut()

		elem = driver.find_element_by_id('cz.seznam.mapy:id/userName')
		#elem = driver.find_element_by_id('cz.seznam.windymaps:id/userName')
		account_name = elem.get_attribute('text')
		if account_name != 'Log in':
			print('Already logged in')
			return
		elem.click()
		timeOut(tick = 2.0)

		timeOut(tick = 3.0)
		print ("loaded ?")
		


		#elem = driver.find_element_by_id('cz.seznam.mapy:id/webView')
		#print (elem.get_attribute('innerHTML'))
		contexts = driver.contexts
		print(contexts)

		current = driver.current_context
		print(current)



		#login
		






		##!! for Android 4, web view
		#login

		#TouchAction(driver).tap(x=168, y=668).perform()
		handle_one_size = driver.get_window_size()
		width = 0.233 * handle_one_size['width']
		height = 0.522 * handle_one_size['height']
		TouchAction(driver).tap(x=width, y=height).perform()

		print ('clicked')


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
		timeOut()

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

		timeOut()

		#enter
		driver.press_keycode(66)








		elem = driver.find_element_by_id('cz.seznam.mapy:id/userName')
		#elem = driver.find_element_by_id('cz.seznam.windymaps:id/userName')
		user_name = elem.get_attribute('text')

		elem = driver.find_element_by_id('cz.seznam.mapy:id/accountName')
		#elem = driver.find_element_by_id('cz.seznam.windymaps:id/accountName')
		account_name = elem.get_attribute('text')


		if user_name == 'mapytesting2' and account_name == 'mapytesting2@seznam.cz':
			print ('Log in success')
		else:
		    print('Log in failed')



	def login_windy():
		timeOut()
		elem = driver.find_element_by_id('cz.seznam.windymaps:id/userName')
		account_name = elem.get_attribute('text')
		if account_name != 'Log in':
			print('Already logged in')
			return
		elem.click()
		timeOut(tick = 2.0)

		timeOut(tick = 3.0)
		print ("loaded ?")
		
		contexts = driver.contexts
		print(contexts)

		current = driver.current_context
		print(current)

		##!! for Android 4, web view
		#login

		# handle_one_size = driver.get_window_size()
		# width = 0.233 * handle_one_size['width']
		# height = 0.522 * handle_one_size['height']
		# TouchAction(driver).tap(x=width, y=height).perform()


		elem = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText').click()
		print ('clicked')


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
		timeOut()

		#"2"
		driver.press_keycode(9)

		# #enter
		# driver.press_keycode(66)
		elem = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').click()



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

		timeOut()

		#enter
		driver.press_keycode(66)




		timeOut()
		print('try open menu')
		menu_windy()
		print('opened')
		
		elem = driver.find_element_by_id('cz.seznam.windymaps:id/userName')
		user_name = elem.get_attribute('text')
		#print(user_name)

		
		elem = driver.find_element_by_id('cz.seznam.windymaps:id/accountName')
		account_name = elem.get_attribute('text')
		#print(account_name)


		if account_name == 'mapytesting2':
			print ('Log in success')
		else:
		    print('Log in failed')





	def logout():
		try:
			elem = driver.find_element_by_id('cz.seznam.mapy:id/accountName')
			elem.click()
			elem = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button')
			elem.click()
			print('Logout success')
		except:
			print('Already Logout')	



	def logout_windy():
		try:
			elem = driver.find_element_by_id('cz.seznam.windymaps:id/accountName')
			elem.click()
			elem = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button')
			elem.click()
			print('Logout success')
		except:
			print('Already Logout')			



	def menuMyMaps():
	    elem = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[1]').click()  		





	def search_element(label):
		while True:
			i = 1
			try:
				elem = driver.find_element_by_xpath(f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.View/androidx.recyclerview.widget.RecyclerView/android.view.View[{i}]/android.widget.TextView[{i}]")	
				name = elem.get_attribute('text')
				print(name)
				print(i)
				if label in name:
					print('found')
					break

				print(relative_pos(739,719)[0])
				print(driver.get_window_size()['width'], 'window size')
					
				new_x = relative_pos(739,719)[0] * driver.get_window_size()['width']
				new_y = relative_pos(739,719)[1] * driver.get_window_size()['height']

				print(new_x,new_y,'new_x and new_y')

				new_x1 = relative_pos(739,670)[0]* driver.get_window_size()['width']
				new_y1 = relative_pos(739,670)[1]* driver.get_window_size()['height']

				#TouchAction(driver).press(x=739, y=719).move_to(x=739, y=670).release().perform()
				TouchAction(driver).press(x=new_x, y=new_y).move_to(x=new_x1, y=new_y1).release().perform()
				i = i + 1	
			except:
				#print('not found')
				#print(i)
				new_x = relative_pos(739,719)[0]* driver.get_window_size()['width']
				new_y = relative_pos(739,719)[1]* driver.get_window_size()['height']

				new_x1 = relative_pos(739,670)[0]* driver.get_window_size()['width']
				new_y1 = relative_pos(739,670)[1]* driver.get_window_size()['height']

				#print(relative_pos(739,719)[0], 'relative position')
				#print(driver.get_window_size()['width'], 'screen width')
				#print(driver.get_window_size()['height'], 'screen height')

				#print(new_x,new_y,'new_x and new_y')
				TouchAction(driver).press(x=new_x, y=new_y).move_to(x=new_x1, y=new_y1).release().perform()
		elem.click()
		timeOut()
		elem = driver.find_element_by_id('cz.seznam.mapy:id/toolbar')
		elem.click()

		elem = driver.find_element_by_id('cz.seznam.mapy:id/gainValue')
		gain = elem.get_attribute('text')

		elem = driver.find_element_by_id('cz.seznam.mapy:id/lossValue')
		loss = elem.get_attribute('text')

		print(gain, 'gain')
		print(loss, 'loss')

		try:
		    elem = driver.find_element_by_id('cz.seznam.mapy:id/elevation')
		    print('found')
		except:
		    print('not') 



	def TC486():
	    for k in locators_mobile.map_screen:
	    	try:
	    		elem = driver.find_element_by_id(locators_mobile.map_screen[k])
	    		print (f'{k} found')
	    	except:
	    	    print (f'{k} not found')
	    print('TC486 Ok')	       

	def TC487():
		#try:
		elem = driver.find_element_by_id(locators_mobile.map_screen['zoom'])
		print('zoom')
		location = elem.location
		print(location, 'location')
		size = elem.size
		print(size, 'size')
		#print(driver.get_window_size()['height'])
		#x1 = driver.get_window_size()['height'] - 756
		#print(x1)
		#y1 = driver.get_window_size()['width']
		#print(y1)
		new_x1 = relative_pos(1047,835)[0]* driver.get_window_size()['width']
		new_y1 = relative_pos(1047,835)[1]* driver.get_window_size()['height']
		TouchAction(driver).press(x = new_x1, y = new_y1).move_to(x = elem.location['x'], y = driver.get_window_size()['height'] - 200).release().perform()
		timeOut()

		print(elem.location['y'])

		print(size['height'])
		#TouchAction().press(x = elem.location['x'] + 30, y = elem.location['y'] + size['height']).move_to(x = elem.location['x'], y = elem.location['y']).release().perform()
		#TouchAction().press(x = 1022, y = 1362).move_to(x = elem.location['x'], y = elem.location['y']).release().perform()
		#TouchAction(driver).tap(x=1022, y=1362).perform()
		#TouchAction(driver).press(x = 994, y = 1036).move_to(x = 994, y = 412).release().perform()
		print(elem.location['x'], "elem.location['x']")
		TouchAction(driver).press(x=elem.location['x'] + 30, y=elem.location['y'] + size['height'] - 100).move_to(x = elem.location['x'], y = elem.location['y']).release().perform()
		timeOut()
		new_x1 = relative_pos(1047,835)[0]* driver.get_window_size()['width']
		new_y1 = relative_pos(1047,835)[1]* driver.get_window_size()['height']
		TouchAction(driver).press(x = elem.location['x'], y = elem.location['y']).move_to(x = new_x1, y = new_y1).release().perform()



		#move
		timeOut()
		TouchAction(driver).press(x = driver.get_window_size()['width'] / 2, y = driver.get_window_size()['height'] / 2).move_to(x = driver.get_window_size()['width'] / 2, y = driver.get_window_size()['height'] / 2 + 100).release().perform()


		#immersive
		timeOut()
		TouchAction(driver).tap(x = driver.get_window_size()['width'] / 2 + 50, y = driver.get_window_size()['height'] / 2 + 50).perform()


		timeOut()
		#elem = driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.View/*')
		elem = driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.View/*')
		#print(elem)
		#print(len(elem), 'found')

		if len(elem) == 0:
			print ('immersive OK')
		else:
			print('immersive not ok')	
		#elem = driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.View*')
		#print(len(elem), 'found')	


		timeOut()
		TouchAction(driver).tap(x = driver.get_window_size()['width'] / 2 + 50, y = driver.get_window_size()['height'] / 2 + 50).perform()






		timeOut()
		TouchAction(driver).long_press(x = driver.get_window_size()['width'] / 2 + 100, y = driver.get_window_size()['height'] / 2).perform()





		# a1 = TouchAction()
		# a1.tap(x = driver.get_window_size()['width'] / 2 + 50, y = driver.get_window_size()['height'] / 2 + 50)
		# #a1.move_to(x = driver.get_window_size()['width'] / 2 + 150, y = driver.get_window_size()['height'] / 2 + 150)
		# a1.release()

		# a2 = TouchAction()
		# a2.tap(x = driver.get_window_size()['width'] / 2 - 50, y = driver.get_window_size()['height'] / 2 - 50)
		# #a1.move_to(x = driver.get_window_size()['width'] / 2 - 150, y = driver.get_window_size()['height'] / 2 - 150)
		# a2.release()



		# ma = MultiAction(driver)
		# ma.add(a1, a2)
		# ma.perform()




		#except:
		    #print('error')
		    	

	def navigation():
		timeOut()
		

		elem = driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[3]')
		#print(type(elem), 'elem type')
		#print(len(elem), 'elem length')
		elem[0].click()
		#start
		elem = driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/androidx.recyclerview.widget.RecyclerView/android.view.View[2]/android.view.View/android.widget.TextView[1]')
		#print(type(elem), 'elem type')
		#print(len(elem), 'elem length')
		elem[0].click()


		elem = driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView')
		#print(type(elem), 'elem type')
		#print(len(elem), 'elem length')
		elem[0].click()


		#finish
		elem = driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/androidx.recyclerview.widget.RecyclerView/android.view.View[3]/android.view.View/android.widget.TextView[1]')
		#print(type(elem), 'elem type')
		#print(len(elem), 'elem length')
		elem[0].click()


		

		elem = driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView')
		elem[0].click()



		



		TouchAction(driver).long_press(x = driver.get_window_size()['width'] / 2, y= driver.get_window_size()['height'] / 2).move_to(x = driver.get_window_size()['width'] / 2 + 100, y= driver.get_window_size()['height'] / 2 + 100).release().perform()

		elem = driver.find_elements_by_id('cz.seznam.mapy:id/mapLocationPickSelect')
		timeOut()
		elem[0].click()


	def offline_maps():
		# elem = driver.find_element_by_xpath(locators_mobile.menu['offline_maps'])
		# elem.click()

		elem = driver.find_elements_by_class_name('android.widget.Button')
		for i in elem:
			if i.text == 'Offline maps':
				i.click()
				break



	def search_menu_item(menu_item):	
		find = 0
		while find == 0:
			elem = driver.find_elements_by_class_name('android.widget.Button')
			for i in elem:
				print(i.text)
				if i.text == menu_item:
					#print(i.get_attribute('text'))
					i.text
					print (i.location)
					elem = i
					find = 1
					break
			if find == 1:		
				i.click()		
			else:
				TouchAction(driver).press(x=driver.get_window_size()['width']/2, y=driver.get_window_size()['height']/2 - 20).move_to(x=driver.get_window_size()['width']/2, y=driver.get_window_size()['height']/2 - 50).release().perform()








	def search_maps(country):	
		find = 0
		while find == 0:
			elem = driver.find_elements_by_id('cz.seznam.mapy:id/offlineCountryTitle')
			for i in elem:
				#print(i.text)
				if i.text == country:
					#print(i.get_attribute('text'))
					i.text
					print (i.location)
					elem = i
					find = 1
					break
			if find == 1:		
				TouchAction(driver).tap(x=driver.get_window_size()['width']-40, y=i.location['y']).perform()		
			else:
				TouchAction(driver).press(x=driver.get_window_size()['width']/2, y=driver.get_window_size()['height']/2).move_to(x=driver.get_window_size()['width']/2, y=driver.get_window_size()['height']/2 - 20).release().perform()
				#elem = driver.find_element_by_id('cz.seznam.mapy:id/groupIcon')
				#TouchAction(driver).press(elem).move_to(x=driver.get_window_size()['width']/2, y=driver.get_window_size()['height']/2 - 20).release().perform()




	def search_maps_windy(country):	
		find = 0
		while find == 0:
			elem = driver.find_elements_by_id('cz.seznam.windymaps:id/offlineCountryTitle')
			for i in elem:
				print(i.text)
				if i.text == country:
					#print(i.get_attribute('text'))
					i.text
					print (i.location)
					elem = i
					find = 1
					break
			if find == 1:		
				TouchAction(driver).tap(x=driver.get_window_size()['width']-40, y=i.location['y']).perform()		
			else:
				TouchAction(driver).press(x=driver.get_window_size()['width']/2, y=driver.get_window_size()['height']/2).move_to(x=driver.get_window_size()['width']/2, y=driver.get_window_size()['height']/2 - 40).release().perform()
				#elem = driver.find_element_by_id('cz.seznam.mapy:id/groupIcon')
				#TouchAction(driver).press(elem).move_to(x=driver.get_window_size()['width']/2, y=driver.get_window_size()['height']/2 - 20).release().perform()





	def search_delete_maps(country):	
		find = 0
		while find == 0:
			elem = driver.find_elements_by_id('cz.seznam.mapy:id/offlineCountryTitle')
			for i in elem:
				if i.get_attribute('text') == country:
					print(i.get_attribute('text'))
					print (i.location)
					elem = i
					find = 1
					break
			if find == 1:		
				TouchAction(driver).tap(x=driver.get_window_size()['width']-40, y=i.location['y']).perform()		
			else:
				print('no downloaded map')
				break



	def search_delete_maps_windy(country):	
		find = 0
		while find == 0:
			elem = driver.find_elements_by_id('cz.seznam.windymaps:id/offlineCountryTitle')
			for i in elem:
				if i.get_attribute('text') == country:
					print(i.get_attribute('text'))
					print (i.location)
					elem = i
					find = 1
					break
			if find == 1:		
				TouchAction(driver).tap(x=driver.get_window_size()['width']-40, y=i.location['y']).perform()		
			else:
				print('no downloaded map')
				break





	def download_map():
		elem = driver.find_element_by_id('android:id/button1')
		elem.click()
		
		try:
			elem = driver.find_element_by_id('cz.seznam.mapy:id/storageCheck')
			elem.click()
		except:
			pass	

		print("downloading...")

		try:
			while True:
				elem = driver.find_element_by_id('cz.seznam.mapy:id/overallProgress')	
		except:
			print('map was downloaded')




	def download_map_windy():
		elem = driver.find_element_by_id('android:id/button1')
		elem.click()
		
		try:
			elem = driver.find_element_by_id('cz.seznam.windymaps:id/storageCheck')
			elem.click()
		except:
			pass	

		print("downloading...")

		try:
			while True:
				elem = driver.find_element_by_id('cz.seznam.windymaps:id/overallProgress')	
		except:
			print('map was downloaded')		
				


	def delete_map():
		elem = driver.find_element_by_id('android:id/button1')
		elem.click()


	def check_downloaded_maps():
		elem = driver.find_elements_by_class_name('android.widget.TextView')
		print(len(elem), 'len of list')
		text = elem[1].text
		print(text)

		if text == 'Downloaded':
			print ('there are downlod maps')
		else:
			print('no downloaded maps')
		driver.back()		


	def check_download():
		pass



	def launch():


		# all_elements()


		# #go to map
		# timeOut(tick = 2.0)
		# goToMap()

		# all_elements()


		# #menu
		# timeOut(tick = 2.0)
		# menu()


		#login check
		#login()


		handle_one_size = driver.get_window_size()
		print(handle_one_size)



	#all_elements()
	#go to map
	timeOut(tick = 2.0)
	#goToMap()



	# Tracker_windy().tracker_button()
	# Tracker_windy().start()
	# Tracker_windy().expand()
	# Tracker_windy().discard()
	# Tracker_windy().discard_discard()


	# Menu_windy().route_planning()
	# RoutePlanning_windy().start()
	# RoutePlanning_windy().search('Prazsky Hrad')
	# RoutePlanning_windy().end()
	# RoutePlanning_windy().my_location()


	# search_button_windy()
	# SearchPage_windy().category_search()
	# SearchPage_windy().clear_search()
	# SearchPage_windy().search_input('Prague')
	# timeOut()
	# driver.back()
	# driver.back()
	# search_button_windy()
	# SearchPage_windy().search_input('Na', 'naseptavac')
	# timeOut()
	# driver.back()
	# driver.back()
	# search_button_windy()
	# SearchPage_windy().history_search()
	# driver.back()
	# driver.toggle_wifi()
	# search_button_windy()
	# SearchPage_windy().search_input('Prague')





	
	# menu()
	# login()
	# logout()

	menu_windy()
	login_windy ()
	logout_windy()


	
	offline_maps()
	timeOut()

	print('start search')
	# search_maps('Bahrain')
	# download_map()
	search_maps_windy('Bahrain')
	download_map_windy()

	# #download Saxony
	# search_maps_windy('Germany')
	# search_maps_windy('Saxony')
	# download_map_windy()
	# # search_maps('Germany')
	# # search_maps('Saxony')
	# # download_map()
	# driver.back()
	# driver.back()



	#menu()
	menu_windy()
	offline_maps()
	check_downloaded_maps()




	#menu()
	menu_windy()
	offline_maps()

	#delete downloaded maps
	search_delete_maps_windy('Bahrain')
	delete_map()
	driver.back()
	

	# menu()
	# offline_maps()
	# search_delete_maps('Germany')
	# search_delete_maps('Saxony')
	# delete_map()
	# driver.back()
	# driver.back()



	#menu()
	menu_windy()
	offline_maps()
	check_downloaded_maps()



	# login()
	# logout()
	




	# Menu().login()
	# LoginPage().user_name('mapytesting2')
	# LoginPage().password('testingmapy')
	# LoginPage().sign_in_button()
	# LoginPage().check_login()
	# timeOut()
	# driver.back()
	# Menu().logout()
	# driver.back()



	# Menu().tracker_switch()
	# driver.back()
	# Menu().start_tracker()
	# Tracker().start()
	# Tracker().tracker_button()
	# Tracker().expand()
	# Tracker().discard()
	# Tracker().discard_discard()



	# Menu().offline_maps()
	# driver.back()
	# Menu().places_and_routes()
	# driver.back()
	# Menu().activities()
	# driver.back()
	# Menu().route_planning()
	# driver.back()
	# Menu().trips_nearby()
	# driver.back()
	# driver.back()
	# Menu().offline_maps()
	# driver.back()
	# Menu().report_problem()
	# driver.back()
	# Menu().first_aid()
	# driver.back()



	# Menu_windy().offline_maps()
	# driver.back()
	# Menu_windy().route_planning()
	# driver.back()
	# Menu_windy().my_maps()
	# driver.back()
	# Menu_windy().first_aid()
	# driver.back()
	# Menu_windy().report_problem()
	# driver.back()
	# Menu_windy().about()
	# driver.back()



	



	# for i in Menu().buttons():
	# 	print(i.get_attribute('text'))




	

	# Menu().route_planning()
	# #select start/end
	# elem = driver.find_elements_by_id('cz.seznam.mapy:id/routePartRow')
	# #change start/finish
	# TouchAction(driver).long_press(elem[0]).move_to(x=360, y=1100).release().perform()

	# #click start
	# elem[0].click()
	# #click "select a marker on the map"
	# elem = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
	# #move map 
	# TouchAction(driver).press(x=driver.get_window_size()['width']/2, y=driver.get_window_size()['height']/2 - 20).move_to(x=driver.get_window_size()['width']/2, y=driver.get_window_size()['height']/2 - 50).release().perform()
	# #click 'select' button
	# elem = driver.find_element_by_id('cz.seznam.mapy:id/mapLocationPickSelect').click()



	# #select start/end
	# elem = driver.find_elements_by_id('cz.seznam.mapy:id/routePartRow')
	# #select end 
	# elem[1].click()
	# #click "select a marker on the map"
	# elem = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
	# #move map 
	# TouchAction(driver).press(x=driver.get_window_size()['width']/2, y=driver.get_window_size()['height']/2).move_to(x=driver.get_window_size()['width']/2, y=driver.get_window_size()['height']/2 - 20).release().perform()
	# #click 'select' button
	# elem = driver.find_element_by_id('cz.seznam.mapy:id/mapLocationPickSelect').click()



	# for i in range(5):
	# 	print('Next button')
	# 	timeOut()
	# 	elem = driver.find_element_by_xpath('(//android.widget.ImageButton[@content-desc="Add marker"])[1]').click()
	# 	elem = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
	# 	#timeOut()
	# 	TouchAction(driver).press(x=driver.get_window_size()['width']/2, y=driver.get_window_size()['height']/2).move_to(x=driver.get_window_size()['width']/2, y=driver.get_window_size()['height']/2 - 20).release().perform()
	# 	elem = driver.find_element_by_id('cz.seznam.mapy:id/mapLocationPickSelect').click()









	# #multi action
	# timeOut()
	# a1 = TouchAction(driver).press(x=driver.get_window_size()['width']/2 + 10, y=driver.get_window_size()['height']/2).move_to(x=driver.get_window_size()['width']/2, y=driver.get_window_size()['height']/2 - 50).wait(500).release()
	# a2 = TouchAction(driver).press(x=driver.get_window_size()['width']/2 - 10, y=driver.get_window_size()['height']/2).move_to(x=driver.get_window_size()['width']/2, y=driver.get_window_size()['height']/2 + 50).wait(500).release()
	
	# m = MultiAction(driver)
	# m.add(a1,a2)
	# m.perform()



	
	# #maximaize card
	# timeOut()
	# TouchAction(driver).press(x=driver.get_window_size()['width'] / 2, y=driver.get_window_size()['height'] / 2 - 200).perform()
	
	# elem = driver.find_element_by_id('cz.seznam.mapy:id/toolbarContainer').click()
	# elem = driver.find_element_by_id('cz.seznam.mapy:id/expandIcon').click()

	# elem = driver.find_element_by_id('cz.seznam.mapy:id/weatherChart')
	# TouchAction(driver).long_press(elem).move_to(x=100, y=1200).release().perform()


	#tap like simple click
	#press like long press
	#release like отпустить
	#The available events from the spec are: * press * release * moveTo * tap * wait * longPress * cancel * perform
	#http://appium.io/docs/en/writing-running-appium/touch-actions/



	









if __name__ == '__main__':
	s3()
	# t1 = threading.Thread(target=s3, args=[4000])
	# t2 = threading.Thread(target=s3, args=[4001])


	# t1.start()
	# t2.start()

	# t1.join()
	# t2.join()




