# fighter_data.gd
class_name FighterData
extends Resource

@export_group("Identidad")
@export var fighter_name: String = "Luchador"
@export var fighter_type: String = "Normal" # Aquí luego metemos el Enum de tipos
@export var fighting_style: String = "Callejero I" # Enum de estilos

@export_group("Apariencia")
@export var appearance: AppearanceData

@export_group("Equipamiento")
@export var class_data: ClassData # Los stats base (vida, esquive)
@export var equipped_moves: Array[MoveData] = [] # 1 a 4 movimientos
@export var equipped_ultis: Array[MoveData] = [] # 0 a 4 ultis
@export var equipped_passives: Array[String] = [] # Pasivas (por ahora IDs o nombres)

@export_group("Estadísticas actuales")
# Estos no se exportan al editor, se calculan en el juego
var current_level: int = 1
var current_prestige: int = 0
var current_xp: int = 0
