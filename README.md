🔕 Silent SOS - Emergency Alert System
Silent SOS is a discreet and reliable emergency alert system that allows users to send emergency messages via SMS, WhatsApp, and Email with just a click—without making noise or drawing attention.

It can be useful in unsafe situations where you cannot call or speak, but need urgent help.

🚨 Features
📩 Send Emergency SMS using Twilio

💬 Send WhatsApp Alerts

📧 Send Email Alerts

🖥️ Easy-to-use GUI built with Python and Tkinter

🔐 Uses environment variables to keep sensitive data safe

🛠️ Tech Stack
Python 3

Tkinter – GUI Framework

Twilio API – SMS & WhatsApp messages

smtplib – Send emails

dotenv – Securely load credentials from .env file

📦 Installation
1. Clone the repository
bash
Copy code
git clone https://github.com/your-username/silent-sos.git
cd silent-sos
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Set up .env file
Create a .env file in the root directory and add the following details:

env
Copy code
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=+1234567890

WHATSAPP_FROM=whatsapp:+your_twilio_whatsapp_number
WHATSAPP_TO=whatsapp:+receiver_number

EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_email_password_or_app_password
EMAIL_TO=receiver_email@gmail.com
⚠️ Don't commit .env to public repositories.

▶️ Running the Application
bash
Copy code
python gui.py
This will open a simple GUI with buttons like:

Send SMS

Send WhatsApp

Send Email

Clicking any will send predefined emergency messages to configured contacts.

📷 Screenshots
Main GUI	SMS Sent

❓ When to Use
In case of stalking, kidnapping, or unsafe surroundings

While traveling alone

In domestic violence or abuse cases

Any situation where calling is not possible

🧠 Future Improvements
📍 Add GPS Location in the message

🛜 Enable Internet-based fallback if SMS fails

📱 Convert into a cross-platform mobile app using Kivy or React Native

🔊 Add sound alert toggle or volume controls

🔒 Safety Note
Twilio trial accounts allow sending messages only to verified numbers. For broader use, upgrade your account and configure billing safely.

🧹 Deactivating or Releasing Twilio Number
If the project is no longer in use:

Visit Twilio Console > Phone Numbers

Click on your number → "Release Number"

This stops billing and frees the number

💡 Project Name Inspiration
“Silent SOS” – Because help shouldn’t make noise when danger is loud.

📄 License
This project is licensed under the MIT License.
