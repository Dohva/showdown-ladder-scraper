# showdown-ladder-scraper
This repo scrapes Pokemon Showdown for leaderboard statistics for the current generation.
Statistics are stored in the /data folder, and changes can be tracked through version control.

The GitHub action is based on [this](https://simonwillison.net/2020/Oct/9/git-scraping/) article, and is implemented with a few changes.

Notably the datatype changes from .json to .html as this is what is available.
And there is added support for hitting multiple endpoints.
