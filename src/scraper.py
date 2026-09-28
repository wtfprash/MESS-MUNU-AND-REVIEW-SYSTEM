import requests
from bs4 import BeautifulSoup
from src.constants import TARGET_URL, MEALS, DEFAULT_MENU

def fetch_mess_menu():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        response = requests.get(TARGET_URL, headers=headers, timeout=4)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            scraped_menu = {}
            day_elements = soup.find_all("div", class_="day-block")
            if day_elements:
                for day_elem in day_elements:
                    day_name = day_elem.find("h3").text.strip()
                    scraped_menu[day_name] = {}
                    for meal in MEALS:
                        items = day_elem.find_all("li", class_=meal.lower())
                        scraped_menu[day_name][meal] = [item.text.strip() for item in items]
                return scraped_menu
    except Exception:
        pass
    
    return DEFAULT_MENU
