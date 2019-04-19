## Path of Exile Trade Parser

This Python 3 script allows you to connect to https://www.pathofexile.com/trade and automatically be notified for items that are placed on public stash tabs and match a specific search pattern. When that occurs, the most recent item gets copied to your clipboard and allows you to instantly message the seller ingame.

### Dependencies


* BeautifulSoup 
* pygame
* pyperclip
* requests
* websocket-client

### Installation

```
pip install -r requirements.txt
```

### Usage

```python
python main.py
```

A user input is required in order to enter the desired search pattern (e.g. Ab3LSL) and a valid session id (poesessid) from https://www.pathofexile.com

## Notes
This is a fairly rudimentary script that requires improvement, I've just made it to help out a friend that loves Path of Exile and I've decided to share it should someone else find it useful

## Known issues 
This works decently for specific filters, if your filter is too broad you will receive several items per iteration and you will only have the most recent one on your clipboard
