"""CAPTCHA classes.

Example:
    Create a new CAPTCHA object for holding the question and MD5 encoded
    answers:

        captcha = Captcha("Is the sky blue?", [
            "a6105c0a611b41b08f1209506350279e"])
        print(captcha.question)
        print(captcha.check_answer('no'))

Example:
    Serialize a CAPTCHA object for storage, for example inside a Flask session:

        captcha = Captcha("Is the sky blue?", [
            "a6105c0a611b41b08f1209506350279e"])
        session["captcha"] = captcha.serialize()
        # ...
        captcha = Captcha.deserialize(session["captcha"])
"""
import hashlib
import json


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

    def serialize(self):
        """Convert a CAPTCHA object to a JSON string.

        Can be later deserialized with the deserialize() class method.

        Returns:
            str: A JSON representation of the CAPTCHA object.
        """
        return json.dumps(self.__dict__)

    @classmethod
    def deserialize(cls, json_data):
        """Convert a JSON string of a CAPTCHA into a CAPTCHA object.

        Args:
            json_data (str): A JSON representation of a CAPTCHA object.

        Returns:
            Captcha: The deserialized CAPTCHA object.
        """
        data = json.loads(json_data)
        return cls(question=data["question"], answers=data["answers"])
