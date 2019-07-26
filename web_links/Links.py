from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from multiprocess import Process
import locators
from selenium.webdriver.common.by import By

import csv
import pyperclip

import math

def timeOut(delay = 100000000, tick = 1):
	#default delay 3 s
	for i in range(int(delay * tick)):
	    pass


def chrome_prod():

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--disable-infobars")
	driver = webdriver.Chrome(chrome_options=chrome_options)
	driver.maximize_window()
	production = "https://en.mapy.cz/zakladni?x=14.3999996&y=50.0499992&z=11"
	production_max_zoom = "https://en.mapy.cz/zakladni?x=14.3999996&y=50.0499992&z=18"
	test = "https://en.mapy.test.dszn.cz/zakladni?x=14.3999996&y=50.0499992&z=11"
	test_max_zoom = "https://en.mapy.test.dszn.cz/zakladni?x=14.3999996&y=50.0499992&z=18"
	dev = "https://mapy.dev.dszn.cz/zakladni?x=14.3999996&y=50.0499992&z=11"
	
	#production = test

	driver.get(production)



	class TransportType_planning(object):
		"""docstring for TransportType"""
		def __init__(self):
			self.all_types = driver.find_elements_by_class_name('type-radiocheck')

		def length(self):
			print(len(self.all_types), 'all transport types')

		def auto(self):
			self.all_types[0].click()

		def byke(self):
			self.all_types[3].click()


		

	class TransportType_trip(object):
		"""docstring for TransportType"""
		def __init__(self):
			self.all_types = driver.find_elements_by_class_name('type-radiocheck')


		def foot(self):
			self.all_types[0].click()

		def byke(self):
			self.all_types[1].click()

		def max_dist(self):
			elem = driver.find_element_by_class_name('circuit-bar-button')
			ActionChains(driver).drag_and_drop_by_offset(elem,1000, 1000).perform()	


	class ChangeMap(object):
		def __init__(self):
			self.elem = driver.find_element_by_css_selector('.icon.mapset').click()
			self.maps =  driver.find_elements_by_tag_name('li')


		def base(self):
			self.maps[-16].click()					

		def historic(self):
			self.maps[-4].click()

		def traffic(self):
			self.maps[-7].click()		




	
	def share_button():
		
		elem = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/button')
		elem.click()
		elem = driver.find_element(By.CLASS_NAME, 'share-slider')
		elem.click()


	



	def signIn_check():
		#signIn
		elem = driver.find_element_by_xpath(locators.register['signIn'])
		elem.click()
		handle= driver.window_handles

		#print(handle[1])
		driver.switch_to_window(handle[1])
		elem = driver.find_element_by_xpath(locators.register['mail']).send_keys( "mapytesting2" )
		elem = driver.find_element_by_xpath(locators.register['pass']).send_keys( "testingmapy" )
		elem = driver.find_element_by_xpath(locators.register['enter']).click()
		timeOut()
		handle= driver.window_handles
		driver.switch_to_window(handle[0])




	def search_link(search_text):
		elem = driver.find_element_by_xpath('//*[@id="input-search"]').send_keys(search_text)
		timeOut()
		elem = driver.find_element_by_xpath('//*[@id="input-search"]').send_keys(u'\ue007')


	def tools_share(category):
		#nastroje
		timeOut()
		#elem = driver.find_element_by_class_name("icon tools")
		elem = driver.find_element(By.CSS_SELECTOR, '.icon.tools')
		#elem = driver.find_element_by_xpath('//*[@id="map"]/div[2]/div[2]/div[8]/div/button[1]/span')
		elem.click()
		timeOut()
		print('tools clicked')

		#share
		elem = driver.find_element_by_xpath('//*[@id="mapycz"]/div[5]/div/div[1]/span')
		elem.click()
		timeOut()



		#share form with slider with 
		#slide button
		elem = driver.find_elements(By.CLASS_NAME, 'share-slider')
		if len(elem) > 0:
			elem[0].click()
			print('slider clicked')

			#copy button in share form with slider
			timeOut()
			elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button')
			elem.click()
			timeOut()

		else:	
			#copy button
			elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/button')
			elem.click()
			timeOut()



		print(pyperclip.paste())


		with open('links.csv', 'a') as csvFile:
			writer = csv.writer(csvFile)
			row = [f'{category}', f'{pyperclip.paste()}']
			writer.writerow(row)
		csvFile.close()


		#close share
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/button')
		elem.click()
		timeOut()


		#close tools
		elem = driver.find_element_by_xpath('//*[@id="mapycz"]/div[5]/button')
		elem.click()
		timeOut()








	def my_points():
		"""
			10 points from logged in account
			add two lines to csv - unsaved 10 points and saved 10 points
		"""

		#nastroje
		timeOut()
		elem = driver.find_element(By.CSS_SELECTOR, '.icon.tools')
		elem.click()
		timeOut()
		print('tools clicked')

		#my mark
		elem = driver.find_element_by_xpath('//*[@id="mapycz"]/div[5]/div/div[8]/span ')
		elem.click()
		timeOut()

		#select map
		elem = driver.find_element_by_xpath('//*[@id="map"]')

		for i in range(10):
			ActionChains(driver).move_by_offset(-10, 0).click().perform()	
		timeOut()

		#change last point name
		elem = driver.find_elements(By.TAG_NAME, 'input')
		elem[-3].send_keys('Last')
		timeOut()

		tools_share('Unsaved My points')

		#end adding points - Save button
		elem = driver.find_element_by_xpath('//*[@id="usermarks"]/div/div[2]/ul/li[10]/div[2]/div[2]/button[1]')
		elem.click()

		
		
		#save points Star button
		elem = driver.find_element_by_xpath('//*[@id="usermarks"]/div/div[1]/div/div[2]/div[1]/div[1]/button')
		elem.click()
		timeOut()


		#add name		
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/input')
		for i in range(20):
			elem.send_keys(u'\ue003')
		elem.send_keys('New added points')	
		
		
		#save
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/button[1]')
		elem.click()
		print('saved')

		timeOut(tick = 2.0)




		tools_share('Saved my points')


		# #share
		# elem = driver.find_element_by_xpath('//*[@id="usermarks"]/div/div[1]/div/div[2]/div[1]/div[2]/button')
		# elem.click()
		# timeOut()
		# print('share button')


		# #slide button
		# elem = driver.find_element(By.CLASS_NAME, 'share-slider')
		# elem.click()
		# print('slider clicked')
		# #print(go)



		# timeOut()
		# #copy button
		# elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button')
		# elem.click()
		# timeOut()

		# with open('links.csv', 'a') as csvFile:
		# 	writer = csv.writer(csvFile)
		# 	row = ['Saved my points', f'{pyperclip.paste()}']
		# 	writer.writerow(row)
		# csvFile.close()




	def measurements():
		timeOut()	
		elem = driver.find_element_by_xpath('//*[@id="map"]/div[2]/div[2]/div[7]/div/button[1]/span').click()
		timeOut()



		elem = driver.find_element_by_xpath(locators.tools['my_points']).click()
		timeOut()

		elem = driver.find_element_by_xpath('//*[@id="map"]')
		# timeOut()

		
		# #two_points
		# elem.click()
		# ActionChains(driver).move_by_offset(50, 50).click().perform()


		#many points
		for i in range(10):
			if i%50 == 0:
				#ActionChains(driver).send_keys(u'\ue015').perform()
				ActionChains(driver).click_and_hold(elem).move_by_offset(100, 100).release().perform()
			else:
				ActionChains(driver).move_by_offset(-10, 0).click().perform()	
		timeOut()



		#ukoncit mereni button
		elem = driver.find_element_by_xpath('//*[@id="scene"]/button').click()
		#elem = driver.find_element_by_xpath('//*[@id="map"]').click()
		timeOut()


		tools_share('Unsaved measurements')


		#save mereni
		elem = driver.find_element_by_xpath('//*[@id="distance-meter"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/button').click()
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/button[1]').click()


		tools_share('Saved measurements')



	def poi_detail():
		search_link('Eiffel tower')
		#elem = driver.find_elements(By.CLASS_NAME, 'content')
		#elem[0].click()

		tools_share('Unsaved poi detail')

		timeOut()
		#elem = driver.find_element_by_css_selector('svg.icon.icon-star-line').click()
		elem = driver.find_elements(By.CSS_SELECTOR, "div[class='icon-action']")
		elem[1].click()
		#elem = driver.find_element_by_xpath('//*[@id="detail"]/div[3]/div[5]/div[2]/button').click()
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/button[1]').click()

		tools_share('Saved poi detail')


		elem = driver.find_element_by_xpath('//*[@id="detail"]/div[3]/div[6]/div[2]/button').click()

		#add name		
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[1]/input')
		for i in range(20):
			elem.send_keys(u'\ue003')
		elem.send_keys('Vlastni nazev poi detail')	

		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[4]/button[1]').click()


		tools_share('Saved poi detail changed name')


	def coor():
		elem = driver.find_element_by_id('map')
		
		print(elem.size)
		print(elem.location)

		elem.click()


		ActionChains(driver).move_by_offset(100, 100).context_click().perform()
		timeOut()
		elem = driver.find_element_by_partial_link_text('What')
		elem.click()

		tools_share('Unsaved coor')

		elem = driver.find_element_by_xpath('//*[@id="detail"]/div[3]/div[4]/div[2]/button').click()
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/button[1]').click()
		
		tools_share('Saved coor')


		elem = driver.find_element_by_xpath('//*[@id="detail"]/div[3]/div[5]/div[2]/button').click()
		#add name		
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[1]/input')
		for i in range(20):
			elem.send_keys(u'\ue003')
		elem.send_keys('Vlastni nazev coor')	

		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[4]/button[1]').click()


		tools_share('Saved coor changed name')




	def planning_unsaved():
		#Planning button
		planning_button = driver.find_element(By.CSS_SELECTOR, "button.icon.route")
		
		


		planning_button.click()
		start = driver.find_element_by_xpath('//*[@id="route-form"]/div[3]/div[1]/div/input')
		finish = driver.find_element_by_xpath('//*[@id="route-form"]/div[3]/div[2]/div/input')
		#start
		start.send_keys("Praha")
		start.send_keys(u'\ue007')
		timeOut()

		tools_share('Unsaved route with one point')
		
		#Finish
		finish.send_keys("Mlada Boleslav")
		finish.send_keys(u'\ue007')
		timeOut()

		tools_share('Unsaved route')



		planning_button.click()
		start = driver.find_element_by_xpath('//*[@id="route-form"]/div[3]/div[1]/div/input')
		finish = driver.find_element_by_xpath('//*[@id="route-form"]/div[3]/div[2]/div/input')
		
		#start
		start.send_keys("Praha")
		start.send_keys(u'\ue007')
		timeOut()

		#Finish
		finish.send_keys("Budapest")
		finish.send_keys(u'\ue007')
		timeOut()

		# auto = TransportType()
		# auto.length()
		# auto.byke()

		timeOut()
		avoid_pay = driver.find_element_by_xpath('//*[@id="route-params-box"]/div/div[2]/div/label[3]/span')
		avoid_Slovakia = driver.find_element_by_xpath('//*[@id="route-params-box"]/div/div[2]/div/label[3]/div/ul/li[2]/label/span/p[1]')
		
		

		avoid_pay.click()
		avoid_Slovakia.click()
		timeOut()
		tools_share('Unsaved Praha Budapest no Slovakia')



		no_pay = driver.find_element_by_xpath('//*[@id="route-params-box"]/div/div[2]/div/label[3]/div/div[2]/label/span/p')
		avoid_pay.click()
		no_pay.click()
		timeOut()
		tools_share('Unsaved Praha Budapest no pay')



		all_pay = driver.find_element_by_xpath('//*[@id="route-params-box"]/div/div[2]/div/label[3]/div/div[2]/label/span/p')
		avoid_pay.click()
		all_pay.click()
		timeOut()
		tools_share('Unsaved Praha Budapest pay')



		avoid_pay.click()
		avoid_Slovakia = driver.find_element_by_xpath('//*[@id="route-params-box"]/div/div[2]/div/label[3]/div/ul/li[2]/label/span/p[1]')
		avoid_Slovakia.click()
		avoid_Hungary = driver.find_element_by_xpath('//*[@id="route-params-box"]/div/div[2]/div/label[3]/div/ul/li[3]/label/span/p[1]')
		avoid_Hungary.click()
		timeOut()
		tools_share('Unsaved Praha Budapest part pay')




	def planning_saved():
		planning_button = driver.find_element(By.CSS_SELECTOR, "button.icon.route")
		planning_button.click()
		start = driver.find_element_by_xpath('//*[@id="route-form"]/div[3]/div[1]/div/input')
		finish = driver.find_element_by_xpath('//*[@id="route-form"]/div[3]/div[2]/div/input')
		#start
		start.send_keys("Praha")
		start.send_keys(u'\ue007')
		timeOut()
		
		#Finish
		finish.send_keys("Mlada Boleslav")
		finish.send_keys(u'\ue007')
		timeOut()


		#save
		elem = driver.find_elements(By.CSS_SELECTOR, "div[class='icon-action']")
		elem[0].click()
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/button[1]').click()


		tools_share('Saved route')



		planning_button.click()
		start = driver.find_element_by_xpath('//*[@id="route-form"]/div[3]/div[1]/div/input')
		finish = driver.find_element_by_xpath('//*[@id="route-form"]/div[3]/div[2]/div/input')
		
		#start
		start.send_keys("Praha")
		start.send_keys(u'\ue007')
		timeOut()

		#Finish
		finish.send_keys("Budapest")
		finish.send_keys(u'\ue007')
		timeOut()


		timeOut()
		avoid_pay = driver.find_element_by_xpath('//*[@id="route-params-box"]/div/div[2]/div/label[3]/span')
		avoid_Slovakia = driver.find_element_by_xpath('//*[@id="route-params-box"]/div/div[2]/div/label[3]/div/ul/li[2]/label/span/p[1]')
		
		
		avoid_pay.click()
		avoid_Slovakia.click()
		timeOut()



		#save
		elem = driver.find_elements(By.CSS_SELECTOR, "div[class='icon-action']")
		elem[0].click()
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/button[1]').click()

		tools_share('Saved Praha Budapest no Slovakia')





		no_pay = driver.find_element_by_xpath('//*[@id="route-params-box"]/div/div[2]/div/label[3]/div/div[2]/label/span/p')
		avoid_pay.click()
		no_pay.click()
		timeOut()


		#save
		elem = driver.find_elements(By.CSS_SELECTOR, "div[class='icon-action']")
		elem[0].click()
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/button[2]')
		elem.click()
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[1]/input')
		for i in range(40):
			elem.send_keys(u'\ue003')
		elem.send_keys('Praha Budapest no pay')
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[4]/button[1]').click()

		tools_share('Saved Praha Budapest no pay')








		all_pay = driver.find_element_by_xpath('//*[@id="route-params-box"]/div/div[2]/div/label[3]/div/div[2]/label/span/p')
		avoid_pay.click()
		all_pay.click()
		timeOut()


		#save
		elem = driver.find_elements(By.CSS_SELECTOR, "div[class='icon-action']")
		elem[0].click()
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/button[2]')
		elem.click()
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[1]/input')
		for i in range(40):
			elem.send_keys(u'\ue003')
		elem.send_keys('Praha Budapest pay')
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[4]/button[1]').click()

		tools_share('Saved Praha Budapest pay')



		avoid_pay.click()
		avoid_Slovakia = driver.find_element_by_xpath('//*[@id="route-params-box"]/div/div[2]/div/label[3]/div/ul/li[2]/label/span/p[1]')
		avoid_Slovakia.click()
		avoid_Hungary = driver.find_element_by_xpath('//*[@id="route-params-box"]/div/div[2]/div/label[3]/div/ul/li[3]/label/span/p[1]')
		avoid_Hungary.click()
		timeOut()
		


		#save
		elem = driver.find_elements(By.CSS_SELECTOR, "div[class='icon-action']")
		elem[0].click()
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/button[2]')
		elem.click()
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[1]/input')
		for i in range(40):
			elem.send_keys(u'\ue003')
		elem.send_keys('Saved Praha Budapest part pay')
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[4]/button[1]').click()
			
		tools_share('Saved Praha Budapest part pay')
		



	def vylet():
		elem = driver.find_element_by_id('map')


		# ActionChains(driver).move_by_offset(100, 100).context_click().perform()
		# timeOut()

		timeOut()
		ActionChains(driver).move_to_element(elem).context_click().perform()
		timeOut()



		elem = driver.find_element_by_partial_link_text('Trip')
		elem.click()

		timeOut()

		trip = TransportType_trip()
		trip.byke()
		timeOut()
		trip.max_dist()
		tools_share('Unsaved trip byke max')


		#save
		elem = driver.find_elements(By.CSS_SELECTOR, "div[class='icon-action']")
		elem[0].click()
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/button[1]').click()


		tools_share('Saved trip byke max')




	def vylet_places():

		search_link('Slechtova restaurace')
		elem = driver.find_element_by_id('map')

		timeOut()
		ActionChains(driver).move_to_element(elem).context_click().perform()
		timeOut()

		elem = driver.find_element_by_partial_link_text('Trip')
		elem.click()

		timeOut()

		trip = TransportType_trip()
		#trip.foot()
		#timeOut()
		#trip.max_dist()
		tools_share('Unsaved trip foot with places')



		#save
		elem = driver.find_elements(By.CSS_SELECTOR, "div[class='icon-action']")
		elem[0].click()
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/button[1]').click()


		tools_share('Saved trip foot with places')



	def map():
		url = driver.current_url
		driver.get(url[:-2] + '19')

		tools_share('Base map max zoom')

		#change map button
		elem = driver.find_element_by_css_selector('.icon.mapset').click()
		elem = driver.find_element_by_class_name('letecka').click()
		tools_share('Aerial map max zoom')


		#traffic
		elem = driver.find_element_by_css_selector('.icon.mapset').click()
		elem = driver.find_element_by_class_name('dopravni').click()
		tools_share('Traffic map')


		#historic
		elem = driver.find_element_by_css_selector('.icon.mapset').click()
		elem = driver.find_element_by_xpath('//*[@id="mapset-switch"]/ul[2]/li[12]').click()
		tools_share('Historic map')


		#base
		elem = driver.find_element_by_css_selector('.icon.mapset').click()
		elem = driver.find_element_by_xpath('//*[@id="mapset-switch"]/ul[2]/li[1]').click()	

		elem = driver.find_element_by_css_selector('.icon.ophoto').click()		
		tools_share('Aerial from button')


	def panorama():
		driver.get(production + '&pano=1')
		#elem = driver.find_element_by_id('map')
		elem = driver.find_element_by_css_selector('.icon.mapset')
		ActionChains(driver).move_to_element_with_offset(elem, 150, 150).click().perform()

		#ActionChains(driver).move_by_offset(150, 150).perform()
		tools_share('Panorama')



	def d3():
		elem = driver.find_element_by_class_name('left3d-btn').click()
		timeOut(tick = 2.0)
		tools_share('3D')




	#???maybe out somewhere
	#driver.close()



	#browser('chrome', 'prod')
	
	signIn_check()
	
	search_link('golf')
	timeOut()
	tools_share('Search link')


	driver.get(production)
	my_points()

	driver.get(production)
	measurements()
	driver.get(production)

	poi_detail()

	driver.get(test_max_zoom)
	timeOut()
	coor()

	driver.get(production)
	planning_unsaved()
	driver.get(production)
	planning_saved()


	driver.get(production)
	vylet()
	driver.get(production)
	vylet_places()


	driver.get(production)
	map()


	driver.get(production)
	panorama()


	driver.get(production)
	d3()




	#a = TransportType()
	#a.length()



if __name__ == '__main__':
	chrome_prod()		

