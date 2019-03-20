from driver_init import driver


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