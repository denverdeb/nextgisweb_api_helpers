import os
import requests

dir = os.path.dirname(os.path.abspath(__file__))
ngw_host = 'https://sandbox.nextgis.com'
auth = ('administrator', 'demodemo')

def create_ngw_user():
    api_url = ngw_host + '/api/component/auth/user/'

    new_user ={
            "display_name": "Test user",
            "keyname": "test_user",
            "password":"secret",
            "disabled": False,
            #"member_of": [ 5 ]
    }
    
    resp = requests.post(api_url, auth=auth, json=new_user, timeout=30)

    if resp.status_code == 200:
        print('Пользователь создан')
    elif resp.status_code == 422:
        response = requests.get(api_url+'?brief=true', auth=auth, timeout=30)
        if response.status_code == 200:
            js_list = response.json()
            i = 0
            for res in js_list:
                #js = res[i]
                #print(js)
                if res['keyname'] == 'test_user':
                    id = res['id']
                    break
                i = i + 1
            user_update ={
                'password':'new_secret'
            }
            resp1 = requests.put(api_url+str(id), auth=auth, json=user_update, timeout=30)
            if resp1.status_code == 200:
                print('Пароль пользователя обновлен')
    else:
        print('Произошла ошибка')

if __name__ == '__main__':
    create_ngw_user()