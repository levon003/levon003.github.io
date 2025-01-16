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

3. I installed [yt-dlp](https://github.com/yt-dlp/yt-dlp) and ran it to download all videos listed in the `liked_videos.txt` file to the specified folder:

  ```bash
  yt-dlp \
      -P ~/Downloads/liked_tiktok_videos \
      -a liked_videos.txt \
      -o "%(uploader)s_%(upload_date)s_%(id)s.%(ext)s" \
      --write-info-json
  ```

For each `.mp4` video file, a corresponding `.info.json` file is created with the uploader's display name and video description along with other metadata about the video file.

## Expect unavailable videos

I was pretty shocked by the deletion rate of TikTok videos. Of my 3,837 TikTok likes, only 1,915 of those videos were available to download: that's a 50.1% loss. Many American uploaders may have deleted their accounts or cleared out their older videos. However, this is an extremely non-random sample collected at a single moment in time, so it's hard to speculate what the true loss rate is.

In general, some video deletions should be expected: people and platforms delete social media posts all the time.
A [2010 study](https://ojs.aaai.org/index.php/ICWSM/article/view/14270) conducted by Zeynep Tufekci found that 81% of sruveyed Facebook users (_n_=328) deleted info from their profile "because of a privacy or visibility concern".
A [2013 study](https://arxiv.org/abs/1309.2648) of Twitter by Hany SalahEldeen and Michael Nelson found that 11% of tweets are deleted within a year of their creation.
[Brennan Schaffner et al.](https://dl.acm.org/doi/abs/10.1145/3555142) looked at account deletion on several platforms including TikTok in 2022, but didn't attempt to estimate deletion rates by platform.
