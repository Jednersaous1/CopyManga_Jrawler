# CopyManga_Jrawler

[中文文档](https://github.com/Jednersaous1/CopyManga_Jrawler/blob/main/README_CN.md)

> [!NOTE]
> Recommend using Python Virtual Environment!
>
> Only tested on Python 3.12.8, MacOS arm64 platform

## Functions

**Download all manga source pictures for all chapters as `.jpg` format**

**Download single chapter's manga source pictures as `.jpg` format**

**Later more functions to be Continued**

## Usage
Provide two methods for authentication (You should choose only one of them at the least)

1. Token authentication

2. Username and Password (All Plaintext! But won't save anywhere)

```
> git clone https://github.com/Jednersaous1/CopyManga_Jrawler.git
> pip install -r requirements.txt
> ./crawler.py -h
usage: crawler.py [-h] -m MANGA [-c COOKIE] [-u USERNAME] [-p PASSWORD] [-ch [CHAPTER ...]]

CopyManga_Jrawler Help Manual

options:
  -h, --help            show this help message and exit
  -m MANGA, --manga MANGA
                        Enter wanted manga's name with pinyin format
  -c COOKIE, --cookie COOKIE
                        Enter your copymanga website's cookie(token)
  -u USERNAME, --username USERNAME
                        Enter your username
  -p PASSWORD, --password PASSWORD
                        Enter your password
  -ch [CHAPTER ...], --chapter [CHAPTER ...]
                        Enter specific chapter that you want download from the manga
```

### Examples

First website option is "https://www.mangacopy.com/" So make sure your token is correct for this site

```
> ./crawler.py -m swyjdwhzwhywbsjmsnbw -c [Your token]

> ./crawler.py -m wueyxingxuanlv -c [Your token] -ch 6 7 8

> ./crawler.py -m wueyxingxuanlv -u [Your username] -p [Your password]

> ./crawler.py -m wueyxingxuanlv -u [Your username] -p [Your password] -ch 5
```