import genshin
import asyncio
from win10toast import ToastNotifier
import socket
import time

# windows toast
toast = ToastNotifier()

# set cookies
cookies = genshin.utility.get_browser_cookies(browser="chrome")
client = genshin.Client(cookies, lang="ko-kr")

async def daily_reward():
    try:
        reward = await client.claim_daily_reward(game="genshin")
        toast.show_toast(
            title = "원신 출석체크 알림",
            msg = f"{reward.name} {reward.amount}개",
            duration = 3,
            threaded = True
        )

    except genshin.AlreadyClaimed:
        return

    except genshin.InvalidCookies:
        toast.show_toast(
            title = "원신 출석체크 알림",
            msg = "Chrome에 로그인을 해주세요.",
            duration = 3,
            threaded = True
        )
        time.sleep(5)
        asyncio.run(daily_reward())

i: int = 0
while True:
    # internet connect
    ipadd = socket.gethostbyname(socket.gethostname())

    if i == 0:
        print("인터넷 연결 확인중..")
        i += 1

    if ipadd != "127.0.0.1":
        time.sleep(5)
        asyncio.run(daily_reward())
        break

time.sleep(2)