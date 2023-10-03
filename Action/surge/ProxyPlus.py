import requests
GlobalPlus = requests.get("https://ruleset.skk.moe/List/non_ip/global_plus.conf").text
Global = requests.get("https://ruleset.skk.moe/List/non_ip/global.conf").text

result = list()
for rawresult in [GlobalPlus, Global]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Surge/ProxyPlus.list", "w") as f:
    f.write("\n".join(result))