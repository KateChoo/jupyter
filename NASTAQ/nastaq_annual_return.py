from requests_html import HTMLSession
import json
import csv
session = HTMLSession()
r = session.get('https://en.wikipedia.org/wiki/Nasdaq-100')
try:
    # 找尋table
    table_class = '.wikitable.sortable'  # r_table[1]

    r_table = r.html.find(table_class)
    # print(r_table[1].text)
    #!!!!!!!!!  直接找th         ==========================*==========
    headers = []
    th = r_table[1].find('th')
    for header in th:
        headers.append(header.text.replace('\n', '-').replace('\xa0', ''))
    print(headers)
    # YEAR!!!!!!!!!  直接找td ==========================*==========
    td = r_table[1].find('td')  # !!!!!
    year = []

    for td_year in td[0::4]:
        year.append(td_year.text)

    # print(year)
     # Closing level!!!!!!!!!             ==========================*==========
    closing_level = []

    for td_closing in td[1::4]:
        closing_level.append(td_closing.text)

     # idx_points!!!!!!!!!             ==========================*==========
    idx_points = []

    for td_idx_p in td[2::4]:
        idx_points.append(td_idx_p.text.replace('\u2212', '-'))
    # idx_percentage!!!!!!!!!             ==========================*==========

    idx_percentage = []

    for td_idx_perc in td[3::4]:
        idx_percentage.append(td_idx_perc.text.replace('\u2212', '-') + '%')

    # =======*=========*====*
    #data = dict(zip(year, closing_level))
    data = dict(zip(year, idx_points))
    #data = dict(zip(year, idx_percentage))
    # print(data)
    json_object = json.dumps(data)
    print(json_object)
except:
    print('website may not be approachable ')
