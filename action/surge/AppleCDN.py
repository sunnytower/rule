import requests

AppleCDN = requests.get("https://ruleset.skk.moe/List/domainset/apple_cdn.conf").text

result = list()
for rawresult in [AppleCDN]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)

result_text = '\n'.join(result)

with open("./Surge/AppleCDN.list", "w") as f:
    f.write(result_text)
