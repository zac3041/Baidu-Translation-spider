import requests
import execjs
cookies = {
    'PSTM': '1676516073',
    'BAIDUID': '9E228668B81BA44D7C70779EC84ED1AF:FG=1',
    'BIDUPSID': 'D7112B867062DA7408D3EFB420F31EDA',
    'REALTIME_TRANS_SWITCH': '1',
    'FANYI_WORD_SWITCH': '1',
    'HISTORY_SWITCH': '1',
    'SOUND_SPD_SWITCH': '1',
    'SOUND_PREFER_SWITCH': '1',
    'BAIDUID_BFESS': '9E228668B81BA44D7C70779EC84ED1AF:FG=1',
    'ZFY': 'lR9X5YUeJHY1Do8OqqLL:A:An0w4uoE10mafn9SRjhMVk:C',
    'delPer': '0',
    'PSINO': '6',
    'RT': 'z=1&dm=baidu.com&si=e16561da-80c3-499b-93dd-d7653848713a&ss=ljpingjj&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=5mdj&nu=1irpc9387&cl=5lld&ul=b9h1f1&hd=b9h1g7',
    'BDRCVFR[dG2JNJb_ajR]': 'mk3SLVN4HKm',
    'BDRCVFR[-pGxjrCMryR]': 'mk3SLVN4HKm',
    'BA_HECTOR': '2021840k85a18l048h058l2d1iba12o1o',
    'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
    'H_PS_PSSID': '36556_38642_38831_39027_39023_38956_39040_38818_38825_38987_39085_26350_39095_39051_39100_38950',
    'BCLID': '12568793464885186616',
    'BCLID_BFESS': '12568793464885186616',
    'BDSFRCVID': 'oekOJexroG0ZmSbfRm_PM5smG_weG7bTDYrEOwXPsp3LGJLVFakFEG0Pts1-dEu-S2OOogKKy2OTH9DF_2uxOjjg8UtVJeC6EG0Ptf8g0M5',
    'BDSFRCVID_BFESS': 'oekOJexroG0ZmSbfRm_PM5smG_weG7bTDYrEOwXPsp3LGJLVFakFEG0Pts1-dEu-S2OOogKKy2OTH9DF_2uxOjjg8UtVJeC6EG0Ptf8g0M5',
    'H_BDCLCKID_SF': 'JnuJoK-htID3J4Dkbn0MjjoH-UnLqhJq0mOZ0l8Ktq3Phn3oh4jEW4COXHoe2xb-JJvH2fjmWIQahC8xbqJcDfKnWfvz2hcEK6c4KKJxtMKWeIJoLfFajbLihUJiBbFHBan7VlbIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbCDRe5LKD6jM-l-X5to05TIX3b7Efb7qjp7_bJ7KhUbQWxcg5t5NaGOT2C5bal3rfn5jjP5xQhFXQtnfXpOe-n7rKhc1QqQHjpQHQT3m5bJLqfO4-CrgteO9Wb3cW-IK8UbSefOPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JDMr0exbH55uJfRkJoM5',
    'H_BDCLCKID_SF_BFESS': 'JnuJoK-htID3J4Dkbn0MjjoH-UnLqhJq0mOZ0l8Ktq3Phn3oh4jEW4COXHoe2xb-JJvH2fjmWIQahC8xbqJcDfKnWfvz2hcEK6c4KKJxtMKWeIJoLfFajbLihUJiBbFHBan7VlbIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbCDRe5LKD6jM-l-X5to05TIX3b7Efb7qjp7_bJ7KhUbQWxcg5t5NaGOT2C5bal3rfn5jjP5xQhFXQtnfXpOe-n7rKhc1QqQHjpQHQT3m5bJLqfO4-CrgteO9Wb3cW-IK8UbSefOPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JDMr0exbH55uJfRkJoM5',
    'Hm_lvt_64ecd82404c51e03dc91cb9e8c025574': '1689660465',
    'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574': '1689661005',
    'ab_sr': '1.0.1_M2JkNTMzZjFlMGRiYmI5NDJlZjkxYjRjMjYwMmExODcxMDE5YjAzZTIyNDVkMTMzNDM4MDFjOTQ5ZmI0Mjc0ZjFlMzJjY2QwZjJjZTE2ZmQ1MmFiMmU2MDE5NDU1MTYwMTNhOTc3NzFiNjhkMGEwZGUxZWVhMTkyMjY2NTRhNDZlODBmMjI3ZWZmMzhkYjU0ZjFhMGU1ZjM5M2I4YzRhZQ==',
}
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Acs-Token': '1689661306271_1689661509977_GIB+6GNJCXWsn1iQSSUjP7yYZjvNvje+x4o35fdQdq8hoXu2F1GYV6zV/biUyte8+hcwuqe/HU6FdvtbvH97O9XMqzTVnPKgE7klUQnCsrUeXvn/1HpZ1nv4p27uEUCPrpk5eVVFyrND3/x6r+TiAzciwELjsvw9V8YnSz0Rabf3tK0P7+4rX7fyQgM+w0cIl7iSvqqknfJAYG3rZt0vYL8tq1VmzxIq01rUbyBMvaUlRjS36zQtDDtPScFqoZ1bnaTyHOwJW1QK9eQTjJuyKi/wk2ASO4a/u6TS8nh0zlj0S4FxkND1CYSjNar5pn+vrwcuFfzR63vMxw+LDTgXOA4vyXuGz05kyWKJ6ADyJxK58KaILwdncCAoLFjfAlx419nAEINouK95CTYUnhq43bMxD8vqpev9tujSJSsqb9DB2vQvdf6GEBL4vjLLE1Oc2RKRX+JBQXTto0lMDkq7MmrZ93kuWHQMQ5CqEkjjPujJYo9cuPH6JnbyV800tkt5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
params = (
    ('from', 'zh'),
    ('to', 'en'),
)
query = '百度翻译接口'
ext = execjs.compile(open('./js1.js','r',encoding='utf-8').read()).call('maji123',query)

data = {
  'from': 'zh',
  'to': 'en',
  'query': query,
  'transtype': 'realtime',
  'simple_means_flag': '3',
  'sign': ext,
  'token': 'fb322830f10e2534a92d4d32ac718da8',
  'domain': 'common',
  'ts': '1689661509964'
}
response = requests.post('https://fanyi.baidu.com/v2transapi', headers=headers, cookies=cookies, data=data).text
print(response.encode('utf-8').decode('unicode_escape'))