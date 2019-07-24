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
	test = "https://mapy.test.dszn.cz/zakladni?x=14.3999996&y=50.0499992&z=11"
	dev = "https://mapy.dev.dszn.cz/zakladni?x=14.3999996&y=50.0499992&z=11"
	driver.get(production)



	class TransportType(object):
		"""docstring for TransportType"""
		def __init__(self):
			self.all_types = driver.find_elements_by_class_name('type-radiocheck')

		def length(self):
			print(len(self.all_types), 'all transport types')

		def auto(self):
			self.all_types[0].click()

		def byke(self):
			self.all_types[3].click()		

	
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


	def delete_all():
		
		elem = driver.find_element_by_xpath('//*[@id="layout-bar"]/button[3]/span[2]')
		elem.click()

		#elem = driver.find_elements_by_class_name('head-section')
		elem = driver.find_elements_by_css_selector('items.sortable.items.public')
		#elem = driver.find_elements(By.CLASS_NAME, "folder")
		#elem = driver.find_elements(By.CSS_SELECTOR, '.icon.tools')
		#elem = driver.find_elements(By.CSS_SELECTOR, '.icon.tools')
		print(len(elem))
		#elem.click()
		#elem[-1].click()
		#elem = driver.find_elements(By.CLASS_NAME, 'contextmenu-item')
		#elem[-1].click()

		#elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/button[1]')
		#elem.click()

		


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
		
















	def zoom_check():
		#zoom
		elem = driver.find_element_by_xpath('//*[@id="map"]/div[2]/div[2]/div[6]/div/button[1]')
		elem.click()
		cur_url = driver.current_url
		timeOut(tick = 0.5)
		try:
			cur_url[-2:] == '10'
			print('zoom out ok')
		except:
			print ('error zoom out')	

		elem = driver.find_element_by_xpath('//*[@id="map"]/div[2]/div[2]/div[6]/div/button[2]')
		elem.click()
		cur_url = driver.current_url
		try:
			cur_url[-2:] == '11'
			print('zoom in ok')
		except:
			print ('error zoom in')




	def tools_check():
		#nastroje
		elem = driver.find_element_by_xpath('//*[@id="map"]/div[2]/div[2]/div[7]/div/button[1]')
		elem.click()
		
		try:	
		    elem = driver.find_element_by_xpath('//*[@id="mapycz"]/div[5]')	
		except:
		    print ('no tools pop-up')
		elem = driver.find_element_by_xpath('//*[@id="map"]/div[2]/div[2]/div[7]/div/button[1]')
		elem.click()
		try:	
		    elem = driver.find_element_by_xpath('//*[@id="mapycz"]/div[5]')	
		except:
		    print ('tools pop-up hiden')    





	def reportError_check():
		#report error
		elem = driver.find_element_by_xpath('//*[@id="map"]/div[2]/div[2]/div[7]/div/button[2]')
		elem.click()
		
		try:	
		    elem = driver.find_element_by_xpath('//*[@id="mapycz"]/div[5]')	
		except:
		    print ('no error pop-up')

		elem = driver.find_element_by_xpath('//*[@id="map"]/div[2]/div[2]/div[7]/div/button[2]')
		elem.click()
		try:	
		    elem = driver.find_element_by_xpath('//*[@id="mapycz"]/div[5]')	
		except:
		    print ('error pop-up hiden')





	def resize_check():
		#resize
		elem = driver.find_element_by_xpath('//*[@id="resizer"]')
		elem.click()


		body= driver.find_element_by_tag_name("Body").get_attribute("class")
		print (body)

		cur_url = driver.current_url
		try:
			cur_url[-1] == '0'
			print('resize ok')
		except:
			print ('error resize')



		driver.get(production + '&l=0')
		elem = driver.find_element_by_id('resizer')
		elem.click()
		print('resize back')
		
		timeOut(tick = 2.0)


		body= driver.find_element_by_tag_name("Body").get_attribute("class")
		print (body)

		cur_url = driver.current_url
		try:
			cur_url[-1] == '1'
			print('resize back ok')
		except:
			print ('error resize back')







	def measure_check():
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
		for i in range(1000):
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



		#save mereni
		elem = driver.find_element_by_xpath('//*[@id="distance-meter"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/button').click()
		elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/button[1]').click()





		elem = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/p/span[1]')
		#print (elem.get_attribute('innerHTML'))
		gain = elem.get_attribute('innerHTML')
		print (gain, 'gain')


		elem = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/p/span[2]')
		#print (elem.get_attribute('innerHTML'))
		loss = elem.get_attribute('innerHTML')
		print (loss, 'loss')



		elem = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[6]/span[1]')
		#print (elem.get_attribute('innerHTML'))
		low = elem.get_attribute('innerHTML')
		print (low, 'lowest')



		elem = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[7]/span[1]')
		#print (elem.get_attribute('innerHTML'))
		high = elem.get_attribute('innerHTML')
		print (high, 'highest')


#input-search
	def search_check():
		elem = driver.find_element_by_xpath('//*[@id="input-search"]').send_keys( "Leeds" )
		timeOut()
		elem = driver.find_element_by_xpath('//*[@id="input-search"]').send_keys(u'\ue007')
		#timeOut(tick = 0.3)
		#elem = driver.find_element_by_xpath('//*[@id="search"]/form/span').click()
		timeOut(tick = 3.0)
		#//*[@id="search"]/div[1]/img


	def click_6000():
		pass
		# elem = driver.find_element_by_id('map')
		# print (elem.size)


		# actionChains = webdriver.ActionChains(driver)

		# #scroll = TouchAction(driver)
		# #scroll.press(x=480, y=761).move_to(x=469, y=430).release().perform()

			




		




	    


		             			











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

	driver.get(production_max_zoom)
	timeOut()
	coor()

	driver.get(production)
	planning_unsaved()
	driver.get(production)
	planning_saved()

	#a = TransportType()
	#a.length()



if __name__ == '__main__':
	chrome_prod()		

