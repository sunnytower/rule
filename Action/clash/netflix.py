import requests

Netflix = requests.get("https://raw.txn3.dev/Onlookers-Group/Texonin-LAB-Public/main/Surge/rule/Netflix.list").text

result = list()
for rawresult in [Netflix]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Clash/Netflix.txt", "w") as f:
    f.write("\n".join(result))