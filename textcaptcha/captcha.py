"""CAPTCHA classes.

Example:
    Create a new CAPTCHA object for holding the question and MD5 encoded
    answers:

        captcha = Captcha("Is the sky blue?", [
            "a6105c0a611b41b08f1209506350279e"])
        print(captcha.question)
        print(captcha.check_answer('no'))
"""
import hashlib


class Captcha:
    """Class for a single CAPTCHA challenge."""

    def __init__(self, question, answers):
        """Create a new CAPTCHA object.

        Args:
            question (str): The question to be displayed to the user.
            answers (list[str]): A list of MD5 encoded answers which are
                correct.

        """
        self.question = question
        self.answers = answers

    def check_answer(self, answer):
        """Check an answer against the correct answer(s) for the CAPTCHA question.

        Args:
            answer (str): The answer from the user to be checked.

        Returns:
            bool: Whether the answer was correct or not. True if the answer was
                correct, False if it was not.
        """
        # Sanitise answer
        answer = answer.strip().lower().encode()
        # Generate MD5 hash of answer
        answer = hashlib.md5(answer).hexdigest()

        # Check whether the answer is in the list of correct answers
        return answer in self.answers
