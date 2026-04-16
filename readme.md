# Drone Safety Cheaking System

A full-stack web application that helps drone pilots assess flight safety based on real-time weather conditions in Hong Kong. The system integrates **Hong Kong Observatory (HKO) Open Data API** and **web scraping** to provide location-specific wind speed, temperature, rainfall, and daytime/nighttime information.

## Features

- **Real-time Temperature** - Retrieved from HKO Open Data API
- **10 mins mean wind speed** - Extracted from HKO text-only page via web scraping
- **Rainfall Detection** - Checks whether rain is recorded in the selected district
- **Daytime / Nighttime Checking** - Uses sunrise/sunset data to restrict flying after dark
- **Safety Message** - Combines wind speed, rainfall, and daytime into clear safety messages

## Run the app

### 1. Clone the repository
```bash
git clone https://github.com/hilton3104/droneWeatherChecking_flaskWeb.git
cd droneWeatherChecking_flaskWeb
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
# or
venv\Scripts\activate   # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

### 5. Open in browser
Visit http://127.0.0.1:5000

### 6. Stop the server and deactivate virtual environment
- To stop the Flask development server, press **`Ctrl + C`** in the terminal.
- To deactivate the virtual environment, simply run:

```bash
deactivate
```

## How to use
1. Select a location (e.g., 京士柏, 西貢, 大美督)
2. Click "查詢天氣狀況" button
3. The system display:
    - Temperature (°C)
    - Wind Speed (km/h)
    - Current Time (HH/MM)
    - Rainfall Status (Yes/No)
    - Safety Message

## Safety Logic
| Condition | Recommendation |
| ----- | ----- |
| Wind Speed < 15km/h, no rain, daytime | Safe to fly |
| Wind Speed 15 - 30km/h, no rain, daytime | Fly with caution |
| Wind Speed >= 30km/h, or rain, or nighttime | Not safe to fly |

## Notes
- **Data Source:** All weather data (temperature, wind speed, rainfall, sunrise/sunset time) are provided by the **Hong Kong Observatory (HKO)**. This project is for **educational purpose only**.
- **No Guarantee:** This system works as of the development date (**April 2026**). However, HKO may update its website structure or API endpoints at any time, which could break the web scraping or API calls. **Long-term functionality is not guaranteed.**
- **For Reference Only:** The flight safety recommendations are based on simplified rules (wind < 15 km/h, no rain, daytime). Real drone operations must always follow **official regulations**, manufacturer guidelines, and on-site risk assessments.