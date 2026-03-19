#!/usr/bin/env python3
"""Send an email from the Forge Gmail account via SMTP."""
import smtplib
import sys
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

def load_env():
    env_path = Path(__file__).parent.parent / ".env"
    env = {}
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                env[key.strip()] = val.strip()
    return env

def send_email(to_addr, subject, body, reply_to_message_id=None, thread_subject=None):
    env = load_env()
    sender = env.get("FORGE_EMAIL", "voltage.the.forge@gmail.com")
    password = env.get("FORGE_APP_PASSWORD", "")

    if not password:
        print("ERROR: FORGE_APP_PASSWORD not set in .env", file=sys.stderr)
        sys.exit(1)

    msg = MIMEMultipart()
    msg["From"] = f"The Forge <{sender}>"
    msg["To"] = to_addr
    msg["Subject"] = subject

    if reply_to_message_id:
        msg["In-Reply-To"] = reply_to_message_id
        msg["References"] = reply_to_message_id

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

    print(f"Sent to {to_addr}: {subject}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python send_email.py <to> <subject> <body> [reply_to_message_id]", file=sys.stderr)
        sys.exit(1)

    to = sys.argv[1]
    subj = sys.argv[2]
    body = sys.argv[3]
    reply_id = sys.argv[4] if len(sys.argv) > 4 else None

    send_email(to, subj, body, reply_id)
