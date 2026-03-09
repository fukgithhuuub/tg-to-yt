import google_auth_oauthlib.flow
import os

# Scopes needed for the YouTube API.
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def main():
    client_id = input("Enter your Client ID: ")
    client_secret = input("Enter your Client Secret: ")

    client_config = {
        "installed": {
            "client_id": client_id,
            "project_id": "youtube-upload-bot",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": client_secret,
            "redirect_uris": ["http://localhost:8080/"]
        }
    }

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_config(
        client_config, SCOPES)

    # Use run_local_server for a local desktop application.
    # This will open the user's browser for authorization.
    creds = flow.run_local_server(port=8080)

    print("\n--- AUTHENTICATION SUCCESSFUL ---")
    print(f"Your Refresh Token: {creds.refresh_token}")
    print("\nAdd this token to your GOOGLE_REFRESH_TOKEN environment variable.")

if __name__ == "__main__":
    main()
