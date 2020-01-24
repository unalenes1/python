# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:31:46 2019

@author: Casper
"""

from bs4 import BeautifulSoup
import urllib.request

url = "https://portal-widgets-v3.foreks.com/gold"
url_oku = urllib.request.urlopen(url)
soup = BeautifulSoup(url_oku, 'html.parser')

deneme=soup.body.table.tbody.tr
driver.find_element_by_css_selector("soup.body.table.tbody.tr > fieldset > label:nth-child(1)")
print(driver)

print("-------")
print(deneme)