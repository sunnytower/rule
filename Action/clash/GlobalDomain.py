import requests

GlobalDomain = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Proxy/Proxy_Domain.yaml").text

result = list()
for rawresult in [GlobalDomain]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)
result_text = '\n'.join(result)

with open("./Clash/GlobalDomain.txt", "w") as f:
    f.write("\n".join(result))

