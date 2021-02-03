from urllib.request import urlopen
import json

owner = "kalenikov"
repo = "job4j_elementary"

url = f'https://api.github.com/repos/{owner}/{repo}/commits?per_page=3'

response = urlopen(url).read()
data = json.loads(response.decode())

for commit in data:
    print(commit['html_url'])
    print(commit['commit']['message'])
    print(commit['commit']['author']["date"])
