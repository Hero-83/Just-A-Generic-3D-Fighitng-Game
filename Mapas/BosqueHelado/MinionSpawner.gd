extends Node3D

@export var escena_minion: PackedScene
@export var maximo_minions: int = 3
@export var intervalo_spawn: float = 5.0
@export var distancia_libre: float = 2.0

var puntos_spawn: Array[Marker3D] = []
var tiempo_spawn: float = 0.0


func _ready():
	for hijo in get_children():
		if hijo is Marker3D:
			puntos_spawn.append(hijo)

	call_deferred("generar_iniciales")


func _physics_process(delta: float):
	if contar_minions() >= maximo_minions:
		tiempo_spawn = 0.0
		return

	tiempo_spawn += delta

	if tiempo_spawn >= intervalo_spawn:
		tiempo_spawn = 0.0
		generar_minion()


func contar_minions() -> int:
	var cantidad: int = 0

	for minion in get_tree().get_nodes_in_group("minions"):
		if not minion.is_queued_for_deletion():
			cantidad += 1

	return cantidad


func generar_iniciales():
	for i in range(maximo_minions):
		if not generar_minion():
			break


func generar_minion() -> bool:
	if escena_minion == null:
		return false

	if contar_minions() >= maximo_minions:
		return false

	if puntos_spawn.is_empty():
		return false

	var disponibles: Array[Marker3D] = []

	for punto in puntos_spawn:
		if punto_libre(punto):
			disponibles.append(punto)

	if disponibles.is_empty():
		return false

	var punto: Marker3D = disponibles.pick_random()

	var minion = escena_minion.instantiate() as Node3D

	if minion == null:
		return false

	minion.position = to_local(punto.global_position)

	add_child(minion)

	print("Minions vivos: ", contar_minions())

	return true


func punto_libre(punto: Marker3D) -> bool:
	for grupo in ["minions", "player"]:

		for personaje in get_tree().get_nodes_in_group(grupo):

			if not personaje is Node3D:
				continue

			if personaje.is_queued_for_deletion():
				continue

			var distancia = punto.global_position.distance_to(
				personaje.global_position
			)

			if distancia < distancia_libre:
				return false

	return true
