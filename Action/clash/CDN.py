import requests
cdn = requests.get("https://ruleset.skk.moe/Clash/domainset/cdn.txt").text

result = list()
for rawresult in [cdn]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)

result_text = '\n'.join(result)


with open("./Clash/CDN.txt", "w") as f:
    f.write(result_text)