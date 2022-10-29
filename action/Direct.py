import requests
Scholar = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Scholar/Scholar.list").text
Direct = requests.get("https://ruleset.skk.moe/List/non_ip/domestic.conf").text

result = list()
for rawresult in [Scholar, Direct]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)

result_text = '\n'.join(result)


with open("./Domestic.list", "w") as f:
    f.write(result_text)

AppleCDN = requests.get("https://ruleset.skk.moe/List/domainset/apple_cdn.conf").text
result.extend([item for item in AppleCDN.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)
with open("./Direct.list", "w") as f:
    f.write(result_text)