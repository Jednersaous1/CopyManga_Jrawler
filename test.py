l = ['https://ss.mangafuna.xyz/s/shengxiadebangxiong/b0673/1741796016770001.jpg.c800x.webp', 'https://ss.mangafuna.xyz/s/shengxiadebangxiong/b0673/1741796019120011.jpg.c800x.webp', 'https://ss.mangafuna.xyz/s/shengxiadebangxiong/b0673/1741796023410013.jpg.c800x.webp', 'https://ss.mangafuna.xyz/s/shengxiadebangxiong/b0673/1741796027640007.jpg.c800x.webp', 'https://hi77-overseas.mangafuna.xyz/static/websitefree/jpg/loading.jpg', 'https://hi77-overseas.mangafuna.xyz/static/websitefree/jpg/loading.jpg', 'https://hi77-overseas.mangafuna.xyz/static/websitefree/jpg/loading.jpg', 'https://hi77-overseas.mangafuna.xyz/static/websitefree/jpg/loading.jpg', 'https://ss.mangafuna.xyz/s/shengxiadebangxiong/b0673/1741796049370009.jpg.c800x.webp', 'https://ss.mangafuna.xyz/s/shengxiadebangxiong/b0673/1741796053260002.jpg.c800x.webp', 'https://ss.mangafuna.xyz/s/shengxiadebangxiong/b0673/1741796057090014.jpg.c800x.webp', 'https://ss.mangafuna.xyz/s/shengxiadebangxiong/b0673/1741796061190008.jpg.c800x.webp', 'https://ss.mangafuna.xyz/s/shengxiadebangxiong/b0673/1741796065130004.jpg.c800x.webp', 'https://ss.mangafuna.xyz/s/shengxiadebangxiong/b0673/1741796069510005.jpg.c800x.webp']

print(len(l))


import json
import urllib.request

def main(json_path="url.json"):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data: dict = json.load(f)
            print(data)
            print(type(data))
            print(data.get("1"))
            return data
    except:
        pass

def check(url: dict):
    for _, value in url.items():
        s = urllib.request.Request(value)
        try:
            urllib.request.urlopen(s)
            return value
        except Exception as e:
            print(f"Accesss Error {e}")
            continue
    return None


if __name__ == "__main__":
    url = main()

    if a:=check(url):
        print("yes")
        print(a)
