import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import concurrent.futures

def fetch_links(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()

        for tag in soup.find_all("a", href=True):
            href = tag['href']
            full_url = urljoin(url, href)
            if urlparse(full_url).scheme in ['http', 'https']:
                links.add(full_url)

        return list(links)
    except Exception as e:
        print(f"❌ Failed to fetch page: {e}")
        return []

def check_link(link):
    try:
        res = requests.head(link, timeout=5)
        return (link, res.status_code)
    except Exception:
        return (link, None)

def main():
    website = input("🔗 Enter website URL: ")
    print(f"🔍 Fetching links from: {website}")

    links = fetch_links(website)
    print(f"🔗 Total links found: {len(links)}\n")

    print("📡 Checking links...\n")
    working, broken = [], []

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(check_link, links)

        for link, status in results:
            if status == 200:
                working.append(link)
                print(f"✅ {link}")
            else:
                broken.append(link)
                print(f"❌ {link} [Status: {status}]")

    print("\n🔎 Summary Report")
    print(f"✅ Working links: {len(working)}")
    print(f"❌ Broken links: {len(broken)}")

if __name__ == "__main__":
    main()
