import { useState } from 'react';
import Boton from './componentes/Boton';
import FilaEstudiante from './componentes/FilaEstudiante';

export default function App() {
  const [estudiantes, setEstudiantes] = useState([]);
  const [nombreInput, setNombreInput] = useState('');
  const [notaInput, setNotaInput] = useState('');
  const [cargando, setCargando] = useState(false);
  const [error, setError] = useState('');

  function agregar() {
    if (nombreInput.trim() === '') {
      setError('Se debe insertar el nombre del estudiante.');
      return;
    }
    if (notaInput === '') {
      setError('Se debe insertar la nota del estudiante.');
      return;
    }
    const notaNumero = parseFloat(notaInput);
    if (notaNumero < 0 || notaNumero > 5) {
      setError('La nota debe estar entre 0 y 5.');
      return;
    }
    setError(''); 
    
    const nuevo = { 
      id: Date.now(), 
      nombre: nombreInput.trim(),
      nota: notaNumero 
    };
    
    setEstudiantes([...estudiantes, nuevo]);
    setNombreInput('');
    setNotaInput('');
  }
  return (
    <>
      <h1>Notas</h1>
      
      <table border="1" cellPadding="10" style={{ borderCollapse: 'collapse', marginBottom: '20px' }}>
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Nota</th>
            <th>Estado</th>
          </tr>
        </thead>
        <tbody>
          {estudiantes.map(e => (
            <FilaEstudiante key={e.id} estudiante={e} />
          ))}
        </tbody>
      </table>

      <div style={{ marginBottom: '20px' }}>
        <input 
          type="text" 
          placeholder="Nombre del estudiante" 
          value={nombreInput} 
          onChange={(e) => setNombreInput(e.target.value)} 
          style={{ marginRight: '10px' }}
        />
        <input 
          type="number" 
          placeholder="Nota" 
          value={notaInput} 
          onChange={(e) => setNotaInput(e.target.value)} 
        />
      </div>

      {error && <p style={{ color: 'red', fontWeight: 'bold' }}>{error}</p>}

      <Boton 
        alHacerClic={agregar} 
        variante="primario"
      >
        Agregar estudiante
      </Boton>
    </>
  );
}