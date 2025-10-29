# ベースイメージとして公式の Node.js イメージを使用
FROM node:16

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# package.json と package-lock.json をコピー
COPY package*.json ./

# 必要な依存関係をインストール
RUN npm install

# アプリケーションのソースコードをコピー
COPY . .

# アプリケーションが使用するポートを公開
EXPOSE 3000

# デフォルトのコマンドを設定（開発用に nodemon を使用）
CMD ["npm", "run", "dev"]