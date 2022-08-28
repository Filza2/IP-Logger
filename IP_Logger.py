try:
    import re,time,secrets,random
    from colorama import Fore
    from requests import get,post
    rc=Fore.LIGHTRED_EX;Rc=Fore.RED;gc=Fore.GREEN;Gc=Fore.LIGHTGREEN_EX;rsc=Fore.RESET;cya=Fore.CYAN;wh=Fore.WHITE;bc=Fore.BLUE
    seth=secrets.token_hex
except ModuleNotFoundError:exit('[!] Missing Module !')
def get_info_log():
	global ID,confirmation,confirmed
	count_refresh=0
	data=f'''-----------------------------35055216101048598748523257939
Content-Disposition: form-data; name="interval"

all
-----------------------------35055216101048598748523257939
Content-Disposition: form-data; name="page"

1
-----------------------------35055216101048598748523257939
Content-Disposition: form-data; name="sort"

created
-----------------------------35055216101048598748523257939
Content-Disposition: form-data; name="order"

desc
-----------------------------35055216101048598748523257939
Content-Disposition: form-data; name="code"

{ID}
-----------------------------35055216101048598748523257939--
'''
	while True:
		time.sleep(1)
		req=post('https://iplogger.org/logger/',headers={'Host': 'iplogger.org','Cookie': f'cursor={seth(12)}; clhf03028ja={seth(12)}; 375263813157358497=2; integrity={seth(12)}; _ga=GA1.2.{seth(9)}.{seth(10)}; _gid=GA1.2.{seth(9)}.{seth(10)}; cookies-consent={confirmed}; confirmation={confirmation}; 399813053157358497=3; 399795493157358497=3','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','X-Requested-With': 'XMLHttpRequest','Content-Type': 'multipart/form-data; boundary=---------------------------35055216101048598748523257939','Content-Length': '639','Origin': 'https://iplogger.org','Referer': f'https://iplogger.org/logger/{ID}/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers'},data=data)
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
				print(f"\n{Rc}[{wh}+{Rc}] {Rc}Target Found")				
				req_more=post('https://iplogger.org/logger/more/',headers={'Host': 'iplogger.org','Cookie': f'cursor={seth(12)}; clhf03028ja={seth(12)}; 375263813157358497=2; integrity={seth(12)}; _ga=GA1.2.{seth(9)}.{seth(10)}; _gid=GA1.2.{seth(9)}.{seth(10)}; cookies-consent={confirmed}; confirmation={confirmation}; 399813053157358497=3; 399795493157358497=3; 399822453157358497=3; 399830823157358497=3; _gat=1','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Content-Length': '32','Origin': 'https://iplogger.org','Referer': f'https://iplogger.org/logger/{ID}/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers'},data=f'index={smart_code}&code={ID}')
				latitude=req_more.json()['smart']['latitude']
				longitude=req_more.json()['smart']['longitude']
				print(f'''
{wh}[{Rc}+{wh}] {rc}ip{rsc} : [{Rc}{ip_ip}{wh}]	
{wh}[{Rc}+{wh}] Time : [{Rc}{ip_time}{wh}]
{wh}[{Rc}+{wh}] Date : [{Rc}{ip_date}{wh}]
{wh}[{Rc}+{wh}] Org : [{Rc}{ip_text}{wh}]
{wh}[{Rc}+{wh}] {rc}Country{rsc} : [{Rc}{country_name}{wh}]
{wh}[{Rc}+{wh}] {rc}City{rsc} : [{Rc}{city}{wh}]
{wh}[{Rc}+{wh}] Platform : [{Rc}{platform}{wh}]
{wh}[{Rc}+{wh}] Browser : [{Rc}{browser}{wh}]
{wh}[{Rc}+{wh}] Referer : [{Rc}{referer}{wh}]			
{wh}[{Rc}+{wh}] User Agent : [{Rc}{useragent}{wh}]
{wh}[{Rc}+{wh}] Latitude : [{Rc}{latitude}{wh}]
{wh}[{Rc}+{wh}] Longitude : [{Rc}{longitude}{wh}]
{wh}[{Rc}+{wh}] {rc}Location{rsc} : [{Rc}https://www.google.com/maps?q={latitude},{longitude}{wh}]''')
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
				print(Rc+"\n--------------------------------")
				break
			elif req.json()['found']==0:print(f"\r{Rc}[{wh}-{Rc}] {wh}Searching For Target  {rc}<{count_refresh}>",end='')
			else:print(Rc+f"\n[!] Error{wh} ",req.text);exit()
		except:print(Rc+f'[!] Error >{wh}:',req.text);exit()
def get_stat():
	global ID,confirmation,confirmed
	cu1=get(f'https://iplogger.org/logger/{ID}/',headers={'Host': 'iplogger.org','Cookie': f'cursor={seth(12)}; clhf03028ja={seth(12)}; 375263813157358497=2; integrity={seth(12)}; _ga=GA1.2.{seth(9)}.{seth(10)}; _gid=GA1.2.{seth(9)}.{seth(10)} cookies-consent={confirmed}; confirmation={confirmation}','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://iplogger.org/','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Te': 'trailers'})
	link_target=re.findall('''    <div>
	        It's your logger link
	        <span data-copy="(.*?)" data-shortlink-place="copy">copy</span>
	    </div>''',cu1.text)[0]
	link_admin=f'https://iplogger.org/logger/{ID}/'
	domain=['2no.co','yip.su','02ip.ru','ezstat.ru','maper.info']
	dcu1=f'''-----------------------------42567996029474889951243244680
Content-Disposition: form-data; name="code"

{ID}
-----------------------------42567996029474889951243244680
Content-Disposition: form-data; name="name"

shortlink
-----------------------------42567996029474889951243244680
Content-Disposition: form-data; name="domain"

{random.choice(domain)}
-----------------------------42567996029474889951243244680
Content-Disposition: form-data; name="manual"

{str(link_target).split('https://iplogger.org/')[1]}
-----------------------------42567996029474889951243244680--
'''
	r_domain=post('https://iplogger.org/logger/update/',headers={'Host': 'iplogger.org','Cookie': f'cursor={seth(12)}; clhf03028ja={seth(12)}; 375263813157358497=2; integrity={seth(12)}; _ga=GA1.2.{seth(9)}.{seth(10)}; _gid=GA1.2.{seth(9)}.{seth(10)}; cookies-consent={confirmed}; confirmation={confirmation}; 399813053157358497=3; 399795493157358497=3','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','X-Requested-With': 'XMLHttpRequest','Content-Type': 'multipart/form-data; boundary=---------------------------42567996029474889951243244680','Content-Length': '576','Origin': 'https://iplogger.org','Referer': f'https://iplogger.org/logger/{ID}','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers'},data=dcu1)
	if 'domain' in r_domain.text:pass
	elif 'update' in r_domain.text:pass
	elif 'errors' in r_domain.text:exit(f'{Rc}[!] Failed in Getting Links Retry Please')
	else:exit(f'{Rc}[!] Failed in Getting Links Retry Please')
	cu2=get(f'https://iplogger.org/logger/{ID}/',headers={'Host': 'iplogger.org','Cookie': f'cursor={seth(12)}; clhf03028ja={seth(12)}; 375263813157358497=2; integrity={seth(12)}; _ga=GA1.2.{seth(9)}.{seth(10)}; _gid=GA1.2.{seth(9)}.{seth(10)} cookies-consent={confirmed}; confirmation={confirmation}','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://iplogger.org/','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Te': 'trailers'})
	link_target=re.findall('''    <div>
	        It's your logger link
	        <span data-copy="(.*?)" data-shortlink-place="copy">copy</span>
	    </div>''',cu2.text)[0]
	try:
		print(f"{Rc}[{wh}+{Rc}] {gc}Admin Link{wh}:{str(link_admin)}")
		print(f"{Rc}[{wh}+{Rc}] {rc}Target Link{wh}:{str(link_target)}")
		print("---"*20)
	except:exit(f'{Rc}[!] Failed in Getting Links Retry Please')
	try:rtest=get(f'https://iplogger.org/logger/{ID}/')
	except:exit(f'{Rc}[{wh}!{Rc}] Recheck Your url and Retry Please...')
	get_info_log()
def crate_link():
	global ID,confirmation,confirmed
	url=input(f"{Rc}[{wh}?{Rc}] {wh}Type Url To short it:  ")#https://t.me/TweakPY
	if url=='':exit(f"{Rc}[{wh}!{Rc}] Retry ...")
	elif url.isdigit()==True:exit(f'{Rc}[{wh}!{Rc}] url must be string not number !')
	check_url=post('https://iplogger.org/check/destination/',headers={'Host': 'iplogger.org','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Content-Length': '32','Origin': 'https://iplogger.org','Referer': 'https://iplogger.org/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers'},data=f'destination={url}')
	if 'host' in check_url.text:pass
	elif 'errors' in check_url.text:exit(f'{Rc}[{wh}!{Rc}] Recheck Your url and Retry Please...')
	else:exit(f'{Rc}[{wh}!{Rc}] Error')
	dc1='''-----------------------------360206707140116872261249431275
Content-Disposition: form-data; name="destination"

'''+url+'''
-----------------------------360206707140116872261249431275--
'''
	rc1=post('https://iplogger.org/create/shortlink/',headers={'Host': 'iplogger.org','Cookie': f'cursor={seth(12)}; clhf03028ja={seth(12)}; 375263813157358497=2; integrity={seth(12)}; _ga=GA1.2.{seth(9)}.{seth(10)}; _gid=GA1.2.{seth(9)}.{seth(10)}; _gat=1; cookies-consent=1661695701','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','X-Requested-With': 'XMLHttpRequest','Content-Type': 'multipart/form-data; boundary=---------------------------360206707140116872261249431275','Content-Length': '238','Origin': 'https://iplogger.org','Referer': 'https://iplogger.org/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers'},data=dc1)
	dc2='''-----------------------------335747790239813231522432462056
Content-Disposition: form-data; name="rules"

on
-----------------------------335747790239813231522432462056--
'''
	rc2=post('https://iplogger.org/create/confirmation/',headers={'Host': 'iplogger.org','Cookie': f'cursor={seth(12)}; clhf03028ja={seth(12)}; 375263813157358497=2; integrity={seth(12)}; _ga=GA1.2.{seth(9)}.{seth(10)}; _gid=GA1.2.{seth(9)}.{seth(10)}; _gat=1; cookies-consent=1661695701','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','X-Requested-With': 'XMLHttpRequest','Content-Type': 'multipart/form-data; boundary=---------------------------335747790239813231522432462056','Content-Length': '176','Origin': 'https://iplogger.org','Referer': 'https://iplogger.org/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers'},data=dc2)
	confirmation=rc2.json()['confirm']['code']
	confirmed=rc2.json()['confirm']['confirmed']
	dc3='''-----------------------------72491027839422916342211687263
Content-Disposition: form-data; name="destination"

'''+url+'''
-----------------------------72491027839422916342211687263--
'''
	rc3_id=post('https://iplogger.org/create/shortlink/',headers={'Host': 'iplogger.org','Cookie': f'cursor={seth(12)}; clhf03028ja={seth(12)}; 375263813157358497=2; integrity={seth(12)}; _ga=GA1.2.{seth(9)}.{seth(10)}; _gid=GA1.2.{seth(9)}.{seth(10)} cookies-consent={confirmed}; confirmation={confirmation}','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','X-Requested-With': 'XMLHttpRequest','Content-Type': 'multipart/form-data; boundary=---------------------------72491027839422916342211687263','Content-Length': '217','Origin': 'https://iplogger.org','Referer': 'https://iplogger.org/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers'},data=dc3)
	if 'error' in rc3_id.text:exit(f'{Rc}[!] BAN{wh} ')
	else:
		try:
			ID=str(rc3_id.json()['go']).split('/')[2]
			print(f'{Rc}[{wh}+{Rc}] {gc}Done{wh} Crate Tracking Link')
		except:
			print(Rc+'[-] Error Try Later After a minute or check Your url')
	get_stat()
def main():
    print("""
██╗██████╗     ██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
██║██╔══██╗    ██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
██║██████╔╝    ██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
██║██╔═══╝     ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
██║██║         ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
╚═╝╚═╝         ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
                     By @TweakPY - @vv1ck""")
    print(f"{Rc}[{wh}+{Rc}] {rc}Let's Go we Have Target To Find . 🏃‍♂️")
    crate_link()
main()
