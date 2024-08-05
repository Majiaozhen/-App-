from flask import Flask
import requests

url = 'https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie': '_xsrf=pZS7sAJjycegxXjXzt4jlzVc9KqyV5mz; _zap=7e886673-d04f-4929-a2bd-9c0a13f602c9; d_c0=AQCSp6It0BiPTtKujBaUAA_Qnl4_JWUPies=|1719067467; q_c1=443474bf893f4efb9ed522a52a85fc5c|1719067985000|1719067985000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1719067462,1719136914,1721051793; HMACCOUNT=AB590CE3066BBE0A; __zse_ck=001_3tF5sM1FLFo6kEu4FviAYyh26zPt2PRtWMIFU=4Op2W58jDHec=YLVQk5Ev5xkO+QYiURgddMTHY9h48FAeVJ9j7AAxG=qJkeEKIHtQ/Tq7+g+glsodLgf248az5vTxi; tst=h; SESSIONID=1k1Hbw1KNFN6L5qDKD8jPKLAEvdiuNvGzfmMGdt8oLr; JOID=W18VBk2kEfmZbGPnBajgYZ3PQjYUm33N0gEa0UvlWbCqI1mYRi84avNtauUDy138vxUTqG_WwIeyeLtMJ1INKJE=; osd=Vl8VB06pEfmYb27nBanjbJ3PQzUZm33M0Qwa0UrmVLCqIlqVRi85af5tauQAxl38vhYeqG_Xw4qyeLpPKlINKZI=; captcha_session_v2=2|1:0|10:1721052047|18:captcha_session_v2|88:aHJRM1QweHNCYi9DQXpNQ0Q3NS9VZU1Zb2x2S2dSbStPQ2RpblBqS24yajVhSkNuY3ZabjNYQXVNTUpybFJBcg==|43b9c74809caa48a5e47d30627fdb9c86700c356324ad91cb92f4ab98bb34e8b; __snaker__id=x5GTeWjyd1yPumLF; gdxidpyhxdE=lZ6TtNvZbPXMfZy%5CDvKW5zIL8nOtcZaV0goYVlH6S92ZYhqkmIY7tvs5uKQrtKB5DtApNCjWEDpTbiSDQYRtnlB86EklmTwndEOJN5%2BN%2FHG%5CD%2F8UfqTMHYQ%2B4wRqIMOCgfZPzORN6rUd5pzrmdrWvyfJSAP%5CX16%2B3d%2FEJDZcKf%5CI7%2BAv%3A1721052947398; captcha_ticket_v2=2|1:0|10:1721052057|17:captcha_ticket_v2|728:eyJ2YWxpZGF0ZSI6IkNOMzFfRGU0eG5ZT3ZhRWxwT05yd3JaRjF3ekpLOXI4anhYcSpLTXVTZHkxQmJUa3BGaEpoUndHRDlfQl9zaVRGSFdyTXZPR1pUWmI2eWh4VWpjS3UqKkFPcHFodlp5bFRDR1NXLnJPRlJMbzJraTl2UURmNVFvV0ZFaEVJdnNCVENHMXpTSDlHdll3RlFNVlZfQzlvWnJ0MkExUy5RTnVRaUd4OVMwTnpWUGlFdnZyR29LVWpSdG85emN2MUtBUktNcGJwcEFfTy44bXJrLkdMSXBuTG9rZ3p2S1pDMFg2YTFWSVlZU0F5V3NaSWV2UDBiblNVUzhtOVhzSW1IRW8qQlpQVDgzOE5pUFJlcVFiQnk0dmIyUXFEaEZkVl9UNkZwMzNvU1h1T1RzcjJzM0Njd2Q1S1kwUVVPc2VpbCpLSnJqWTVYLkZjREpRZk8yYndIb3ZYYVYuMm1xdW9ydjYqTjQqNHprSnpLb0hmUHBRaWxoRkRYbVVVWnNlZEN1d2lYWklrcGtNVWpPZVBpVFY1T3lWckJaTUZYeGFiY09aZEtyQnI0aUtUMEN3VzhHYUJzSGl1bS53OVNsLmlKcXBnbU1pQnZia1FGYXc1MXJGOWF1bHJnSEFEUG1adG94SVhoTTlWKkdmSkNCTy5jVURRazZrekxkVExINkd3R01Ib3F0MEcqdGFpSU03N192X2lfMSJ9|e51717132a28b2bd4ff11603aa8517efed2c1be6fc546a8b5b8aeb4668a1e1f9; z_c0=2|1:0|10:1721052078|4:z_c0|92:Mi4xRUh2eENnQUFBQUFCQUpLbm9pM1FHQ1lBQUFCZ0FsVk5ybm1DWndCOWRSdVlqNE84NDdic2FibzB1UEFfVms4VGlB|97dc9d662ec825278548fa44d71bd19e2d04c66bbc21127c9c266f3c0f117cd0; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1721052157; BEC=ec64a27f4feb1b29e8161db426d61998',
    'Priority': 'u=1, i',
    'Referer': 'https://www.zhihu.com/hot',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-Api-Version': '3.0.76',
    'X-Forwarded-For': '4.2.2.2',
    'X-Requested-With': 'fetch',
    'X-Zse-93': '101_3_3.0',
    'X-Zse-96': '2.0_0iMkUbH6FDrXOxNrwNaM6HiQOAMG+RbacjzdXzyxWzdlD5+Mve7kH8qD3qM8t6tY',
    'X-Zst-81': '3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZMTY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIeQuK7AFpS6O1vukyQ_R0rRnsyukMGvxBEqeCiRnxEL2ZZrxmDucmqhPXnXFMTAoTF6RhRuLPF4XOscxBLuN_pBS8PCFYZGxY8GeBFBLVS8LBDrOYo4L8h9VOxuC18X2feUSTvHXMZbLfxJXLQBOBbw3poUcVJwVBBhHG60F96wLLswxGcQL8c72_fBCMxgLMtBNCJhosQXSGduYY2H9m1CwL9uc07hN1EJH_EGtxngCm0CXMSiU_OUF9Oqfz5C2f0JN90gH_kBSGYgXKO9LmrgcmPB3qcBeGTqoYnB3_ShSquqHLLUU9hqV8kCw1RuY0BCeBr4XV8cNBF9CLICpMUJxVSXXmRGL8UGQVwBo9ChXC18LC'
}
r = requests.get(url, headers=headers, verify=False)
print(r.status_code)
json_data = r.json()
# print(json_data)

list = []
data_list = json_data['data']
order = 1
for data in data_list:
    list.append(order)
    title = data['target']['title_area']['text']
    list.append(title)

    desc = data['target']['excerpt_area']['text']
    list.append(desc)

    url = data['target']['link']['url']
    list.append(url)

    hot = data['target']['metrics_area']['text']
    list.append(hot)

    ans_num = data['feed_specific']['answer_count']
    list.append(ans_num)

    order = order + 1

app = Flask(__name__)

# print(list)
str1 = str(list)
print(str1)


@app.route('/data_list')
def hello_world():  # put application's code here
    return str1


if __name__ == '__main__':
    app.run()
