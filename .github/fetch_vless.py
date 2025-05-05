from telethon.sync import TelegramClient
import re
import os

api_id = int(os.environ["TG_API_ID"])
api_hash = os.environ["TG_API_HASH"]
channel = os.environ["TG_CHANNEL"]

client = TelegramClient('anon', api_id, api_hash)

vless_found = None

with client:
    for message in client.iter_messages(channel, limit=10):
        if message.text and 'vless' in message.text.lower():
            matches = re.findall(r'vless://[^\s]+', message.text)
            if matches:
                vless_found = "\n".join(matches)
                break

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(vless_found or "هیچ کانفیگ vless پیدا نشد.")
