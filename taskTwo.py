"""
Сценарий 2 - открытие стек-панели.
1.	Открыть браузер.
2.	Очистить кэш браузера.
3.	Перейти на https://online.sbis.ru/auth/?ret=%2Fauth
4.	Кликнуть на элемент “ДЕМО”
5.	Кликнуть на элемент “Электронный документооборот”
6.	Кликнуть на первый элемент в списке 
"""

import pychrome
from pychrome import tab
import subprocess
import time

SEARCH_DEMO = '[href="/auth/?ret=%2Fauth&tab=demo"]'
SEARCH_ITEM_DOC = '.demo-Auth__item.reporting '
SEARCH_NAVIG_PANEL = 'a:nth-child(3) span.NavigationPanels-Accordion__title.NavigationPanels-Accordion__title_level-1'
SEARCH_SUBMENU = 'td:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a > span.NavigationPanels-SubMenu__subMenuTitle.NavigationPanels-Accordion__prevent-default'
SEARCH_CONTAINER = '.controls-GridViewV__itemsContainer > div:nth-child(1) > div:nth-child(4) > div'


def fieldId(tab, node_id, selector):
    return tab.call_method("DOM.querySelector", nodeId=node_id, selector=selector)["nodeId"] 

def get_click_coords(node_id):
    box_model = tab.call_method("DOM.getBoxModel", nodeId=node_id)["model"]["content"]
    return box_model[0], box_model[1]

def mouseClick(tab, xCoord, yCoord):
    tab.call_method("Input.dispatchMouseEvent", type="mousePressed", x=xCoord, y=yCoord, button="left", clickCount=1)
    tab.call_method("Input.dispatchMouseEvent", type="mouseReleased", x=xCoord, y=yCoord, button="left", clickCount=1)

def findField(selector):
    tab.call_method("DOM.enable")
    id_root = tab.call_method("DOM.getDocument")["root"]["nodeId"] 
    input_log = fieldId(tab, node_id=id_root, selector=selector)
    input_field_box_model = get_click_coords(node_id=input_log)
    mouseClick(tab, input_field_box_model[0], input_field_box_model[1])

subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir=remote-profile")
time.sleep(5)

browser = pychrome.Browser(url='http://127.0.0.1:9222')
tab = browser.new_tab()

tab.start()
tab.call_method("Network.enable")
tab.call_method("Network.clearBrowserCache")
tab.call_method("Page.navigate", url="https://online.sbis.ru/auth/?ret=%2Fauth", _timeout=5) 
tab.wait(5)

input_elem_demo = findField(selector=SEARCH_DEMO)
tab.wait(5)
input_elem_item_doc = findField(selector=SEARCH_ITEM_DOC)
tab.wait(10)
input_elem_navig_panel = findField(selector=SEARCH_NAVIG_PANEL)
tab.wait(5)
input_elem_sub_menu = findField(selector=SEARCH_SUBMENU)
tab.wait(7)
input_elem_cont = findField(selector=SEARCH_CONTAINER)
tab.wait(5)
time.sleep(5)

tab.stop()
browser.close_tab(tab)   