---
layout: post
title:  "Downloading TikTok videos is easy with yt-dlp"
tags: tiktok "social media" short
excerpt: "TikTok's data export tool combined with yt-dlp makes it easy to download TikTok videos and metadata."
---

TikTok is getting banned in the United States... or maybe its not?!??
Regardless, TikTok's [data export tool](https://support.tiktok.com/en/account-and-privacy/personalized-ads-and-data/requesting-your-data) combined with [yt-dlp](https://github.com/yt-dlp/yt-dlp) makes it easy to download TikTok videos and metadata.

Here's how I was able to download all the videos I liked as a TikTok user:

1. I [exported](https://support.tiktok.com/en/account-and-privacy/personalized-ads-and-data/requesting-your-data) my TikTok data in JSON format.

2. I extracted the liked video links into a .txt file using a snippet of Python: (See Jupyter [notebook](https://github.com/levon003/levon003.github.io/blob/main/src/tiktok_download/TikTokUserDataExploration.ipynb).)

  ```python
  import json
  with open("user_data_tiktok.json") as infile, open("liked_videos.txt", "w") as outfile:
      user_data = json.load(infile)
      activity = user_data["Activity"]
      likes = activity["Like List"]["ItemFavoriteList"]
      for like in likes:
          outfile.write(like["link"] + "\n")
  ```

3. I installed [yt-dlp](https://github.com/yt-dlp/yt-dlp) and ran it to download all videos in the folder:

  ```bash
  yt-dlp \
      -P ~/Downloads/liked_tiktok_videos \
      -a liked_videos.txt \
      -o "%(uploader)s_%(upload_date)s_%(id)s.%(ext)s" \
      --write-info-json
  ```

For each `.mp4` video file, a corresponding `.info.json` file is created with the uploader's display name and video description along with other metadata about the video file.

I was pretty shocked by the deletion rate of TikTok videos; many American uploaders may have deleted their accounts or cleared out their older videos. Of my 3,837 TikTokLikes, only 1,915 of those videos were available to download: that's a 50.1% loss.
