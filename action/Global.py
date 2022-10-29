import requests
Global = requests.get("https://ruleset.skk.moe/List/non_ip/global.conf").text
Global_plus = requests.get("https://ruleset.skk.moe/List/non_ip/global_plus.conf").text
telegram0 = requests.get("https://ruleset.skk.moe/List/non_ip/telegram.conf").text
telegram1 = requests.get("https://ruleset.skk.moe/List/ip/telegram.conf").text
#Blocked = requests.get("https://raw.githubusercontent.com/Blankwonder/surge-list/master/blocked.list").text

result = list()
for rawresult in [Global, Global_plus, telegram0, telegram1]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)
result.extend(["DOMAIN-SUFFIX,jable.tv", "DOMAIN-SUFFIX,x18r.com", "DOMAIN-SUFFIX,av01.tv", "DOMAIN-SUFFIX,18comic.vip"])

result_text = '\n'.join(result)


with open("./Global.list", "w") as f:
    f.write(result_text)
