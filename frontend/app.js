const express = require('express'); // 必要ならインストール: npm install node-fetch
const app = express();

app.set('view engine', 'ejs');
app.use(express.urlencoded({ extended: true }));

// GETメソッド: フォームを表示
app.get('/home', (req, res) => {
  res.render('home', { message: null, imageUrl: null });
});

// POSTメソッド: FastAPIにデータを送信して結果を取得
app.post('/home', async (req, res) => {
  const inputData = req.body.data; // ユーザーが入力したデータ
  try {
    // FastAPIの /analyze エンドポイントにリクエストを送信
    const analyzeResponse = await fetch('http://localhost:8000/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ data: inputData.split(',').map(Number) }) // 数値配列を送信
    });
    if (!analyzeResponse.ok) {
      throw new Error('Failed to fetch analysis data');
    }
    const result = await analyzeResponse.json();
    const imageUrl = `http://localhost:8000/plot?data=${inputData}`;

    // 結果をテンプレートに渡す
    res.render('home', {
      message: `平均: ${result.mean}, 中央値: ${result.median}, 分散: ${result.variance}, 標準偏差: ${result.std_dev}`,
      imageUrl: imageUrl
    });
  } catch (error) {
    console.error(error);
    res.render('home', { message: 'エラーが発生しました。', imageUrl: null });
  }
});

app.listen(3000, () => {
  console.log('Server is running on http://localhost:3000');
});