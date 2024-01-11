# Coded By AmmarBN
# Ini adalah tools Open Souce Code, Jangan Lupa Subscribe
# Souce Code Ini telah dipersingkat
# Menggunakan Api Flask Yang dibuat Oleh AmmarBN
# Agar dapat digunaakan lebih mudah Oleh semua orang
# API ini juga lagi tahap pengenmbangan (akan terus di update)

#-------------------[ Library Tools Python ]------------------#
import os
import sys
import time
import requests
import bs4
import json
import re
import uuid
import datetime
import random
import string
import inquirer
from inquirer.themes import GreenPassion
from datetime import datetime
from bs4 import BeautifulSoup
from colorama import Fore, init, Back
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel


#-------------------[ Color Tools (biasa,colorama,rich color ]------------------#
H = "\033[1;92m"  # Hijau
putih = "\033[1;97m"  # Putih
Ab = "\033[1;90m"  # Abu Abu
Y = "\033[1;93m"  # Kuning
U = "\033[1;95m"  # Ungu
gktau = "33[37;1m"  # Entah
B = "\033[1;96m"  # Biru
W = "\033[1;0m"
N = '\x1b[0m'
# Tulisan Background Merah
bg = "\033[1;0m\033[1;41msubscribe\033[1;0m"
bg2 = "\033[1;0m\033[1;41m(Ammar-Executed)\033[1;0m"
BL = Fore.BLUE
WH = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
YE = Fore.YELLOW
Z2 = "[#000000]"  # HITAM
M2 = "[#FF0000]"  # MERAH
H2 = "[#00FF00]"  # HIJAU
K2 = "[#FFFF00]"  # KUNING
B2 = "[#00C8FF]"  # BIRU
U2 = "[#AF00FF]"  # UNGU
N2 = "[#FF00FF]"  # PINK
O2 = "[#00FFFF]"  # BIRU MUDA
P2 = "[#FFFFFF]"  # PUTIH
J2 = "[#FF8F00]"  # JINGGA
A2 = "[#AAAAAA]"  # ABU-ABU

#-------------------[ For Get User ID ]------------------#
console = Console()
current_user = os.getlogin()

#-------------------[ Jadwal Waktu ]------------------#
now = datetime.now()
hours = now.hour
if 4 <= hours < 12:
    timenow = ", Selamat Pagi"
elif 12 <= hours < 15:
    timenow = ", Selamat Siang"
elif 15 <= hours < 18:
    timenow = ", Selamat Sore"
else:
    timenow = ", Selamat Malam"
day = datetime.now().strftime("%d-%b-%Y")

# Path file untuk menyimpan hitungan
counter_file_path = 'counter.txt'

#------------APIKEY------------------
key = "AmmarBN"  # change apikey every 5 days
#------------APIKEY------------------

#-------------------[ Clear Terminal ]------------------#
def clear():
	os.system('clear')

#-------------------[ Get hit total ]------------------#
def get_execution_count():
    # Cek apakah file counter.txt sudah ada atau belum
    if not os.path.exists(counter_file_path):
        # Jika belum, inisialisasi hitungan ke 0
        with open(counter_file_path, 'w') as counter_file:
            counter_file.write('0')

    # Baca hitungan dari file
    with open(counter_file_path, 'r') as counter_file:
        count = int(counter_file.read())

    return count

def increment_execution_count():
    # Dapatkan hitungan saat ini
    count = get_execution_count()

    # Tambah 1 ke hitungan
    count += 1

    # Simpan kembali hitungan ke file
    with open(counter_file_path, 'w') as counter_file:
        counter_file.write(str(count))

    return count


#-------------------[ Pengulangan Back To Menu ]------------------#
def ulang():
	try:
		back = input(f"{putih}[{Y}?{putih}] Back to menu ({H}y{Y}/{H}n{putih}){R}:{H} ")
		if back == "y" or back == "Y":
			os.system("clear")
			banner()
			main()
		elif back == "n" or back == "N":
			sys.exit(f"{putih}[{R}!{putih}] Thanks For Use My Tools {Y}:D")
	except KeyboardInterrupt:
		sys.exit(f"\n{putih}[{R}!{putih}] System terminated        ")

#-------------------[ Logo/Banner Tools ]------------------#
def banner():
	print (f"""
{U}╔═╗{putih}┌┐┌┬ ┬     {U}╔═╗{putih}┌─┐┌─┐┌┬┐ {R}-⌲{putih} Creator{R}:{H} AmmarBN
{U}╚═╗{putih}│││└┬┘ {Y}─── {U}╚═╗{putih}├─┘├─┤│││ {R}-⌲{putih} Support{R}:{H} Subscriber
{U}╚═╝{putih}┘└┘ ┴      {U}╚═╝{putih}┴  ┴ ┴┴ ┴ {R}-⌲{putih} Information{R}:{putih} Open Source Code {Y}>\<
{Ab}──────────────────────────────────────────────────────────────────{putih}""")

#-------------------[ Opsi Ke 2 (Extra Tools) ]------------------#
def option2():
	#-------------------[ Openai API TOOLS ]------------------#
	os.system("clear")
	banner()
	opsi2_panel = Panel(f"{P2}7{M2}.{P2}  Tools {H2}ChatGPT	{P2}8{M2}.{P2}  Get {H2}UserAgent	{P2}9{M2}.  {P2}Get {H2}Proxy\n{P2}10{M2}.{P2} Download {H2}Instagram	{P2}11{M2}.{P2} Download {H2}Youtube	{P2}12{M2}.{P2} Download {H2}Tiktok\n{P2}13{M2}.{P2} Back Option {H2}1",width=75)
	console.print(Columns([opsi2_panel]))
	panel_input = input(f"{putih}={R}⟩{putih} Please select Tools{R}:{Y} ")
	if panel_input == "7" or panel_input == "07":
		user_history = {}
		previous_user_message = None
		os.system("clear")
		banner()
		tools_panel = Panel(f"{P2}Tools{M2}:{H2} ChatGPT")
		new_panel = Panel(f"{P2}Info{M2}:{H2} CTRL C{P2} to stop")
		console.print(Columns([new_panel, tools_panel], equal=True))
		chatting = True
		while chatting:
			try:
				gpt_input = input(f"{putih}={R}⟩{putih} Enter Text{R}:{Y} ")
				if gpt_input:
					user_history[gpt_input] = None

				gpt=requests.get(f"https://hoshiyuki-api.my.id/api/openai?text={gpt_input}&apikey={key}")
				json_result = gpt.json()
				#user_history[previous_user_message] = json_result['result']
				if "result" in json_result:
					user_history[gpt_input] = json_result['result']
					print(f"{putih}[{Y}Anda{putih}] {R}:{H} {gpt_input}")
					if user_history[gpt_input]:
						print(f"{putih}[{Y}ChatGPT{putih}] {R}:{H} {user_history[gpt_input]}")

					#print (f"{putih}[{Y}Anda{putih}] {R}:{H} {gpt_input}\n{putih}[{Y}ChatGPT{putih}] {R}:{H} "+user_history)
			except KeyboardInterrupt:
				sys.exit(f"\n{putih}[{R}!{putih}] System terminated")
	#-------------------[ Get Unlimited User Agent Tools ]------------------#
	elif panel_input == "8" or panel_input == "08":
		os.system("clear")
		banner()
		tools_panel = Panel(f"{P2}Tools{M2}:{H2} Get Unlimited User Agent")
		new_panel = Panel(f"{P2}Info{M2}:{H2} CTRL C{P2} to stop")
		console.print(Columns([new_panel, tools_panel], equal=True))
		try:
			shut_down = int(input(f"{putih}[{R}!{putih}] Ingin Dump Berapa User Agent{R}:{H} "))
			get_ua_response = requests.get(f"https://hoshiyuki-api.my.id/user-agent?jum={shut_down}&apikey={key}")
			if get_ua_response.status_code == 200:
				data = get_ua_response.json()
				user_agents = data.get('user_agents')
				if user_agents:
					print(f"{putih}[{R}!{putih}] Daftar User-Agent{R}:{H} ")
					for user_agent in user_agents:
						print(user_agent)
						ulang()
#			if ________get_ua_________.status_code == 200:
#				get_ua = data.get('user_agents')
#				if get_ua:
#					print (f"{putih}[{R}!{putih}] Daftar User-Agent{R}:{Y} ")
#					for user_agent in get_ua:
#						print(user_agent)
#						ulang()
		except KeyboardInterrupt:
			sys.exit(f"\n{putih}[{R}!{putih}] System terminated")
		except ValueError:
				sys.exit(f"\n{putih}[{R}!{putih}] Masukkan Jumlah Dengan Benar")
	#-------------------[ Get Unlimited Proxy Tools ]------------------#
	elif panel_input == "9" or panel_input == "09":
		clear()
		banner()
		tools_panel = Panel(f"{P2}Tools{M2}:{H2} Get Unlimited Proxy")
		new_panel = Panel(f"{P2}Info{M2}:{H2} CTRL C{P2} to stop")
		console.print(Columns([new_panel, tools_panel], equal=True))
		try:
			hihi = int(input(f"{putih}[{R}!{putih}] Ingin Dump Berapa Proxy{R}:{H} "))
			get_proxy_response = requests.get(f"https://hoshiyuki-api.my.id/proxy?jum={hihi}&apikey={key}")
			if get_proxy_response.status_code == 200:
				data = get_proxy_response.json()
				proxy = data.get('proxies')
				if proxy:
					print(f"{putih}[{R}!{putih}] Daftar Proxy{R}:{H} ")
					for proxies in proxy:
						print(proxies)
						ulang()
#			data = ________get_proxy_________.json()
#			if ________get_proxy_________.status_code == 200:
#				get_proxy = data.get('proxies')
#				if get_proxy:
#					print (f"{putih}[{R}!{putih}] Daftar Proxy{R}:{Y} ")
#					for proxies in get_proxy:
#						print(proxies)
#						ulang()
		except KeyboardInterrupt:
			sys.exit(f"\n{putih}[{R}!{putih}] System terminated")
		except ValueError:
			sys.exit(f"\n{putih}[{R}!{putih}] Masukkan Jumlah Dengan Benar")
	#-------------------[ Instagram Downloaders Tools ]------------------#
	elif panel_input == "10":
		clear
		banner()
		folder_path = "/storage/emulated/0/sny"
# Create the folder if it doesn't exist
		if not os.path.exists(folder_path):
			os.makedirs(folder_path)
		tools_panel = Panel(f"{P2}Tools{M2}:{H2} Download Instagram")
		new_panel = Panel(f"{P2}Info{M2}:{H2} CTRL C{P2} to stop")
		console.print(Columns([new_panel, tools_panel], equal=True))
		try:
			vid_img = input(f"{putih}[{Y}?{putih}] Video/Img{R}:{H} ")
			url_input = input(f"{putih}[{Y}?{putih}] Masukkan Url Instagram {R}:{H} ")
			url = "https://hoshiyuki-api.my.id/download/igdl?url=" + url_input + "&apikey=" + key
			response = requests.get(url)
			if response.status_code == 200:
				data = response.json()
				result = data.get('result', [])
				if result:
					for item in result:
						download_url = item.get('url')
						if download_url:
							responsee = requests.get(download_url)
							file_name = str(uuid.uuid4())
							if vid_img.lower() == 'video' or vid_img.lower() == 'Video':
								file_name += ".mp4"
							elif vid_img.lower() == 'img' or vid_img.lower() == 'Img':
								file_name += ".webp"
							file_path = os.path.join(folder_path, file_name)
							with open(file_path, "wb") as file:
								file.write(responsee.content)
								print(f"{putih}[{H}✓{putih}] Download URL{R}:{H} {download_url}")
								print(f"{putih}[{H}✓{putih}] File saved as{R}:{H} {file_path}")
								ulang()

		except KeyboardInterrupt:
			sys.exit(f"\n{putih}[{R}!{putih}] System terminated")
		except ValueError:
			sys.exit(f"\n{putih}[{R}!{putih}] Masukkan Jumlah Dengan Benar")
	#-------------------[ Youtube Downloader Mp3/Mp4 Tools ]------------------#
	elif panel_input == "11":
		clear()
		banner()
		tools_panel = Panel(f"{P2}Tools{M2}:{H2} Download Youtube mp3/mp4")
		new_panel = Panel(f"{P2}Info{M2}:{H2} CTRL C{P2} to stop")
		console.print(Columns([new_panel, tools_panel], equal=True))
		url = input(f"{putih}[{Y}?{putih}] Masukkan Url{R}:{H}  ")
		download_path = "/storage/emulated/0/sny/youtube"
		if not os.path.exists(download_path):
			os.makedirs(download_path)
		def download_ytdl_data(url, download_path):
			api_url = requests.get(f"https://hoshiyuki-api.my.id/download/ytdl?url={url}&apikey={key}")
			#response = requests.get(api_url)
			if api_url.status_code == 200:
				response_json = api_url.json()
				size_url = response_json["Data"][0]["title"]
				audio_url = response_json["Data"][0]["mp3"]
				video_url = response_json["Data"][0]["link"]
				user_input = input(f"{putih}[{R}?{putih}] Convert {H}Video{U}/{H}Audio{Y}?{putih} ({H}video{U}/{H}audio{putih}){R}:{H} ").lower()
				if user_input == "video":
				# Mendownload video tanpa watermark dan menyimpan sebagai .mp4
					video_response = requests.get(video_url)
					video_path = os.path.join(download_path, "ytdl_vid.mp4")
					with open(video_path, "wb") as video_file:
						video_file.write(video_response.content)
						print(f"{putih}[{R}•{putih}] Title{R}:{H} {size_url}")
						print(f"{putih}[{H}✓{putih}] Video youtube berhasil diunduh dan disimpan di {H}", video_path)
				elif user_input == "audio":
				# Mendownload audio dan menyimpan sebagai .mp3
					audio_response = requests.get(audio_url)
					audio_path = os.path.join(download_path, "ytdl_audio.mp3")
					with open(audio_path, "wb") as audio_file:
						audio_file.write(audio_response.content)
						print(f"{putih}[{R}•{putih}] Title{R}:{H} {size_url}")
						print(f"{putih}[{H}✓{putih}] Audio berhasil diunduh dan disimpan di {H}", audio_path)
						ulang()
				else:
					print(f"{putih}[{R}!{putih}] Pilihan tidak valid. Silakan pilih {U}'{Y}video{U}'{putih} atau {U}'{Y}audio{U}'{putih}.")
			else:
				print(f"{putih}[{R}!{putih}] Gagal mendapatkan data TikTok. Kode status{R}: {Y}", response.status_code)
				ulang()
		download_ytdl_data(url, download_path)
	#-------------------[ Downloader Tiktok No Watermark ]------------------#
	elif panel_input == "12":
		clear()
		banner()
		tools_panel = Panel(f"{P2}Tools{M2}:{H2} Download Tiktok No Wm/Audio")
		new_panel = Panel(f"{P2}Info{M2}:{H2} CTRL C{P2} to stop")
		console.print(Columns([new_panel, tools_panel], equal=True))
		url = input(f"{putih}[{Y}?{putih}] Masukkan Url{R}:{H}  ")
		download_path = "/storage/emulated/0/sny/tiktok"
		if not os.path.exists(download_path):
			os.makedirs(download_path)
		def download_tiktok_data(url, download_path):
			api_url = requests.get(f"https://hoshiyuki-api.my.id/download/tiktok?url={url}&apikey={key}")
			#response = requests.get(api_url)
			if api_url.status_code == 200:
				response_json = api_url.json()
				audio_url = response_json["data"]["url"]["audio"]
				video_url = response_json["data"]["url"]["nowm"]
				user_input = input(f"{putih}[{R}?{putih}] Convert {H}Video{U}/{H}Audio{Y}?{putih} ({H}video{U}/{H}audio{putih}){R}:{H} ").lower()
				if user_input == "video":
				# Mendownload video tanpa watermark dan menyimpan sebagai .mp4
					video_response = requests.get(video_url)
					video_path = os.path.join(download_path, "tiktok_video.mp4")
					with open(video_path, "wb") as video_file:
						video_file.write(video_response.content)
						print(f"{putih}[{H}✓{putih}] Video tanpa watermark berhasil diunduh dan disimpan di {H}", video_path)
				elif user_input == "audio":
				# Mendownload audio dan menyimpan sebagai .mp3
					audio_response = requests.get(audio_url)
					audio_path = os.path.join(download_path, "tiktok_audio.mp3")
					with open(audio_path, "wb") as audio_file:
						audio_file.write(audio_response.content)
						print(f"{putih}[{H}✓{putih}] Audio berhasil diunduh dan disimpan di {H}", audio_path)
						ulang()
				else:
					print(f"{putih}[{R}!{putih}] Pilihan tidak valid. Silakan pilih {U}'{Y}video{U}'{putih} atau {U}'{Y}audio{U}'{putih}.")
			else:
				print(f"{putih}[{R}!{putih}] Gagal mendapatkan data TikTok. Kode status{R}: {Y}", response.status_code)
				ulang()
		download_tiktok_data(url, download_path)
	elif panel_input == "13":
		main()
	else:
		sys.exit(f"{putih}[{R}!{putih}] Invalid Input Option")

#-------------------[ Opsi Utama Tools ]------------------#
def option1():
	opsi1_panel = Panel(f"{P2}1{M2}.{P2} Spam {H2}Sms{M2},{H2}Call{M2},{H2}WhatsApp     {P2}2{M2}.{P2} Spam {H2}Call	{P2}3{M2}.{P2} Spam {H2}Gmail\n{P2}4{M2}.{P2} Information		      {P2}5{M2}.{P2} Check{H2} Apikey	{P2}6{M2}.{H2} Extra Tools", width=75)
	console.print(Columns([opsi1_panel]))
	panel_input = input(f"{putih}={R}⟩{putih} Please select Tools{R}:{Y} ")
	#-------------------[ Spam Sms,Call,WhatsApp (opsi 1) ]------------------#
	if panel_input == "1" or panel_input == "01":
		try:
			#-------------------[ Get Random UserAgent ]------------------#
			api_url = "https://rest-api-flask-eosin.vercel.app/user-agent"
			api_params = {"jum": 1, "apikey": "Hoshiyuki"}
			api_response = requests.get(api_url, params=api_params)
			if api_response.status_code == 200:
				user_agents = api_response.json().get("user_agents", [])
				user_agent = user_agents[0] if user_agents else "Isi Default User-Agent (bebas)"
				os.system("clear")
				banner()
				tools_SNY_panel = Panel(f"{P2}Tools{M2}:{H2} Spam SNY")
				new_panel = Panel(f"{P2}Info{M2}:{H2} CTRL C{P2} to stop")
				console.print(Columns([new_panel, tools_SNY_panel], equal=True))
				nomor = int(input(f"{putih}[{Y}?{putih}] Input Number ({Y}8xxx{putih}){R}:{H} "))
				email = input(f"{putih}[{Y}?{putih}] Input Email ({Y}optional{putih}){R}:{H} ")
				api_sny = requests.get(f"https://hoshiyuki-api.my.id/api/spam-otten?nomor={nomor}&apikey={key}").text
				api_sny2 = requests.get(f"https://hoshiyuki-api.my.id/api/spam-sny?nomor={nomor}&email={email}&apikey={key}").text
				headdooit = {    "Host": "www.dooitwell.id",    "Content-Length": "36",    "Sec-Ch-UA": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',    "Accept": "application/json, text/plain, */*",    "Content-Type": "application/json;charset=UTF-8",    "Sec-Ch-UA-Mobile": "?1",    "User-Agent":user_agent,    "Sec-Ch-UA-Platform": '"Android"',    "Origin": "https://www.dooitwell.id",    "Sec-Fetch-Site": "same-origin",    "Sec-Fetch-Mode": "cors",    "Sec-Fetch-Dest": "empty",    "Referer": "https://www.dooitwell.id/register",    "Accept-Encoding": "gzip, deflate, br",    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}
				payloaddooit = {"code": "+62", "phone": nomor}
				responsedooit = requests.post("https://www.dooitwell.id/site/generateotp", headers=headdooit, json=payloaddooit).text
				api__call = requests.get(f"https://hoshiyuki-api.my.id/api/spam-call?nomor={nomor}&apikey={key}")
				if "failed" in api_sny:
					print(f"{putih}[{R}!{putih}] Failed Sending Spam pls wait {H}1{putih} minutes")
					ulang()
#					print (f"{putih}[{H}✓{putih}] Successfully Sending Spam{H} "+nomor+"{Y} &{H} "+email)
				else:
					print (f"{putih}[{H}✓{putih}] Successfully Sending Spam{H} {nomor}{Y} &{H} {email}")
					ulang()
#					sys.exit(f"{putih}[{R}!{putih}] Failed Sending Spam pls wait {H}1{putih} minutes")

		except KeyboardInterrupt:
			sys.exit(f"\n{putih}[{R}!{putih}] System terminated                   ")
		except ValueError:
			sys.exit(f"\n{putih}[{R}!{putih}] Masukkan Nomor dengan benar")
	#-------------------[ Spam Call Tools ]------------------#
	if panel_input == "2" or panel_input == "02":
		try:
			os.system("clear")
			banner()
			tools_call_panel = Panel(f"{P2}Tools{M2}:{H2} Spam Call Target")
			new_panel = Panel(f"{P2}Info{M2}:{H2} CTRL C{P2} to stop")
			console.print(Columns([new_panel, tools_call_panel], equal=True))
			nomor = int(input(f"{putih}[{Y}?{putih}] Input Number ({Y}8xxx{putih}){R}:{H} "))
			api_call = requests.get(f"https://hoshiyuki-api.my.id/api/spam-call?nomor={nomor}&apikey={key}")
			response = api_call.text
			if "success" in response:
				# print (response)
				print (f"{putih}[{H}✓{putih}] Berhasil Kirim Call ke {Y}{nomor}")
				ulang
			else:
				# print (response)
				print (f"{putih}[{R}!{putih}] Gagal Kirim Call Ke {Y}{nomor}")
				ulang()
		except KeyboardInterrupt:
			sys.exit(f"\n{putih}[{R}!{putih}] System terminated               ")
		except ValueError:
			sys.exit(f"\n{putih}[{R}!{putih}] Masukkan Nomor dengan benar")
	#-------------------[ Spam Gmail API ]------------------#
	elif panel_input == "3" or panel_input == "03":
		try:
			os.system("clear")
			banner()
			tools_email_panel = Panel(f"{P2}Tools{M2}:{H2} Spam Email Target")
			new_panel = Panel(f"{P2}Info{M2}:{H2} CTRL C{P2} to stop")
			console.print(Columns([new_panel, tools_email_panel], equal=True))
			email = input(f"{putih}[{Y}?{putih}] Input Email ({Y}blablabla@gmail.com{putih}){R}:{H} ")
			api_email = requests.get(f"https://hoshiyuki-api.my.id/api/spam-gmail?email={email}&apikey={key}")
			response = api_email.text
			if "success" in response:
				print (f"{putih}[{H}✓{putih}] Berhasil Kirim Email ke {Y}{email}")
				ulang()
			else:
				print (f"{putih}[{R}!{putih}] Gagal Kirim Email Ke {Y}{email}")
				ulang()
		except KeyboardInterrupt:
			sys.exit(f"\n{putih}[{R}!{putih}] System terminated")
	elif panel_input == "4" or panel_input == "04":
		print (f"{putih}[{R}!{putih}] Notice{R}:{Y} Disclaimer, Halo Pengguna Ini adalah Tools Open Source Yang dikenbangkan menggunakan API, tools Ini dikembangkan oleh AmmarBN dan aktivasi menggunakan APIKEY, apikey Di Tools ini akan expired setiap 5 hari, jadi setiap 5 Hari Kalian harus mendownload ulang APIKEY di link yang sudah disediakan.\nIngat, Source Code ini dibuat untuk dipelajari Bukan di recode!!!, jika mau recode -> repost Silakan ijin ke admin dahulu, jika melanggar Admin Akan menonaktifkan apikey, bagaimana admin bisa tau? admin dapat mengecek logs requests API dari terminal\n{putih}[{H}•{putih}] Kalian Juga dapat memberibatau mengajukan minimal 3 api spam dan dapatkan premium apikey yang aktif seumur hidup, sekian. Selamat Mencoba\n{putih}[{Y}•{putih}] Contact{R}:{H} https://t.me/SariiRooti\n{putih}[{Y}•{putih}] Email Support{R}:{H} ammarexecuted@gmail.com")
		ulang()

	#-------------------[ Check Expired Apikey ]------------------#
	elif panel_input == "5" or panel_input == "05":
		print (f"{putih}[{R}!{putih}] Trial Apikey{R}:{H} {key}")
		key_put = input(f"{putih}[{R}!{putih}] Masukkan Apikey Yang mau di cek{R}:{H} ")
		check_api = requests.get(f"https://hoshiyuki-api.my.id/check?apikey={key_put}").text
		print (f"{check_api}")
		ulang()

	#-------------------[ Slide to option 2 ]------------------#
	elif panel_input == "6" or panel_input == "06":
		option2()
	else:
		sys.exit(f"{putih}[{R}!{putih}] Invalid Input Option")

# Di dalam fungsi main atau tempat utama eksekusi skrip
def main():
    # Tambahkan logika untuk menampilkan jumlah eksekusi
	clear()
	banner()
	execution_count = increment_execution_count()
	user_panel = Panel(f"{P2}Total Hit{M2}:{H2} {execution_count}")
	id_panel = Panel(f"{P2}Your Id{M2}:{H2} {current_user}")
	date_panel = Panel(f"{P2}Date{M2}:{H2} {day}")
	new_panel = Panel(f"{K2}Spesial New Year Spam {H2}Sms{M2},{H2}WhatsApp{M2},{H2}Call{P2} Open Source Code")
	console.print(Columns([user_panel, id_panel, date_panel], equal=True))
	console.print(Columns([new_panel], equal=True))
	option1()
    # ... (kode utama skrip)

if __name__ == "__main__":
    main()
