"""
Ranger II — Animaciones
Combos: golpe_fuerte, golpe_ligero (arco der→izq), L_H (lanza al aire), L_L, L_L_H
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
TRONCO = ["Centro Arriba", "Centro Bajo"]

# ─── GOLPE FUERTE: disparo (30f) ──────────────────────────────────
nueva_accion("ranger2_golpe_fuerte", 30)
bpy.context.scene.frame_set(1)
reset_pose()
kf_todos(BRAZOS + TRONCO, 1)

bpy.context.scene.frame_set(8)
r("Hombro Derecho", -20, 0, 0)
r("Hombro Izquierdo", -15, 0, 0)
r("Centro Arriba", 0, -10, 0)
kf_todos(BRAZOS + TRONCO, 8)

bpy.context.scene.frame_set(10)
r("Hombro Derecho", -20, -15, 0)
r("Centro Arriba", 5, -10, 0)
kf_todos(BRAZOS + TRONCO, 10)

bpy.context.scene.frame_set(30)
reset_pose()
kf_todos(BRAZOS + TRONCO, 30)

# ─── GOLPE LIGERO: arco arriba-der → abajo-izq (22f) ──────────────
nueva_accion("ranger2_golpe_ligero", 22)
bpy.context.scene.frame_set(1)
reset_pose()
kf_todos(BRAZOS + TRONCO, 1)

# Pose inicial — arma arriba derecha
bpy.context.scene.frame_set(5)
r("Hombro Derecho", -40, 30, 0)
r("BrazoSupDer", -20, 0, 0)
r("Centro Arriba", -10, 20, 0)
kf_todos(BRAZOS + TRONCO, 5)

# Impacto — abajo izquierda
bpy.context.scene.frame_set(9)
r("Hombro Derecho", 30, -20, 0)
r("BrazoSupDer", 15, 0, 0)
r("Centro Arriba", 15, -20, 0)
kf_todos(BRAZOS + TRONCO, 9)

bpy.context.scene.frame_set(22)
reset_pose()
kf_todos(BRAZOS + TRONCO, 22)

# ─── COMBO L_H: ligero + arco de vuelta lanzando al aire (40f) ────
nueva_accion("ranger2_combo_L_H", 40)
bpy.context.scene.frame_set(1)
reset_pose()
kf_todos(BRAZOS + TRONCO, 1)

# Arco der→izq (igual que ligero)
bpy.context.scene.frame_set(5)
r("Hombro Derecho", -40, 30, 0)
r("Centro Arriba", -10, 20, 0)
kf_todos(BRAZOS + TRONCO, 5)

bpy.context.scene.frame_set(9)
r("Hombro Derecho", 30, -20, 0)
r("Centro Arriba", 15, -20, 0)
kf_todos(BRAZOS + TRONCO, 9)

# Arco de vuelta izq→der más rápido y fuerte (lanzamiento)
bpy.context.scene.frame_set(14)
r("Hombro Derecho", -50, 35, 0)
r("BrazoSupDer", -25, 0, 0)
r("Centro Arriba", -15, 25, 0)
kf_todos(BRAZOS + TRONCO, 14)

# Impacto hacia arriba
bpy.context.scene.frame_set(18)
r("Hombro Derecho", -60, 0, 20)
r("BrazoSupDer", -30, 0, 0)
r("Centro Arriba", -20, 0, 0)
kf_todos(BRAZOS + TRONCO, 18)

bpy.context.scene.frame_set(40)
reset_pose()
kf_todos(BRAZOS + TRONCO, 40)

# ─── COMBO L_L: ligero + arco + vuelve a posición disparo (38f) ───
nueva_accion("ranger2_combo_L_L", 38)
bpy.context.scene.frame_set(1)
reset_pose()
kf_todos(BRAZOS + TRONCO, 1)

bpy.context.scene.frame_set(5)
r("Hombro Derecho", -40, 30, 0)
r("Centro Arriba", -10, 20, 0)
kf_todos(BRAZOS + TRONCO, 5)

bpy.context.scene.frame_set(9)
r("Hombro Derecho", 30, -20, 0)
r("Centro Arriba", 15, -20, 0)
kf_todos(BRAZOS + TRONCO, 9)

# Segundo arco — termina en posición de disparo
bpy.context.scene.frame_set(16)
r("Hombro Derecho", -40, 30, 0)
r("Centro Arriba", -10, 20, 0)
kf_todos(BRAZOS + TRONCO, 16)

bpy.context.scene.frame_set(22)
r("Hombro Derecho", -20, 0, 0)
r("Hombro Izquierdo", -15, 0, 0)
r("Centro Arriba", 0, -10, 0)
kf_todos(BRAZOS + TRONCO, 22)

bpy.context.scene.frame_set(38)
reset_pose()
kf_todos(BRAZOS + TRONCO, 38)

# ─── COMBO L_L_H: L_L + disparo (50f) ────────────────────────────
nueva_accion("ranger2_combo_L_L_H", 50)
bpy.context.scene.frame_set(1)
reset_pose()
kf_todos(BRAZOS + TRONCO, 1)

bpy.context.scene.frame_set(5)
r("Hombro Derecho", -40, 30, 0)
r("Centro Arriba", -10, 20, 0)
kf_todos(BRAZOS + TRONCO, 5)

bpy.context.scene.frame_set(9)
r("Hombro Derecho", 30, -20, 0)
r("Centro Arriba", 15, -20, 0)
kf_todos(BRAZOS + TRONCO, 9)

bpy.context.scene.frame_set(16)
r("Hombro Derecho", -40, 30, 0)
r("Centro Arriba", -10, 20, 0)
kf_todos(BRAZOS + TRONCO, 16)

# Posición disparo
bpy.context.scene.frame_set(22)
r("Hombro Derecho", -20, 0, 0)
r("Hombro Izquierdo", -15, 0, 0)
r("Centro Arriba", 0, -10, 0)
kf_todos(BRAZOS + TRONCO, 22)

# Retroceso disparo
bpy.context.scene.frame_set(30)
r("Hombro Derecho", -20, -15, 0)
r("Centro Arriba", 5, -10, 0)
kf_todos(BRAZOS + TRONCO, 30)

bpy.context.scene.frame_set(50)
reset_pose()
kf_todos(BRAZOS + TRONCO, 50)

print("✓ Ranger II: 5 acciones creadas")
