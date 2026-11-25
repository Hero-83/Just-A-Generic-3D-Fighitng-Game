extends Node3D

@export var semilla: int = 110
var rng := RandomNumberGenerator.new()
var nieve := StandardMaterial3D.new()
var tronco := StandardMaterial3D.new()
var hojas := StandardMaterial3D.new()
var hielo := StandardMaterial3D.new()

func _ready() -> void:
	rng.seed = semilla
	nieve.albedo_color = Color("dceaf3")
	tronco.albedo_color = Color("554b50")
	hojas.albedo_color = Color("345e68")
	hielo.albedo_color = Color("8ab9d2")
	hielo.roughness = 0.35
	bloque(Vector3(80, 1, 80), Vector3(0, -0.5, 0), nieve)
	for x in [-40.0, 40.0]:
		limite(Vector3(x, 3, 0), Vector3(1, 6, 80))
	for z in [-40.0, 40.0]:
		limite(Vector3(0, 3, z), Vector3(80, 6, 1))
	for x in range(-36, 37, 5):
		for z in range(-36, 37, 5):
			var p := Vector3(x + rng.randf_range(-1.4, 1.4), 0, z + rng.randf_range(-1.4, 1.4))
			if p.length() < 19.0 or rng.randf() < 0.22:
				continue
			arbol(p, rng.randf_range(3.8, 7.5))
	for i in range(22):
		var a := rng.randf_range(0, TAU)
		var r := rng.randf_range(21, 34)
		var p := Vector3(cos(a)*r, 0, sin(a)*r)
		var s := rng.randf_range(0.7, 1.8)
		var mesh := SphereMesh.new()
		mesh.radial_segments = 5
		mesh.rings = 3
		mesh.radius = s
		mesh.height = s * 1.5
		var body := StaticBody3D.new()
		add_child(body)
		body.position = p + Vector3.UP * s * 0.35
		visual(body, mesh, hielo, Vector3.ZERO)
		var shape := SphereShape3D.new()
		shape.radius = s * 0.8
		colision(body, shape)
	# Cámara de inspección: desactivar al integrar la cámara del jugador.

func visual(parent: Node3D, mesh: Mesh, mat: Material, pos: Vector3) -> void:
	var instancia := MeshInstance3D.new()
	instancia.mesh = mesh
	instancia.material_override = mat
	parent.add_child(instancia)
	instancia.position = pos

func colision(parent: StaticBody3D, shape: Shape3D) -> void:
	var c := CollisionShape3D.new()
	c.shape = shape
	parent.add_child(c)

func bloque(size: Vector3, pos: Vector3, mat: Material) -> void:
	var body := StaticBody3D.new()
	add_child(body)
	body.position = pos
	var mesh := BoxMesh.new()
	mesh.size = size
	visual(body, mesh, mat, Vector3.ZERO)
	var shape := BoxShape3D.new()
	shape.size = size
	colision(body, shape)

func limite(pos: Vector3, size: Vector3) -> void:
	var body := StaticBody3D.new()
	add_child(body)
	body.position = pos
	var shape := BoxShape3D.new()
	shape.size = size
	colision(body, shape)

func arbol(p: Vector3, h: float) -> void:
	var body := StaticBody3D.new()
	add_child(body)
	body.position = p + Vector3.UP * h * 0.25
	var stem := CylinderMesh.new()
	stem.top_radius = h * 0.035
	stem.bottom_radius = h * 0.055
	stem.height = h * 0.5
	stem.radial_segments = 7
	visual(body, stem, tronco, Vector3.ZERO)
	var shape := CylinderShape3D.new()
	shape.radius = h * 0.055
	shape.height = h * 0.5
	colision(body, shape)
	for i in range(3):
		var radius := h * (0.25 - i * 0.055)
		var cone := CylinderMesh.new()
		cone.top_radius = 0.0
		cone.bottom_radius = radius
		cone.height = h * 0.46
		cone.radial_segments = 7
		var y := h * (0.16 + i * 0.18)
		visual(body, cone, hojas, Vector3.UP * y)
		var cap := CylinderMesh.new()
		cap.top_radius = 0.0
		cap.bottom_radius = radius * 0.78
		cap.height = h * 0.36
		cap.radial_segments = 7
		visual(body, cap, nieve, Vector3.UP * (y + h * 0.065))
