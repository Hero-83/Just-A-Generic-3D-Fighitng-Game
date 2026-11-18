"""
Ranger I — Animaciones
Ejecutar desde Base.blend en la pestaña Scripting.
Combos: golpe_ligero (culatazo), golpe_fuerte (disparo), combo_L_H
"""
import bpy
from math import radians

arm = bpy.data.objects["Esqueleto"]
bpy.context.view_layer.objects.active = arm
arm.select_set(True)
bpy.ops.object.mode_set(mode='POSE')

def r(bone, x, y, z):
    b = arm.pose.bones[bone]
    b.rotation_mode = 'XYZ'
    b.rotation_euler = (radians(x), radians(y), radians(z))

def kf(bone, frame):
    arm.pose.bones[bone].keyframe_insert("rotation_euler", frame=frame)

def kf_todos(bones, frame):
    for b in bones: kf(b, frame)

def reset_pose():
    bpy.ops.pose.select_all(action='SELECT')
    bpy.ops.pose.rot_clear()

def nueva_accion(nombre, total_frames):
    if nombre in bpy.data.actions:
        bpy.data.actions.remove(bpy.data.actions[nombre])
    ac = bpy.data.actions.new(nombre)
    arm.animation_data_create()
    arm.animation_data.action = ac
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = total_frames
    return ac

BRAZOS = ["Hombro Derecho", "BrazoSupDer", "BrazoInfDer",
          "Hombro Izquierdo", "BrazoSupIzq", "BrazoInfIzq"]

# ─── GOLPE LIGERO: culatazo (20 frames) ───────────────────────────
# startup 1-5, activo 6-8, recovery 9-20
nueva_accion("ranger1_golpe_ligero", 20)
bpy.context.scene.frame_set(1)
reset_pose()
kf_todos(BRAZOS, 1)

# Carga hacia atrás
bpy.context.scene.frame_set(5)
r("Hombro Derecho", 0, -30, 0)
r("BrazoSupDer", 20, 0, 0)
kf_todos(BRAZOS, 5)

# Impacto — empuja el arma hacia adelante
bpy.context.scene.frame_set(7)
r("Hombro Derecho", 0, 40, 0)
r("BrazoSupDer", -10, 0, 0)
r("Centro Arriba", 0, 15, 0)
kf_todos(BRAZOS + ["Centro Arriba"], 7)

# Recovery — vuelve a neutral
bpy.context.scene.frame_set(20)
reset_pose()
kf_todos(BRAZOS + ["Centro Arriba"], 20)

# ─── GOLPE FUERTE: disparo (30 frames) ────────────────────────────
# startup 1-8, activo 9-11 (flash), recovery 12-30
nueva_accion("ranger1_golpe_fuerte", 30)
bpy.context.scene.frame_set(1)
reset_pose()
kf_todos(BRAZOS, 1)

# Apunta
bpy.context.scene.frame_set(8)
r("Hombro Derecho", -20, 0, 0)
r("BrazoSupDer", -10, 0, 0)
r("Hombro Izquierdo", -15, 0, 0)
r("Centro Arriba", 0, -10, 0)
kf_todos(BRAZOS + ["Centro Arriba"], 8)

# Retroceso del disparo
bpy.context.scene.frame_set(10)
r("Hombro Derecho", -20, -15, 0)
r("Centro Arriba", 5, -10, 0)
kf_todos(BRAZOS + ["Centro Arriba"], 10)

# Recovery
bpy.context.scene.frame_set(30)
reset_pose()
kf_todos(BRAZOS + ["Centro Arriba"], 30)

# ─── COMBO L+H: culatazo → disparo (40 frames) ────────────────────
nueva_accion("ranger1_combo_L_H", 40)
bpy.context.scene.frame_set(1)
reset_pose()
kf_todos(BRAZOS + ["Centro Arriba"], 1)

# Carga culatazo
bpy.context.scene.frame_set(5)
r("Hombro Derecho", 0, -30, 0)
r("BrazoSupDer", 20, 0, 0)
kf_todos(BRAZOS, 5)

# Impacto culatazo
bpy.context.scene.frame_set(7)
r("Hombro Derecho", 0, 40, 0)
r("Centro Arriba", 0, 15, 0)
kf_todos(BRAZOS + ["Centro Arriba"], 7)

# Transición — retrocede para aprovechar distancia
bpy.context.scene.frame_set(14)
r("Hombro Derecho", -20, 0, 0)
r("Hombro Izquierdo", -15, 0, 0)
r("Centro Arriba", 0, -10, 0)
kf_todos(BRAZOS + ["Centro Arriba"], 14)

# Disparo
bpy.context.scene.frame_set(22)
r("Hombro Derecho", -20, -15, 0)
r("Centro Arriba", 5, -10, 0)
kf_todos(BRAZOS + ["Centro Arriba"], 22)

# Recovery
bpy.context.scene.frame_set(40)
reset_pose()
kf_todos(BRAZOS + ["Centro Arriba"], 40)

print("✓ Ranger I: 3 acciones creadas")
