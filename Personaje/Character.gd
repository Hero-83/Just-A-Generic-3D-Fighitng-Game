# character.gd
class_name Character
extends CharacterBody3D

@export var fighter_data: FighterData

@onready var model: CharacterModel = $CharacterModel
@onready var stats: CharacterStats = $CharacterStats # El que hicimos antes
@onready var state_machine: CharacterStateMachine = $StateMachine
@onready var hurtbox: Hurtbox = $Hurtbox

func _ready() -> void:
	if fighter_data:
		# 1. Cargar stats
		stats.apply_class(fighter_data.class_data)
		
		# 2. Cargar visuales
		model.apply_appearance(fighter_data.appearance)
		
		# 3. Cargar movimientos y ultis
		# (Aquí le pasas el array de movimientos al StateMachine o al CombatResolver)
		
func _physics_process(delta: float) -> void:
	# La regeneración de estamina que definimos
	_handle_stamina_regen(delta)
	
	# El movimiento base (caminar/correr) lo maneja el StateMachine
	move_and_slide()

func _handle_stamina_regen(delta: float) -> void:
	var regen_mult := 1.0
	
	if state_machine.current_state.name == "Idle":
		# Si llevas mucho tiempo quieto, 150% (esto requeriría un timer)
		regen_mult = 1.5
	elif state_machine.current_state.name in ["Running", "Attacking", "Dashing"]:
		# 50% mientras gastas
		regen_mult = 0.5
		
	stats.current_stamina = minf(
		stats.current_stamina + (stats.stamina_regen * regen_mult * delta),
		stats.max_stamina
	)
