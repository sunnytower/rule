import requests

# GlobalDomain = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Global/Global_Domain.list").text
GlobalDomain = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Proxy/Proxy_Domain.list").text

result = list()
for rawresult in [GlobalDomain]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)
result_text = '\n'.join(result)

with open("./Surge/GlobalDomain.list", "w") as f:
    f.write("\n".join(result))