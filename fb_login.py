import mechanize
import stalker
while(True):
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	cookies = mechanize.CookieJar()
	browser.set_cookiejar(cookies)
	browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
	browser.set_handle_refresh(False)

	url = 'http://m.facebook.com/login.php'
	browser.open(url)
	browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
	browser.form['email'] = 'USER EMAIL'
	browser.form['pass'] = 'PASSWORD'
	response = browser.submit()
	response = browser.open("https://m.facebook.com/buddylist.php?ref_component=mbasic_home_header&ref_page=%2Fwap%2Fhome.php&refid=7")

	chatSourceCode = response.read()
	
	stalker.allOnline(chatSourceCode)
	
	out=open('out.html','wb')
	out.write(chatSourceCode)
	out.close()
