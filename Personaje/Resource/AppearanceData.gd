# appearance_data.gd
class_name AppearanceData
extends Resource

@export_group("Cuerpo")
@export var skin_tone: Color = Color.WHITE
@export var hair_id: int = 0
@export var beard_id: int = 0
@export var eyes_id: int = 0
@export var eyebrows_id: int = 0
@export var mouth_id: int = 0

@export_group("Ropa")
@export var shirt_id: int = 0
@export var pants_id: int = 0
@export var outerwear_id: int = 0 # Chaquetas
@export var shoes_id: int = 0

@export_group("Accesorios")
@export var hat_id: int = 0
@export var face_accessory_id: int = 0
@export var neck_accessory_id: int = 0
@export var arm_accessory_id: int = 0
@export var hand_accessory_id: int = 0
@export var knee_accessory_id: int = 0
@export var leg_accessory_id: int = 0
