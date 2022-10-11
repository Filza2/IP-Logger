try:
    import re,time,random;from colorama import Fore;from requests import get,post
    rc=Fore.LIGHTRED_EX;Rc=Fore.RED;gc=Fore.GREEN;Gc=Fore.LIGHTGREEN_EX;rsc=Fore.RESET;cya=Fore.CYAN;wh=Fore.WHITE;bc=Fore.BLUE
except Exception as e:print(f'[!] Download The Missing Module ! , {e}');exit()
def Get_INF():
    global ID,confirmation
    data=f'''-----------------------------200558575026989648353507342586
Content-Disposition: form-data; name="interval"

all
-----------------------------200558575026989648353507342586
Content-Disposition: form-data; name="page"

1
-----------------------------200558575026989648353507342586
Content-Disposition: form-data; name="sort"

created
-----------------------------200558575026989648353507342586
Content-Disposition: form-data; name="order"

desc
-----------------------------200558575026989648353507342586
Content-Disposition: form-data; name="code"

{ID}
-----------------------------200558575026989648353507342586--'''
    count_refresh=0
    while True:
        time.sleep(1)
        req=post('https://iplogger.org/logger/',headers={
            'Host': 'iplogger.org',
            'Cookie': f'confirmation={confirmation}',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'multipart/form-data; boundary=---------------------------200558575026989648353507342586',
            'Content-Length': '645',
            'Origin': 'https://iplogger.org',
            'Referer': f'https://iplogger.org/logger/{ID}/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Te': 'trailers'},data=data)
        count_refresh+=1
        con=str(req.json()['content']).split('[')[1].split(']')[0]
        try:
            if req.json()['found']==1:         	
                ip_ip=re.findall('<div class=\"ip-address\">(.*?)<\/div>',con)[0]
                ip_time=re.findall('<div class=\"ip-time\">(.*?)<\/div>',con)[0]
                ip_date=re.findall('<div class=\"ip-date\">(.*?)<\/div>',con)[0]
                ip_text=re.findall('<div class=\"ip-text\">(.*?)<\/div>',con)[0]
                country_name=re.findall('<span class=\"country-name\">(.*?)<\/span>',con)[0]
                city=re.findall('<span class=\"country-description\">(.*?)<\/span>',con)[0]
                platform=str(re.findall('<div class=\"platform\" data-icon=\"(.*?)\"><span>(.*?)<\/span><\/div>',con)[0]).split(',')[1].split(')')[0];platform=str(platform).split("'")[1]
                browser=str(re.findall('<div class=\"browser\" data-icon=\"(.*?)\"><span>(.*?)<\/span><\/div>',con)[0]).split(',')[1].split(')')[0];browser=str(browser).split("'")[1]
                referer=str(re.findall('<div class=\"visitor-referer\"><a title=\"(.*?)\">(.*?)<\/a><\/div>',con)[0]).split(',')[1].split(')')[0];referer=str(referer).split("'")[1]
                useragent=re.findall('<div class=\"visitor-useragent\"><div>(.*?)<\/div><\/div>',con)[0]
                smart_code=re.findall('<a class=\"more-info-modal\" data-accuracy=\"ip\" title=\"ip\" data-dialog=\"more-info\" data-prepare=\"more_info\" data-index=\"(.*?)\">Smart data<\/a>',con)[0]
                print("\n--------------------------------")
                print(f"\n{rc}[{wh}+{rc}] {rc}Target Found")				
                req_more=post('https://iplogger.org/logger/more/',headers={'Host': 'iplogger.org','Cookie': f'confirmation={confirmation}','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Content-Length': '32','Origin': 'https://iplogger.org','Referer': f'https://iplogger.org/logger/{ID}/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers'},data=f'index={smart_code}&code={ID}')
                latitude=req_more.json()['smart']['latitude']
                longitude=req_more.json()['smart']['longitude']
                print(f'''
{wh}[{rc}+{wh}] {rc}ip{rsc} : [{Rc}{ip_ip}{wh}]	
{wh}[{rc}+{wh}] Time : [{Rc}{ip_time}{wh}]
{wh}[{rc}+{wh}] Date : [{Rc}{ip_date}{wh}]
{wh}[{rc}+{wh}] Org : [{Rc}{ip_text}{wh}]
{wh}[{rc}+{wh}] {rc}Country{rsc} : [{Rc}{country_name}{wh}]
{wh}[{rc}+{wh}] {rc}City{rsc} : [{Rc}{city}{wh}]
{wh}[{rc}+{wh}] Platform : [{Rc}{platform}{wh}]
{wh}[{rc}+{wh}] Browser : [{Rc}{browser}{wh}]
{wh}[{rc}+{wh}] Referer : [{Rc}{referer}{wh}]			
{wh}[{rc}+{wh}] User Agent : [{Rc}{useragent}{wh}]
{wh}[{rc}+{wh}] Latitude : [{Rc}{latitude}{wh}]
{wh}[{rc}+{wh}] Longitude : [{Rc}{longitude}{wh}]
{wh}[{rc}+{wh}] {rc}Location{rsc} : [{Rc}https://www.google.com/maps?q={latitude},{longitude}{wh}]''')
                ip_saver=f'''[+] ip : [{ip_ip}]	
[+] Time : [{ip_time}]
[+] Date : [{ip_date}]
[+] Org : [{ip_text}]
[+] Country : [{country_name}]
[+] City : [{city}]
[+] Platform : [{platform}]
[+] Browser : [{browser}]
[+] Referer : [{referer}]			
[+] User Agent : [{useragent}]
[+] Latitude : [{latitude}]
[+] Longitude : [{longitude}]
[+] Location : [https://www.google.com/maps?q={latitude},{longitude}]'''
                with open('ip_logger.txt', 'a') as x:
                    x.write(ip_saver+'\n')
                print(rc+"\n--------------------------------")
                break
            elif req.json()['found']==0:print(f"\r{rc}[{wh}-{rc}] {wh}Searching For Target  {rc}<{count_refresh}>",end='')
            else:print(rc+f"\n[!] Error{wh} ",req.text);exit()
        except:print(rc+f'[!] Error >{wh}:',req.text);exit()
def Get_Status():
    global ID,confirmation
    rlink=get(f'https://iplogger.org/logger/{ID}/',headers={
        'Host': 'iplogger.org',
        'Cookie': f'confirmation={confirmation}',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://iplogger.org/',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Te': 'trailers'})
    link_target=re.findall('''    <div>
	        It's your logger link
	        <span data-copy="(.*?)" data-shortlink-place="copy">copy</span>
	    </div>''',rlink.text)[0]
    link_admin=f'https://iplogger.org/logger/{ID}/'
    domain=['2no.co','yip.su','02ip.ru','ezstat.ru','maper.info']
    d=str(f'''-----------------------------4032452102242058801219818235
Content-Disposition: form-data; name="code"

{ID}
-----------------------------4032452102242058801219818235
Content-Disposition: form-data; name="name"

shortlink
-----------------------------4032452102242058801219818235
Content-Disposition: form-data; name="domain"

{random.choice(domain)}
-----------------------------4032452102242058801219818235
Content-Disposition: form-data; name="manual"

{str(link_target).split('https://iplogger.com/')[1]}
-----------------------------4032452102242058801219818235--''')
    rupdate=post('https://iplogger.org/logger/update/',headers={
        'Host': 'iplogger.org',
        'Cookie': f'confirmation={confirmation}',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'multipart/form-data; boundary=---------------------------4032452102242058801219818235',
        'Content-Length': '536',
        'Origin': 'https://iplogger.org',
        'Referer': f'https://iplogger.org/logger/{ID}/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Te': 'trailers'},data=d)
    if 'domain' in rupdate.text:
        try:link_target=rupdate.json()['value']
        except:exit(f'{rc}[!] Failed in update Link Retry Please')
    elif 'update' in rupdate.text:
        try:link_target=rupdate.json()['value']
        except:exit(f'{rc}[!] Failed in update Link Retry Please')
    elif 'errors' in rupdate.text:exit(f'{rc}[!] Failed in Getting Links Retry Please')
    else:exit(f'{rc}[!] Failed in Getting Links Retry Please')
    try:
        print(f"{rc}[{wh}+{rc}] {gc}Admin Link{wh} : {str(link_admin)}")
        print(f"{rc}[{wh}+{rc}] {rc}Target Link{wh} : {str(link_target)}")
        print("---"*20)
    except:exit(f'{rc}[!] Failed in Getting Links Retry Please')
    try:rtest=get(f'https://iplogger.org/logger/{ID}/')
    except:exit(f'{rc}[{wh}!{rc}] Recheck Your url and Retry Please...')
    Get_INF()
def Crate_Link():
    global ID,confirmation
    confirmation='ih3JMiZ3OaTx6vwKncORs14MTvoJe59C'#confirmation code 

    url=input(f"{rc}[{wh}?{rc}] {wh}Type Url To short it : ")#https://t.me/TweakPY
    if url=='':exit(f"{rc}[{wh}!{rc}] Retry ...")
    elif url.isdigit()==True:exit(f'{rc}[{wh}!{rc}] url must be string not number !')
    check_url=post('https://iplogger.org/check/destination/',headers={'Host': 'iplogger.org','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Content-Length': '32','Origin': 'https://iplogger.org','Referer': 'https://iplogger.org/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers'},data=f'destination={url}')
    if 'host' in check_url.text:pass
    elif 'errors' in check_url.text:exit(f'{rc}[{wh}!{rc}] Recheck Your url and Retry Please...')
    else:exit(f'{rc}[{wh}!{rc}] Error')
    rc3_id=post('https://iplogger.org/create/shortlink/',headers={
        'Host': 'iplogger.org',
        'Cookie': f'confirmation={confirmation}',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'multipart/form-data; boundary=---------------------------85430372024056842421057916995',
        'Content-Length': '195',
        'Origin': 'https://iplogger.org',
        'Referer': 'https://iplogger.org/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Te': 'trailers'},data=f'''-----------------------------85430372024056842421057916995
Content-Disposition: form-data; name="destination"

{url}
-----------------------------85430372024056842421057916995--''')
    if 'error' in rc3_id.text:print(rc3_id.text);exit(f'{rc}[!] Error ..{wh} ')
    else:
        try:
            ID=str(rc3_id.json()['go']).split('/')[2]
            print(f'{rc}[{wh}+{rc}] {gc}Done{wh} Crate Tracking Link')
        except:
            print(rc+'[-] Error Try Later After a minute or check Your url')
    Get_Status()
def Header():
    print("""
██╗██████╗     ██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
██║██╔══██╗    ██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
██║██████╔╝    ██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
██║██╔═══╝     ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
██║██║         ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
╚═╝╚═╝         ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
                     By @TweakPY - @vv1ck""")
    print(f"{rc}[{wh}+{rc}] {rc}Let's Go we Have Target To Find . 🏃‍♂️")
    Crate_Link()
Header()
