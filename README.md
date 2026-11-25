# JAG3DFG · Registro de notas del equipo 25493

Este repositorio reúne el videojuego de combate 3D del semestre y la práctica web de Buenas Prácticas de Desarrollo de Software. El registro permite al docente ingresar calificaciones, consultar quién aprobó y ver el promedio del grupo.

## Integrantes

Eissan Charris es el único integrante. Los talleres anteriores documentan su trabajo en el formulario React, la extracción de componentes y el despliegue de la primera API de notas en EC2. Los nuevos commits se registran con la identidad Git configurada, Hero-83.

## Tecnologías

React, Vite, Node.js 24, Express, cors, dotenv y Vitest. El despliegue utilizó Amazon S3 para archivos estáticos y EC2 con systemd para la API. Godot 4 corresponde al videojuego.

## Cómo levantarlo en local

En una terminal, desde la carpeta que contendrá el repositorio:

~~~sh
git clone --branch feature/entrega-equipo25493 https://github.com/Hero-83/Just-A-Generic-3D-Fighitng-Game.git
cd Just-A-Generic-3D-Fighitng-Game/Cosas-que-pidio-el-profe/vite/practica-react
npm ci
npm --prefix api ci
cp .env.example .env
cp api/.env.example api/.env
npm --prefix api start
~~~

En otra terminal, desde practica-react, ejecutar `npm run dev -- --strictPort` y abrir http://localhost:5173. VITE_API_URL indica dónde escucha la API. FRONT_ORIGIN identifica el origen exacto que podrá leer sus respuestas desde el navegador. PORT define el puerto del servidor. Los ejemplos configuran localhost y el puerto 3000. El repositorio de datos es temporal y se vacía al reiniciar el proceso.

## Endpoints de la API

| Método | Ruta | Operación | Respuesta |
|---|---|---|---|
| GET | /estudiantes | Lista los registros con su ID y estado | 200, arreglo |
| POST | /estudiantes | Recibe un nombre y una nota numérica | 201, registro creado. 400, nombre vacío, nota inválida o JSON mal formado |
| GET | /estudiantes/resumen | Total, promedio y cantidad de aprobados | 200, objeto. Promedio nulo con lista vacía |
| GET | /salud | Comprueba el servicio | 200, estado |
| GET | /equipo | Identifica al equipo | 200, equipo e integrantes |
| GET | /notas | Conserva la consulta del corte anterior | 200, promedio y aprobación del promedio |

Ejemplo de cuerpo JSON: `{"nombre":"Ana","nota":3}`. La escala admite valores de 0 a 5. Una nota de 3,0 aprueba. El servidor asigna el ID y calcula el estado. Un cuerpo de más de 16 KiB recibe 413 y una ruta desconocida recibe 404.

## Cómo correr las pruebas

Desde practica-react ejecutar `npm test`. Para repetir al guardar cambios, usar `npm run test:watch`. Las pruebas cubren la frontera de aprobación, los extremos de la escala, registros inválidos y el resumen de grupos vacíos y con datos. La auditoría del 24 de noviembre de 2026 reportó 0 vulnerabilidades tanto en el cliente como en la API (`npm audit` en cada carpeta).

## Despliegue

El [sitio del equipo](http://cuc-bp-equipo25493-sitio-202-elcm.s3-website-us-east-1.amazonaws.com/) publicó el registro de notas. El 24 de noviembre se comprobó su conexión con Express en EC2 y se terminó la instancia tras guardar las evidencias. El equipo utilizó la IPv4 automática. Para repetir el despliegue:

1. En EC2 Linux, instalar Node 24 en el PATH del sistema y copiar la carpeta api a /opt/notas/api. Desde allí ejecutar `npm ci --omit=dev`. Crear .env con PORT=3000 y FRONT_ORIGIN igual al origen HTTP del sitio S3, sin barra final. Usar un usuario de servicio con acceso de lectura a esa carpeta (la unidad incluida usa ec2-user).
2. Instalar notas.service en /etc/systemd/system, ejecutar `sudo systemctl daemon-reload` y `sudo systemctl enable --now notas`. Permitir en el Security Group únicamente TCP 3000 desde los clientes del sitio público. Administrar mediante Session Manager con un rol habilitado en el lab. Mantener SSH cerrado.
3. Abrir http://IP-PUBLICA:3000/salud. En practica-react crear .env.production con VITE_API_URL=http://IP-PUBLICA:3000 y sustituir IP-PUBLICA por la asignada a la instancia. Ejecutar `npm run build`. Subir el contenido de dist al bucket de sitio estático, con index.html en la raíz. Conservar una copia de la web anterior si se reutiliza el bucket.
4. Abrir el endpoint web de S3, registrar una nota y verificar el resumen desde el navegador. Capturar la URL, la respuesta directa de EC2 y las reglas de entrada. Comprobar que el acceso anónimo a un objeto existente del segundo bucket privado devuelve 403.
5. Tras capturar las evidencias, terminar la instancia del ejercicio y liberar la Elastic IP si se reservó una. Conservar las capturas del cierre.

El archivo histórico Cosas-que-pidio-el-profe/index.js corresponde al user data del corte anterior. El servicio actual arranca api/src/servidor.js.

<details>
<summary>Diseño y planificación del videojuego</summary>

# JAG3DFG — Just A Generic 3D Fighting Game

> Juego de combate 3D con sistema híbrido de tiempo real y turnos, inspirado en YOMI HUSTLE pero con mecánicas de RPG.

![Estado](https://img.shields.io/badge/estado-en%20desarrollo-yellow)
![Motor](https://img.shields.io/badge/motor-Godot%204-blue)
![Licencia](https://img.shields.io/badge/licencia-por%20definir-lightgrey)

---

## 📖 Descripción

**JAG3DFG** (*Just A Generic 3D Fighting Game*) es un juego de pelea en 3D
donde cada intercambio importa. Los personajes gestionan **estamina**,
eligen **posturas** y administran **dos barras separadas**: vida y esquive.
Inspirado por sistemas de combate tipo *YOMI HUSTLE*, pero con progresión
de RPG: niveles, prestigios, movimientos especiales y ultis.

El objetivo es un juego donde las decisiones en tiempo real pesan tanto
como la construcción del personaje.

🔗 **Sitio del proyecto:** [cuc-bp-equipo25493-sitio-202-elcm.s3-website-us-east-1.amazonaws.com](http://cuc-bp-equipo25493-sitio-202-elcm.s3-website-us-east-1.amazonaws.com/)

---

## ⚔️ Pilares del combate

### Sistema híbrido tiempo real / turnos
Puedes atacar, moverte y cambiar de postura mientras tengas estamina.
No hay turnos estrictos: la presión la marca el recurso.

### Estamina
- Se regenera pasivamente.
- 100% de regen en reposo.
- 50% mientras atacas o corres.
- 150% si llevas mucho tiempo quieto y sin recibir daño.

### Doble barra: Vida y Esquive
- **Vida:** daño normal.
- **Esquive:** recurso limitado que se gasta para sobrevivir a ataques
  especiales.
- Ninguna de las dos se regenera sola (solo con pasivas o pociones).
- Algunos ataques ignoran una barra y golpean la otra.

### Posturas
- **Bloqueo:** reduce daño, pero empeora contra ataques de agarre insta.
- **Esquive:** bloquea agarres, reduce daño a la barra de esquive.
- Son estados persistentes: se rompen al moverte o atacar.

### Ultis variables
Se cargan sobreviviendo, matando y haciendo daño. Cada personaje las usa
distinto: cambio temporal de movimientos, versión potenciada de un ataque,
o un golpe único devastador.

### Zona que cierra
Los combates no duran para siempre. El **vacío** se cierra con el tiempo
y hace daño creciente hasta matar por contacto.

---

## 👥 Modos de juego (planeados)

| Modo | Descripción |
|------|-------------|
| 1v1 | Duelo clásico |
| 2v2 / 3v3 | Por bandos |
| 1v1v1v1 | Free for all |
| Control asimétrico | Un jugador con varios personajes vs varios jugadores con uno |

---

## 🧠 Sistema de personajes (planeado)

- **Tipos:** Normal, Agua, Fuego, Hielo, Llamas Azules, etc.
- **Estilos:** Callejero, Boxeador, y más (con niveles I, II...).
- **Rareza:** definida por Tipo × Estilo (los personalizados empiezan
  iguales; los predeterminados tienen rareza predefinida).
- **Movimientos:** 1–4 equipables.
- **Pasivas:** 0–3.
- **Ultis:** 0–4 variantes.
- **Pociones:** 3 slots, mejorables a 5.

### Tipos de movimiento
- Parrys
- Agarres insta (ej. Toque de Midas)
- Agarres
- Dashes
- Dashes de agarre
- Invocadores
- Manipulación de entorno
- Construcción de entorno

---

## 📈 Progresión (en diseño)

### Personaje
- Empieza en **nivel 1, prestigio 0**.
- Nivel máximo inicial: 5.
- Cada prestigio sube el cap (+4 niveles).
- Tope: **100 niveles / 25 prestigios**.
- P25 otorga un cosmético de maestría.
- Al prestigiar: reset de puntos de nivel, bonus permanente.

### Jugador (cuenta)
- 100 niveles.
- 100 prestigios (en evaluación).
- Recompensas por hitos.

---

## 🛠️ Stack técnico

- **Motor:** Godot 4
- **Lenguaje:** GDScript
- **Arquitectura de clases:** `Resource` (ClassData) para definir clases
  como datos editables sin tocar código.
- **Web:** `index.html` estático para presentación del proyecto.

---

## 🚧 Estado del proyecto

| Área | Estado |
|------|--------|
| Diseño de combate | ✅ Definido |
| Sistema de stats | ✅ Definido |
| Sistema de clases (Godot) | 🟡 En progreso |
| Movimiento con estamina | ⏳ Pendiente |
| Posturas | ⏳ Pendiente |
| Hitbox / Hurtbox | ⏳ Pendiente |
| Daño dual (vida / esquive) | ⏳ Pendiente |
| Movimientos especiales | ⏳ Pendiente |
| Ultis | ⏳ Pendiente |
| Progresión y prestigios | 🟡 En diseño |
| Rareza y tipos | 🟡 En diseño |
| Interfaz y arte | ⏳ Pendiente |

Leyenda: ✅ hecho · 🟡 en progreso · ⏳ pendiente

---

## 🗺️ Roadmap

1. **Núcleo de combate**
   - Movimiento (caminar, correr, dash) con coste de estamina
   - Regeneración condicional de estamina
   - Posturas (bloqueo / esquive)
   - Hitbox / hurtbox con `DamageData`
   - Ataque básico con startup / active / recovery
   - Daño dual (vida / esquive)

2. **Sistema de personajes**
   - Clases como `Resource`
   - Movimientos equipables
   - Pasivas
   - Ultis

3. **Progresión**
   - Niveles y puntos de stat
   - Prestigios
   - Recompensas

4. **Meta**
   - Rareza de personajes
   - Modos multijugador
   - Zona del vacío

5. **Presentación**
   - UI / HUD
   - Arte y animaciones
   - Web del proyecto

---

## 📁 Estructura del proyecto (planeada)

## Despliegue en AWS

| Integrante | URL del sitio | Bucket publico | Bucket privado |
|---|---|---|---|
| Eissan Charris | http://cuc-bp-equipo25493-sitio-202-elcm.s3-website-us-east-1.amazonaws.com/ | cuc-bp-equipo25493-sitio-202-elcm  | cuc-bp-eq25493-charris-priv-2026 |

Lo pasamos a S3 en vez de a netlify por que el profe lo pidio
</details>
