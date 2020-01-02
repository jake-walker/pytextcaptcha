"""CAPTCHA fetchers.

Example:
    Create a new CAPTCHA fetcher for fetching CAPTCHA questions from the API:

        fetcher = CaptchaFetcher()
        captcha = fetcher.fetch()
"""

import requests
import urllib.parse
from .captcha import Captcha


class CaptchaFetcher:
    """A class for fetching CAPTCHA questions from the API."""
    def __init__(self, id="example"):
        """Create a new CAPTCHA fetcher.

        Args:
            id (str, optional): An ID for interacting with the TextCaptcha API.
                It should be an email address or domain name. Defaults to
                "example".
        """
        self.id = id

    def fetch(self):
        """Fetch a new CAPTCHA question from the API.

        Returns:
            Captcha: A Captcha object containing the question and answers from
                the API.
        """
        # Fetch a new captcha question from the API
        res = requests.get("http://api.textcaptcha.com/{}.json".format(
            urllib.parse.quote(self.id)))
        # Get the JSON response
        content = res.json()

        # Create a new captcha object using the question and answer from the
        # API
        return Captcha(content["q"], content["a"])
