import requests

RejectDomain = requests.get("https://raw.githubusercontent.com/DivineEngine/Profiles/master/Surge/Ruleset/Guard/AdvertisingPlus.list").text

result = list()
for rawresult in [RejectDomain]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Surge/DE/RejectDomain.list", "w") as f:
    f.write("\n".join(result))
   