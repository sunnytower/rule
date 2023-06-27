import requests

Download = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Download/Download.list").text

result = list()
for rawresult in [Download]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Surge/BM/Download.list", "w") as f:
    f.write("\n".join(result))