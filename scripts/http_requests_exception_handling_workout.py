import requests
import logging

logger = logging.getLogger(__name__)


def make_request(url, kwargs=None):
    response = requests.get(url=url)
    logger.info(response.text)


def try_invalid_address():
    # Handling cases where the specified address could not be found
    try:
        url = "http://definitelynotadomainnamehyenn.com"
        make_request(url)

    except requests.exceptions.ConnectionError:
        logger.error("Could not connect to the specified domain name.")


def try_timeout_issues():
    # Errors connecting to the server
    # Using a short connect_timeout in this case helps to see
    # what happens when the connection times out
    connect_timeout = 0.0001
    try:
        url = "http://google.com"
        make_request(url, timeout=connect_timeout)
    except requests.exceptions.ConnectTimeout:
        logger.error("Too slow.")


def main():
    try_invalid_address()

if __name__ == '__main__':
    main()
