from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Summary API is running. Try /api/data or /api/summary"}

@app.get("/api/data")
def get_data():
    with open("MData.json", "r") as file:
        data = json.load(file)
    return {"data": data}

@app.get("/api/summary")
def get_summary():
    with open("MData.json", "r") as file:
        data = json.load(file)

    total_events = len(data)
    anomaly_count = sum(1 for item in data if item.get("class") != 0)
    pressure_values = [item.get("P-TPT", 0) for item in data if "P-TPT" in item]

    anomaly_rate = anomaly_count / total_events if total_events else 0
    avg_pressure = sum(pressure_values) / len(pressure_values) if pressure_values else 0

    return {
        "totalEvents": total_events,
        "anomalyRate": round(anomaly_rate, 4),
        "avgPressure": round(avg_pressure, 2)
    }
