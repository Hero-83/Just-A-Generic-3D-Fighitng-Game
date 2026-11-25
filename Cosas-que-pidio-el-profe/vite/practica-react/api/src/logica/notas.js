const NOTA_MINIMA = 0;
const NOTA_MAXIMA = 5;
const NOTA_APROBATORIA = 3;

function aprobado(nota) {
  return nota >= NOTA_APROBATORIA;
}

function validarEstudiante(datos) {
  if (typeof datos?.nombre !== 'string' || !datos.nombre.trim()) {
    return 'Escribe el nombre del estudiante.';
  }
  if (!Number.isFinite(datos.nota) || datos.nota < NOTA_MINIMA || datos.nota > NOTA_MAXIMA) {
    return `La nota debe ser un número entre ${NOTA_MINIMA} y ${NOTA_MAXIMA}.`;
  }
  return null;
}

function resumen(estudiantes) {
  const total = estudiantes.length;
  const suma = estudiantes.reduce((acumulado, e) => acumulado + e.nota, 0);
  return {
    total,
    promedio: total ? suma / total : null,
    aprobados: estudiantes.filter(e => aprobado(e.nota)).length
  };
}

module.exports = { aprobado, validarEstudiante, resumen };
