import socket # socket digunakan untuk menghubungkan komuniksai antar server dan klien
import requests # Requests adalah library dengan banyak fitur,melempar parameter dalam URL, mengirim header khusus dan verifikasi SSL
import pprint #untuk memformat struktur data yang mudah di baca interpreter dan manusia
import json # json digunakan untuk mentransfer data


hostname = input('Masukkan nama domain : ')
ip_adress = socket.gethostbyname(hostname) 

request_url = 'https://geolocation-db.com/jsonp/' + ip_adress
response = requests.get(request_url)
geolocation = response.content.decode()  #decode untuk melihat hasil textnya jelas
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)

for k,v in geolocation.items():
    pprint.pprint(str(k) + ':' + str(v))

print(f'Domain name : {hostname}')
print(f'IP Adress : {ip_adress}')
