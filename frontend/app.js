const express = require('express');
const app = express();

app.set('view engine', 'ejs');
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.redirect('/home');
});

app.get('/home', (req, res) => {
  res.render('home', { message: null }); // ← dataが未定義の場合に備えて
});

app.post('/home', async (req, res) => {
  const response = await fetch('http://localhost:8000');
  const data = await response.json();
  // 取得したJSONをそのまま返す
  console.log(data);
  const message = data.message; // 例: { "message": "Hello, FastAPI!" }

  res.render('home', { message });
});

app.listen(3000, () => {
  console.log('Server is running on http://localhost:3000');
});