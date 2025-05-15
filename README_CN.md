# CopyManga_Jrawler

> [!NOTE]
> 推荐使用Python虚拟环境运行
>
> 仅在Python 3.12.8, MacOS arm64平台下测试无误

## 功能

**下载指定漫画所有话的图片资源，并以`.jpg`后缀保存**

**下载指定漫画指定话的图片资源，并以`.jpg`后缀保存**

**更多功能敬请期待**

## 用法
提供两种认证方法（你至少应该选择一种）

1. 指定`token`认证

2. 指定`用户名密码`认证（用户名密码均明文 但不会保存在任何地方）

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

### 例子

首选的WebUrl是 "https://www.mangacopy.com/" 所以确保你的token对应的是该网站的token

```
> ./crawler.py -m swyjdwhzwhywbsjmsnbw -c [你的token]

> ./crawler.py -m wueyxingxuanlv -c [你的token] -ch 6 7 8

> ./crawler.py -m wueyxingxuanlv -u [你的用户名] -p [你的密码]

> ./crawler.py -m wueyxingxuanlv -u [你的用户名] -p [你的密码] -ch 5
```