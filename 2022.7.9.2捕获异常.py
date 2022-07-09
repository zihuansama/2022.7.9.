import urllib.request
import urllib.error

url = 'http://www.gou2dan1111.com'

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/03.0.1264.49'
}
try:
    request = urllib.request.Request(url=url,headers=headers)

    response = urllib.request.urlopen(request)
    content =response.read().decode('utf-8')
    print(content)
except urllib.error.HTTPError:
    print('错误')
except urllib.error.URLError:
    print('网址错误')
