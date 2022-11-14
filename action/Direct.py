import requests
Direct = requests.get("https://ruleset.skk.moe/List/non_ip/direct.conf").text
Domestic = requests.get("https://ruleset.skk.moe/List/non_ip/domestic.conf").text
CN = requests.get("https://raw.githubusercontent.com/Blankwonder/surge-list/master/cn.list").text

result = list()
for rawresult in [Direct, Domestic, CN]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)

result_text = '\n'.join(result)


with open("./Direct.list", "w") as f:
    f.write(result_text)
