import requests

Apple = requests.get("https://ruleset.skk.moe/List/non_ip/apple_services.conf").text

result = list()
for rawresult in [Apple]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)

result_text = '\n'.join(result)

with open("./Apple.list", "w") as f:
    f.write(result_text)
