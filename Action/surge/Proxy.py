import requests
cdn = requests.get("https://ruleset.skk.moe/List/non_ip/cdn.conf").text
stream = requests.get("https://ruleset.skk.moe/List/non_ip/stream.conf").text
streamIP = requests.get("https://ruleset.skk.moe/List/ip/stream.conf").text
telegram = requests.get("https://ruleset.skk.moe/List/non_ip/telegram.conf").text
telegramIP = requests.get("https://ruleset.skk.moe/List/ip/telegram.conf").text
# paypal = requests.get("https://raw.githubusercontent.com/DivineEngine/Profiles/master/Surge/Ruleset/Extra/PayPal.list").text

result = list()
for rawresult in [cdn, stream, streamIP, telegram, telegramIP]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Surge/Proxy.list", "w") as f:
    f.write("\n".join(result))
