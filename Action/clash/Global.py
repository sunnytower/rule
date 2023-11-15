import requests

Global = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Proxy/Proxy.list").text
# GamePlatform = requests.get("https://raw.githubusercontent.com/LoveMyself666/ACL4SSR/master/Clash/GamePlatform.list")

result = list()
for rawresult in [Global]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)
result_text = '\n'.join(result)

with open("./Clash/Global.txt", "w") as f:
    f.write("\n".join(result))
