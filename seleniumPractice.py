# No matter what you do, our autograder will only run your analyze() function 
# and expect it to return the correct answers of Q1 & Q2 as a list
# and generate three screenshots for Q3 with '1.png', '2.png', & '3.png' as filenames.
import lxml.html
import urllib.request
from selenium import webdriver
def analyze():
    # write your codes here...
    URL='http://www.ptt.cc'
    URN='/bbs/Boy-Girl/'
    h={'User-Agent':'Mozilla/5.0'}
    r=urllib.request.Request(URL+URN,headers=h)
    data=urllib.request.urlopen(r).read()
    t=lxml.html.fromstring(data.decode('utf-8'))
    
    #1
    y = t.xpath('//a[contains(text(),"上頁")]')[0]
    returnLink = y.attrib.get('href')
    page = returnLink[returnLink.find('index')+5:returnLink.find('.html')]

    #2
    numOfFamous = len(t.xpath('//span[@class="hl f1"]'))
    if numOfFamous!=0:
        theFamousArticlePath=t.xpath('//span[@class="hl f1"]')[numOfFamous-1].getparent().getparent().getchildren()
        for temp in theFamousArticlePath:
            if temp.get('class')=='title':
                divTitle = temp.getchildren()
    else:
        i=0
        while(True):
            uri ='http://www.ptt.cc/bbs/Boy-Girl/index%s.html' %str(int(page)-i)
            R = urllib.request.Request(uri,headers=h)
            temData = urllib.request.urlopen(R).read()
            tem =lxml.html.fromstring(temData.decode('utf-8'))           
            numOfFamous = len(tem.xpath('//span[@class="hl f1"]'))
            i=i+1
            if numOfFamous != 0:
                break;
        theFamousArticlePath=tem.xpath('//span[@class="hl f1"]')[numOfFamous-1].getparent().getparent().getchildren()
        for temp in theFamousArticlePath:
            if temp.get('class')=='title':
                divTitle = temp.getchildren()
        famousURN=divTitle[0].get('href')
    
    #3
    driver=webdriver.Chrome()
    driver.get(URL+URN)
    for i in range(1,4):
        btn = driver.find_element_by_xpath('//a[contains(text(),"上頁")]')
        btn.click()
        driver.save_screenshot(str(i)+'.png')
    driver.quit()
    
    

            
    return [page,divTitle[0].text,famousURN]

analyze()    