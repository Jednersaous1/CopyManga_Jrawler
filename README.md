# CopyManga_Jrawler

> [!NOTE]
> Recommend using Python Virtual Environment!
> Only tested on Python 3.12.8, MacOS arm64 platform

## Functions

**Only achieved downloading all manga pictures for all chapters as .jpg format**
**Later to be Continued**

## Usage
```
> pip install -r requirements.txt
> ./crawler.py -h
usage: crawler.py [-h] -m MANGA -c COOKIE

CopyManga_Jrawler Help Manual

options:
  -h, --help            show this help message and exit
  -m MANGA, --manga MANGA
                        Enter wanted manga's name
  -c COOKIE, --cookie COOKIE
                        Enter your copymanga website's cookie(token)
```
### Examples
```
> ./crawler.py -m swyjdwhzwhywbsjmsnbw -c [Your token]
```