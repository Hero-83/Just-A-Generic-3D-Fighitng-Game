const base = import.meta.env.VITE_API_URL?.replace(/\/$/, '');

async function solicitar(ruta, opciones) {
  if (!base) throw new Error('Configura VITE_API_URL para conectar el registro de notas.');
  const respuesta = await fetch(base + ruta, opciones);
  const datos = await respuesta.json();
  if (!respuesta.ok) throw new Error(datos.error || 'No se pudo completar la solicitud.');
  return datos;
}

export const listar = () => solicitar('/estudiantes');
export const obtenerResumen = () => solicitar('/estudiantes/resumen');
export const agregar = estudiante => solicitar('/estudiantes', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(estudiante)
});
