# import requests
#
#
# def test_movie_check():
#     url = 'http://api.douban.com/v2/movie/in_theaters'
#     params = {
#         'apikey': '0df993c66c0c636e29ecbb5344252a4a',
#         'start': 0,
#         'count': 10
#     }
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
#     }
#     r = requests.get(url=url, params=params, headers=headers)
#     response = r.json()
#     print(response)
#     assert response['count'] == params['count']
#     # assert response['start'] == params['start']
#     # assert response['title'] == '正在上映的电影-北京'
#
#
# test_movie_check()

list1 = [2,3,5,1,3,4]
list2 = [6,2,3,8,1,0,2]
# l= list1
# l.extend(list2)
# print(l)
# l = list(set(l))
# l.sort(reverse=True)
#
#
# print(l)
l= []
for i in list1:
    l.append(i)
for x in list2:
    if x not in l:
        l.append(x)
print(l)
print(sorted(l,reverse=True))
