import { useEffect, useState } from 'react';
import Boton from './componentes/Boton';
import FilaEstudiante from './componentes/FilaEstudiante';
import * as api from './api';

export default function App() {
  const [lista, setLista] = useState([]);
  const [resumen, setResumen] = useState(null);
  const [nombre, setNombre] = useState('');
  const [nota, setNota] = useState('');
  const [error, setError] = useState('');
  const [ocupado, setOcupado] = useState(true);

  async function cargar() {
    setOcupado(true);
    setError('');
    try {
      const [filas, cifras] = await Promise.all([api.listar(), api.obtenerResumen()]);
      setLista(filas);
      setResumen(cifras);
    } catch (err) {
      setError(err.message);
    } finally {
      setOcupado(false);
    }
  }

  useEffect(() => { cargar(); }, []);

  function limpiar() {
    setNombre('');
    setNota('');
  }

  async function guardar(evento) {
    evento.preventDefault();
    setOcupado(true);
    setError('');
    try {
      await api.agregar({ nombre, nota: Number(nota) });
      limpiar();
      await cargar();
    } catch (err) {
      setError(err.message);
      setOcupado(false);
    }
  }

  return (
    <main>
      <h1>Registro de notas</h1>
      <form onSubmit={guardar}>
        <label>Estudiante<input required value={nombre} onChange={e => setNombre(e.target.value)} /></label>
        <label>Nota<input required type="number" step="any" value={nota} onChange={e => setNota(e.target.value)} /></label>
        <Boton tipo="submit" cargando={ocupado}>Agregar estudiante</Boton>
        <Boton alHacerClic={limpiar} cargando={ocupado}>Limpiar campos</Boton>
      </form>
      {error && <p role="alert">{error}</p>}
      <section>
        <h2>Resultados</h2>
        {resumen && <p>{resumen.total} registros · {resumen.aprobados} aprobados · Promedio {resumen.promedio?.toFixed(2) ?? '—'}</p>}
        <table><thead><tr><th>Nombre</th><th>Nota</th><th>Estado</th></tr></thead>
          <tbody>{lista.map(e => <FilaEstudiante key={e.id} estudiante={e} />)}</tbody>
        </table>
        <Boton alHacerClic={cargar} cargando={ocupado}>Actualizar resultados</Boton>
      </section>
    </main>
  );
}
