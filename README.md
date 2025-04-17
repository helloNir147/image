# image
⸻
Discord IP Logger

A small Python script that functions as an IP logger and sends collected data to Discord using a webhook. The script handles HTTP requests, extracts relevant visitor information (like IP, browser, OS, location), and sends it directly to a Discord channel.

Features
	•	Sends IP, operating system, browser, and User-Agent details.
	•	Supports sending coordinates (lat, lon) with a Google Maps link.
	•	Bot detection and IP blacklist blocking.
	•	Automatically logs visits via Discord webhook.
	•	Optionally displays a thank-you message to visitors.

Requirements
	•	Python 3.x
	•	Modules:
	•	requests
	•	httpagentparser

To install the required modules:

pip install requests httpagentparser

Usage
	1.	Edit your Webhook URL in the config dictionary:

"webhook": "https://discord.com/api/webhooks/...",

	2.	Save the script as main.py (or any name you prefer).
	3.	Create an index.html file to be served when a user accesses the root path (/).
	4.	Run the script:

python main.py

Note: This script is built on Python’s built-in http.server. If you’re using a different server environment (like Flask or FastAPI), you’ll need to adjust the handler class accordingly.

Code Structure
	•	config: General settings – bot name, embed color, message display options, etc.
	•	is_bot(ip, user_agent): Returns True if the request is likely from a bot.
	•	send_log_to_discord(data): Sends the log data to the configured Discord webhook.
	•	create_report(...): Builds and sends the data report to Discord.
	•	handler: Handles GET requests and triggers the logging process.

Important Notes
	•	For educational purposes only! Do not use this script to invade user privacy or track people without consent.
	•	Make sure you’re complying with Discord’s Terms of Service and any applicable privacy laws.
	•	Do not share your webhook URL publicly.

⸻

It's the same thing, only it's in Hebrew🌵🩴.

⸻

Discord IP Logger

סקריפט קטן ב־Python שמשמש כלוגר IP עם שליחת מידע לדיסקורד דרך Webhook. הסקריפט מקבל בקשות HTTP, שומר מידע רלוונטי מהגולשים (כמו IP, דפדפן, מיקום גיאוגרפי) ושולח אותו ל־Discord.

תכונות
	•	שליחת פרטי IP, מערכת הפעלה, דפדפן ו־User-Agent.
	•	תמיכה בשליחת קואורדינטות (lat, lon) לקישור Google Maps.
	•	זיהוי בוטים וחסימת כתובות IP ברשימה שחורה.
	•	שליחה אוטומטית של לוג דרך Webhook.
	•	הצגת הודעת תודה (אופציונלית) למשתמשים שנכנסים לקישור.

דרישות
	•	Python 3.x
	•	מודולים:
	•	requests
	•	httpagentparser

התקנת התלויות:

pip install requests httpagentparser

שימוש
	1.	ערוך את כתובת ה־Webhook שלך בתוך מילון config בקובץ:

"webhook": "https://discord.com/api/webhooks/...",

	2.	שמור את הקובץ כ־main.py (או כל שם אחר).
	3.	צור קובץ index.html שנטען כשגולש נכנס לדף הראשי (/).
	4.	הרץ את הסקריפט:

python main.py

אם אתה משתמש בסביבת הרצה כמו Flask או FastAPI – תצטרך להתאים את המחלקה handler אליה, אך הקוד הנוכחי בנוי על http.server המובנה של פייתון.

מבנה הקוד
	•	config: הגדרות כלליות – שם הבוט, צבע ההודעה, האם להציג הודעה, ועוד.
	•	is_bot(ip, user_agent): מחזיר True אם מדובר בבוט.
	•	send_log_to_discord(data): שולח את הלוג ל־Webhook.
	•	create_report(...): יוצר הודעה ומעביר אותה לדיסקורד.
	•	handler: מחלקה שמטפלת בבקשות GET ומבצעת את כל הלוגיקה.

הערות חשובות
	•	לשימוש חינוכי בלבד! אין להשתמש בקוד הזה כדי לעקוב או לפגוע בפרטיות של אנשים.
	•	ודא שאתה עומד בתנאי השימוש של Discord ושל כל שירות שאתה משתמש בו.
	•	אל תשתף את כתובת ה־Webhook שלך בפומבי.

⸻

