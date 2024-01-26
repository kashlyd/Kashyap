import sys
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

def check_website(url):
    try:
        response = urlopen(url)
        print(f"The website at {url} is accessible. Status code: {response.getcode()}")
    except HTTPError as e:
        print(f"Error accessing {url}: HTTPError - {e}")
    except URLError as e:
        print(f"Error accessing {url}: URLError - {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_website.py <url>")
    else:
        url = sys.argv[1]
        check_website(url)
