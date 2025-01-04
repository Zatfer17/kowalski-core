from trafilatura import fetch_url, extract


def get_url_content(url: str) -> str:
    try:
        downloaded = fetch_url(url)
        return extract(downloaded, output_format="markdown")
    except:
        return None