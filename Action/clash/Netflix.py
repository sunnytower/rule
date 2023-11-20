import requests
urls = [
"https://raw.txn3.dev/Onlookers-Group/Texonin-LAB-Public/main/Surge/rule/Netflix.list",
]
result = []
for url in urls:
    resource_text = requests.get(url).text
    for item in resource_text.split("\n"):
        if (item not in result) and (not item.startswith('#')):
            result.append(item)


with open("./Clash/Netflix.txt", "w") as f:
    f.write("\n".join(result))