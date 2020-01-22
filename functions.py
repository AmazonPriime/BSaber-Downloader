import argparse, os, requests

difficulties = ("Easy", "Normal", "Hard", "Expert", "ExpertPlus")
non_dirs = ("__pycache__", ".git", ".DS_Store")

# Boolean type for argparser - credit: https://stackoverflow.com/a/43357954/6806453
def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


# Integer type for argparser
def int_check(n):
    try:
        n = int(n)
        if n > 0:
            return n
        else:
            raise argparse.ArgumentTypeError("Integer must be greater than 0.")
    except:
        raise argparse.ArgumentTypeError("Integer value expected.")


# Difficulty type for argparser
def difficulty_check(s):
    for difficulty in difficulties:
        if s.lower() == difficulty.lower(): return difficulty
    raise argparse.ArgumentTypeError("Invalid difficulty must be one of: 'Easy', 'Normal', 'Hard', 'Expert' or 'ExpertPlus'.")


# Gets set of first string (for songs will be the song id) from each file in song directory
def get_songids(path):
    dirs = os.listdir(path)
    ids = set()
    for dir in dirs:
        if os.path.isdir(os.path.join(path, dir)) and not dir in non_dirs:
            ids.add(dir.split()[0])
    return ids


# Downloads the song from beatsaver
def download(song, location):
    url = "https://beatsaver.com/api/download/key/%s" % song['Key']
    response = requests.get(url)
    with open(location + ".zip", "wb") as f:
        f.write(response.content)
