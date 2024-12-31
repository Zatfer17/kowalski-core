from trafilatura import fetch_url, extract


def get_url_content(url: str) -> str:
    downloaded = fetch_url(url)
    return extract(downloaded, output_format="markdown")