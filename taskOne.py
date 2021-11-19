# Сценарий 1 - открытие страницы.
# 1.	Открыть браузер.
# 2.	Очистить кэш браузера
# 3.	Перейти на http://tensor.ru/
# Собрать максимально возможное количество метрик, характеризующих скорость открытия страницы (например, события жизненного цикла страницы https://www.w3.org/TR/navigation-timing/)

import json
import pychrome
from pychrome import tab
import subprocess
import time


metrics = "JSON.stringify(window.performance.timing);"

subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir=remote-profile")
time.sleep(5)

browser = pychrome.Browser(url='http://127.0.0.1:9222')
tab = browser.new_tab()

tab.start()
tab.Network.enable()
tab.Network.clearBrowserCache()
tab.Performance.enable()
tab.Page.navigate(url= "http://tensor.ru/", _timeout=20) 
tab.wait(20)

tab.Runtime.enable() 
scriptId = tab.Runtime.compileScript(expression=metrics, sourceURL="http://tensor.ru/", persistScript=True)
timing_data = json.loads(tab.Runtime.runScript(scriptId=scriptId["scriptId"])["result"]["value"])
print(timing_data)

timings = {}
timings["severConnectTime"] = timing_data["connectEnd"] - timing_data["connectStart"]
timings["pageLoadTime"] = timing_data["loadEventEnd"] - timing_data["navigationStart"]
timings["renderTime"] = timing_data["domComplete"] - timing_data["domLoading"]
timings["domainLookup"] = timing_data["domainLookupEnd"] - timing_data["domainLookupStart"]
timings["interactive"] = timing_data["domInteractive"] - timing_data["domLoading"]
timings["contentLoadedEvent"] = timing_data["domContentLoadedEventEnd"] - timing_data["domContentLoadedEventStart"]
timings["processingToInteractive"] = timing_data["domInteractive"] - timing_data["domLoading"]


tab.wait(2)
tab.stop()
browser.close_tab(tab)   