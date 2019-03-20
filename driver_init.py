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
  "autoGrantPermissions": "true"
}




driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
print('start wait')
driver.implicitly_wait(30)
print('end wait')