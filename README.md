Phishing URL Detector
A simple command-line tool to check if a URL might be a phishing site.
Features

Checks URLs against known phishing sites
Detects suspicious keywords in URLs
Easy to use command-line interface
Lightweight with minimal dependencies

Installation

Make sure you have Python installed (Python 3.6 or higher)
Clone this repository:
git clone https://github.com/chisomobanja/phishing-detector.git
cd phishing-detector

Install the required packages:
Copypip install requests tldextract


Usage
Run the program with:
Copypython detector.py
Then simply enter any URL you want to check. The program will tell you if it appears safe or suspicious.
Type quit to exit the program.
Development Roadmap
Current Branch: main
Contains the basic implementation with command-line interface.
Future Development
Immediate Plans

Create a blacklist-updates branch
git checkout -b blacklist-updates

Implement regular updates of phishing site database
Add multiple blacklist sources
Improve blacklist caching


Create a ui-development branch
git checkout -b ui-development

Add a simple GUI using Tkinter
Provide visual indicators for safe/unsafe sites
Create browser extension



Long-term Plans

Add machine learning capabilities to detect phishing patterns
Implement browser integration
Create a web service API

How It Works
The detector uses several methods to identify potential phishing sites:

Checking URLs against known blacklists
Analyzing domains for suspicious patterns
Looking for common phishing keywords

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
