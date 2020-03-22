"""Tests for textcaptcha package."""

from textcaptcha import Captcha, CaptchaFetcher
import pytest
import json


@pytest.fixture
def example_captcha():
    """Create an example CAPTCHA object.

    Returns:
        Captcha: An example CAPTCHA object.
    """
    return Captcha("Is the sky blue?", ["a6105c0a611b41b08f1209506350279e"])


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


def test_captcha_check_answer(example_captcha):
    """Test whether the captcha answer checking works."""
    assert example_captcha.check_answer("Yes") is True


def test_captcha_serialize_valid(example_captcha):
    """Test whether captcha serialization works."""
    serialized_captcha = example_captcha.serialize()

    json.loads(serialized_captcha)


def test_captcha_deserialize_valid():
    """Test whether captcha deserialization works."""
    serialized_captcha = ('{"question": "Is the sky blue?", "answers": '
                          '["a6105c0a611b41b08f1209506350279e"]}')
    captcha = Captcha.deserialize(serialized_captcha)

    assert captcha.question == "Is the sky blue?"
    assert captcha.answers == ["a6105c0a611b41b08f1209506350279e"]
