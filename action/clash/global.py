import requests

Global = requests.get("https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Clash/Global/Global_Domain.txt").text

result = list()
for rawresult in [Global]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Clash/Global.txt", "w") as f:
    f.write("\n".join(result))