import requests
Scholar = requests.get("https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Scholar.list").text
# Domestic = requests.get("https://ruleset.skk.moe/Clash/non_ip/domestic.txt").text
Direct = requests.get("https://ruleset.skk.moe/Clash/non_ip/direct.txt").text
DirectIP = requests.get("https://ruleset.skk.moe/Clash/ip/domestic.txt").text

result = list()
for rawresult in [Scholar, Domestic, Direct, DirectIP]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)

result_text = '\n'.join(result)


with open("./Clash/Direct.txt", "w") as f:
    f.write(result_text)