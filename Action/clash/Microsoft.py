import requests

Microsoft = requests.get("https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Microsoft.list").text

result = list()
for rawresult in [Microsoft]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Clash/Microsoft.txt", "w") as f:
    f.write("\n".join(result))