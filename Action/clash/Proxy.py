import requests
stream = requests.get("https://ruleset.skk.moe/Clash/non_ip/stream.txt").text
streamIP = requests.get("https://ruleset.skk.moe/Clash/ip/stream.txt").text
telegram = requests.get("https://ruleset.skk.moe/Clash/non_ip/telegram.txt").text
telegramIP = requests.get("https://ruleset.skk.moe/Clash/ip/telegram.txt").text

result = list()
for rawresult in [stream, streamIP, telegram, telegramIP]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Clash/Proxy.txt", "w") as f:
    f.write("\n".join(result))