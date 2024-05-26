import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","6435225"))
API_HASH = getenv("API_HASH","4e984ea35f854762dcde906dce426c2d")
BOT_TOKEN = getenv("BOT_TOKEN","")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1002136795173"))
BOTADDLOGS = int(getenv("BOTADDLOGS", "-1002136795173")) # LOGGER_ID Id Also Use No Problem
GBAN_LOGS = int(getenv("GBAN_LOGS", "-1002136795173"))
GCAST_USERS = list(map(int, getenv("GCAST_USERS", "7142645781").split()))
OWNER_ID = int(getenv("OWNER_ID", 7142645781))
OWNER = int(getenv("OWNER", 7142645781))
OWNER_USERNAME = getenv("OWNER_USERNAME","VP_1203")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/vicky0604hello/guppshupp")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN",None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/botverse_community")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/CNC_GROUPS")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5400"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", 7000))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", 7000))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999")) 
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
AMBOT = [
    "🔎",
    "🔍",
    "🧪",
    "ᴘʟꜱ ᴡᴀɪᴛ..",
    "ᴘʀᴏᴄᴇꜱꜱɪɴɢ..",
]

START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/9405aafe6384e21b46af5.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/9405aafe6384e21b46af5.jpg")
PLAYLIST_IMG_URL = "https://graph.org/file/9405aafe6384e21b46af5.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://graph.org/file/9405aafe6384e21b46af5.jpg")
TELEGRAM_AUDIO_URL = "https://graph.org/file/9405aafe6384e21b46af5.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/9405aafe6384e21b46af5.jpg"
STREAM_IMG_URL = "https://graph.org/file/9405aafe6384e21b46af5.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/9405aafe6384e21b46af5.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/9405aafe6384e21b46af5.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/9405aafe6384e21b46af5.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/9405aafe6384e21b46af5.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/9405aafe6384e21b46af5.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
