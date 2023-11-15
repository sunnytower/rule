import requests

GlobalDomain = requests.get("# Global = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Proxy/Proxy_Domain.yaml").text").text

result = list()
for rawresult in [GlobalDomain]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Clash/GlobalDomain.txt", "w") as f:
    f.write("\n".join(result))

