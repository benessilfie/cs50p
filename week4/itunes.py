import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit()

res = requests.get(
    f"https://itunes.apple.com/search?entity=song&limit=5&term=weezer {sys.argv[1]}")

# print(json.dumps(res.json(), indent=2))
o = res.json()

for result in o["results"]:
    print(result["trackName"])
