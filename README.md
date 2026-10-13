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