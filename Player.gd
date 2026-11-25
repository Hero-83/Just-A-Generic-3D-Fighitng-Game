extends CharacterBody3D
@export var spawn_jugador: Marker3D

@export_category("Estadisticas")
@export var vida_maxima: int = 1000
@export var dano: int = 50

@export_category("Movimiento")
@export var velocidad_caminar: float = 2.5
@export var velocidad_correr: float = 5.0
@export var fuerza_salto: float = 5.0
@export var sensibilidad: float = 0.003

@export_category("Combate")
@export var alcance_L: float = 8.0
@export var alcance_H: float = 8.0
@export var alcance_LH: float = 3.0

@export_category("Animaciones")
@export var animaciones: AnimationPlayer
@export var anim_L: String = "Ranger1_L"
@export var anim_H: String = "Ranger1_H"
@export var anim_LH: String = "Ranger1_LH"

@export var modelo_mira_positivo_z: bool = false

@onready var brazo_camara: SpringArm3D = $SpringArm3D

var vida: int
var muerto: bool = false
var atacando: bool = false
var combo_pendiente: bool = false

var ataque_actual: String = ""
var tiempo_ataque: float = 0.0
var duracion_ataque: float = 0.0
var golpe_aplicado: bool = false

var ultima_animacion: String = ""
var animacion_pausada: bool = false

var gravedad: float = ProjectSettings.get_setting(
    "physics/3d/default_gravity"
)


func _ready():
	$SpringArm3D/Camera3D.call_deferred("make_current")
	if spawn_jugador != null:
		global_transform = spawn_jugador.global_transform
	vida = vida_maxima
	add_to_group("player")

	if animaciones == null:
		animaciones = find_child(
			"AnimationPlayer", true, false
		) as AnimationPlayer

	brazo_camara.add_excluded_object(get_rid())

	Input.mouse_mode = Input.MOUSE_MODE_CAPTURED

	reproducir("Caminar", true)


func _unhandled_input(event):
	if muerto:
		return

	if event is InputEventMouseMotion:
		if Input.mouse_mode == Input.MOUSE_MODE_CAPTURED:

			rotate_y(-event.relative.x * sensibilidad)

			brazo_camara.rotation.x -= (
				event.relative.y * sensibilidad
			)

			brazo_camara.rotation.x = clampf(
				brazo_camara.rotation.x,
				deg_to_rad(-65),
				deg_to_rad(25)
			)

	if event is InputEventMouseButton and event.pressed:

		if event.button_index == MOUSE_BUTTON_LEFT:
			if not atacando:
				iniciar_ataque(anim_L)

		elif event.button_index == MOUSE_BUTTON_RIGHT:

			if atacando and ataque_actual == anim_L:
				combo_pendiente = true

			elif not atacando:
				iniciar_ataque(anim_H)

	if event is InputEventKey and event.pressed:

		if event.physical_keycode == KEY_ESCAPE:
			Input.mouse_mode = Input.MOUSE_MODE_VISIBLE
			get_tree().change_scene_to_file(
                "res://MainMenu.tscn"
			)

		if event.physical_keycode == KEY_SPACE:
			if is_on_floor():
				velocity.y = fuerza_salto


func _physics_process(delta: float):
	if global_position.y < -20.0:
		if spawn_jugador != null:
			global_transform = spawn_jugador.global_transform
		else:
			global_position = Vector3(0, 2, 5)
		velocity = Vector3.ZERO
		return
	if muerto:
		return

	if not is_on_floor():
		velocity.y -= gravedad * delta

	velocity.x = 0.0
	velocity.z = 0.0

	actualizar_ataque(delta)

	if atacando:
		move_and_slide()
		return

	var x: float = 0.0
	var z: float = 0.0

	if Input.is_physical_key_pressed(KEY_W):
		z -= 1.0

	if Input.is_physical_key_pressed(KEY_S):
		z += 1.0

	if Input.is_physical_key_pressed(KEY_A):
		x -= 1.0

	if Input.is_physical_key_pressed(KEY_D):
		x += 1.0

	var entrada = Vector3(x, 0.0, z)

	var corriendo = Input.is_physical_key_pressed(
		KEY_SHIFT
	)

	var velocidad_actual = (
		velocidad_correr if corriendo
		else velocidad_caminar
	)

	if entrada.length() > 0.0:

		var direccion = (
			global_transform.basis * entrada.normalized()
		)

		velocity.x = direccion.x * velocidad_actual
		velocity.z = direccion.z * velocidad_actual

		animar_movimiento(x, z, corriendo)

	else:
		reproducir("Caminar", true)

	move_and_slide()


func animar_movimiento(
	x: float,
	z: float,
	corriendo: bool
):
	var prefijo = "Correr" if corriendo else "Caminar"
	var sufijo: String = ""

	if z < 0:
		if x > 0:
			sufijo = "_AlfrenteDer"
		elif x < 0:
			sufijo = "_AlfrenteIzq"
		else:
			sufijo = "_Adelante" if corriendo else ""

	elif z > 0:
		if x > 0:
			sufijo = "_AtrasDer"
		elif x < 0:
			sufijo = "_AtrasIzq"
		else:
			sufijo = "_Atras"

	elif x > 0:
		sufijo = "_Derecha"

	elif x < 0:
		sufijo = "_Izquierda"

	var nombre = prefijo + sufijo

	if animaciones != null:
		if not animaciones.has_animation(nombre):
			nombre = (
				"Correr_Adelante" if corriendo
				else "Caminar"
			)

	reproducir(nombre)


func reproducir(nombre: String, pausada: bool = false):
	if animaciones == null:
		return

	if not animaciones.has_animation(nombre):
		return

	if ultima_animacion == nombre:
		if animacion_pausada == pausada:
			if pausada or animaciones.is_playing():
				return

	ultima_animacion = nombre
	animacion_pausada = pausada

	if pausada:
		animaciones.play(nombre, 0.0)
		animaciones.seek(0.0, true)
		animaciones.pause()
	else:
		animaciones.play(nombre, 0.15)


func iniciar_ataque(nombre: String):
	if animaciones == null:
		return

	if not animaciones.has_animation(nombre):
		push_warning("Animacion no disponible: " + nombre)
		return

	atacando = true
	ataque_actual = nombre

	tiempo_ataque = 0.0
	golpe_aplicado = false
	ultima_animacion = ""

	duracion_ataque = maxf(
		animaciones.get_animation(nombre).length,
		0.05
	)

	animaciones.stop()
	animaciones.play(nombre)


func actualizar_ataque(delta: float):
	if not atacando:
		return

	tiempo_ataque += delta

	if not golpe_aplicado:
		if tiempo_ataque >= duracion_ataque * 0.5:
			golpe_aplicado = true
			aplicar_dano()

	if tiempo_ataque >= duracion_ataque:

		atacando = false
		ultima_animacion = ""

		if combo_pendiente:
			combo_pendiente = false
			iniciar_ataque(anim_LH)


func aplicar_dano():
	var alcance: float = alcance_L

	if ataque_actual == anim_H:
		alcance = alcance_H

	elif ataque_actual == anim_LH:
		alcance = alcance_LH

	var frente = -global_transform.basis.z

	if modelo_mira_positivo_z:
		frente = -frente

	var enemigo_elegido: Node3D = null
	var menor_distancia: float = alcance

	for enemigo in get_tree().get_nodes_in_group("minions"):

		if not enemigo is Node3D:
			continue

		if enemigo.is_queued_for_deletion():
			continue

		var diferencia = (
			enemigo.global_position - global_position
		)

		diferencia.y = 0.0

		var distancia = diferencia.length()

		if distancia > menor_distancia:
			continue

		if frente.dot(diferencia.normalized()) < 0.65:
			continue

		var consulta = PhysicsRayQueryParameters3D.create(
			global_position + Vector3.UP,
			enemigo.global_position + Vector3.UP
		)

		consulta.exclude = [get_rid()]

		var resultado = get_world_3d().direct_space_state.intersect_ray(
			consulta
		)

		if not resultado.is_empty():
			if resultado["collider"] != enemigo:
				continue

		enemigo_elegido = enemigo
		menor_distancia = distancia

	if is_instance_valid(enemigo_elegido):
		if enemigo_elegido.has_method("recibir_dano"):
			enemigo_elegido.recibir_dano(dano)


func recibir_dano(cantidad: int):
	if muerto:
		return

	vida = maxi(vida - cantidad, 0)

	print("Vida del jugador: ", vida)

	if vida <= 0:
		morir()


func morir():
	muerto = true
	velocity = Vector3.ZERO

	Input.mouse_mode = Input.MOUSE_MODE_VISIBLE

	get_tree().call_deferred(
		"change_scene_to_file",
        "res://MainMenu.tscn"
	)
func configurar_colision():
	collision_layer = 1
	collision_mask = 1

	var colision = get_node_or_null("CollisionShape3D")

	if colision == null:
		colision = CollisionShape3D.new()
		colision.name = "CollisionShape3D"
		add_child(colision)

	var capsula = CapsuleShape3D.new()
	capsula.radius = 0.4
	capsula.height = 2.0

	colision.shape = capsula
	colision.position = Vector3(0, 1, 0)
	colision.rotation = Vector3.ZERO
	colision.scale = Vector3.ONE
	colision.disabled = false
