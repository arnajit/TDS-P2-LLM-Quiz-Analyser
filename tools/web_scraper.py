from langchain_core.tools import tool
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

@tool
def get_rendered_html(url: str) -> dict:
    """
    Fetch and return the fully rendered HTML of a webpage.
    Automatically extract:
    - All image URLs
    - First audio URL (<audio> or <source>)
    - Any MP3 links found in <a> tags
    """
    print("\nFetching and rendering:", url)
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto(url, wait_until="networkidle")
            content = page.content()

            browser.close()

            soup = BeautifulSoup(content, "html.parser")

            # -----------------------------
            # EXTRACT IMAGES
            # -----------------------------
            imgs = [
                urljoin(url, img["src"])
                for img in soup.find_all("img", src=True)
            ]

            # -----------------------------
            # EXTRACT AUDIO URL
            # -----------------------------
            audio_url = None

            # Case 1: <audio src="">
            audio_tag = soup.find("audio")
            if audio_tag and audio_tag.get("src"):
                audio_url = urljoin(url, audio_tag["src"])

            # Case 2: <audio><source src=""></audio>
            if not audio_url and audio_tag:
                source_tag = audio_tag.find("source")
                if source_tag and source_tag.get("src"):
                    audio_url = urljoin(url, source_tag["src"])

            # -----------------------------
            # Case 3: Detect MP3 in <a href="file.mp3">
            # -----------------------------
            if not audio_url:
                for a in soup.find_all("a", href=True):
                    if a["href"].lower().endswith(".mp3"):
                        audio_url = urljoin(url, a["href"])
                        break

            # -----------------------------
            # Truncate huge HTML
            # -----------------------------
            if len(content) > 300000:
                content = content[:300000] + "... [TRUNCATED]"
            print("AUDIO URL FOUND:", audio_url)
            return {
                "html": content,
                "images": imgs,
                "audio_url": audio_url,
                "url": url
            }

    except Exception as e:
        return {"error": f"Error fetching/rendering page: {str(e)}"}
