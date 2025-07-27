import tkinter as tk
from tkinter import messagebox
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")  # Format: +1xxxxxxx

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_alert():
    to_number = phone_entry.get().strip()
    alert_message = message_entry.get("1.0", tk.END).strip()

    if not to_number or not alert_message:
        messagebox.showerror("Error", "Please enter both phone number and message.")
        return

    if not to_number.startswith("+"):
        messagebox.showerror("Error", "Phone number must include country code (e.g., +91 for India, +1 for USA).")
        return

    # Send SMS
    try:
        print(f"SMS to: {to_number}")
        sms = client.messages.create(
            body=alert_message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_number
        )
        messagebox.showinfo("SMS Sent", "✅ SMS sent successfully!")
    except Exception as e:
        print("❌ Failed to send SMS:\n", e)
        messagebox.showerror("SMS Failed", f"Failed to send SMS:\n{e}")

    # Send WhatsApp
    try:
        print(f"WhatsApp to: {to_number}")
        whatsapp = client.messages.create(
            body=alert_message,
            from_="whatsapp:" + TWILIO_PHONE_NUMBER,
            to="whatsapp:" + to_number
        )
        messagebox.showinfo("WhatsApp Sent", "✅ WhatsApp message sent successfully!")
    except Exception as e:
        print("❌ Failed to send WhatsApp message:\n", e)
        messagebox.showerror("WhatsApp Failed", f"Failed to send WhatsApp message:\n{e}")

# GUI Setup
root = tk.Tk()
root.title("Emergency Alert Bot")

tk.Label(root, text="Enter Phone Number (+countrycode...):").pack(pady=5)
phone_entry = tk.Entry(root, width=30)
phone_entry.pack(pady=5)

tk.Label(root, text="Enter Message:").pack(pady=5)
message_entry = tk.Text(root, height=5, width=40)
message_entry.pack(pady=5)

send_button = tk.Button(root, text="Send Alert", command=send_alert)
send_button.pack(pady=10)

root.mainloop()
