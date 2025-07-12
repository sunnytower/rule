import requests
urls = [
# "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/OpenAi.list",
"https://ruleset.skk.moe/Clash/non_ip/ai.txt",
]
result = []
for url in urls:
    resource_text = requests.get(url).text
    for item in resource_text.split("\n"):
        if (item not in result) and (not item.startswith('#')):
            result.append(item)


with open("./clash/OpenAI.txt", "w") as f:
    f.write("\n".join(result))
