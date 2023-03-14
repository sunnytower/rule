import requests

Microsoft = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Microsoft/Microsoft.list").text

result = list()
for rawresult in [Microsoft]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Surge/BM/Microsoft.list", "w") as f:
    f.write("\n".join(result))