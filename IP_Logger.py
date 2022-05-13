try:
    import datetime,re,time,secrets,random
    from colorama import Fore
    from requests import get,post
    rc=Fore.LIGHTRED_EX;Rc=Fore.RED;gc=Fore.GREEN;Gc=Fore.LIGHTGREEN_EX;rsc=Fore.RESET;cya=Fore.CYAN;wh=Fore.WHITE;bc=Fore.BLUE
    seth=secrets.token_hex
except Exception as FIL:exit(FIL)
def get_info_log():
    global ID,confcode
    count_refresh=0
    da='%Y-%m-%d'
    n=datetime.datetime.now()
    date=n.strftime(da)
    while True:
        time.sleep(6.5)
        req=post(f'https://iplogger.org/ajax/',headers={'Host': 'iplogger.org','Cookie': f'clhf03028ja={seth(12)}; 372349273157743448=3; 372351643157743448=3; 372370633157743448=3; 372424063157294943=3; 372424983157294943=3; auth_code=NO_AUTH; eid={seth(12)}; 194703703157294943=3; page=1; _ga=GA1.2.{seth(9)}.{seth(10)}; _gid=GA1.2.{seth(9)}.{seth(10)}; _ygid={seth(10)}; timezone=America%2FNew_York; cookies-consent=1; confcode={confcode}; 372426753157294943=3; 372428383157294943=3; 372429043157294943=3; nobots=null; 372430943157294943=3; advanced=1; 372438283157294943=3; 372438683157294943=3; limit=100; unique=null; 372439153157294943=3; 372439783157294943=3; 372740723157294943=3; PHPSESSID=; 372742363157294943=3','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Content-Length': '104','Origin': 'https://iplogger.org','Referer': f'https://iplogger.org/logger/{ID}/tab=info/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers','Connection': 'close'},data=f'a=stat&go=load&page=1&id={ID}&unique=0&nobots=1&sd={date}&ed={date}&limit=100&sort=date&ord=desc')
        count_refresh+=1
        con=req.json()['content']
        try:
            if req.json()['show']==1:
                print("\n--------------------------------")
                print(f"\n{Rc}[{wh}+{Rc}] {Rc}Target Found")
                print(con)
                with open('ip_logger.html', 'a') as x:
                    x.write(con+'\n')
                print("\n--------------------------------")
                print(f'{Rc}[{wh}+{Rc}] {gc}Go To File ip_logger.html File and open it in the web to view informaion or Simply read The File if You know How To Read it')
                break
            elif req.json()['found']==1:         	
                print("\n--------------------------------")
                print(f"\n{Rc}[{wh}+{Rc}] {Rc}Target Found")
                print(con)
                with open('ip_logger.html', 'a') as x:
                    x.write(con+'\n')
                print("\n--------------------------------")
                print('[+] Go To File ip_logger.html File and open it in the web to view informaion or Simply read The File if You know How To Read it')
                break
            elif req.json()['pages']==1:
                print("\n--------------------------------")
                print(f"\n{Rc}[{wh}+{Rc}] {Rc}Target Found")
                print(con)
                with open('ip_logger.html', 'a') as x:
                    x.write(con+'\n')
                print("\n--------------------------------")
                print(f'{Rc}[{wh}+{Rc}] {gc}Go To File ip_logger.html File and open it in the web to view informaion or Simply read The File if You know How To Read it')
                break
            elif 'Unfortunately, we have to limit the use of some aimless our services.' in req.text:
                print("--------------------")
                print(f'\n{Rc}[{wh}-{Rc}] {rc}Watch Out Ban coming.')
            elif req.json()['pages']==0:        
                print("\n--------------------")
                print(f"\n{Rc}[{wh}-{Rc}] {wh}Searching For Target  {rc}<{count_refresh}>")
            else:
                print(Rc+f"\n[!] Error{wh} ",req.text)
        except:
            print(Rc+f'[!] Error >{wh}:',req.text)

def get_stat():
    global ID
    domain=['2no.co','yip.su','02ip.ru','ezstat.ru']
    req_domain=post(f'https://iplogger.org/ajax/',headers={'Host': 'iplogger.org','Cookie': f'clhf03028ja={seth(12)}; 372349273157743448=3; 372351643157743448=3; 372370633157743448=3; 372424063157294943=3; 372424983157294943=3; auth_code=NO_AUTH; eid={seth(12)}; 194703703157294943=3; page=1; _ga=GA1.2.{seth(9)}.{seth(10)}; _gid=GA1.2.{seth(9)}.{seth(10)}; _ygid={seth(10)}; timezone=America%2FNew_York; cookies-consent=1; confcode={confcode}; 372426753157294943=3; 372428383157294943=3; 372429043157294943=3; nobots=null; 372430943157294943=3; advanced=1; 372438283157294943=3; 372438683157294943=3; limit=100; unique=null; 372439153157294943=3; 372439783157294943=3; 372740723157294943=3; PHPSESSID=; 372742363157294943=3','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Content-Length': '104','Origin': 'https://iplogger.org','Referer': f'https://iplogger.org/logger/{ID}/tab=info/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers','Connection': 'close'},data=f'a=stat&go=domain&id={ID}&domain={random.choice(domain)}')
    if 'domain' in req_domain.text:pass
    else:exit(f'{Rc}[!] Failed in Getting Links Retry Please')
    try:
        req=get(f'https://iplogger.org/logger/{str(ID)}/tab=info/')
    except:
        exit(f'{Rc}[{wh}!{Rc}] Recheck Your url and Retry Please...')
    link_admin=re.findall('''	<td>
			Link for viewing statistics
		</td>
		<td>
			<div class='copyimg stuck' data-clipboard-text='(.*?)'>copy</div>
			<input name='copylink' type='text' id='fromlogger' value='(.*?)' readonly>
		</td>''', req.text)
    link_target=re.findall('''<tr>
		<td style='width: 300px;'>
			Your IPLogger link for collecting statistics
		</td>
		<td>
			<div class='copyimg stuck changer' data-clipboard-text='(.*?)'>copy</div>
			<input name='copylink' type='text' class='changer' id='fromfirst' value='(.*?)' readonly>
		</td>
	</tr>''',req.text)
    try:
        print(f"{Rc}[{wh}+{Rc}] {gc}Admin Link{wh}:{str(link_admin).split('[(')[1].split(',')[0]}")
        print(f"{Rc}[{wh}+{Rc}] {rc}Target Link{wh}:{str(link_target).split('[(')[1].split(',')[0]}")
        print("---"*20)
    except:
        exit(f'{Rc}[!] Failed in Getting Links Retry Please')
    get_info_log()
def crate_link():
    global ID,confcode
    url=input(f"{Rc}[{wh}?{Rc}] {wh}Type Url To short it:  ")#Ex : https://t.me/TweakPY
    if url=='':exit(f"{Rc}[{wh}!{Rc}] Retry ...")
    elif url.isdigit()==True:exit(f'{Rc}[{wh}!{Rc}] url must be string not number !')
    head={'Host': 'iplogger.org','Cookie': f'clhf03028ja={seth(12)}; 372349273157743448=3; 372351643157743448=3; 372370633157743448=3; 372424063157294943=3; 372424983157294943=3; auth_code=NO_AUTH; eid={seth(12)}; 194703703157294943=3; page=null; _ga=GA1.2.{seth(9)}.{seth(10)}; _gid=GA1.2.{seth(9)}.{seth(10)}; _ygid={seth(10)}; timezone=America%2FNew_York; cookies-consent=1; confcode={confcode}; 372426753157294943=3; 372428383157294943=3; 372429043157294943=3; nobots=null; 372430943157294943=3; advanced=1; 372438283157294943=3; 372438683157294943=3; limit=100; unique=null; 372439153157294943=3; 372439783157294943=3; 372740723157294943=3; PHPSESSID=; 372742363157294943=3; _gat=1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Content-Length': '55','Origin': 'https://iplogger.org','Referer': 'https://iplogger.org/','Te': 'trailers','Connection': 'close'}
    try:
        url_one=url.split('/')[2]
        url_tow=url.split('/')[3]
    except:
        exit(f'{Rc}[{wh}!{Rc}] Please check your url ...')
    try:
        url_three=url.split('/')[4]
    except:
        go=post('https://iplogger.org/ajax/',headers=head,data=f'a=new&go=create&type=2&url=https%3A%2F%2F{url_one}%2F{url_tow}')
        if 'error' in go.text:
            exit(f'{Rc}[!] BAN{wh} {go.text}')
        else:
            try:
                ID=str(go.json()['go']).split('/')[2]
                print(f'{Rc}[{wh}+{Rc}] {gc}Done{wh} Crate Tracking Link')
            except:
                print(Rc+'[-] Error Try Later After a minute or change The confcode or check Your url')
    try:
        go=post('https://iplogger.org/ajax/',headers=head,data=f'a=new&go=create&type=2&url=https%3A%2F%2F{url_one}%2F{url_tow}%2F{url_three}')
        if 'error' in go.text:
            exit(f'{Rc}[!] BAN{wh} {go.text}')
        else:
            try:
                ID=str(go.json()['go']).split('/')[2]
                print(f'{Rc}[{wh}+{Rc}] {gc}Done{wh} Crate Tracking Link')
            except:
                print(Rc+f'[-] Error Try Later After a minute or change The confcode or check Your url')
    except:pass
    get_stat()
def main():
    global confcode
    print("""
██╗██████╗     ██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
██║██╔══██╗    ██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
██║██████╔╝    ██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
██║██╔═══╝     ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
██║██║         ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
╚═╝╚═╝         ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
                     By @TweakPY - @vv1ck""")
    print(f"{Rc}[{wh}+{Rc}] {rc}Let's Go we Have Target To Find . 🏃‍♂️")
    confcode=''#[!] if You don't Type confcode this will be Auto From The tool {recommend to change code}
    if confcode=="":confcode="hs5kyne5fykk0hk6h8z3z47y"
    crate_link()
main()
