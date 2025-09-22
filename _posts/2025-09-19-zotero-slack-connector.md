---
layout: post
title:  "Zotero Slack Connector: a Slack bot for notifications about new papers"
tags: [zotero, slack, python, code, short]
excerpt: "I created a small open-source tool for notifying a Slack channel when new papers are added to a Zotero group."
image: /images/zotero_slack_connector_report.png
---

I love [Zotero](https://www.zotero.org/), an open-source citation management tool.

One cool Zotero feature is group libraries, where a group of people can see and contribute to a shared collection of papers.
Inevitably, group libraries receive uneven usage; some people on a team will use Zotero a lot, while others will forget it ever existed and continue emailing themselves PDFs.

I wanted to increase the visibility of Zotero usage for every member of the team, so I created a Slack bot that would keep a channel updated with newly-added papers.

You can find the `zotero-slack-connector` [on GitHub](https://github.com/DigitalHarborFoundation/zotero-slack-connector): <https://github.com/DigitalHarborFoundation/zotero-slack-connector>

The Slack bot sends two kinds of messages:
 - Recent papers: a list of the most recent papers added to a Zotero group
 - Papers added since last message: a list of the papers added to a Zotero group since the Slack bot's last message in a particular Slack channel

By default, it will show you up to three of the most recently-added papers.

![Example recent papers report.](/images/zotero_slack_connector_report.png){:style="display:block; margin-left: auto; margin-right: auto;"}
*An example recent papers report.*

If you want to use the Zotero Slack bot, it's straightforward to set up yourself.
 - Clone or download [the repository](https://github.com/DigitalHarborFoundation/zotero-slack-connector).
 - Build the Docker image – and optionally push it to a container registry of some kind.
 - Set credentials appropriately in a `.env` file:
   - Slack app: [create a new app](https://docs.slack.dev/quickstart/) with the appropriate credentials. I recommend the following Bot Token Scopes: `channels:{history,join,manage,read}`, `chat:write`, `groups:{history,read}`, `im:{history,read}`, `links:write`, `mpim:history`, `users:read`. Set `SLACK_BOT_TOKEN` to the Bot User OAuth Token generated when you install the App in your workspace.
   - Slack channels: add the bot to a channel (or group message or IM). Retrieve the channel ID and store it in `SLACK_CHANNEL_IDS`. Multiple channels are not currently supported, but it would be a trivial extension of the current implementation.
   - Zotero API: If pulling from a private group, follow the instructions [here](https://www.zotero.org/support/dev/web_api/v3/basics) to generate an API key and set `ZOTERO_API_KEY`.
   - Zotero group: set `ZOTERO_GROUP_ID` to the integers in [the group's](https://www.zotero.org/groups/) URL.
 - Run the Docker image on a regular interval.

I chose to use Google Cloud's Cloud Run functions and Cloud Scheduler to run the image every day. This kind of light usage is well within the free tier, so there's no cost to this approach.