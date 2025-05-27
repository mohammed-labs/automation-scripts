import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/dp/B09GFPVD9Y"
headers = {"User-Agent": "Mozilla/5.0"}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

title = soup.select_one('#productTitle').get_text(strip=True)
price = soup.select_one('.a-price-whole').get_text(strip=True)

print(f"{title} → ₹{price}")
