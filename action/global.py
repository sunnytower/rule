import requests
Global = requests.get("https://ruleset.skk.moe/List/non_ip/global.conf").text
Global_plus = requests.get("https://ruleset.skk.moe/List/non_ip/global_plus.conf").text
#Blocked = requests.get("https://raw.githubusercontent.com/Blankwonder/surge-list/master/blocked.list").text

result = list()
result.extend(["DOMAIN-SUFFIX,jable.tv", "DOMAIN-SUFFIX,x18r.com", "DOMAIN-SUFFIX,av01.tv", "DOMAIN-SUFFIX,18comic.vip", "DOMAIN-KEYWORD,jav"])
for rawresult in [Global, Global_plus]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)

result_text = '\n'.join(result)


with open("./proxy.list", "w") as f:
    f.write(result_text)
