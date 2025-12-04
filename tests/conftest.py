"""
This module contains shared fixtures.
"""

import json
import pytest
import selenium.webdriver


@pytest.fixture(scope='session')
def config():

    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Validate config values
    assert config["browser"] in ["Firefox", "Chrome", "Headless Chrome"]
    assert isinstance(config["implicit_wait"], int)
    assert config["implicit_wait"] > 0

    return config


@pytest.fixture
def browser(config):

    # Initialize the WebDriver instance
    if config["browser"] == "Firefox":
        b = selenium.webdriver.Firefox()

    elif config["browser"] == "Chrome":
        b = selenium.webdriver.Chrome()

    elif config["browser"] == "Headless Chrome":
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument("--headless=new")
        opts.add_argument("--window-size=1920,1080")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument("--no-sandbox")
        opts.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        b = selenium.webdriver.Chrome(options=opts)


    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Implicit wait from config.json
    b.implicitly_wait(config["implicit_wait"])

    yield b

    b.quit()
