import requests
import tldextract
from datetime import datetime

def check_url(url):
    # Make sure URL has proper format for processing
    if not url.startswith('http'):
        url = 'http://' + url
    
    # Extract the domain
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"
    
    # Check against OpenPhish blacklist
    try:
        blacklist_url = "https://openphish.com/feed.txt"
        response = requests.get(blacklist_url, timeout=5)
        if response.status_code == 200:
            blacklist = response.text.splitlines()
            if url in blacklist or domain in blacklist:
                return f"WARNING: {url} appears to be a phishing site!"
    except:
        pass  # If blacklist check fails, continue with other checks
    
    # Simple check for suspicious keywords in the URL
    suspicious_words = ['secure', 'account', 'banking', 'login', 'verify', 'paypal', 'signin']
    if any(word in url.lower() for word in suspicious_words):
        return f"CAUTION: {url} contains suspicious keywords. Be careful!"
    
    return f"SAFE: {url} passed our basic checks."

# Simple command line interface
if __name__ == "__main__":
    print("=== Simple Phishing URL Checker ===")
    print("Type 'quit' to exit")
    
    while True:
        url = input("\nEnter a URL to check: ")
        if url.lower() in ['quit', 'exit', 'q']:
            break
        
        result = check_url(url)
        print(result)
