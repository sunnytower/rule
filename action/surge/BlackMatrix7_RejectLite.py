import requests

Reject1 = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AdvertisingLite/AdvertisingLite.list").text

result = list()
for rawresult in [Reject1]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Surge/BM/RejectLite.list", "w") as f:
    f.write("\n".join(result))