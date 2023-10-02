import requests
Scholar = requests.get("https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Scholar.list").text
Domestic = requests.get("https://ruleset.skk.moe/List/non_ip/domestic.conf").text
Direct = requests.get("https://ruleset.skk.moe/List/non_ip/direct.conf").text
CN = requests.get("https://raw.githubusercontent.com/Blankwonder/surge-list/master/cn.list").text

result = list()
for rawresult in [Scholar, Domestic, Direct, CN]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)

result_text = '\n'.join(result)


with open("./Clash/Direct.txt", "w") as f:
    f.write(result_text)