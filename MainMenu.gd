extends Control

@onready var btn_singleplayer: Button = $CenterContainer/VBoxContainer/Singleplayer
@onready var btn_multiplayer: Button = $CenterContainer/VBoxContainer/Multiplayer
@onready var btn_training: Button = $CenterContainer/VBoxContainer/Training


func _ready():
	Input.mouse_mode = Input.MOUSE_MODE_VISIBLE

	btn_multiplayer.disabled = true
	btn_training.disabled = true

	btn_singleplayer.disabled = false
	btn_singleplayer.pressed.connect(_on_singleplayer)

	btn_singleplayer.grab_focus()


func _on_singleplayer():
	get_tree().change_scene_to_file(
        "res://Mapas/BosqueHelado/BosqueHelado.tscn" 
	)
