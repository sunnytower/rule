import requests
urls = [
# "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Proxy/Proxy_All_No_Resolve.list",
"https://ruleset.skk.moe/List/non_ip/cdn.conf",
"https://ruleset.skk.moe/List/non_ip/global.conf"
]
result = []
for url in urls:
    resource_text = requests.get(url).text
    for item in resource_text.split("\n"):
        if (item not in result) and (not item.startswith('#')):
            result.append(item)


with open("./surge/Global.txt", "w") as f:
    f.write("\n".join(result))