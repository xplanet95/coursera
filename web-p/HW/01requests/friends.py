import requests as r
import re
import datetime as dt

def cnt(result):
    date_obj = dt.date.today()
    friends_bdate_lst = []
    for i in result['response']['items']:
        if 'bdate' in i:
            if i['bdate'].count('.') > 1:
                friends_bdate_lst.append(date_obj.year - int(re.search(r'\d\d\d\d', i['bdate']).group(0)))
    lst_of_cort = list(set((i, friends_bdate_lst.count(i)) for i in friends_bdate_lst))
    p = sorted(lst_of_cort, key=lambda x: (-x[1], x[0]))
    return p



def calc_age(uid):
    ACCESS_TOKEN = 'f2f72a10f2f72a10f2f72a10bdf28d2f06ff2f7f2f72a10937d24100b99ed20d5558b2f'
    API_VK = '5.81'
    url_users_id = 'https://api.vk.com/method/users.get'
    url_friends_lst ='https://api.vk.com/method/friends.get'
    params = {
        'user_ids': uid,
        'access_token': ACCESS_TOKEN,
        'v': API_VK,
        'fields': 'bdate'
    }
    vk_id = r.get(url_users_id, params).json()['response'][0]['id']

    params_2 = {
        'user_id': vk_id,
        'access_token': ACCESS_TOKEN,
        'v': API_VK,
        'fields': 'bdate'
    }

    # friends_id_lst = [i['id'] for i in r.get(url_friends_lst, params_2).json()['response']['items']]
    res = cnt(r.get(url_friends_lst, params_2).json())
    return res

if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)