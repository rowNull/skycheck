<!-- @format -->

# Project Phases & Sprints — SkyCheck: Weather App

---

## Overview

**Goal:** Build and deploy a Python-based weather app that fetches real-time data from the OpenWeather API. User types any city name and gets temperature, humidity, and sky conditions in under 2 seconds.

**Target Completion:** 7 Days (1 Week)
**Stack:** Python, OpenWeather API (REST), CLI or simple web UI (Flask or Tkinter)

---

## Phase 1 — Project Setup & Foundation
**Day 1 Morning**

**Goal:** Establish the codebase, tooling, API access, and project structure before writing any feature code.

### Sprint 1.1 — Repository & Tooling

- **Create GitHub repo** with `main` and `dev` branches
- Add `.gitignore` (Python template), `LICENSE`, `README.md`
- Set up virtual environment:
  ```
  python -m venv venv
  source venv/bin/activate
  ```
- Create folder layout:
  ```
  /skycheck
    main.py
    weather.py
    config.py
    utils.py
  /tests
  .env.example
  requirements.txt
  ```
- Add `.env.example` with:
  ```
  OPENWEATHER_API_KEY=your_key_here
  ```
- Document run instructions in README

**Important:** Never commit your real API key. Always use `.env` and add it to `.gitignore`.

---

### Sprint 1.2 — API Account & Key Setup

- Sign up at [openweathermap.org](https://openweathermap.org)
- Generate a free API key
- Confirm key is active (can take up to 2 hours)
- Test key manually in browser:
  ```
  https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_KEY&units=imperial
  ```
- Store key in `.env` file locally
- Install dependencies:
  ```
  pip install requests python-dotenv
  pip freeze > requirements.txt
  ```

**Important:** Free tier allows 60 calls/minute — more than enough for this project.

---

## Phase 2 — Core API Integration
**Day 1 Afternoon – Day 2**

**Goal:** Write the core logic that fetches weather data from OpenWeather and returns clean, usable data.

### Sprint 2.1 — Weather Fetch Function

- Create `weather.py` with a `get_weather(city)` function
- Call `GET https://api.openweathermap.org/data/2.5/weather`
  - Params: `q={city}`, `appid={key}`, `units=imperial`
- Parse and return:
  - `temperature` (°F)
  - `humidity` (%)
  - `description` (e.g. "clear sky", "light rain")
  - `city_name`
  - `country_code`
- Handle HTTP errors (401 unauthorized, 404 city not found)
- Return `None` or raise custom exception on failure

**Important:** Confirm raw API response structure in browser before writing parse logic.

---

### Sprint 2.2 — Config & Environment Setup

- Create `config.py` to load env variables:
  ```python
  from dotenv import load_dotenv
  import os
  load_dotenv()
  API_KEY = os.getenv("OPENWEATHER_API_KEY")
  BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
  ```
- Import config into `weather.py` — no hardcoded keys anywhere
- Add basic input sanitization in `utils.py`:
  - Strip whitespace from city name
  - Capitalize city for display

**Important:** All secrets must come from environment — never from code.

---

### Sprint 2.3 — Error Handling

- Handle the following cases gracefully:
  - City not found (404) → print "City not found. Please check spelling."
  - Invalid API key (401) → print "API key error. Check your .env file."
  - No internet / timeout → print "Connection error. Please check your network."
  - Empty input → prompt user to enter a city name
- Log errors to console with clear messages (no stack traces shown to user)

**Important:** App should never crash on bad input — always recover gracefully.

---

## Phase 3 — User Interface
**Day 3**

**Goal:** Build the user-facing interface. Choose ONE of the two options below based on what you want to showcase on your portfolio.

### Sprint 3.1 — CLI Interface (Option A — Simpler, Faster)

- Build interactive CLI in `main.py`:
  ```
  Welcome to SkyCheck 🌤️
  Enter a city name: San Francisco
  
  📍 San Francisco, US
  🌡️  Temperature: 62°F
  💧 Humidity: 74%
  ☁️  Conditions: Overcast clouds
  ```
- Loop: after showing results, ask "Search another city? (y/n)"
- Exit cleanly on "n" or Ctrl+C
- Add color output using `colorama` library

**Important:** CLI is faster to build and still demonstrates real API + Python skills clearly.

---

### Sprint 3.2 — Web UI with Flask (Option B — Better Portfolio Piece)

- Install Flask: `pip install flask`
- Create `app.py` with two routes:
  - `GET /` → renders search form
  - `POST /weather` → accepts city, calls `get_weather()`, renders result
- Create `/templates/index.html`:
  - Simple search form (city input + submit button)
  - Display result card: city, temp, humidity, conditions, weather icon
- Create `/static/style.css`:
  - Clean, minimal design matching the SkyCheck card aesthetic
  - Mobile responsive
- Use OpenWeather icon URLs for weather condition icons:
  ```
  https://openweathermap.org/img/wn/{icon}@2x.png
  ```

**Important:** Flask Option B takes ~1 extra day but looks significantly better on your portfolio. Recommended.

---

## Phase 4 — Testing
**Day 4**

**Goal:** Write basic tests to validate the app works correctly and handles edge cases.

### Sprint 4.1 — Unit Tests

- Create `tests/test_weather.py`
- Write tests for:
  - Valid city returns correct data structure
  - Invalid city returns `None` or raises expected exception
  - Empty city input is caught before API call
  - Temperature is a number, humidity is 0–100
- Run tests:
  ```
  python -m pytest tests/
  ```

**Important:** Even 4–5 basic tests demonstrate professional habits that most intern applicants skip entirely — this is a differentiator.

---

### Sprint 4.2 — Manual QA

- Test with a variety of city inputs:
  - Common city: "New York"
  - City with spaces: "Los Angeles"
  - City with accents: "São Paulo"
  - Misspelled city: "Nwe York"
  - Empty string: ""
  - Numbers only: "12345"
- Confirm all error messages display correctly
- Confirm results display in under 2 seconds

**Important:** Document any edge case bugs found and fix before moving to deployment.

---

## Phase 5 — Deployment
**Day 5**

**Goal:** Deploy the app so it is publicly accessible and linkable from the portfolio.

### Sprint 5.1 — Prepare for Deployment

- Create `Procfile` (for Railway or Render):
  ```
  web: python app.py
  ```
- Update `app.py` to use dynamic port:
  ```python
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port)
  ```
- Add all dependencies to `requirements.txt`
- Test app runs correctly locally before deploying

**Important:** App must run clean locally before attempting deployment.

---

### Sprint 5.2 — Deploy to Railway or Render

- **Option A — Railway** (already familiar from sasaeyebrowsthreading project):
  - Create new Railway project
  - Link GitHub repo
  - Add `OPENWEATHER_API_KEY` as environment variable in Railway dashboard
  - Deploy and confirm live URL works

- **Option B — Render** (free tier, no credit card):
  - Create account at render.com
  - New Web Service → connect GitHub repo
  - Add environment variable for API key
  - Deploy and confirm live URL

**Important:** Never add API key to code — always use platform environment variables.

---

### Sprint 5.3 — Confirm Live Deployment

- Test live URL with multiple cities
- Confirm error states work on live version
- Check page load speed (target: under 2 seconds)
- Share live URL with yourself and test on mobile

**Important:** Get the live URL — you need it for your portfolio and resume.

---

## Phase 6 — Portfolio & Resume Integration
**Day 6**

**Goal:** Make this project visible and compelling to recruiters.

### Sprint 6.1 — Polish README

- Update `README.md` to include:
  - Project description (1–2 sentences)
  - Live demo link
  - Screenshot or GIF of the app in action
  - Tech stack list
  - Local setup instructions:
    ```
    git clone https://github.com/rowNull/skycheck
    cd skycheck
    pip install -r requirements.txt
    cp .env.example .env  # add your API key
    python app.py
    ```
  - API reference link (OpenWeather)

**Important:** A good README is the difference between a recruiter clicking your GitHub link and closing it immediately.

---

### Sprint 6.2 — Add to Portfolio Website

- Add SkyCheck to `rownull.github.io/portfolio`
- Project card should include:
  - Screenshot of the weather result UI
  - Title: "SkyCheck — Real-Time Weather App"
  - Description: "Python + Flask app using OpenWeather REST API. Returns temperature, humidity, and sky conditions for any city in under 2 seconds."
  - Tech tags: Python, Flask, REST API, OpenWeather
  - Links: Live Demo + GitHub

**Important:** This project directly addresses the REST API gap on your resume. Make sure it is prominently featured.

---

### Sprint 6.3 — Update Resume

- Add SkyCheck to the Projects section:
  ```
  SkyCheck — Weather App (Python, Flask, REST API)
  • Built and deployed a real-time weather app using Python and Flask
  • Integrated OpenWeather REST API to fetch live temperature, humidity, and sky conditions
  • Implemented error handling for invalid cities, network failures, and API errors
  • Deployed on Railway with environment-based API key management
  ```
- Add Python and Flask to Technical Skills → Languages and Frameworks sections

**Important:** This single project adds Python, Flask, and REST API (proven) to your resume — three major skill gaps addressed at once.

---

## Phase 7 — Optional Enhancements
**Day 7 (if time allows)**

**Goal:** Add quality-of-life features that make the project stand out further.

### Sprint 7.1 — 5-Day Forecast

- Add second API call to `/forecast` endpoint
- Display next 5 days with high/low temps and conditions

### Sprint 7.2 — Unit Toggle

- Add toggle button for °F / °C
- Store preference in session

### Sprint 7.3 — Search History

- Store last 5 searched cities in session
- Display as quick-access buttons below search bar

**Important:** These do not block core functionality or deployment. Only pursue if Days 1–6 are complete and solid.

---

## Day-by-Day Summary

| Day | Focus | Done When |
|-----|-------|-----------|
| Day 1 | Setup, API key, fetch function | API returns weather data in terminal |
| Day 2 | Error handling, config, utils | App handles bad inputs gracefully |
| Day 3 | Flask UI (or CLI) | User can search a city and see results |
| Day 4 | Testing, manual QA | Tests pass, edge cases handled |
| Day 5 | Deployment | Live URL accessible publicly |
| Day 6 | README, portfolio, resume update | Project visible on portfolio + resume updated |
| Day 7 | Optional enhancements | Forecast, toggle, or history feature |

---

## End of Document
