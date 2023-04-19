# Twitter Bot Detection API
Bu proje; Twitter bot hesaplarını algılayan, FastAPI ve MongoDB kullanılarak oluşturulmuş bir REST API'sidir. Twitter hesaplarını bot olarak sınıflandırmak için önceden eğitilmiş bir makine öğrenimi modeli kullanır.
## API Endpoints
<h3> GET /classify_bots </h3>

<h4> Açıklama:</h4>Twitter hesabının bot olup olmamamısını sınıflandırır.

### Parametereler:

<strong> screen_name:</strong> Twitter hesabının ekran ismi. Gerekli.

<strong> description:</strong> Twitter hesabının açıklaması. Gerekli.

<strong> location:</strong> Twitter hesabının lokasyonu. Opsiyonel.

<strong> verified:</strong> Twitter hesabının doğrulanıp doğrulanmadığı. Gerekli.

<h4> Çevirdiği: </h4>

<p> <strong> is_bot: </strong>Twitter hesabının bot olarak sınıflandırılıp sınıflandırılmadığını gösteren bir boolean değeri.</p>

<h5> Örnek Request: </h5>

```
curl --location --request GET 'http://localhost:8000/classify_bots?screen_name=elonmusk&description=Technoking%20of%20Tesla,%20Imperator%20of%20Mars&location=SpaceX%20Launch%20Pad&verified=true'
```

<h6> Veya projenin içerisindeki client.py ile: </h6>

```
python client.py
```

<h5> Örnek Response: </h5>

```
{
  "is_bot": false
}
```
<h3> GET /bot_ids </h3>

<h4> Açıklama: </h4><p>Veritabanındaki tüm bot sınıflandırma id'lerinin bir listesini alır.</p>

<h4> Çevirdiği: </h4><p>Veritabanındaki bot sınıflandırma id'lerinin bir listesi.</p>

<h5> Örnek Request: </h5>

```
curl --location --request GET 'http://localhost:8000/bot_ids'
```
<h5> Örnek Response: </h5>

```
{
  "ids": [
    "611b461c5d36e5b5f150ed11",
    "611b46215d36e5b5f150ed13"
  ]
}
```
<h3>GET /bot_results/{id}</h3>

<h4> Açıklama: </h4>Spesifik id'nin bot sınıflandırma sonuçlarını gösterir.

### Parametereler:

<strong> id: </strong> Alınacak bot sınıflandırma sonucunun kimliği.

<strong> screen_name:</strong> Twitter hesabının ekran ismi

<strong> description:</strong> Twitter hesabının açıklaması.

<strong> location:</strong> Twitter hesabının lokasyonu.

<strong> verified:</strong> Twitter hesabının doğrulanıp doğrulanmadığı.

<strong> is_bot:</strong> Twitter hesabının bot olarak sınıflandırılıp sınıflandırılmadığını gösteren bir boolean değeri.

<h5> Örnek Request:</h5>

```
curl --location --request GET 'http://localhost:8000/bot_results/611b461c5d36e5b5f150ed11'
```
<h5> Örnek Response:</h5>

```
{
  "id": "611b461c5d36e5b5f150ed11",
  "screen_name": "elonmusk",
  "description": "Doge coin.",
  "location": "USA",
  "verified": true,
  "is_bot": false
}
```
## API'ın Çalıştırılması:
1. Gerekli paketleri yüklemek için şunları çalıştırın: <strong> pip -r requirements.txt. </strong> 
2. Local makinede bir MongoDB server başlatın.
3. API Server'ını terminalde şunu çalıştırarak başlatın: <strong> uvicorn main:app --reload. </strong>
4. Twitter hesaplarının bot olup olmadığını sınıflandırmak için yukarıda belirtilen API endpoint'lerini kullanın.
