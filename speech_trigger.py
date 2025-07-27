import speech_recognition as sr  # 🔹 Voice recognition ke liye library

def listen_for_command():
    recognizer = sr.Recognizer()  # 🔸 Recognizer object create kiya
    with sr.Microphone() as source:  # 🎙️ Mic se input lene ke liye
        print("🔊 Bolo 'help me' to trigger emergency alert...")
        recognizer.adjust_for_ambient_noise(source)  # 🔇 Background noise adjust karta hai
        audio = recognizer.listen(source)  # 🎧 Sunta hai audio input

    try:
        command = recognizer.recognize_google(audio)  # 🔎 Google API se voice ko text me convert karta hai
        print("🗣️ Tumne bola:", command)
        if "help me" in command.lower():  # ✅ Trigger word check karte hai
            print("🚨 Emergency Trigger Detected!")
            return True
        else:
            print("😶 Trigger word nahi mila.")
            return False
    except sr.UnknownValueError:
        print("❌ Voice samajh nahi aayi.")
        return False
    except sr.RequestError as e:
        print(f"⚠️ API Error: {e}")
        return False

# Testing ke liye
if __name__ == "__main__":
    triggered = listen_for_command()
    if triggered:
        print("👉 Ab email aur sms bhejna yaha se trigger hoga.")
