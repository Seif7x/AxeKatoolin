#!/usr/bin/env python -tt
from core.categories import *
import sys, os

# colors
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[33m"
cyan = "\033[1;36m"
reset = "\033[0m"

# option menu
menu_list = {
	"1":"show_categories",
	"2":"update",
	"3":"help",
	"4":"exit",
	"show":"show_categories",
	"clear":"clean_screen",
	"update":"update",
	"help":"help",
	"exit":"exit",
}

menu_list_set = {
	"load":"load_category",
	"search":"search_tool"
}

def load(fuction, param=False):
	"""
	If the function exists, it is loaded
	"""
	if param == False:
		globals()[fuction]()
	else:
		globals()[fuction](param)

def show_categories():
	"""
	Displays the categories available in the 'categories' dictionary of the core/categories.py file
	"""
	print("\n%s:: Categories:%s\n" %(green, reset))
	for name in list(categories.items()):
		category = name[1][0]
		category = format(category)
		if name[0]%2 != 0:
			print(" "+str(name[0]).rjust(2) + ")", category.ljust(23)[:23], end=' ')
		else:
			print(" "+str(name[0]).rjust(2) + ")", category)
	print(" ")

def load_category(key):
	"""
	When loading a category you can install one or more tools of that category
	"""
	if int(key) in list(categories.keys()):
		os.system('clear')
		category = categories[int(key)][0]
		category = format(category)
		print(green + ":: " + category + reset + "\n")
		show_tools(categories[int(key)][1])
		tools = categories[int(key)][1]
		site = categories[int(key)][0]
		action = False
		while action == False:
			try:
				option = eval(input(": Axekatoolin (%s%s%s) > " %(yellow, site, reset)))
			except KeyboardInterrupt:
				delete_repository()
				print("..."); break
			try:
				if option == 'back':
					delete_repository()
					break
				elif option == 'clear':
					os.system('clear')
				elif option == 'show':
					show_tools(categories[int(key)][1])
				elif option == 'help':
					help(True)
				elif option == '99':
					add_repository()
					for tool in tools:
						install_tool = "apt install -y " + tool
						os.system(install_tool)
				elif int(option) in range(1,len(tools)+1):
					add_repository()
					install_tool = "apt install -y " + tools[int(option)-1]
					os.system(install_tool)
			except:
				pass
	else:
		print(red + "E: The command is invalid!" + reset)

def search_tool(tool):
	"""
	Shows in which category the tool you are looking for is available
	"""
	print(": Find " + yellow + tool + reset)
	print(": Available in:")
	for lists in list(categories.items()):
		tools = lists[1][1]
		category = lists[1][0]
		category = format(category)
		if tool in tools:
			print(" [%s+%s] %s" %(green, reset, category))

def show_tools(tools):
	"""
	Show all tools in the loaded category
	"""
	for tool in enumerate(tools):
		if tool[0]%2 == 0:
			print(" "+str(tool[0]+1).rjust(2) + ")", tool[1].ljust(23)[:23], end=' ')
		else:
			print(" "+str(tool[0]+1).rjust(2) + ")", tool[1])
	print("\n 99) ALL")

def add_repository():
	"""
	The Kali Linux repository is added in '/etc/apt/sources.list.d /'
	"""
	if os.path.exists("/etc/apt/sources.list.d/Axekatoolin.list"):
		add_key()
	else:
		try:
			f = open("/etc/apt/sources.list.d/Axekatoolin.list", "wb")
			f.write("#Axekatoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free\n# For source package access, uncomment the following line\n# deb-src http://http.kali.org/kali kali-rolling main contrib non-free\n")
			f.close()
			print(green + "\n[+] Add repository\n" + reset)
			add_key()
		except IOError:
			print(red+"E: Please run as root"+reset)
			sys.exit()

def delete_repository():
	"""
	The Kali Linux repository is removed from '/etc/apt/sources.list.d/'
	"""
	repository = "/etc/apt/sources.list.d/Axekatoolin.list"
	if os.path.exists(repository):
		os.remove(repository)
		print(green + "\n[+] Repository deleted\n" + reset)

def add_key():
	"""
	Repository keyserver is added
	"""
	tmp_key = "/tmp/key_Axekatoolin.txt"
	if os.path.exists(tmp_key):
		pass
	else:
		os.system("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6")
		f = open(tmp_key, "wb")
		f.write("Axekatoolin\n")
		f.close()
		print(green + "\n[+] Add keyserver\n" + reset)
		os.system('apt-get update -o Dir::Etc::sourcelist="sources.list.d/Axekatoolin.list" -o Dir::Etc::sourceparts="-" -o apt::Get::List-Cleanup="0"')
		print(green + "\n[+] Update\n" + reset)

def banner():
	version = "v1.3b"
	tools = num_tools()
	options = """
 1) View Categories
 2) Update Axekatoolin
 3) Help

 4) Exit
	"""
	print((""" \033	
 \033[1;36m $$\   $$\             $$\                         $$\ $$\           
  \033[1;36m$$ | $$  |            $$ |                        $$ |\__|          
  \033[1;36m$$ |$$  /  $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\  
  \033[1;36m$$$$$  /   \____$$\ \_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\ 	
  
  \033[1;36m$$  $$<    $$$$$$$ |  
 	
\033[1;35m                 _              _         _                     
\033[1;35m                / \   __  _____| |/ /__ _| |_ ___   ___ |   (_)_ __  
\033[1;35m               / _ \  \ \/ / _ \ ' // _` | __/ _ \ / _ \|   | | '_ \ 
\033[1;35m              / ___ \  >  <  __/ . \ (_| | || (_) | (_) |   | | | | |
\033[1;35m             /_/   \_\/_/\_\___|_|\_\__,_|\__\___/ \___/|___|_|_| |_|

 
 \033[1;36mKali linux tools installer\033[1;m 
 
 
 \033[1;36m$$ |\$$\  $$  __$$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
 $$ | \$$\ \$$$$$$$ |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |
 \__|  \__| \_______|   \____/  \______/  \______/ \__|\__|\__|  \__| 
 
 
 
 V3.1 by AxeDx7
  \033[1;m

 \033[1;32m+ -- -- +=[ Updated by  AxeDx7 | Homepage: www.https://github.com/Seif7x\033[1;m
 \033[1;32m+ -- -- +=[ Original  Author: LionSec | Homepage: www.neodrix.com\033[1;m
 \033[1;32m+ -- -- +=[ 331 Tools \033[1;m""") %(cyan,reset,cyan,version,reset,green,tools,reset))
print(options)

def update():
	"""
	Update 'Axekatoolin' with: git pull
	"""
	try:
		os.system('git pull')
		print(yellow + "W: Please restart Axekatoolin" + reset)
	except:
		print(red + "E: can't start update please use <git pull>"+reset)

def help(x=False):
	"""
	Displays tool help
	"""
	if x != True:
		print(""": load=<category>   Load category
: search=<tool>     Find tool
: clear             Clean screen  
: 1, show           Show categories
: 2, update         Update Axekatoolin (git pull)
: 3, help           Show help
: 4, exit           Exit Axekatoolin""")
	else:
		print(""": <option>  Install tool
: 99        Install all tools in the category
: back      Return to previous menu
: clear     Clean screen
: show      Show tools
: help      Show help""")

def clean_screen():
	os.system('clear')
	banner()

def exit():
	print("\nClosing, bye! - Axekatoolin")
	sys.exit()

def num_tools():
	"""
	Obtains the number of tools available
	"""
	num = 0
	for name in list(categories.items()):
		tools = name[1][1]
		num+= len(tools)
	return num

def format(category):
	category = category.replace('_', ' ')
	category = category.title()
	return category
