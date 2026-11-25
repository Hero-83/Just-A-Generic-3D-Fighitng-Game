const router = require('express').Router();
const repo = require('../datos/repositorio');
const { aprobado, validarEstudiante, resumen } = require('../logica/notas');

function conEstado(estudiante) {
  return { ...estudiante, aprobado: aprobado(estudiante.nota) };
}

router.get('/', (_, res) => res.json(repo.listar().map(conEstado)));
router.get('/resumen', (_, res) => res.json(resumen(repo.listar())));
router.post('/', (req, res) => {
  const error = validarEstudiante(req.body);
  if (error) return res.status(400).json({ error });
  res.status(201).json(conEstado(repo.agregar(req.body)));
});

module.exports = router;
