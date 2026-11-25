extends CharacterBody3D

@export_category("Estadisticas")
@export var vida_maxima: int = 100
@export var dano: int = 50
@export_category("Movimiento")
@export var velocidad: float = 5.0
@export var velocidad_retroceso: float = 2.5
@export_category("Combate")
@export var distancia_deteccion: float = 25.0
@export var distancia_minima: float = 6.0
@export var distancia_maxima: float = 8.0
@export var distancia_LH: float = 3.0
@export var espera_LH: float = 1.0
@export var espera_H: float = 5.0
@export var intervalo_ataque: float = 2.0
@export_category("Animaciones")
@export var animaciones: AnimationPlayer
@export var anim_idle: String = "Caminar"
@export var anim_correr: String = "Correr_Adelante"
@export var anim_apuntar: String = "Apuntar_Adelante"
@export var anim_retroceder: String = "Apuntar_Atras"
@export var anim_L: String = "Ranger1_L"
@export var anim_LH: String = "Ranger1_LH"
@export var anim_H: String = "Ranger1_H"
@export var modelo_mira_positivo_z: bool = false

var vida: int
var objetivo: Node3D
var tiempo_cerca: float = 0.0
var tiempo_rango: float = 0.0
var cooldown: float = 0.0
var atacando: bool = false
var muerto: bool = false
var ataque_actual: String = ""
var tiempo_anim: float = 0.0
var duracion_ataque: float = 0.0
var golpe_aplicado: bool = false
var victima: Node3D
var ultima_animacion: String = ""
var animacion_pausada: bool = false
var gravedad: float = ProjectSettings.get_setting("physics/3d/default_gravity")

func _ready():
	vida = vida_maxima
	add_to_group("minions")
	if animaciones == null:
		animaciones = find_child("AnimationPlayer", true, false) as AnimationPlayer
	if animaciones != null:
		print("Animaciones: ", animaciones.get_animation_list())
	reproducir(anim_idle, true)

func _physics_process(delta: float):
	if muerto:
		return
	if not is_on_floor():
		velocity.y -= gravedad * delta
	else:
		velocity.y = 0.0
	velocity.x = 0.0
	velocity.z = 0.0
	cooldown = maxf(cooldown - delta, 0.0)
	if not is_instance_valid(objetivo):
		tiempo_cerca = 0.0
		tiempo_rango = 0.0
		buscar_objetivo()
	if not is_instance_valid(objetivo):
		actualizar_ataque(delta)
		if not atacando:
			reproducir(anim_idle, true)
		move_and_slide()
		return
	var direccion: Vector3 = objetivo.global_position - global_position
	direccion.y = 0.0
	var distancia: float = direccion.length()
	if distancia > distancia_deteccion:
		objetivo = null
		tiempo_cerca = 0.0
		tiempo_rango = 0.0
		actualizar_ataque(delta)
		if not atacando:
			reproducir(anim_idle, true)
		move_and_slide()
		return
	var visible: bool = puede_ver(objetivo)
	if distancia > 0.01:
		direccion = direccion.normalized()
		look_at(global_position + direccion, Vector3.UP, modelo_mira_positivo_z)
	if visible and distancia <= distancia_LH:
		tiempo_cerca += delta
	else:
		tiempo_cerca = 0.0
	if visible and distancia >= distancia_minima and distancia <= distancia_maxima:
		tiempo_rango += delta
	else:
		tiempo_rango = 0.0
	actualizar_ataque(delta)
	if atacando:
		move_and_slide()
		return
	# Los ataques especiales tienen prioridad sobre L.
	if tiempo_cerca >= espera_LH:
		tiempo_cerca = 0.0
		iniciar_ataque(anim_LH)
	elif tiempo_rango >= espera_H:
		tiempo_rango = 0.0
		iniciar_ataque(anim_H)
	elif distancia > distancia_maxima:
		velocity.x = direccion.x * velocidad
		velocity.z = direccion.z * velocidad
		reproducir(anim_correr)
	elif distancia < distancia_minima:
		velocity.x = -direccion.x * velocidad_retroceso
		velocity.z = -direccion.z * velocidad_retroceso
		reproducir(anim_retroceder)
	else:
		reproducir(anim_apuntar, true)
		if visible and cooldown <= 0.0:
			iniciar_ataque(anim_L)
	move_and_slide()

func buscar_objetivo():
	var menor: float = distancia_deteccion
	for candidato in get_tree().get_nodes_in_group("player"):
		if not candidato is Node3D:
			continue
		var distancia: float = global_position.distance_to(candidato.global_position)
		if distancia <= menor and puede_ver(candidato):
			objetivo = candidato
			menor = distancia

func puede_ver(candidato: Node3D) -> bool:
	var consulta = PhysicsRayQueryParameters3D.create(global_position + Vector3.UP * 1.5, candidato.global_position + Vector3.UP)
	consulta.exclude = [get_rid()]
	var resultado = get_world_3d().direct_space_state.intersect_ray(consulta)
	return resultado.is_empty() or resultado["collider"] == candidato

func reproducir(nombre: String, pausada: bool = false):
	if animaciones == null or not animaciones.has_animation(nombre):
		return
	if ultima_animacion == nombre and animacion_pausada == pausada and (pausada or animaciones.is_playing()):
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
	if animaciones == null or not animaciones.has_animation(nombre):
		push_warning("Animacion no disponible: " + nombre)
		cooldown = intervalo_ataque
		return
	atacando = true
	ataque_actual = nombre
	victima = objetivo
	tiempo_anim = 0.0
	golpe_aplicado = false
	ultima_animacion = ""
	animacion_pausada = false
	duracion_ataque = maxf(animaciones.get_animation(nombre).length, 0.05)
	animaciones.stop()
	animaciones.play(nombre)

func actualizar_ataque(delta: float):
	if not atacando:
		return
	tiempo_anim += delta
	if not golpe_aplicado and tiempo_anim >= duracion_ataque * 0.5:
		golpe_aplicado = true
		if is_instance_valid(victima):
			var alcance: float = distancia_LH if ataque_actual == anim_LH else distancia_maxima
			var diferencia: Vector3 = victima.global_position - global_position
			diferencia.y = 0.0
			if diferencia.length() <= alcance and puede_ver(victima) and victima.has_method("recibir_dano"):
				victima.recibir_dano(dano)
	if tiempo_anim >= duracion_ataque:
		atacando = false
		cooldown = intervalo_ataque
		ultima_animacion = ""

func recibir_dano(cantidad: int):
	if muerto:
		return
	vida = maxi(vida - cantidad, 0)
	if vida == 0:
		muerto = true
		velocity = Vector3.ZERO
		queue_free()
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
