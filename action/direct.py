import requests
Scholar = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Scholar/Scholar.list").text
Direct = requests.get("https://github.com/Blankwonder/surge-list/raw/master/cn.list").text

result = list()
for rawresult in [Scholar,Direct]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)

result_text = '\n'.join(result)


with open("./Direct.list", "w") as f:
    f.write(result_text)
