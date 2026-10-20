# character_model.gd
class_name CharacterModel
extends Node3D

@onready var skin_mesh: MeshInstance3D = $SkinMesh
@onready var skeleton: Skeleton3D = $Skeleton3D

# Nodos de anclaje para los accesorios
@onready var head_anchor: BoneAttachment3D = $Skeleton3D/HeadAnchor
@onready var hand_anchor: BoneAttachment3D = $Skeleton3D/HandAnchor
# ... etc

# Aquí guardamos los modelos actuales para borrarlos si cambian
var current_accessories: Dictionary = {}

func apply_appearance(data: AppearanceData) -> void:
	# 1. Aplicar color de piel (asumiendo que usas un ShaderMaterial)
	var mat = skin_mesh.get_active_material(0).duplicate()
	mat.set_shader_parameter("skin_tone", data.skin_tone)
	skin_mesh.set_surface_override_material(0, mat)
	
	# 2. Cargar modelos 3D de accesorios
	_update_accessory("head", data.hat_id, head_anchor)
	_update_accessory("face", data.face_accessory_id, head_anchor)
	# ... lo mismo para todas las partes
	
	# 3. Aquí conectarías con un AnimationTree para cambiar
	# las animaciones según el estilo (ej. Boxeador vs Callejero)
	_setup_animations(data)

func _update_accessory(slot: String, id: int, anchor: Node3D) -> void:
	# Si ya había uno, lo borramos
	if current_accessories.has(slot):
		current_accessories[slot].queue_free()
		
	if id > 0:
		# Aquí buscas el modelo 3D en tu base de datos
		var new_mesh = load_accessory_model(slot, id) 
		anchor.add_child(new_mesh)
		current_accessories[slot] = new_mesh

func _setup_animations(data: AppearanceData) -> void:
	# Dependiendo del estilo del FighterData, cargas un AnimationTree distinto
	pass
