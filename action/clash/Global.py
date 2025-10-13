import requests
urls = [
"https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Global/Global.list",
]
result = []
for url in urls:
    resource_text = requests.get(url).text
    for item in resource_text.split("\n"):
        if (item not in result) and (not item.startswith('#')):
            result.append(item)


with open("./clash/Global.txt", "w") as f:
    f.write("\n".join(result))
