## Bible Gateway Search
This workflow will scrape biblegateway.com to find passages you request.

#### Requirements:  
Python 3, and the BeautifulSoup4 and requests python modules.  
To install the modules: `pip3 install bs4 requests`

#### Setup:
Edit the Alfred `DEFAULT_BIBLE_VERSION` environment variable to your favorite bible version. This will set the default bible version used to retrieve bible verses. Valid version strings can be found by viewing the version dropdown selector at biblegateway.com. A few examples are: ESV, RVR1960, SG21

#### Usage:

###### Keyword
`bb {query}`

Your query should resemble bible references with or without specifying a version/translation seperated by a space at the end.

Ex:  
`bb 1 Timothy 3:15`  
`bb 1Tim3:15-17`  
`bb 1Tim3:15,4:10-13 esv`  
`bb Juan 3:16, Matt 20:1 nasb`

Action the item in three different ways:

* Actioning the item with no modifier keys held down will open the requested passage(s) on the BibleGateway website

* Holding `Command` and actioning the item will copy the passage(s) to your clipboard. Press `Command+V` to paste them.

* Holding `Option` and actioning the item will show the passage(s) in large type.

###### Hotkey
You can highlight/select any passage reference and use the hotkey `Command+Option+Control+B` to show the passage in large type. Try it out on one of the references above.

#### License:
Apache 2.0

Copyright © Joshua Smith
