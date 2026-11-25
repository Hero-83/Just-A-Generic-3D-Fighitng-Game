const { randomUUID } = require('node:crypto');
const estudiantes = [];

function agregar({ nombre, nota }) {
  const estudiante = { id: randomUUID(), nombre: nombre.trim(), nota };
  estudiantes.push(estudiante);
  return estudiante;
}

module.exports = { agregar, listar: () => estudiantes.slice() };
