from re                     import match as re_match
from youtube_transcript_api import YouTubeTranscriptApi
from trafilatura            import fetch_url, extract

    
def extract_video_id(url:str) -> str:
    youtube_regex = (
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
    )
    match = re_match(youtube_regex, url)
    if match:
        return match.group(6)
    raise ValueError(f"Invalid YouTube URL: {url}")

def get_yt_content(url:str) -> str:
    video_id = extract_video_id(url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([item['text'] for item in transcript])

def get_url_content(url: str) -> str:
    downloaded = fetch_url(url)
    return extract(downloaded, output_format="markdown", include_comments=False, include_tables=False, no_fallback=True)

def get_content(url:str):
    URL_REGEX = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    YT_REGEX  = r"(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+"
    if re_match(YT_REGEX, url):
        return get_yt_content(url)
    elif re_match(URL_REGEX, url):
        return get_url_content(url)
    return url