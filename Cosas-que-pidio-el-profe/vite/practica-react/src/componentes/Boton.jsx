export default Boton;
function Boton({ children, alHacerClic, variante = "primario", cargando = false }) {
  const estilo = {
    backgroundColor: variante === "peligro" ? "#d32f2f" : "#1976d2",
    color: "white",
    padding: "8px 16px",
    border: "none",
    borderRadius: "4px",
    cursor: cargando ? "not-allowed" : "pointer",
    opacity: cargando ? 0.6 : 1
  };

  return (
    <button style={estilo} onClick={alHacerClic} disabled={cargando}>
      {children}
    </button>
  );
}