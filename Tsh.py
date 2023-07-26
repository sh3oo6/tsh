from time import sleep; import requests
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon import TelegramClient , functions
import asyncio
use = ["dexcc44"]
led=TelegramClient('ledA', 2192036, '3b86a67fc4e14bd9dcfc2f593e75c841')
led.start()
while True:
 i=0
 while True:
  i+=1
  if i == 500:
   del i
   break
  while True:
   sleep(0.1)
   for user in use:
    req = requests.get(f"https://t.me/{user}")
    if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
        async def hh():
            take =await led(UpdateUsernameRequest(user))
            if take==True:
                print('jj')
        loop = asyncio.get_event_loop()
        loop.run_until_complete(hh())
    else:
     print(f"NOOOOOOOOOOO : {user}" + str(i))

   break

