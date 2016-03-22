from lxml import html
import os

def allOnline(source):
	oldList=[]
	main_tree = html.fromstring(source)
	olFriends=main_tree.xpath('//a[@class="bt"]/text()')
	try:
		ListFile=open('list.frnd','r')
		oldList=ListFile.read().split('\n')
		#print oldList
		ListFile.close()
	except:
		pass
	ListFile=open('list.frnd','w')
	for friend in olFriends:
		if "Dushyant" in friend:
			if friend not in oldList:
				os.system('aplay dushyant.wav >/dev/null 2>&1')
		ListFile.write(friend)
		ListFile.write('\n')
	ListFile.close()
		#print friend


