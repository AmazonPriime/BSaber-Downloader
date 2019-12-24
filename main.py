import sys, os, requests, json

working_dir = os.getcwd();
download_dir = os.path.join(working_dir, "downloads")
difficulties = ["ExpertPlus", "Expert", "Hard", "Normal", "Easy"]

def getURL(key):
    return "https://beatsaver.com/api/download/key/%s" % key

def download(song):
    url = getURL(song['Key'])
    response = requests.get(url)
    with open(os.path.join(working_dir, "downloads", str(song['Key']) + ".zip"), "wb") as f:
        f.write(response.content)

with open(os.path.join(working_dir, "combinedScrappedData.json")) as f:
    data = json.load(f)

if not os.path.isdir(download_dir):
    os.mkdir(download_dir)

for song in data:
    for difficulty in song['Diffs']:
        if difficulty['Diff'] == "ExpertPlus" and difficulty['Ranked'] == 1 and difficulty['Stars'] > 4:
            download(song)
