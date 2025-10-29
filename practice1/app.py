from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import matplotlib
matplotlib.use("Agg")  # 追加

import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from fastapi.responses import StreamingResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ExpressのURL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataModel(BaseModel):
    data: List[float]



@app.post("/analyze")
def analyze_data(data: DataModel):
    numbers = data.data
    mean = np.mean(numbers)
    median = np.median(numbers)
    variance = np.var(numbers)
    std_dev = np.std(numbers)

    return {
        "mean": mean,
        "median": median,
        "variance": variance,
        "std_dev": std_dev
    }

@app.get("/plot")
def plot_data_get(data: str, graph_type: str = "line"):
    try:
        numbers = list(map(float, data.split(',')))
        plt.figure(figsize=(8, 6))
        if graph_type == "line":
            plt.plot(numbers, marker='o', label='Line Graph')
        elif graph_type == "bar":
            plt.bar(range(len(numbers)), numbers, label='Bar Graph')
        elif graph_type == "scatter":
            plt.scatter(range(len(numbers)), numbers, label='Scatter Plot')
        else:
            return {"error": "Invalid graph type"}
        plt.title("Data Visualization")
        plt.xlabel("Index")
        plt.ylabel("Value")
        plt.legend()
        plt.grid()
        buf = BytesIO()
        plt.savefig(buf, format='png')
        plt.close()  # 追加
        buf.seek(0)
        return StreamingResponse(buf, media_type="image/png")
    except Exception as e:
        return {"error": str(e)}
