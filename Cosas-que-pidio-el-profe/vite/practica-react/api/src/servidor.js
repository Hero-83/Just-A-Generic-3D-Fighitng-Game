require('dotenv').config({ quiet: true });
const express = require('express');
const cors = require('cors');
const estudiantes = require('./rutas/estudiantes');
const repo = require('./datos/repositorio');
const { aprobado, resumen } = require('./logica/notas');

const origen = process.env.FRONT_ORIGIN;
if (!origen || new URL(origen).origin !== origen) {
  throw new Error('Configura FRONT_ORIGIN con el origen exacto del front, sin barra final.');
}
const app = express();
app.use(cors({ origin: origen }));
app.use(express.json({ limit: '16kb' }));
app.use('/estudiantes', estudiantes);
app.get('/salud', (_, res) => res.json({ estado: 'ok' }));
app.get('/equipo', (_, res) => res.json({ equipo: 'Equipo 25493', integrantes: ['Eissan Charris'] }));
app.get('/notas', (_, res) => {
  const { promedio } = resumen(repo.listar());
  res.json({ promedio, aprobado: promedio !== null && aprobado(promedio) });
});
app.use((_, res) => res.status(404).json({ error: 'Ruta no encontrada.' }));
app.use((err, req, res, siguiente) => {
  if (res.headersSent) return siguiente(err);
  if (err.type === 'entity.parse.failed') return res.status(400).json({ error: 'El JSON es inválido.' });
  if (err.type === 'entity.too.large') return res.status(413).json({ error: 'El cuerpo supera el límite.' });
  res.status(500).json({ error: 'Error interno.' });
});
app.listen(process.env.PORT || 3000);
