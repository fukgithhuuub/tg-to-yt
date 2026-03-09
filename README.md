# Telegram to YouTube Bot

This bot allows you to upload videos sent to a Telegram bot directly to your YouTube channel. It is designed to be easily deployable on [Render](https://render.com/).

## Features
- Uploads any video sent to the bot.
- Uses the video caption as the YouTube video title.
- Handles OAuth2 authentication with refresh tokens for long-term access.

## Prerequisites

1.  **Telegram Bot Token:**
    - Create a bot using [@BotFather](https://t.me/botfather) on Telegram and get your API token.

2.  **Google Cloud Project & YouTube Data API:**
    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Create a new project.
    - Enable the **YouTube Data API v3**.
    - Configure the **OAuth Consent Screen** (choose 'External' and add your email). Add the scope `.../auth/youtube.upload`.
    - Create **OAuth 2.0 Client IDs** (Application type: Desktop App).
    - Note down your **Client ID** and **Client Secret**.

3.  **Get Refresh Token:**
    - Install the requirements locally: `pip install -r requirements.txt`.
    - Run the helper script: `python get_refresh_token.py`.
    - Follow the instructions to authorize the app and copy the **Refresh Token**.

## Deployment on Render

1.  Create a new **Web Service** or **Worker** on Render.
2.  Connect your GitHub repository.
3.  Set the environment variables in the Render dashboard:
    - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
    - `GOOGLE_CLIENT_ID`: Your Google OAuth 2.0 Client ID.
    - `GOOGLE_CLIENT_SECRET`: Your Google OAuth 2.0 Client Secret.
    - `GOOGLE_REFRESH_TOKEN`: The Refresh Token you generated.
4.  Render will automatically use the `Procfile` and `requirements.txt` to deploy the bot.

## Usage
- Start the bot on Telegram by sending `/start`.
- Send any video to the bot. You can include a caption, which will be used as the video title on YouTube.
- The bot will download the video and upload it to your YouTube channel (initially set to 'private').

> **Note:** Telegram bots have a file size limit for downloading (20MB for standard bots). For larger videos, you may need to use a different method or a self-hosted Telegram Bot API server.

## Local Development
1.  Clone the repository.
2.  Create a `.env` file with the required environment variables.
3.  Install dependencies: `pip install -r requirements.txt`.
4.  Run the bot: `python bot.py`.
