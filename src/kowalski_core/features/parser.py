import re

from youtube_transcript_api import YouTubeTranscriptApi
from trafilatura import fetch_url, extract


class Parser():
    
    def _extract_video_id(self, url:str) -> str:
        youtube_regex = (
            r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
            r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
        )
        match = re.match(youtube_regex, url)
        if match:
            return match.group(6)
        raise ValueError(f"Invalid YouTube URL: {url}")

    def _get_yt_content(self, url:str) -> str:
        video_id = self._extract_video_id(url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([item['text'] for item in transcript])
    
    def _get_url_content(self, url: str) -> str:
        downloaded = fetch_url(url)
        return extract(downloaded, output_format="markdown")

    def get_type_source_content(self, source:str):
        URL_REGEX = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        YT_REGEX  = r"(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+"
        if re.match(YT_REGEX, source):
            media   = 'yt'
            content = self._get_yt_content(source)
        elif re.match(URL_REGEX, source):
            content = self._get_url_content(source)
            media   = 'url'
        else:
            media   = 'note'
            content = source
            source  = None
        return media, source, content