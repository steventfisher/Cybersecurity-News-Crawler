# Cybersecurity News Crawler
There are numerous Cybersecurity news sites on the web.  This application is used to try and collaborate those stories.

I have written a cybersecurity news crawler for my project for CS 645(Internet Security) at UNR.  
Which will crawl various predefined websites and search for articles pertaining to various keywords that are in the system.  The sites and keywords can be appended to by either using the maintenance option in the program or by editing the 
links.txt and keywords.txt documents respectivley.

In order to run the program, there are a couple of libraries that need to be installed. These libraries
are listed below:

-You will need to install BeautifulSoup. This is different depending on your system. Below is installation
using pip.
```
pip install BeautifulSoup4
```

-You will need to install lxml. This is different depending on your system. Below is installation
using pip.
```
pip install lxml
```
In addition to the keyword and links documents, there is also a list of words that would invalidate a link.
(i.e. pdf, .doc, twitter.com,...)

Upon completion of running the program will generate an html document with links to all the articles
collected, the user is then given a choice as to whether or not open the link.

# Road-map
What I plan on adding to the Cybersecurity-News-Crawler is as follows in no particular order:
* Write crawled sites to a database in order to maintain a history
* Dynamically locate to webiste to crawl baased on search results
* allow the addition of blocked words based on flagging
* store list of news sites in database
* create front-end in and reformat results in order to make more user friendly.

# License

Cybersecurity-News-Crawler is free software, and may be redistributed under the terms specified in the [LICENSE](https://github.com/steventfisher/Cybersecurity-News-Crawler/blob/master/LICENSE).
