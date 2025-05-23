FROM python:3.10-slim

# 作業ディレクトリの設定
WORKDIR /app

# 必要なパッケージのインストール
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  build-essential \
  && rm -rf /var/lib/apt/lists/*

# アプリケーションのコードをコピー
COPY ../../source /app

# 依存関係のインストール
RUN pip install --no-cache-dir -r requirements.txt

# 環境変数の設定
ENV PYTHONPATH /src
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPYCACHEPREFIX=/var/cache/python

# ポートの公開
EXPOSE 8501
