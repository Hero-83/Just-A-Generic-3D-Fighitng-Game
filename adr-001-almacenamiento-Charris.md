# ADR-001: Diseño del almacenamiento del proyecto en Amazon S3

- Fecha: 2026-10-20
- Autor: Michael Ripoll
- Estado: Aceptada

## Contexto
El proyecto **JAG3DFG** (Just A Generic 3D Fighting Game) se encuentra en fase de desarrollo. Necesitamos un lugar centralizado para alojar tanto el sitio web del juego (index.html) como los datos dinámicos generados por los jugadores (perfiles, skins personalizadas, progreso de niveles y telemetría de combate). Al principio, todos los archivos se guardaban en un solo lugar de forma desordenada, lo que generaba problemas de seguridad (cualquiera podía ver datos de otros), riesgos de pérdida de progreso por sobrescrituras accidentales y un aumento constante de los costos de AWS al acumular copias de seguridad sin control. El reto es estructurar un sistema seguro, escalable y rentable.

## Decisión
Se decidió adoptar una arquitectura de **dos buckets separados** con políticas de acceso distintas:
1. **Bucket Público (`cuc-bp-equipo25493-sitio-202-elcm`):** Destinado exclusivamente a los archivos web estáticos (HTML/CSS) y los datos base del juego (stats de personajes). Tiene lectura pública y no requiere versionado.
2. **Bucket Privado (`cuc-bp-eq25493-charris-priv-2026`):** Destinado a los datos sensibles de los usuarios. Se divide en tres prefijos (carpetas): `skins_jugadores/`, `progreso_cuentas/` y `telemetria_combate/`. Se activó el **versionado** para proteger los datos de sobrescrituras. Además, se implementó una **regla de ciclo de vida** (Lifecycle Rule) con los siguientes plazos: a los 30 días los archivos pasan a Standard-IA, a los 90 días a Glacier, y las versiones no vigentes se eliminan a los 30 días.

## Alternativas consideradas
1. **Un solo bucket para todo (público o privado):** Se descartó porque mezclar los archivos del sitio web con los datos privados de los jugadores es un riesgo de seguridad crítico. Si el bucket era público, los perfiles se filtraban; si era privado, el sitio web no cargaba para nadie sin usar credenciales de AWS en el navegador (lo cual es una mala práctica).
2. **No configurar el versionado ni la regla de ciclo de vida:** Se descartó porque un error en el código del juego podría sobrescribir la partida de un jugador con datos vacíos, destruyendo su progreso para siempre. Sin embargo, activar el versionado sin límites dispararía los costos de almacenamiento a largo plazo, por lo que la regla de ciclo de vida se volvió obligatoria.

## Consecuencias
### Positivas
- **Seguridad:** Los datos de los jugadores están aislados y protegidos de accesos no autorizados.
- **Durabilidad:** El versionado permite recuperar el progreso de un jugador si un bug corrompe su archivo actual.
- **Eficiencia de costos:** La regla de ciclo de vida mueve automáticamente los datos inactivos a almacenamiento más barato (Glacier) y elimina la basura acumulada, ahorrando casi un 50% en la factura de AWS a fin de año.

### Costos o desventajas que aceptamos
- Si un jugador estuvo inactivo por más de 90 días (cuyos datos estarán en Glacier), recuperar su cuenta tendrá un pequeño costo de "recuperación" y tardará algunas horas cuando vuelva a iniciar sesión.
- La configuración inicial en la consola de AWS requiere tiempo y conocimiento técnico de políticas IAM.

### Qué habría que revisar más adelante
- Evaluar si a medida que crezca la base de jugadores, conviene automatizar la creación de estos buckets mediante código (Infraestructura como Código) usando Terraform o AWS CDK, en lugar de hacerlo a mano en la consola.
- Revisar en 6 meses si la telemetría de combate (los logs de partidas) realmente necesita estar 90 días en Glacier, o si se puede borrar por completo a los 15 días ya que los datos de balance suelen ser útiles solo a corto plazo.