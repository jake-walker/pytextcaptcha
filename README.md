# TextCaptcha

> A Python library for using text-based CAPTCHAs from <http://textcaptcha.com/>.

<a href="https://ci.jakewalker.xyz/jake-walker/pytextcaptcha/"><img alt="Build Status" src="https://img.shields.io/drone/build/jake-walker/pytextcaptcha/master?server=https%3A%2F%2Fci.jakewalker.xyz&style=flat-square"></a>
<a href="https://pypi.org/project/textcaptcha/"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/textcaptcha?style=flat-square"></a>
<img alt="GitHub License" src="https://img.shields.io/github/license/jake-walker/pytextcaptcha?style=flat-square">

This is a simple wrapper around the [TextCaptcha](http://textcaptcha.com/) API which is a service which provides text-based CAPTCHA questions which helps to prevent spam from robots.

This is designed to be implemented into a server-side application such as a Discord Bot, IRC, SMS, etc...

**Note:** *The TextCaptcha API is only suitable for low traffic websites. For more than 5 requests per second, your usage will be rate limited.*

## Installation

Use `pip` to install on all systems:

```bash
pip install textcaptcha
```

## Usage Example

This example will ask a CAPTCHA question and ask for an answer which is then checked against the actual answer.

```python
import textcaptcha

# Create a captcha fetcher to fetch captcha questions from the API
fetcher = textcaptcha.CaptchaFetcher()
# Fetch a new captcha from the API
captcha = fetcher.fetch()

# Print the captcha question to the console
print(captcha.question)
# Get a response from the user
answer = input("Answer: ")

# Check that the answer is correct
if captcha.check_answer(answer):
    print("You're not a robot!")
else:
    print("You are a robot, sorry!")
```

## Development Setup

This project uses Poetry to manage dependencies and packaging. [Here](https://python-poetry.org/docs/#installation) are the installation instructions for Poetry.

## Contributing

1. Fork it (https://github.com/jake-walker/pytextcaptcha/fork)
2. Create your feature branch (`git checkout -b feature/foobar`)
3. Commit your changes (`git commit -am "Add some foobar"`)
4. Push to the branch (`git push origin feature/foobar`)
5. Create a new pull request
