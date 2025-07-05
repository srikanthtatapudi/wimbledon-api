from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel

app = FastAPI()

WIMBLEDON_DATA = {
    2021: {
        "champion": "Novak Djokovic",
        "runner_up": "Matteo Berrettini",
        "score": "6–7(4–7), 6–4, 6–4, 6–3",
        "sets": 4,
        "tiebreak": True
    },
    2019: {
        "champion": "Novak Djokovic",
        "runner_up": "Roger Federer",
        "score": "7–6(7–5), 1–6, 7–6(7–4), 4–6, 13–12(7–3)",
        "sets": 5,
        "tiebreak": True
    },
    2018: {
        "champion": "Novak Djokovic",
        "runner_up": "Kevin Anderson",
        "score": "6–2, 6–2, 7–6(7–3)",
        "sets": 3,
        "tiebreak": True
    }
}

class WimbledonFinal(BaseModel):
    year: int
    champion: str
    runner_up: str
    score: str
    sets: int
    tiebreak: bool

@app.get("/wimbledon", response_model=WimbledonFinal)
async def get_wimbledon_final(year: int = Query(..., description="Year of the Wimbledon final", ge=1877)):
    match_data = WIMBLEDON_DATA.get(year)
    if not match_data:
        raise HTTPException(status_code=404, detail=f"Wimbledon final data not found for year {year}")
    return WimbledonFinal(year=year, **match_data)
