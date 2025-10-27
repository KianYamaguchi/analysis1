from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
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
def plot_data_get(data: str):
    # クエリパラメータを受け取り、数値リストに変換
    numbers = list(map(float, data.split(',')))

    # グラフを作成
    plt.figure(figsize=(8, 6))
    plt.plot(numbers, marker='o', label='Data Points')
    plt.title("Data Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend()
    plt.grid()

    # 画像をバイナリデータとして返す
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")
