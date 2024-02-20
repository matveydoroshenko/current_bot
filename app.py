import os
import random

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telethon import TelegramClient, events
from telethon.tl.functions.messages import ImportChatInviteRequest


def get_files_in_directory(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename)
                         .replace(".session", ""))
    return files


clients = []
for session in get_files_in_directory("tdatas"):
    clients.append(TelegramClient(session, 23657696, "b65d4dafab5e53b6ed4001e2dac6bf66"))

main_client = TelegramClient("tdatas/main", 22234293, "c3eb415eb9e016ce568127beb0c3b7c2")


@main_client.on(events.NewMessage(chats=-4126892756))
async def group_message(event):
    c = clients[random.randint(0, len(clients) - 1)]
    try:
        await c(ImportChatInviteRequest('GXgMoE16bdBiNzQ8'))
    except:
        pass
    try:
        await c(ImportChatInviteRequest('5AnMRe7jS9AzZDky'))
    except:
        pass
    try:
        await c.get_me()
    except:
        await c.start()
    await c.send_message(entity=-4111403268, message=event.text)

main_client.start()
main_client.run_until_disconnected()
