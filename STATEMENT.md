# Problem & Project Statement

## Problem Definition
Students at VIT Bhopal frequently face uncertainty regarding daily mess menu items across different catering vendors (Mayuri, CRCL, Rassense). Existing solutions either lack rating mechanisms to capture real-time student sentiment or suffer from intermittent availability due to web layout changes or anti-scraping policies.

## Project Goal
To develop a resilient desktop application that provides:
1. Dynamic browsing of mess menus filtered by caterer, day, and meal time.
2. A dual-mode menu engine capable of web-scraping live data with an instant, pre-populated local database fallback.
3. A local rating and feedback persistence system to track student satisfaction per meal.

## Scope & Limitations
* **Scope**: Desktop GUI interface (Tkinter), web scraping with BeautifulSoup, local JSON persistence, and unit testing suite.
* **Limitations**: Automated scraping depends on `messmenu.me` DOM consistency. Feedback storage is currently kept local to the user client.
