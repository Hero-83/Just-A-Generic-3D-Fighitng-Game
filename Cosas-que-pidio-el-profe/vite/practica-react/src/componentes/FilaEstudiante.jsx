export default FilaEstudiante;
function FilaEstudiante({ estudiante }) {
  const estado = estudiante.nota >= 3.0 ? 'Aprobado' : 'Reprobado';
  const color = estudiante.nota >= 3.0 ? 'green' : 'red';

  return (
    <tr>
      <td>{estudiante.nombre}</td>
      <td>{estudiante.nota}</td>
      <td style={{ color: color, fontWeight: "bold" }}>{estado}</td>
    </tr>
  );
}