import requests

Reject1 = requests.get("https://raw.githubusercontent.com/DivineEngine/Profiles/master/Surge/Ruleset/Guard/Advertising.list").text
Reject2 = requests.get("https://raw.githubusercontent.com/DivineEngine/Profiles/master/Surge/Ruleset/Guard/Hijacking.list").text
# Privacy = requests.get("https://raw.githubusercontent.com/DivineEngine/Profiles/master/Surge/Ruleset/Guard/Privacy.list").text

result = list()
for rawresult in [Reject1 , Reject2]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Surge/DE/Reject.list", "w") as f:
    f.write("\n".join(result))