import requests
Global = requests.get("https://raw.githubusercontent.com/DivineEngine/Profiles/master/Surge/Ruleset/Global.list").text
Telegram0 = requests.get("https://raw.githubusercontent.com/DivineEngine/Profiles/master/Surge/Ruleset/Extra/Telegram/Telegram.list").text
Blocked = requests.get("https://raw.githubusercontent.com/Blankwonder/surge-list/master/blocked.list").text
Spotify = requests.get("https://raw.githubusercontent.com/DivineEngine/Profiles/master/Surge/Ruleset/StreamingMedia/Music/Spotify.list").text
Youtube = requests.get("https://raw.githubusercontent.com/DivineEngine/Profiles/master/Surge/Ruleset/StreamingMedia/Video/YouTube.list").text

result = list()
for rawresult in [Global, Telegram0, Blocked, Spotify, Youtube]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)
result.extend(["DOMAIN-SUFFIX,jable.tv", "DOMAIN-SUFFIX,x18r.com", "DOMAIN-SUFFIX,av01.tv"])

result_text = '\n'.join(result)


with open("./Surge/DE/Global.list", "w") as f:
    f.write(result_text)

