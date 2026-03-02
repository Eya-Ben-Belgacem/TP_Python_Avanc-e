import requests
import urllib3
from bs4 import BeautifulSoup

# Désactiver les avertissements SSL (réseau école/université)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# PARTIE 1 : GET Request
url = "http://www.example.com"
response = requests.get(url, verify=False)

print(response)
print(response.status_code)
# PARTIE 2 : POST Request
data = {"name": "Salah", "message": "Hello!"}
url_post = "https://httpbin.org/post"

response_post = requests.post(url_post, json=data)
response_data = response_post.json()
print(response_data)
# PARTIE 3 : Handling Errors
response_err = requests.get("https://httpbin.org/status/404")

if response_err.status_code != 200:
    print(f"HTTP Error: {response_err.status_code}")
# PARTIE 4 : Timeout
url_slow = "https://httpbin.org/delay/10"

try:
    response_timeout = requests.get(url_slow, timeout=5)
except requests.exceptions.Timeout as err:
    print("⏱️ Timeout Error:", err)
# PARTIE 5 : HTTP Headers
auth_token = "XXXXXXXX"

headers = {
    "Authorization": f"Bearer {auth_token}"
}

url_headers = "https://httpbin.org/headers"
response_headers = requests.get(url_headers, headers=headers)
print(response_headers.json())
# PARTIE 6 : Web Scraping
from bs4 import BeautifulSoup

url_scrape = "https://www.example.com"
response_scrape = requests.get(url_scrape, verify=False)
soup = BeautifulSoup(response_scrape.content, "html.parser")

title = soup.title.text
content = soup.find("p").text
links = [a["href"] for a in soup.find_all("a")]

print("Titre :", title)
print(" Contenu :", content)
print(" Liens :", links)
# PARTIE 7 : urllib (comparaison)
import urllib.request
import urllib.parse

# urllib avec GET (example.com n'accepte pas POST)
req = urllib.request.Request("http://example.com")
with urllib.request.urlopen(req) as response:
    html = response.read().decode("utf-8")
print(html[:200])  # affiche les 200 premiers caractères