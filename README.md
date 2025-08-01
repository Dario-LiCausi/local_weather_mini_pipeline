# Local Weather Mini Pipeline

A modular weather ETL app that fetches 7-day forecast data from the [Open-Meteo API](https://open-meteo.com), processes it, and returns a clean, enriched DataFrame ready to be explored or saved. You run it from the terminal, it grabs your location automatically, pulls the data, cleans it, and tells you what's coming: clear skies or storms.

---

## What It Does

- Automatically detects user location via IP (no manual input required)
- Connects to Open-Meteo API and fetches raw forecast data
- Transforms and flattens the JSON into a pandas DataFrame
- Rounds values, renames columns, classifies precipitation (Clear, Light Rain, Rain, Storm)
- Enriches data with location name and load date
- Prints a summary directly in terminal
- Structured in a clean ETL logic: Extract → Transform → (Load coming soon)

---

## What’s Done vs To Do

### Done
- [x] Extract from API using dynamic user location
- [x] Transform raw JSON into structured DataFrame
- [x] Precipitation classification logic
- [x] Location enrichment using reverse geocoding
- [x] Terminal summary output
- [x] Modular class structure for reusability and testing

### To Do
- [ ] Let user pick predefined locations (e.g., Milan, NYC, São Paulo)
- [ ] Add "Load" phase — export to `.csv` or `.parquet`
- [ ] Write unit tests (pytest)
- [ ] Save raw JSON for auditing
- [ ] Visual dashboard with Streamlit or similar

---

## Stack

| Tool        | Purpose                           |
|-------------|-----------------------------------|
| Python      | Core logic                        |
| requests    | Hitting Open-Meteo API            |
| geocoder    | Getting user IP and reverse geocoding |
| pandas      | Data wrangling                    |
| json        | Parsing API response              |

---

## Project Layout

```
local_weather_mini_pipeline/
├── src/
│   ├── app.py                # Menu CLI controller
│   └── ETL/
│       ├── extract.py        # API + geolocation
│       └── transform.py      # Cleans and enriches data
├── data/
│   ├── raw_weather_data.json (optional if you choose to save)
│   └── processed/            # To be used for saved output
└── README.md
```

---

## In Progress

This is part of my portfolio as a junior data engineer, feel free to follow the commits as I complete the pipeline and add new features. The goal is to simulate a real world data flow with minimal overhead and solid modular structure.
