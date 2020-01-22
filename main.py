import sys, os, requests, json, argparse
from functions import str2bool, int_check, difficulty_check, get_songids
from functions import difficulties


# parse the arguments for the CustomLevels location, ranked and stars
parser = argparse.ArgumentParser()
parser.add_argument("location", help = "Path to the directory containing your CustomLevels in BeatSaber")
parser.add_argument("ranked", help = "Whether or not the songs you want are ranked.", type = str2bool)
parser.add_argument("stars", help = "The minumum star difficulty of the songs you want to download. (stars determine the PP of the song)", type = int_check)
parser.add_argument("difficulty", help = "The difficulty of the songs you want to download.", type = difficulty_check)
args = parser.parse_args()


# validation for the location
if not os.path.exists(args.location):
    print("The specified directory does not exist, make sure it's the correct one. For your BeatSaber custom levels.")
    exit(1)

if not os.path.isdir(args.location):
    print("Hmm, this is not a directory. Make sure it's the directory for the custom levels.")
    exit(1)


# get data from JSON
with open(os.path.join(os.getcwd(), "combinedScrappedData.json"), "rb") as f:
    data = json.load(f)


# get list of songs already installed and list of songs to be downloaded then find the ones not installed from the available
ranked = 1 if args.ranked else 0
songs_installed = list(get_songids(args.location))
songs_available = [song for song in data for difficulty in song['Diffs'] if difficulty['Diff'] == args.difficulty and difficulty['Ranked'] == ranked and difficulty['Stars'] >= args.stars]
songs_difference = [song for song in songs_available if song['Key'] not in songs_installed]


# download songs from songs_difference list
c = 0
for song in songs_difference:
    download(song)
    c += 1
    print(f"{c}/{len(songs_difference)} songs", end = "\r")
print(f"{c}/{len(songs_difference)} songs")
