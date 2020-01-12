#!/usr/bin/python
#cari siapa ? author ,semua boleh jadi author
import requests,os
#warna
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'
class vst:
	def __init__(self,url,jum):
		self.url = url
		self.jum = jum
	def banner():
		f='''
 ██▒   █▓ ██▓  ██████  ██▓▄▄▄█████▓ ▒█████   ██▀███  
▓██░   █▒▓██▒▒██    ▒ ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
 ▓██  █▒░▒██▒░ ▓██▄   ▒██▒▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
  ▒██ █░░░██░  ▒   ██▒░██░░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
   ▒▀█░  ░██░▒██████▒▒░██░  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
   ░ ▐░  ░▓  ▒ ▒▓▒ ▒ ░░▓    ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
   ░ ░░   ▒ ░░ ░▒  ░ ░ ▒ ░    ░      ░ ▒ ▒░   ░▒ ░ ▒░
     ░░   ▒ ░░  ░  ░   ▒ ░  ░      ░ ░ ░ ▒    ░░   ░ 
      ░   ░        ░   ░               ░ ░     ░     
     ░                                               
		'''
		return f
	def kunjungi(self):
		return requests.post('http://papaclash.com/visitor2.php',data={'url':self.url,'vst':self.jum,'oke':1}).text
def main():
	try:
		os.system('clear')
		print(k+'visitor Lite bisa digunakan pada jaringan 2g/H/edge dgn cepat')
		print(m+vst.banner())
		print(u+'-'*50)
		url=input(m+'\turl    : '+k)
		jum=int(input(m+'\tjumlah : '+k))-1
		print(u+'-'*50)
		print(m+'['+h+'*'+m+']'+k+'harap tunggu ......'+p)
		krypton=vst
		skuy=krypton(url = url, jum = jum)
		print(skuy.kunjungi())
	except ValueError:
		print('yg anda masukan tidak valid')
		main()
try:
	main()
except (KeyboardInterrupt,EOFError):
	print('sampai jumpa gan')

