'''

1、http报文 实际上是一段有规则的字符串
2、get 请求 url  ， 带参数的get请求，url + 参数
'''

'''
get 
理论上 url url长度其实是没有限制，浏览器对url的长度是有限制的，不同的浏览器url长度限制不一样

带参数的get请求
关键字 params   https://httpbin.org/get?key1=1&key2=2
一般情况下，当你的请求没有指定请求头的Content-Type ：默认值
Content-Type: application/x-www-form-urlencoded  

get的请求参上放在Url,相对于post的请求，没有那么安全
get请求的参数，如果有中文，会进行一个urlencode编码
https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B&fenlei=256&rsv_pq=f90abfaa0007efc6&rsv_t=e66c9P3CVmvZ6maA8xTvevVjpH4jQhrGBNqmkz5ABl1C1M8b9xhsYyGUZig&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=23&rsv_sug1=8&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=3283&rsv_sug4=3852
站长工具urldecode  :  http://tool.chinaz.com/tools/urlencode.aspx
url编码：https://baike.baidu.com/item/URL%E7%BC%96%E7%A0%81/3703727
'''
'''
get请求可以下载文件
1、下载非常小的文件，可以无需分块传输
2、下载大文件，要分块传输
3、下载文件，一般用二进制流，存储时候用wb
'''


'''
shell命令  Linux常用命令  jenkins集成   pythonui自动化   python接口自动化（执行）  pytest和unittest区别   文件的上传下载（怎么上传下载的）   
 ui自动化的维护是怎么维护的
'''




