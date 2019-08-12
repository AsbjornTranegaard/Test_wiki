"""Importing packages"""
#s
from bs4 import BeautifulSoup, NavigableString
import urllib3
import requests
import re

"""
Collecting link
"""

# skal synkroniseres til wikis API, som skal udgøre søgefunktionen

target_url = 'https://en.wikipedia.org/wiki/Second_Schleswig_War'
basis = requests.get(target_url)

soup = BeautifulSoup(basis.text, features="html5lib")

"Create empty lists"
#result = []
results = []
href = []
title = []
href_2 = []
title_2 = []

"""
Scraping links from summary of target article
"""

# Der mangler stadig at hente summary fra målet

# Lav funktion for at hente links og titel


def summary(suppefil):
    for l in suppefil.find('div', class_="mw-parser-output").find_all(recursive=False):
        try:
            temp_name = ""
            #if temp_name == 'p' and l.name != str('p'):     # denne virker ikke, da temp_name slettes efter hvert loop
            #    break
            if l.name == "h2":
                break
            #elif l.name == 'div' and 'role' == 'note':  # ikke sikker på, at denne virker
            #    pass
            #elif l.name == 'h2':
            #    break
            #elif l.name == 'div' and 'class' == 'toclimit-3':  # ikke sikker på, at denne virker
            #    break
            elif l.name == 'p':
                if l.text == '\n' or l.text == '\n\n' or l.text == ' \n' or l.text == '\n\n\n':
                    pass
                else:
                    results.append(l.text)      # her skal indsættes funktion, der henter nye links
            else:                               # Derudover skal resultater gemmes i SQL, så det kan matches med link og titel
                pass
            #temp_name=k.name
        except AttributeError:
            pass
    results.append("\n\n")                      #Denne skal erstattes af funktion, der indsætter tekst i SQL


def primary_links(suppefil):
    for k in suppefil.find('div', class_="mw-parser-output").find_all(recursive=False):
        temp = ""
        if temp == 'p' and k.name != str('p'):
            break
        elif k.name == "h2":
            break
        else:
            for j in k.find_all('a', href=True, title=True, recursive=False):
                href.append('https://en.wikipedia.org' + j['href'])
                title.append(j['title'])
                # indsæt href og title i SQL
        temp = str(k.name)


def secondary_links(suppefil):
    for k in suppefil.find('div', class_="mw-parser-output").find_all(recursive=False):
        temp = ""
        if temp == 'p' and k.name != str('p'):
            break
        elif k.name == "h2":
            break
        else:
            for j in k.find_all('a', href=True, title=True, recursive=False):
                href_2.append('https://en.wikipedia.org' + j['href'])
                title_2.append(j['title'])
                # indsæt href og title i SQL
        temp = str(k.name)


summary(soup)

primary_links(soup)

#links = dict(zip(title, href))
"""
Collecting summaries from related articles
"""


#Denne henter summary fra alle links i 'href', der indeholder alle initiale links
for i in href:
    temp_url = requests.get(str(i), timeout=5)
    suppe = BeautifulSoup(temp_url.text, features="html5lib")
    "Scraping summary"
    summary(suppe)
    secondary_links(suppe)




