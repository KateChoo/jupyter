from requests_html import HTMLSession
import json
session = HTMLSession()
r = session.get('https://en.wikipedia.org/wiki/Nasdaq-100')
try:
    # 找尋table
    # table_class = '.wikitable sortable jquery-tablesorter'  # X
    table_id = '#constituents'  # V
    r_table = r.html.find(table_id)
    #!!!!!!!!!  直接找th         ==========================*==========
    headers = []
    th = r_table[0].find('th')
    for header in th:
        headers.append(header.text)
    # COMPANY!!!!!!!!!  直接找td ==========================*==========
    td = r_table[0].find('td')  # !!!!!
    company = []
    #company_data = {}
    for td_company in td[0::4]:
        # print(td_company.text)
        company.append(td_company.text)
        #company_data['company'] = td_company
    # print(company)
    # TICKER!!!!!!!!!             ==========================*==========
    ticker = []
    for td_ticker in td[1::4]:
        ticker.append(td_ticker.text)
    # print(ticker)
    # ==========================*==========
    data = dict(zip(company, ticker))
    # print(data)
    # ==========================*==========
    json_object = json.dumps(data)
    print(json_object)
    # with open('nastaq_company_ticker', 'w') as fp:
    #     json.dump(json_object, fp)
except:
    print('website may not be approachable ')
