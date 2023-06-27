import requests

ProxyDomain = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Proxy/Proxy_Domain.list").text

result = list()
for rawresult in [ProxyDomain]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Surge/BM/ProxyDomain.list", "w") as f:
    f.write("\n".join(result))