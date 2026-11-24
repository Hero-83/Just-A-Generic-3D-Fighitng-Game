extends Control

@onready var btn_singleplayer: Button = $CenterContainer/VBoxContainer/Singleplayer
@onready var btn_multiplayer: Button = $CenterContainer/VBoxContainer/Multiplayer
@onready var btn_training: Button = $CenterContainer/VBoxContainer/Training


func _ready():
	btn_multiplayer.disabled = true

	btn_singleplayer.pressed.connect(_on_singleplayer)
	btn_training.pressed.connect(_on_training)

	btn_singleplayer.grab_focus()


func _on_singleplayer():
	print("Singleplayer seleccionado")


func _on_training():
	print("Training seleccionado")
