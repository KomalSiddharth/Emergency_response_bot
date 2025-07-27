import smtplib
import geocoder
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# 🔐 Load environment variables
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

# 🌍 Get location using IP
location = geocoder.ip('me')
location_link = f"https://www.google.com/maps?q={location.latlng[0]},{location.latlng[1]}"

# 📧 Compose Email
msg = EmailMessage()
msg['Subject'] = "🚨 Emergency Alert - I need help"
msg['From'] = SENDER_EMAIL
msg['To'] = RECEIVER_EMAIL
msg.set_content(f"""
Hi,

This is an automated emergency alert.

I might be in trouble. Here's my current location:
{location_link}

Please check on me.

- SilentSOS Bot
""")

# 📤 Send Email
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.send_message(msg)
    print("✅ Emergency email sent successfully!")
except Exception as e:
    print("❌ Failed to send email:", e)
