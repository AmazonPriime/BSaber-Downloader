# BSaber-Downloader

## No longer working as beatsaver have added cloudflare to their site, will update in the future

Downloads songs from [BSaber](https://bsaber.com/) using data from [andruzzzhka/BeatSaberScrappedData](https://github.com/andruzzzhka/BeatSaberScrappedData) based on their difficulty, star rating and whether or not they're ranked.

Usage:
* Download the zip or clone the project to your own system.
* Download the ```combinedScrappedData.json``` from [here](https://github.com/andruzzzhka/BeatSaberScrappedData/blob/master/combinedScrappedData.json) and store it in the same directory as ```main.py```.
* If it's not installed, install the ```requests``` module: ```pip3 install requests```.
* Run program from terminal/cmd/powershell with command: ```python3 main.py <CustomLevels folder> <True/False> <integer > 0> <difficulty>```
  * Difficulties accepted: "Easy", "Normal", "Hard", "Expert" or "ExpertPlus"
* If your arguments are correct the songs will be downloaded to your CustomLevels folder.

**CustomLevels folder is located in your ```Beat Saber_Data``` folder, this is found within your Steam folder in ```Program Files (x86)```**

Example: ```C:\Program Files (x86)\Steam\steamapps\common\Beat Saber\Beat Saber_Data\CustomLevels```

Example: ```python3 main.py "C:\Program Files (x86)\Steam\steamapps\common\Beat Saber\Beat Saber_Data\CustomLevels" True 5 Expert```
