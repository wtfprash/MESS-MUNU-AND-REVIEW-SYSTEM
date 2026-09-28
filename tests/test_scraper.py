from src.scraper import fetch_mess_menu
from src.constants import DAYS, MEALS

def test_fetch_mess_menu_structure():
    menu = fetch_mess_menu()
    assert isinstance(menu, dict)
    for day in DAYS:
        assert day in menu
        for meal in MEALS:
            assert meal in menu[day]
            assert isinstance(menu[day][meal], list)
