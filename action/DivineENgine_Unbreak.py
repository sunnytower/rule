import requests
Unbreak = requests.get("https://raw.githubusercontent.com/DivineEngine/Profiles/master/Surge/Ruleset/Unbreak.list").text

result = list()
for rawresult in [Unbreak]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)

result_text = '\n'.join(result)


with open("./Surge/DE/Unbreak.list", "w") as f:
    f.write(result_text)
