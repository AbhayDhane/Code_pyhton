import requests
from datetime import datetime

def fetch_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice/INR.json"
    
    try:
        response = requests.get(url)
        data = response.json()

        usd_rate = data['bpi']['USD']['rate']
        inr_rate = data['bpi']['INR']['rate']
        updated_time = data['time']['updated']
        
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n⏰ {now}")
        print(f"📈 Bitcoin Price:")
        print(f"   USD: ${usd_rate}")
        print(f"   INR: ₹{inr_rate}")
        print(f"   (Last Updated: {updated_time})")
        
    except Exception as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    fetch_bitcoin_price()
