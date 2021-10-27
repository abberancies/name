import os

try:
    import requests, ctypes, json, webbrowser, random, time
    from time import sleep
    from colorama import Fore
    from datetime import date 
    from pypresence import Presence
    from discord_webhook import DiscordWebhook, DiscordEmbed
    from urllib.request import Request, urlopen

except ImportError as e:
    print(f'{Fore.WHITE}[{Fore.YELLOW}Sirius{Fore.RESET}] There was an error importing something, more details here: {str(e)}. Retrying.')
    installing = os.popen('python -m pip install -r requirements.txt').read()
    if 'is not recognized as an internal or external command, operable program or batch file.' in installing:
        print('You do not have pip installed, redirecting to recommended python version.')
        webbrowser.open_new('https://www.python.org/downloads')

#terminal clear for either os - macos/linux/windows
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#main vars
purple = Fore.MAGENTA
reset = Fore.RESET
red = Fore.RED
today = date.today()
d2 = today.strftime("%B %d, %Y")
start_time = time.time()
end_time = int(round((time.time() - start_time) * 1000))
available = 0

def count():
    namecount = 0
    with open("Usernames.txt") as f:
            for namecount, l in enumerate(f):
                pass
            namecount = namecount + 1


    return namecount

ctypes.windll.kernel32.SetConsoleTitleW(f"GitHub Username Checker by pxl#1337")

usernamerich = input(f"[{purple}+{purple}{reset} Enter A Username: ")

#rich presence
with open('config.json') as f:
    config = json.load(f)
    rich_presence = config.get('richpresence')
if rich_presence:
    try:
        rpc = Presence(client_id='859044150887841832')
        rpc.connect()
        rpc.update(large_image='github',state=f'Logged In As: {usernamerich}', details=f'Connected', start=time.time())
    except:
        print(f'[{purple}Error{reset}] Rich Prescence Failed')
        sleep(1)
        clear()

os.system('mode con: cols=120 lines=21')

def logo():
    print(f"""
{purple}════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{purple}                                    

                                                      `          {reset}Github Username Checker{reset}
                                                                {reset}Developed By {red}pxl#1337{reset}                             

{purple}════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{purple}{reset}\n""")
logo()



print(f"[{purple}+{reset}] There are {count()} usernames that you want to check.")

#def getProxy():
#	global proxList
#	global proxList2
#	prox = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=US&ssl=no&anonymity=all")
#	if prox.text == f"[{purple}Error{reset}] You have reached your hourly maximum API requests of 750.":
#		print(f"[{purple}Error{reset}] Please wait an hour before running this script again.")
#		exit()
#	proxyTxt = prox.text.splitlines()
#	proxList = []
#	for line in proxyTxt:
#		proxList.append(line)
#	prox2 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=US&ssl=yes&anonymity=all")
#	if prox2.text == f"[{purple}Error{reset}] You have reached your hourly maximum API requests of 750.":
#		print(f"[{purple}Error{reset}] Please wait an hour before running this script again.")
#		exit()
#	proxyTxt2 = prox2.text.splitlines()
#	proxList2 = []
#	for line in proxyTxt2:
#		proxList2.append(line)
#getProxy()

def main():
    global available
    global usernamestxt
    global availabletxt
    #global randProxy
    #global randProxySSL
    #randProxy = random.choice(proxList)
    #randProxySSL = random.choice(proxList2)
    sleep(0.001)
    with open('Usernames.txt') as fp:
        usernames = fp.read().splitlines()
    for username in usernames:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.208"
            }
        #proxies = {
            #"http": randProxy,
            #"https": randProxySSL
            #}
        url = f"https://github.com/{username}"
        r = requests.get(url, headers=headers)#, proxies=proxies)
        status = r.status_code
        if status == 200:
            print(f"[{purple}x{reset}] {username}")
        if status == 404:
            print(f"[{purple}√{reset}] {username}")
            available += 1
            with open('Available.txt', 'a') as av:
                av.write(username + "\n")

input(f"[{purple}+{reset}] Press ENTER to Start")
os.system("disclaimer.vbs")
main()
def getdeveloper():
    dev = "wodx"
    try:
        dev = urlopen(Request("https://pastebin.com/raw/vxKBu1C9")).read().decode()
    except:
        pass
    return dev
developer = getdeveloper()
web_hook = config.get('webhook')
webhook_url = config.get('webhookurl')
if webhook_url == "":
    print(f"[{purple}Error{reset}] No webhook URL found")
if web_hook:
    try:
        webhook = DiscordWebhook(url=webhook_url)
        embed = DiscordEmbed(title=f'Finished Checking Names', color=0x2f3136)
        embed.set_timestamp()
        embed.add_embed_field(name="Usernames Checked", value=str(count()))
        embed.add_embed_field(name="Total Available", value=str(available))
        embed.add_embed_field(name="Time Taken", value=str(end_time))
        embed.set_footer(text=f'Coded By {developer}')
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        print(f'[{purple}Error{reset}] Webhook Failed')
        sleep(1)

#remove all #'s to use proxies
