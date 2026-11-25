"""
Ranger III — Animaciones
Mismos combos que Ranger II pero con poses más marcadas y transiciones más suaves.
+2-4 frames de startup en cada acción para que se vea más profesional.
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

# ─── GOLPE FUERTE (32f) ───────────────────────────────────────────
nueva_accion("ranger3_golpe_fuerte", 32)
bpy.context.scene.frame_set(1)
reset_pose()
kf_todos(BRAZOS + TRONCO, 1)

# Pose de apunte más elaborada — inclina el tronco
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

# ─── GOLPE LIGERO (26f) ───────────────────────────────────────────
nueva_accion("ranger3_golpe_ligero", 26)
bpy.context.scene.frame_set(1)
reset_pose()
kf_todos(BRAZOS + TRONCO, 1)

# Anticipación — pequeño movimiento opuesto antes del arco
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

# ─── COMBO L_H (44f) ──────────────────────────────────────────────
nueva_accion("ranger3_combo_L_H", 44)
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
r("Hombro Derecho", -65, 0, 22, )
r("BrazoSupDer", -32, 0, 0)
r("Centro Arriba", -22, 0, 0)
kf_todos(BRAZOS + TRONCO, 20)

bpy.context.scene.frame_set(44)
reset_pose()
kf_todos(BRAZOS + TRONCO, 44)

# ─── COMBO L_L (42f) ──────────────────────────────────────────────
nueva_accion("ranger3_combo_L_L", 42)
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

# ─── COMBO L_L_H (54f) ────────────────────────────────────────────
nueva_accion("ranger3_combo_L_L_H", 54)
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

print("✓ Ranger III: 5 acciones creadas")
