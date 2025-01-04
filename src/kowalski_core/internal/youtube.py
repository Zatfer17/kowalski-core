import re

from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url:str) -> str:
    youtube_regex = r"(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})"
    match = re.match(youtube_regex, url)
    if match:
        return match.group(6)
    raise ValueError(f"Invalid YouTube URL: {url}")

def get_yt_content(youtube:str) -> str:
    try:
        video_id = extract_video_id(youtube)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([item["text"] for item in transcript])
    except:
        return None