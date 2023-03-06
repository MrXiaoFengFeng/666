''''
post请求形式
1、表单传输：
请求头：Content-Type : application/x-www-form-urlencoded
请求体：key1=v1&key2=v2   （对比一下get请求:https://httpbin.org/get?key1=1&key2=2）

2、json字符串传输 (json是一个特定格式的字符串，网络传输中只认识字符串)
请求头：Content-Type：application/json
请求体： {
    "some": "data"
}

3、传输文件
请求头：Content-Type：Content-Type
请求体：发文件
注意：发文件的时候，时候带上别的参数，这个参数可以放在请求体里面，也可以放在url里面，具体要看开发怎么设计，大多数放在get里面
'''