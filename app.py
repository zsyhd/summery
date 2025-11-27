from fastapi import FastAPI
import json

app = FastAPI()

# Load JSON data once when the API starts
with open("MData.json", "r") as f:
    DATA = json.load(f)  

@app.get("/api/data")
def get_all_data():
    return {"items": DATA}

@app.get("/api/summary")
def get_summary():
    total_events = len(DATA)
    anomaly_rate = sum(1 for row in DATA if row["class"] != 0) / total_events
    avg_pressure = sum(row["P-TPT"] for row in DATA) / total_events

    return {
        "totalEvents": total_events,
        "anomalyRate": anomaly_rate,
        "avgPressure": avg_pressure
    }
print(">>> THIS IS THE CORRECT APP.PY <<<")
