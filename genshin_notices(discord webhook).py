import requests, time

# data = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
# }

discord_webhook_url = "https://discord.com/api/webhooks/1067436871724048394/uJSbkAjghNufdLU3GOASsUFDdY5btfLAdfR_jCeTzqBS1HBexbCIZDPRIu6kQFwVs4zG"
genshin_cafe_api = "https://apis.naver.com/cafe-web/cafe2/NoticeListV3.json?cafeId=29893655&ad=true&mobileWeb=true&adUnit=MW_CAFE_BOARD&uuid=08eb7691-dd6c-421a-b71d-5aed7a867187"

genshin_notices = []
genshin_notices_copy = []
genshin_notices_summary = []

# while True:
  # time.sleep(2)

r = requests.get(genshin_cafe_api)
j = r.json()
for i in range(5):
  genshin_notices.append(j['message']['result']['articleList'][i]['item']['subject'])
  genshin_notices_summary.append(j['message']['result']['articleList'][i]['item']['summary'])

genshin_notices_copy = genshin_notices.copy()

data = {
  'content': genshin_notices[0]
}

# res = requests.post(discord_webhook_url, json=data)