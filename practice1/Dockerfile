# ベースイメージとして公式の Python イメージを使用
FROM python:3.10-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコンテナにコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# アプリケーションが使用するポートを公開
EXPOSE 8000

# アプリケーションを起動
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]