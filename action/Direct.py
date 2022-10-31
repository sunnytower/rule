import requests
Scholar = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Scholar/Scholar.list").text
Domestic = requests.get("https://ruleset.skk.moe/List/non_ip/domestic.conf").text
cn = requests.get("https://raw.githubusercontent.com/Blankwonder/surge-list/master/cn.list").text
result = list()
for rawresult in [Scholar, Domestic, cn]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)

result_text = '\n'.join(result)


with open("./Direct.list", "w") as f:
    f.write(result_text)
