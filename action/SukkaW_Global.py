import requests
Global = requests.get("https://ruleset.skk.moe/List/non_ip/global.conf").text
Global_plus = requests.get("https://ruleset.skk.moe/List/non_ip/global_plus.conf").text
Telegram0 = requests.get("https://ruleset.skk.moe/List/non_ip/telegram.conf").text
Telegram1 = requests.get("https://ruleset.skk.moe/List/ip/telegram.conf").text
Blocked = requests.get("https://raw.githubusercontent.com/Blankwonder/surge-list/master/blocked.list").text
Spotify = requests.get("https://raw.githubusercontent.com/DivineEngine/Profiles/master/Surge/Ruleset/StreamingMedia/Music/Spotify.list").text
Youtube = requests.get("https://raw.githubusercontent.com/DivineEngine/Profiles/master/Surge/Ruleset/StreamingMedia/Video/YouTube.list").text

result = list()
for rawresult in [Global, Global_plus, Telegram0, Telegram1, Blocked, Spotify, Youtube]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)
result.extend(["DOMAIN-SUFFIX,jable.tv", "DOMAIN-SUFFIX,x18r.com", "DOMAIN-SUFFIX,av01.tv"])

result_text = '\n'.join(result)


with open("./Surge/SW/Global.list", "w") as f:
    f.write(result_text)
