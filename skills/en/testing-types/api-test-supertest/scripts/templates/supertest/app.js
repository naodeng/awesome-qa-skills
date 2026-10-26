const crypto = require('crypto');
const express = require('express');

const app = express();
app.use(express.json());

app.get('/health', (req, res) => {
  res.status(200).json({ ok: true, service: 'supertest-template' });
});

app.post('/api/login', (req, res) => {
  const body = req.body || {};
  if (!body.username || !body.password) {
    return res.status(400).json({ code: 'INVALID_INPUT' });
  }
  return res.status(200).json({ token: crypto.randomBytes(16).toString('hex'), user: body.username });
});

module.exports = app;
