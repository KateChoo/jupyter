from requests_html import HTMLSession
#from requests_html import HTML
session = HTMLSession()

r = session.get(
    'https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films')

#!!!!!心血
data = {}
title = 'i'
title_t = r.html.find(title)
# with open('disney_rhtml.txt', 'w') as file:
for t in title_t[7:]:  # 一個一個試看是哪一個
    title_a = t.find('a')
    for a in title_a:
        # print(a.text)
        data_key = a.text
        data_value = a.absolute_links
        data[data_key] = data_value
    # file.write(data)  # argument must be str, not dict
print(data)

#       可以印出
# title = 'i'
# title_t = r.html.find(title)
# for t in title_t[7:]:  # 一個一個試看是哪一個
#     title_a = t.find('a')
#     for a in title_a:
#         print(a.text)
#         print(a.absolute_links)
#         print('='*50)
