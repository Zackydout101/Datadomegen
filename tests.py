import tls_client
import datadome
import uuid

# Instore
headers = {
    "cache-control": "no-cache",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"105\", \"Google Chrome\";v=\"105\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "user-agent": "Mozilla/5.0 (Linux; Android 9; K21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "accept": "application/json",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.footlocker.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "X-API-LANG": "en-US",
    "X-API-COUNTRY": "US",
    "X-FLAPI-SESSION-ID": str(uuid.uuid4()),
    "X-FL-REQUEST-ID": str(uuid.uuid4()),
}
session = tls_client.Session(client_identifier="chrome_105")
cookie = datadome.Datadome().generate("https://www.footlocker.com/")["value"]
r = session.get(
    "https://www.footlocker.com/zgw/stores-core/v1/stores-by-availability?siteId=FL&lat=26.296846&long=-80.27754&sku=Q7658101&size=08.5",
    headers=headers,
    cookies={"datadome": cookie})
print(r.status_code)

# Product
headers = {
    "cache-control": "no-cache",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"105\", \"Google Chrome\";v=\"105\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "user-agent": "Mozilla/5.0 (Linux; Android 9; K21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "accept": "application/json",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.footlocker.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "X-API-LANG": "en-US",
    "X-API-COUNTRY": "US",
    "X-FLAPI-SESSION-ID": str(uuid.uuid4()),
    "X-FL-REQUEST-ID": str(uuid.uuid4()),
}
session = tls_client.Session(client_identifier="chrome_105")
cookie = datadome.Datadome().generate("https://www.footlocker.com/")["value"]
r = session.get(
    "https://www.footlocker.com/zgw/product-core/v1/pdp/sku/N8490002",
    headers=headers,
    cookies={"datadome": cookie})
print(r.status_code)

# Add to cart
headers = {
    "cache-control": "no-cache",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"105\", \"Google Chrome\";v=\"105\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "user-agent": "Mozilla/5.0 (Linux; Android 9; K21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "accept": "application/json",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.footlocker.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "X-API-LANG": "en-US",
    "X-API-COUNTRY": "US",
    "X-FLAPI-SESSION-ID": str(uuid.uuid4()),
    "X-FL-REQUEST-ID": str(uuid.uuid4()),
    "x-fl-size": "08.5",
    "x-fl-sku": "ML574RD2"
}
session = tls_client.Session(client_identifier="chrome_105")
cookie = datadome.Datadome().generate("https://www.footlocker.com/")["value"]
r = session.post(
    "https://www.footlocker.com/zgw/carts/co-cart-aggregation-service/site/fl/cart/cartItems/addCartItem",
    headers=headers,
    json={
        "size": "08.5",
        "sku": "ML574RD2",
        "productQuantity": 1,
        "fulfillmentMode": "SHIP",
        "responseFormat": "AllItems"
    },
    cookies={"datadome": cookie})
print(r.status_code)

# https://www.idealista.com/en/
headers = {
    "cache-control": "no-cache",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"105\", \"Google Chrome\";v=\"105\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "user-agent": "Mozilla/5.0 (Linux; Android 9; K21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "accept": "application/json",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.footlocker.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "X-API-LANG": "en-US",
    "X-API-COUNTRY": "US",
    "X-FLAPI-SESSION-ID": str(uuid.uuid4()),
    "X-FL-REQUEST-ID": str(uuid.uuid4()),
}
session = tls_client.Session(client_identifier="chrome_105")
cookie = datadome.Datadome().generate("https://www.idealista.com/en/")["value"]
r = session.get(
    "https://www.idealista.com/en/",
    headers=headers,
    cookies={"datadome": cookie})
print(r.status_code)