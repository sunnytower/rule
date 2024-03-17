import requests
urls = [
"https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/Scholar.list",
"https://ruleset.skk.moe/List/non_ip/direct.conf",
"https://ruleset.skk.moe/List/ip/domestic.conf",
"https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/BiliBili/BiliBili.list"
"https://raw.githubusercontent.com/Blankwonder/surge-list/master/cn.list",
]
result = []
for url in urls:
    resource_text = requests.get(url).text
    for item in resource_text.split("\n"):
        if (item not in result) and (not item.startswith('#')):
            result.append(item)


with open("./surge/Direct.list", "w") as f:
    f.write("\n".join(result))
