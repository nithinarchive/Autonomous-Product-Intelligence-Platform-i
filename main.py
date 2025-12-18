from fastapi import FastAPI
from services import get_insights

app = FastAPI(title="Autonomous Product Intelligence API")

@app.get("/insights")
def insights():
    return get_insights()
