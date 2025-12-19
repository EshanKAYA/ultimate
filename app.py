from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # --- 1. API: RASTGELE AJAN (Random User API) ---
    # Bize rastgele bir insan profili verir.
    try:
        user_resp = requests.get('https://randomuser.me/api/')
        user_data = user_resp.json()['results'][0]
        ajan = {
            'isim': f"{user_data['name']['first']} {user_data['name']['last']}",
            'resim': user_data['picture']['large'],
            'ulke': user_data['location']['country'],
            'sehir': user_data['location']['city'],
            'kod_adi': user_data['login']['username']
        }
    except:
        ajan = {'isim': 'Bilinmiyor', 'resim': '', 'ulke': 'Gizli', 'kod_adi': 'Ghost'}

    # --- 2. API: K-9 ORTAĞI (Dog CEO API) ---
    # Bize rastgele bir köpek resmi verir.
    try:
        dog_resp = requests.get('https://dog.ceo/api/breeds/image/random')
        kopek_resmi = dog_resp.json()['message']
    except:
        # Hata olursa varsayılan bir Alman Kurdu resmi
        kopek_resmi = "https://images.dog.ceo/breeds/germanshepherd/n02106662_13910.jpg"

    # --- 3. API: GİZLİ FON / BITCOIN (CoinDesk API) ---
    # Bize anlık Bitcoin fiyatını verir.
    try:
        btc_resp = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        btc_fiyat = btc_resp.json()['bpi']['USD']['rate']
    except:
        btc_fiyat = "ERİŞİM YOK"

    return render_template('index.html', ajan=ajan, kopek=kopek_resmi, para=btc_fiyat)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
