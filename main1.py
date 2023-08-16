# Dex4 = المتغيرات
# Dex3 = المكاتب

from Dex4 import *

@led.on(events.NewMessage(pattern=r'x', outgoing=True))
async def execute_script(events):
    await events.edit('okay')
    await led.send_message('botfather', '/newbot')
    sleep(1)
    await led.send_message('botfather', 'Dex')
    x = 0
    while True:
        i=0
        while True:
            i += +1
            x += +1
            u = str(''.join((random.choice(uss) for i in range(2))))
            e = str(''.join((random.choice(rr) for i in range(1))))
            user = e + u + 'bot'
            if i == 150:
                s= open(f'check.txt', 'w')
                s.write(str(x))
                s.close()
                sleep(1)
                break
            sleep(0.165)
            req = requests.get(f"https://t.me/{user}")
            if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
                p = requests.get(f"https://fragment.com/username/{user}").text
                sleep(0.3)
                if 'Unavailable' in p:
                    try:
                        z = await led.send_message('botfather', user)
                        if z:

                            await led.send_message('botfather', '/newbot')
                            sleep(1)
                            await led.send_message('botfather', 'Dex')

                    except Exception:
                        pass
            else:
                pass
                print('me',(f"NOOO : {user}" + ' ' + str(i) + " " + str(x)))

@led.on(events.NewMessage(pattern=r'p', outgoing=True))
async def execute_script(event):
    s = open(f'check.txt', 'r').read()
    await event.edit(s)

try:
    led.run_until_disconnected()
except Exception:
    pass