import requests

Microsoft = requests.get("https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Microsoft.list").text

result = list()
for rawresult in [Microsoft]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)
result_text = '\n'.join(result)

with open("./Surge/Microsoft.list", "w") as f:
    f.write("\n".join(result))