import requests

ChinaASN = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/ChinaASN/ChinaASN.list").text

result = list()
for rawresult in [Scholar,Direct]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)

result_text = '\n'.join(result)

with open("./ChinaASN.list", "w") as f:
    f.write(result_text)
