## Bible Gateway Search

This workflow will scrape biblegateway.com to find the passage(s) you requested.

#### Requirements:  
python3, BeautifulSoup4 and requests.

#### Usage:

`bb {query}`

Your query should resemble bible references with or without specifying a version/translation seperated by a space at the end.

Ex:  
`bb 1 Timothy 3:15`  
`bb 1Tim3:15-17`  
`bb 1Tim3:15,4:10-13 esv`  
`bb Juan 3:16, Matt 20:1 nasb` 

When you action the query, it will show the passage(s) in large type.  
Hold the `Command` key and action the query to copy the passage(s) to your clipboard. A notification will show on successfull completion 

License: MIT License

Copyright © Joshua Smith
