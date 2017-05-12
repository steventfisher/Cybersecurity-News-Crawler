#/usr/bin/python2

#author: Steven Fisher
#Written for CS 645 at University of Nevada, Reno
#fisher-project.py version 0.5

import sys
import webbrowser
import time
import urllib
from bs4 import BeautifulSoup

def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return

def get_all_links(page):
    s = BeautifulSoup(page, 'lxml')
    links = []
    check_count = 0
    non_valid_link = load_nonvalid()
    for link in s.find_all('a'):
        check_count = 0
        add_link = link.get('href')
        if add_link != None:
            if add_link.find('http') != -1:
                for non_v in non_valid_link:
                    check_lnk = add_link.find(non_v)
                    if check_lnk != -1:
                        check_count += 1
                if check_count == 0:
                    if add_link not in links:
                        links.append(add_link)
    return links
            
def check_targetkeyword(page, keylist):
    key_count = 0
    s = BeautifulSoup(page, 'lxml')
    for key in keylist:
        page_text = s.get_text()
        key_present = page_text.lower().find(key)
        if key_present != -1:
            key_count += 1
    if key_count > 0:
        return 'add_to'
    return ""
        
def add_web_page(add_url):
    file = open('links.txt', 'a')
    file.write(add_url + '\n')
    file.close()

def add_keyword(keyword):
    file = optn('keyword.txt', 'a')
    file.write(keyword + '\n')
    file.close()

def load_news_links():
    file = open('links.txt', 'r')
    lnks = file.read().splitlines()
    file.close()
    return lnks

def load_keywords():
    file = open('keywords.txt', 'r')
    keys = file.read().splitlines()
    file.close()
    return keys

def load_nonvalid():
    file = open('non_valid.txt', 'r')
    nonvld = file.read().splitlines()
    file.close()
    return nonvld

def create_news_site(news_list):
    file_name = 'News ' + time.ctime() + '.html'
    file = open(file_name, 'a')
    file.write('<html>\n')
    file.write('<body>\n')
    for site in news_list:
        file.write('<a href=' + site + '>' + site + '</a><br>\n')
    file.write('</body>\n </html>')
    file.close()
    print 'News article links has been saved to ' + file_name
    open_sel = raw_input('Do you wish to open ' + file_name + '?(y/n) ')
    if open_sel.lower() == 'y' or open_sel.lower() == 'yes' or open_sel.lower() == 'ye':
        webbrowser.open_new(file_name)
    else:
        return

def main():
    good_sel = True
    collection = []
    key_sites = []
    print('\n')
    while good_sel:
        print('Main Menu')
        print('1. Maintenance')
        print('2. Crawl News Sites')
        print('3. Quit')
        selection = raw_input('Please enter 1, 2 or 3: ')

        if selection == '1':
            print('\n'*2)
            print('Crawler Maintenance\n')
            print('1. Add URL to list of sites')
            print('2. Add a keyword to list')
            print('3. Back to main menu')
            maint_sel = raw_input('Please choose 1, 2 or 3: ')
            if maint_sel == '1':
                new_url = raw_input('\nPlease enter in the new url: ')
                add_web_page(new_url)
            elif maint_sel == '2':
                new_key = raw_input('\nPlease enter in a new keyword: ')
                add_keyword(new_key)
            elif maint_sel == '3':
                pass
            else:
                pass
        elif selection == '2':
            sites_tocrawl = load_news_links()
            cyber_words = load_keywords()
            for site in sites_tocrawl:
                collection = get_all_links(get_page(site))
                for subsite in collection:
                    print 'CHECKING FOR KEYWORDS IN: ' + subsite
                    try:
                        keywd = check_targetkeyword(get_page(subsite), cyber_words)
                        if keywd == 'add_to': 
                            key_sites.append(subsite)
                    except:
                        print 'Cannot Access Site'
            web_page = create_news_site(key_sites)
            quit()
        elif selection == '3':
            break
        else:
            print('Invalid Choice')

main()
