

import urllib.request


url = 'http://www.baidu,com'

headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/03.0.1264.49'

}

request = urllib.request.Request(url=url,headers=headers)
# handler    buuld_opener   open


# (1) 获取handler对象

handler = urllib.request.HTTPHandler()

# （2）获取opener  对象

opener = urllib.request.build_opener(handler)

# (3) 调用open 方法

response =  opener.open(request)

content = response.read().decode('utf-8')

print(content)