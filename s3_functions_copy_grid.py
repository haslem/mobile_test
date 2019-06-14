#from driver_init import driver
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.multi_action import MultiAction
import locators_mobile




##real
# desired_cap = {
#   "deviceName": "4df134143e934f4d",
	 #huawei
	 #"deviceName": "WTM9K17224913440",
#   "platformName": "Android",
#   "app": "C:\\my\\auto\\mobile\\mapy-cz-6-5-2.apk"
# }



def nokia():

	##emu
	#somehow also works on real device
	desired_cap = {
	  "platformName": "Android",
	  #"deviceName": "Android Emulator",
	  # #Redmi 4X
	  # "udid": "7e25bb67d740",
	  #Samsung S2
	  #"deviceName": "001a38de4d76af",
	  "deviceName": "Android",
	  # #emulator
	  # "udid": "emulator-5554",
	  # # huawei
	  # "udid": "WTM9K17224913440",
	  # #s3
	  # "udid": "4df134143e934f4d",
	  # #Moto
	  #"udid": "ZH33C2676B",
	  # #Redmi 4x
	  # "udid": "7e25bb67d740",
	   #Nokia
	  "udid": "D1AGAD1762742739",
	  
	  "appPackage": "cz.seznam.mapy",
	  "appWaitActivity": "cz.seznam.mapy.MapActivity",
	  "app": "C:\\my\\auto\\mobile\\mapy-cz-6-9-0.apk",
	  "autoGrantPermissions": "true",
	  "unicodeKeyboard" : "true",
	  "resetKeyboard" : "true",
	  "noReset" : "true"
	}






	print('launched')
	#driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
	driver = webdriver.Remote("http://localhost:4001/wd/hub", desired_cap)
	print('start wait')
	driver.implicitly_wait(30)
	print('end wait')



	def all_elements():
		elementsList = driver.find_elements_by_xpath("//*");
		print(type(elementsList), 'type of elemlist')
		print(len(elementsList), 'len of elementsList')

		return elementsList


	def timeOut(delay = 100000000, tick = 1):
		#default delay 3 s
		for i in range(int(delay * tick)):
		    pass


	def menu():
		elem = driver.find_element_by_id('cz.seznam.mapy:id/menuButton')
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
		#TouchAction(driver).tap(x=410, y=562).perform()
		#TouchAction(driver).tap(x=driver.get_window_size()['width'] * 0.5694, y=driver.get_window_size()['height'] * 0.439).perform()

		elem = driver.find_element_by_id('cz.seznam.mapy:id/userName')
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
		user_name = elem.get_attribute('text')

		elem = driver.find_element_by_id('cz.seznam.mapy:id/accountName')
		account_name = elem.get_attribute('text')


		if user_name == 'mapytesting2' and account_name == 'mapytesting2@seznam.cz':
			print ('Log in success')
		else:
		    print('Log in failed')


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



	def launch():


		handle_one_size = driver.get_window_size()
		print(handle_one_size)

	
	#all_elements()
	#go to map
	timeOut(tick = 2.0)
	#goToMap()


	timeOut(tick = 2.0)
	menu()


	login()	
