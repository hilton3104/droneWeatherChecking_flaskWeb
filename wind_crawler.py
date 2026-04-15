import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

def get_hko_wind_data():
    url = "https://www.hko.gov.hk/textonly/v2/forecast/text_readings_c.htm"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    print("Try to fetch data from HKO...")
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'

    if response.status_code != 200:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return {}
    
    print("Data fetched successfully!")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    pre_tag = soup.find('pre')
    if not pre_tag:
        print("Can't find <pre> tag.")
        return {}
    
    text_content = pre_tag.get_text()
    pattern = r'^([\u4e00-\u9fff]+(?:\s+[\u4e00-\u9fff]+)?)\s+(東|南|西|北|東南|東北|西南|西北|風向不定|N/A|無風)\s+(\d+(?:\.\d+)?)'
    
    wind_data = {}
    for line in text_content.split('\n'):
        line = line.strip()
        if not line:
            continue
            
        match = re.match(pattern, line)
        if match:
            place_raw = match.group(1).strip()
            place = re.sub(r'\s+', '', place_raw)
            wind_speed_str = match.group(2)
            if wind_speed_str == "無風":
                wind_speed = 0.0
            else:
                wind_speed = float(match.group(3))
            
            # Filter out unrealistic wind speeds and ensure place name is valid
            if len(place) > 1 and  0 <= wind_speed < 200:
                wind_data[place] = wind_speed
    
    return wind_data

if __name__ == "__main__":
    wind_data = get_hko_wind_data()
    if wind_data:
        print(f"\n Successfully fetched wind data for {len(wind_data)} locations:")
        for i, (place, speed) in enumerate(wind_data.items()):
            print(f"  {place}: {speed} km/h")