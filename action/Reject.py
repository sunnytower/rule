import requests

Reject1 = requests.get("https://ruleset.skk.moe/List/non_ip/reject.conf").text
Reject2 = requests.get("https://ruleset.skk.moe/List/ip/reject.conf").text

result = list()
for rawresult in [Reject1 , Reject2]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Reject.list", "w") as f:
    f.write("\n".join(result))