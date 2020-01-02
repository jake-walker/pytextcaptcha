"""Tests for textcaptcha package."""

from textcaptcha import Captcha, CaptchaFetcher


def test_captcha_is_returned():
    """Test whether a captcha object is returned from the fetcher."""
    fetcher = CaptchaFetcher()
    captcha = fetcher.fetch()

    assert isinstance(captcha, Captcha)


def test_captcha_question_is_string():
    """Test whether the captcha object has a question."""
    fetcher = CaptchaFetcher()
    captcha = fetcher.fetch()
    q = captcha.question

    assert isinstance(q, str) and len(q) > 0


def test_captcha_check_answer():
    """Test whether the captcha answer checking works."""
    captcha = Captcha("Is the sky blue?", ["a6105c0a611b41b08f1209506350279e"])

    assert captcha.check_answer("Yes")
