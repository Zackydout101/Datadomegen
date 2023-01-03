import urllib.parse
import tls_client
import json

headers = {
    "cache-control": "no-cache",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"105\", \"Google Chrome\";v=\"105\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "user-agent": "Mozilla/5.0 (Linux; Android 9; K21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "accept": "*/*",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.footlocker.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8"
}


class Datadome:
    def __init__(self):
        self.http_client = tls_client.Session(client_identifier="chrome_105")
        self.endpoint = "https://api-js.datadome.co/js/"
        self.version = "4.6.0"
        self.headers = headers

    def get_cid(self, domain: str) -> str | None:
        self.headers["referer"] = domain
        r = self.http_client.get(domain, headers=self.headers)
        if r.status_code == 200:
            return r.cookies.get("datadome")
        else:
            return None

    def generate(self, domain: str) -> dict | None:
        with open(f"static/[{self.version}].json") as f:
            static = json.loads(f.read())
            domain_p = urllib.parse.urlparse(domain)

            # Get cid
            cid = self.get_cid(domain)
            if cid is None:
                cid = "null"
            print(f"{cid=}")

            # Set dynamic values
            static["Referer"] = urllib.parse.quote(domain)
            static["cid"] = cid
            static["jsData"]["dcok"] = "." + domain_p.hostname.replace("www.", "")
            static["jsData"]["ua"] = self.headers["user-agent"]

            # Get and return cookie
            r = self.http_client.post(self.endpoint, headers=self.headers, data=static)
            if r.status_code == 200:
                cookie = r.json()["cookie"]
                return {
                    "value": cookie.split("=")[1].split(";")[0],
                    "cookie": cookie.split(";")[0] + ";",
                    "raw": cookie
                }
            else:
                return None
