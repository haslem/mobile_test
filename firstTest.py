from appium import webdriver

desired_cap = {
  "deviceName": "4df134143e934f4d",
  "platformName": "Android",
  "app": "C:\\my\\auto\\mobile\\Windy Maps_v1.1.0_apkpure.com.apk"
}


driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

print ('Done')