#!/usr/bin/python3
# -*- coding: utf-8 -*- 

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import requests
import re
import pymysql

#someone use this project you shoud change DRIVER_DIR  cuz your chromedriver.exe is not same point
#DRIVER_DIR = "C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome() #chrome driver root
driver.implicitly_wait(1) # to  stabilize the internet
endcheck = True#if information number is done it change False
pagenum=1 #pagenumber
infonum=2 #cuz number start 2 not 1
cnt1=0 #wevity crawling number
cnt2=0 #thinkgood crawling number


conn=pymysql.connect(host="localhost",user='root',password='ffdsffds',db='crawling',charset='utf8') #connecting to sql
curs=conn.cursor()


#-------------------------------------------------------------------------------------
#------------------wevity server receipt crawling ----------------------------------------------------
<<<<<<< HEAD
'''
while(endcheck):    
  driver.get('https://www.wevity.com/?c=find&s=1&mode=ing&gp='+str(pagenum)+'')
  time.sleep(2)
=======

while(endcheck): #infinity roof and if all information are crwaled endcheck is False and come out while   
  driver.get('https://www.wevity.com/?c=find&s=1&mode=ing&gp='+str(pagenum)+'') #wevitiy page. only str(pagenum) is change
  time.sleep(2) #to stabilize the internet
>>>>>>> 0e0d9b91ff1bd07d42fb912f3052d137cceb6222

  while(infonum<=16):
    try:
      time.sleep(1) #to stabilize the internet
      #weivity posts. only str(infonum) is change
      driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div[2]/div[3]/div/ul/li['+str(infonum)+']/div[1]/a').click() 
      
      # Extract the URL of the page and get information  
      URL=(driver.current_url) #
      res=requests.get(URL)
      html=res.text
              
      time.sleep(1) # to stabilize the internet
                    
      print("----- receipt page "+str(pagenum)+" page, "+str(infonum-1)+" information -----")
      # (title)
      re_title = re.compile(">(.*)</h6>", re.MULTILINE)
      title_tag = re_title.findall(html)
      print("title:")
      title='\n'.join(title_tag)
      print(title)

      #(organization)
      re_com = re.compile("주관</span>\s*(.*)\s*</li>", re.MULTILINE)
      com_tag = re_com.findall(html)
      print("com:")
      com='\n'.join(com_tag)
      print(com)

      #(term)
      re_day = re.compile("기간</span>\s*(.*)\s*<span", re.MULTILINE)
      day_tag = re_day.findall(html)
      print("day:")
      day='\n'.join(day_tag)
      print(day)

      #(information)
      re_info = re.compile("viewContents\">\s*(.*)</div>", re.MULTILINE)
      info_tag = re_info.findall(html)
      print("info:")

      info='\n'.join(info_tag)
      info=info.replace("/upload","https://www.wevity.com/upload")
      print(info)

      #(image)
      img_info = re.compile("<img src=\"(/upload/contest.*)\"\s*alt=\"공", re.MULTILINE)
      img_tag = img_info.findall(html)
      print("img:")

      img='\n'.join(img_tag)
      img=img.replace("/upload","https://www.wevity.com/upload")
      print(img)


      #(homepage)
      re_page = re.compile("홈페이지</span>\s*<a href=\"(.*?)\"", re.MULTILINE)
      page_tag = re_page.findall(html)
      print("page:")
      page='\n'.join(page_tag)
      print(page)
      
      try:#title company day information image page bring to homepage
        curs.execute("INSERT INTO avengers_crawling(title,com,day,info,img,page) VALUES(%s,%s,%s,%s,%s,%s)",(title,com,day,info,img,page))
        conn.commit()
        #타이틀 페이지 등의 중복
      except: # if any sources are duplicate then block duplicate data
        conn.rollback()
        print("중복된데이터")

      cnt1 = cnt1+1
              
              
      infonum=infonum+1

      driver.back()

    except NoSuchElementException:# if the crawling of the site's information are done so while statement is not work
      endcheck = False #to change infinity while -> false
      break
  infonum=2  #to reset num because we go next page
  pagenum=pagenum+1
    
  if endcheck == False:
    print("receipt crawling is finish ")
    break
'''
#-------------------------------------------------------------------------------------
#------------------wevity server to be receipt crawling ----------------------------------------------------
<<<<<<< HEAD
'''
endcheck = True
=======

endcheck = True #reset endcheck 
>>>>>>> 0e0d9b91ff1bd07d42fb912f3052d137cceb6222

pagenum2=1
infonum2=2
while(endcheck):  #infinity roof and if all information are crwaled endcheck is False and come out while 
  driver.get('https://www.wevity.com/?c=find&s=1&mode=future&gp='+str(pagenum2)+'') #wevitiy page. only str(pagenum) is change
  time.sleep(2)  # to  stabilize the internet

  while(infonum2 <=16):
    try:
      time.sleep(1) # to  stabilize the internet
      #wevitiy information. only str(infonum) is change
      driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div[2]/div[3]/div/ul/li['+str(infonum2)+']/div[1]/a').click()
      URL=(driver.current_url)
      res=requests.get(URL)
      html=res.text
      
      time.sleep(1) # to  stabilize the internet
          
      print("-----to be receipt "+str(pagenum2)+" page, "+str(infonum2-1)+" information -----")
      # (title)
      re_title = re.compile(">(.*)</h6>", re.MULTILINE)
      title_tag = re_title.findall(html)
      print("title:")
      title='\n'.join(title_tag)
      print(title)

      #(organization)
      re_com = re.compile("주관</span>\s*(.*)\s*</li>", re.MULTILINE)
      com_tag = re_com.findall(html)
      print("com:")
      com='\n'.join(com_tag)
      print(com)

      #(term)
      re_day = re.compile("기간</span>\s*(.*)\s*<span", re.MULTILINE)
      day_tag = re_day.findall(html)
      print("day:")
      day='\n'.join(day_tag)
      print(day)

      #(information)
      re_info = re.compile("viewContents\">\s*(.*)</div>", re.MULTILINE)
      info_tag = re_info.findall(html)
      print("info:")

      info='\n'.join(info_tag)
      info=info.replace("/upload","https://www.wevity.com/upload")
      print(info)
      #(image)
      img_info = re.compile("<img src=\"(/upload/contest.*)\"\s*alt=\"공", re.MULTILINE)
      img_tag = img_info.findall(html)
      print("img:")

      img='\n'.join(img_tag)
      img=img.replace("/upload","https://www.wevity.com/upload")
      print(img)


      #(homepage)
      re_page = re.compile("홈페이지</span>\s*<a href=\"(.*?)\"", re.MULTILINE)
      page_tag = re_page.findall(html)
      print("page:")
      page='\n'.join(page_tag)
      print(page)

      try: #title company day information image page bring to homepage
        curs.execute("INSERT INTO avengers_crawling(title,com,day,info,img,page) VALUES(%s,%s,%s,%s,%s,%s)",(title,com,day,info,img,page))
        conn.commit()
        
      except: # if any sources are duplicate then block duplicate data
        conn.rollback()
        print("중복된데이터")

      cnt1 = cnt1+1
      infonum2=infonum2+1

      driver.back()
            
    except NoSuchElementException:# if the crawling of the site's information are done so while statement is not work
      endcheck = False #to change infinity while -> false
      break
  pagenum2=pagenum2+1
  infonum2=2  #to reset num because we go next page
    
    
  if endcheck == False:
    print("to be receipt crawling is finish ")
    print("wevity server crawling num : "+str(cnt1))
    break


'''        
#-------------------------------------------------------------------------------------
#------------------thinkgood server receipt crawling ----------------------------------------------------
        
        
        
        
        
endcheck = True #reset endcheck

pagenum3=13
infonum3=1
while(endcheck): #infinity roof and if all information are crwaled endcheck is False and come out while 

  driver.get('https://www.thinkcontest.com/Contest/CateField.html?page='+str(pagenum3)+'&s=ing') #thinkgood page. only str(pagenum) is change
  time.sleep(2)  # to  stabilize the internet

  while(infonum3 <=10):
    try:
              
      time.sleep(1)  # to  stabilize the internet
      #thinkgood page. only str(infonum) is change
      driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/table/tbody/tr['+str(infonum3)+']/td[1]/div[1]/a').click()
      URL=(driver.current_url)
      res=requests.get(URL)
      html=res.text

      time.sleep(1)  # to  stabilize the internet
      print("-----to be receipt "+str(pagenum3)+" page, "+str(infonum3)+" information -----")

      # (title)
      re_title = re.compile("<span class=\"title\">(.*)</span>", re.MULTILINE)
      title_tag = re_title.findall(html)
      print("title:")
      title='\n'.join(title_tag)
      print(title)

      #(organization)
      re_com = re.compile("주최</th>\s*<td>(.*)</td>", re.MULTILINE)
      com_tag = re_com.findall(html)
#      print("com:")
      com='\n'.join(com_tag)
#      print(com)

      #(term)
      re_day = re.compile("기간</th>\s*<td>(.*)</td>", re.MULTILINE)
      day_tag = re_day.findall(html)
#      print("day:")
      day='\n'.join(day_tag)
#      print(day)

      #(information)
      re_info = re.compile("<div\sclass=\"info-cont\">.*(?=</section>)", re.MULTILINE|re.S)
      info_tag = re_info.findall(html)
#      print("info:")

      info='\n'.join(info_tag)
      info=info.replace("/ufiles","https://www.thinkcontest.com//ufiles")
#      print(info)

      #(image)
      img_info = re.compile("\"poster\"\s*src=\"(.*)\"\s*style", re.MULTILINE)
      img_tag = img_info.findall(html)
#      print("img:")

      img='\n'.join(img_tag)
      img=img.replace("/ufiles","https://www.thinkcontest.com/ufiles")
#      print(img)


      #(homepage)
      re_page = re.compile("홈페이지</th>\s*<td><a\shref=\"(.*)\"\sclass", re.MULTILINE)
      page_tag = re_page.findall(html)
#      print("page:")
      page='\n'.join(page_tag)
#      print(page)

      try: #title company day information image page bring to homepage
        curs.execute("INSERT INTO avengers_crawling(title,com,day,info,img,page) VALUES(%s,%s,%s,%s,%s,%s)",(title,com,day,info,img,page))
        conn.commit()

      except: # if any sources are duplicate then block duplicate data
        conn.rollback()
        print("중복된데이터")


      cnt2 = cnt2+1
      infonum3=infonum3+1
      driver.back()
            
    except NoSuchElementException:# if the crawling of the site's information are done so while statement is not work
      endcheck = False #to change infinity while -> false
      break
  pagenum3=pagenum3+1        
  infonum3=1  #to reset num because we go next page
    
    
  if endcheck == False: 
    print("to be receipt crawling is finish ")
    print("thinkgood server crawling num : "+str(cnt2))
    break
        
        
#-------------------------------------------------------------------------------------
#------------------thinkgood server to be receipt crawling ----------------------------------------------------
        
        
        
        
        
endcheck = True #reset endcheck

pagenum4=1
infonum4=1
while(endcheck):#infinity roof and if all information are crwaled endcheck is False and come out while 

  driver.get('https://www.thinkcontest.com/Contest/CateField.html?page='+str(pagenum4)+'&s=ing') #thinkgood page. only str(infonum) is change
  time.sleep(2)  # to  stabilize the internet

  while(infonum4 <=10):
    try:
              
      time.sleep(1)  # to  stabilize the internet
      #thinkgood page. only str(infonum) is change
      driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/table/tbody/tr['+str(infonum4)+']/td[1]/div[1]/a').click()
      URL=(driver.current_url)
      res=requests.get(URL)
      html=res.text

      time.sleep(1)  # to  stabilize the internet
              
      print("-----to be receipt "+str(pagenum4)+" page, "+str(infonum4)+" information -----")
      # (title)
      re_title = re.compile("<span class=\"title\">(.*)</span>", re.MULTILINE)
      title_tag = re_title.findall(html)
      print("title:")
      title='\n'.join(title_tag)
      print(title)

      #(organization)
      re_com = re.compile("주최</th>\s*<td>(.*)</td>", re.MULTILINE)
      com_tag = re_com.findall(html)
#      print("com:")
      com='\n'.join(com_tag)
#      print(com)

      #(term)
      re_day = re.compile("기간</th>\s*<td>(.*)</td>", re.MULTILINE)
      day_tag = re_day.findall(html)
 #     print("day:")
      day='\n'.join(day_tag)
#      print(day)
      #(information)
      re_info = re.compile("<div\sclass=\"info-cont\">.*(?=</section>)", re.MULTILINE|re.S)
      info_tag = re_info.findall(html)
 #     print("info:")

      info='\n'.join(info_tag)
      info=info.replace("/ufiles","https://www.thinkcontest.com//ufiles")
#      print(info)

      #(image)
      img_info = re.compile("\"poster\"\s*src=\"(.*)\"\s*style", re.MULTILINE)
      img_tag = img_info.findall(html)
#      print("img:")

      img='\n'.join(img_tag)
      img=img.replace("/ufiles","https://www.thinkcontest.com/ufiles")
 #     print(img)


      #(homepage)
      re_page = re.compile("홈페이지</th>\s*<td><a\shref=\"(.*)\"\sclass", re.MULTILINE)
      page_tag = re_page.findall(html)
 #     print("page:")
      page='\n'.join(page_tag)
#      print(page)

      try: #title company day information image page bring to homepage
        curs.execute("INSERT INTO avengers_crawling(title,com,day,info,img,page) VALUES(%s,%s,%s,%s,%s,%s)",(title,com,day,info,img,page))
        conn.commit()

      except: # if any sources are duplicate then block duplicate data
        conn.rollback()
        print("중복된데이터")



      cnt2 = cnt2+1
      infonum4=infonum4+1

      driver.back()
                  
    except NoSuchElementException:# if the crawling of the site's information are done so while statement is not work
      endcheck = False #to change infinity while -> false
      break
  pagenum4=pagenum4+1    
  infonum4=2  #to reset num because we go next page
    
        
  if endcheck == False:
    print("to be receipt crawling is finish ")
    print("thinkgood server crawling num : "+str(cnt2))
    break        
        
        
print("total crawling num : "+str(cnt1)+str(cnt2)) #
driver.close()
conn.close()
