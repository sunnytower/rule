import requests

CDNDomain = requests.get("https://ruleset.skk.moe/List/domainset/cdn.conf").text

result = list()
for rawresult in [CDNDomain]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)

result_text = '\n'.join(result)

with open("./Surge/CDNDomain.list", "w") as f:
    f.write(result_text)