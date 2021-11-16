# Сценарий 1 - открытие страницы.
# 1.	Открыть браузер.
# 2.	Очистить кэш браузера
# 3.	Перейти на http://tensor.ru/
# Собрать максимально возможное количество метрик, характеризующих скорость открытия страницы (например, события жизненного цикла страницы https://www.w3.org/TR/navigation-timing/)

import pychrome
from pychrome import tab
import subprocess
import time

subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir=remote-profile")
time.sleep(5)

browser = pychrome.Browser(url='http://127.0.0.1:9222')
tab = browser.new_tab()

tab.start()
tab.call_method("Network.enable")
tab.call_method("Network.clearBrowserCache")

time.sleep(5)

tab.stop()
browser.close_tab(tab)   