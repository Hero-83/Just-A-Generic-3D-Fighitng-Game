"""
Ranger Elite — Animaciones
Todos los combos de Ranger III + L_L_L (patada para reposicionar) y L_L_L_H.
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
PIERNA_DER = ["PelvizDer", "PiernaSupDer", "PiernaInfDer"]

# ─── GOLPE FUERTE (32f) — igual que III ───────────────────────────
nueva_accion("elite_golpe_fuerte", 32)
bpy.context.scene.frame_set(1)
reset_pose()
kf_todos(BRAZOS + TRONCO, 1)

bpy.context.scene.frame_set(4)
r("Centro Arriba", -5, -5, 0)
kf_todos(TRONCO, 4)

bpy.context.scene.frame_set(10)
r("Hombro Derecho", -20, 0, 0)
r("Hombro Izquierdo", -15, 0, 0)
r("Centro Arriba", 0, -12, 0)
kf_todos(BRAZOS + TRONCO, 10)

bpy.context.scene.frame_set(12)
r("Hombro Derecho", -20, -18, 0)
r("Centro Arriba", 6, -12, 0)
kf_todos(BRAZOS + TRONCO, 12)

bpy.context.scene.frame_set(32)
reset_pose()
kf_todos(BRAZOS + TRONCO, 32)

# ─── GOLPE LIGERO (26f) — igual que III ───────────────────────────
nueva_accion("elite_golpe_ligero", 26)
bpy.context.scene.frame_set(1)
reset_pose()
kf_todos(BRAZOS + TRONCO, 1)

bpy.context.scene.frame_set(3)
r("Hombro Derecho", -10, -10, 0)
r("Centro Arriba", 5, -10, 0)
kf_todos(BRAZOS + TRONCO, 3)

bpy.context.scene.frame_set(7)
r("Hombro Derecho", -45, 35, 0)
r("BrazoSupDer", -22, 0, 0)
r("Centro Arriba", -12, 22, 0)
kf_todos(BRAZOS + TRONCO, 7)

bpy.context.scene.frame_set(11)
r("Hombro Derecho", 32, -22, 0)
r("BrazoSupDer", 16, 0, 0)
r("Centro Arriba", 16, -22, 0)
kf_todos(BRAZOS + TRONCO, 11)

bpy.context.scene.frame_set(26)
reset_pose()
kf_todos(BRAZOS + TRONCO, 26)

# ─── COMBO L_H (44f) — igual que III ─────────────────────────────
nueva_accion("elite_combo_L_H", 44)
bpy.context.scene.frame_set(1)
reset_pose()
kf_todos(BRAZOS + TRONCO, 1)

bpy.context.scene.frame_set(3)
r("Hombro Derecho", -10, -10, 0)
r("Centro Arriba", 5, -10, 0)
kf_todos(BRAZOS + TRONCO, 3)

bpy.context.scene.frame_set(7)
r("Hombro Derecho", -45, 35, 0)
r("Centro Arriba", -12, 22, 0)
kf_todos(BRAZOS + TRONCO, 7)

bpy.context.scene.frame_set(11)
r("Hombro Derecho", 32, -22, 0)
r("Centro Arriba", 16, -22, 0)
kf_todos(BRAZOS + TRONCO, 11)

bpy.context.scene.frame_set(16)
r("Hombro Derecho", -55, 38, 0)
r("BrazoSupDer", -28, 0, 0)
r("Centro Arriba", -18, 28, 0)
kf_todos(BRAZOS + TRONCO, 16)

bpy.context.scene.frame_set(20)
r("Hombro Derecho", -65, 0, 22)
r("BrazoSupDer", -32, 0, 0)
r("Centro Arriba", -22, 0, 0)
kf_todos(BRAZOS + TRONCO, 20)

bpy.context.scene.frame_set(44)
reset_pose()
kf_todos(BRAZOS + TRONCO, 44)

# ─── COMBO L_L (42f) — igual que III ─────────────────────────────
nueva_accion("elite_combo_L_L", 42)
bpy.context.scene.frame_set(1)
reset_pose()
kf_todos(BRAZOS + TRONCO, 1)

bpy.context.scene.frame_set(3)
r("Hombro Derecho", -10, -10, 0)
r("Centro Arriba", 5, -10, 0)
kf_todos(BRAZOS + TRONCO, 3)

bpy.context.scene.frame_set(7)
r("Hombro Derecho", -45, 35, 0)
r("Centro Arriba", -12, 22, 0)
kf_todos(BRAZOS + TRONCO, 7)

bpy.context.scene.frame_set(11)
r("Hombro Derecho", 32, -22, 0)
r("Centro Arriba", 16, -22, 0)
kf_todos(BRAZOS + TRONCO, 11)

bpy.context.scene.frame_set(18)
r("Hombro Derecho", -45, 35, 0)
r("Centro Arriba", -12, 22, 0)
kf_todos(BRAZOS + TRONCO, 18)

bpy.context.scene.frame_set(24)
r("Hombro Derecho", -20, 0, 0)
r("Hombro Izquierdo", -15, 0, 0)
r("Centro Arriba", 0, -12, 0)
kf_todos(BRAZOS + TRONCO, 24)

bpy.context.scene.frame_set(42)
reset_pose()
kf_todos(BRAZOS + TRONCO, 42)

# ─── COMBO L_L_H (54f) — igual que III ───────────────────────────
nueva_accion("elite_combo_L_L_H", 54)
bpy.context.scene.frame_set(1)
reset_pose()
kf_todos(BRAZOS + TRONCO, 1)

bpy.context.scene.frame_set(3)
r("Hombro Derecho", -10, -10, 0)
r("Centro Arriba", 5, -10, 0)
kf_todos(BRAZOS + TRONCO, 3)

bpy.context.scene.frame_set(7)
r("Hombro Derecho", -45, 35, 0)
r("Centro Arriba", -12, 22, 0)
kf_todos(BRAZOS + TRONCO, 7)

bpy.context.scene.frame_set(11)
r("Hombro Derecho", 32, -22, 0)
r("Centro Arriba", 16, -22, 0)
kf_todos(BRAZOS + TRONCO, 11)

bpy.context.scene.frame_set(18)
r("Hombro Derecho", -45, 35, 0)
r("Centro Arriba", -12, 22, 0)
kf_todos(BRAZOS + TRONCO, 18)

bpy.context.scene.frame_set(24)
r("Hombro Derecho", -20, 0, 0)
r("Hombro Izquierdo", -15, 0, 0)
r("Centro Arriba", 0, -12, 0)
kf_todos(BRAZOS + TRONCO, 24)

bpy.context.scene.frame_set(32)
r("Hombro Derecho", -20, -18, 0)
r("Centro Arriba", 6, -12, 0)
kf_todos(BRAZOS + TRONCO, 32)

bpy.context.scene.frame_set(54)
reset_pose()
kf_todos(BRAZOS + TRONCO, 54)

# ─── COMBO L_L_L: L_L + patada (55f) — EXCLUSIVO ELITE ───────────
nueva_accion("elite_combo_L_L_L", 55)
bpy.context.scene.frame_set(1)
reset_pose()
kf_todos(BRAZOS + TRONCO + PIERNA_DER, 1)

bpy.context.scene.frame_set(3)
r("Hombro Derecho", -10, -10, 0)
r("Centro Arriba", 5, -10, 0)
kf_todos(BRAZOS + TRONCO, 3)

bpy.context.scene.frame_set(7)
r("Hombro Derecho", -45, 35, 0)
r("Centro Arriba", -12, 22, 0)
kf_todos(BRAZOS + TRONCO, 7)

bpy.context.scene.frame_set(11)
r("Hombro Derecho", 32, -22, 0)
r("Centro Arriba", 16, -22, 0)
kf_todos(BRAZOS + TRONCO, 11)

bpy.context.scene.frame_set(18)
r("Hombro Derecho", -45, 35, 0)
r("Centro Arriba", -12, 22, 0)
kf_todos(BRAZOS + TRONCO, 18)

bpy.context.scene.frame_set(24)
r("Hombro Derecho", -20, 0, 0)
r("Hombro Izquierdo", -15, 0, 0)
r("Centro Arriba", 0, -12, 0)
kf_todos(BRAZOS + TRONCO, 24)

# Carga patada — levanta rodilla
bpy.context.scene.frame_set(30)
r("PelvizDer", 0, 0, 10)
r("PiernaSupDer", -60, 0, 0)
r("PiernaInfDer", 40, 0, 0)
r("Centro Arriba", 10, 0, 0)
kf_todos(TRONCO + PIERNA_DER, 30)

# Extensión patada
bpy.context.scene.frame_set(34)
r("PiernaSupDer", -80, 0, 0)
r("PiernaInfDer", 0, 0, 0)
kf_todos(PIERNA_DER, 34)

bpy.context.scene.frame_set(55)
reset_pose()
kf_todos(BRAZOS + TRONCO + PIERNA_DER, 55)

# ─── COMBO L_L_L_H: L_L_L + disparo (65f) — EXCLUSIVO ELITE ──────
nueva_accion("elite_combo_L_L_L_H", 65)
bpy.context.scene.frame_set(1)
reset_pose()
kf_todos(BRAZOS + TRONCO + PIERNA_DER, 1)

bpy.context.scene.frame_set(3)
r("Hombro Derecho", -10, -10, 0)
r("Centro Arriba", 5, -10, 0)
kf_todos(BRAZOS + TRONCO, 3)

bpy.context.scene.frame_set(7)
r("Hombro Derecho", -45, 35, 0)
r("Centro Arriba", -12, 22, 0)
kf_todos(BRAZOS + TRONCO, 7)

bpy.context.scene.frame_set(11)
r("Hombro Derecho", 32, -22, 0)
r("Centro Arriba", 16, -22, 0)
kf_todos(BRAZOS + TRONCO, 11)

bpy.context.scene.frame_set(18)
r("Hombro Derecho", -45, 35, 0)
r("Centro Arriba", -12, 22, 0)
kf_todos(BRAZOS + TRONCO, 18)

bpy.context.scene.frame_set(24)
r("Hombro Derecho", -20, 0, 0)
r("Hombro Izquierdo", -15, 0, 0)
r("Centro Arriba", 0, -12, 0)
kf_todos(BRAZOS + TRONCO, 24)

bpy.context.scene.frame_set(30)
r("PelvizDer", 0, 0, 10)
r("PiernaSupDer", -60, 0, 0)
r("PiernaInfDer", 40, 0, 0)
r("Centro Arriba", 10, 0, 0)
kf_todos(TRONCO + PIERNA_DER, 30)

bpy.context.scene.frame_set(34)
r("PiernaSupDer", -80, 0, 0)
r("PiernaInfDer", 0, 0, 0)
kf_todos(PIERNA_DER, 34)

# Aterriza y apunta
bpy.context.scene.frame_set(40)
reset_pose()
r("Hombro Derecho", -20, 0, 0)
r("Hombro Izquierdo", -15, 0, 0)
r("Centro Arriba", 0, -12, 0)
kf_todos(BRAZOS + TRONCO + PIERNA_DER, 40)

# Disparo
bpy.context.scene.frame_set(48)
r("Hombro Derecho", -20, -18, 0)
r("Centro Arriba", 6, -12, 0)
kf_todos(BRAZOS + TRONCO, 48)

bpy.context.scene.frame_set(65)
reset_pose()
kf_todos(BRAZOS + TRONCO + PIERNA_DER, 65)

print("✓ Ranger Elite: 7 acciones creadas")
