import requests
GlobalPlus = requests.get("https://ruleset.skk.moe/Clash/non_ip/global_plus.txt").text
Global = requests.get("https://ruleset.skk.moe/Clash/non_ip/global.txt").text

result = list()
for rawresult in [GlobalPlus, Global]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Clash/ProxyPlus.txt", "w") as f:
    f.write("\n".join(result))