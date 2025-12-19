from flask import Flask, render_template, request # request'i eklemeyi unutma!
import requests

app = Flask(__name__)

# --- YENİ EKLENECEK KISIM 1: KAYIT LİSTESİ ---
# Bu liste ajanları hafızada tutacak
kaydedilen_ajanlar = []
# ---------------------------------------------

@app.route('/', methods=['GET', 'POST']) # POST metodunu ekledik
def index():
    # --- YENİ EKLENECEK KISIM 2: KAYDETME İŞLEMİ ---
    if request.method == 'POST':
        # Formdan gelen verileri alıp listeye ekliyoruz
        ajan_bilgisi = {
            'isim': request.form.get('isim'),
            'konum': request.form.get('konum'),
            'resim': request.form.get('resim'),
            'gorev': 'GÖREV BEKLİYOR'
        }
        kaydedilen_ajanlar.append(ajan_bilgisi)
    # -----------------------------------------------

    # --- SENİN MEVCUT API KODLARIN BURADA KALSIN ---
    # (Buradaki requests.get kodlarına dokunma)
    # Örnek:
    try:
        ajan = requests.get('https://randomuser.me/api/').json()['results'][0]
        # ... diğer api kodların ...
    except:
        ajan = {'name': {'first': 'Bilinmiyor', 'last': ''}, 'location': {'city': 'Yok', 'country': ''}, 'picture': {'large': ''}}

    # ÖNEMLİ: return kısmına "kayitlar=kaydedilen_ajanlar" ekliyoruz
    return render_template('index.html', ajan=ajan, kopek=kopek_resmi, para=btc_fiyat, kayitlar=kaydedilen_ajanlar)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
