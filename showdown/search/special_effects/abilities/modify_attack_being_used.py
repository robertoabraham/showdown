import constants
from showdown.calculate_damage import is_not_very_effective


def speedboost(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    attacking_move = attacking_move.copy()
    if constants.SELF not in attacking_move:
        attacking_move[constants.SELF] = dict()
    else:
        attacking_move[constants.SELF] = attacking_move[constants.SELF].copy()
    if constants.BOOSTS not in attacking_move[constants.SELF]:
        attacking_move[constants.SELF][constants.BOOSTS] = dict()
    else:
        attacking_move[constants.SELF][constants.BOOSTS] = attacking_move[constants.SELF][constants.BOOSTS].copy()
    if constants.SPEED not in attacking_move[constants.SELF][constants.BOOSTS]:
        attacking_move[constants.SELF][constants.BOOSTS][constants.SPEED] = 0
        attacking_move[constants.SELF][constants.CHANCE] = 100
    attacking_move[constants.SELF][constants.BOOSTS][constants.SPEED] += 1
    return attacking_move


def analytic(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if not first_move:
        attacking_move = attacking_move.copy()
        attacking_move[constants.BASE_POWER] *= 1.3
    return attacking_move


def adaptability(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if attacking_move[constants.TYPE] in attacking_pokemon.types:
        attacking_move = attacking_move.copy()
        attacking_move[constants.BASE_POWER] = int(attacking_move[constants.BASE_POWER] * 4/3)
    return attacking_move


def aerilate(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if attacking_move[constants.TYPE] == 'normal':
        attacking_move = attacking_move.copy()
        attacking_move[constants.BASE_POWER] = int(attacking_move[constants.BASE_POWER] * 1.30)
        attacking_move[constants.TYPE] = 'flying'
    return attacking_move


def compoundeyes(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if attacking_move[constants.ACCURACY] is not True:
        attacking_move = attacking_move.copy()
        attacking_move[constants.ACCURACY] *= 1.3
    return attacking_move


def contrary(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    # look at this logic, I want to fucking die
    if attacking_move[constants.TARGET] in constants.MOVE_TARGET_SELF:
        attacking_move = attacking_move.copy()
        if constants.BOOSTS in attacking_move:
            attacking_move[constants.BOOSTS] = attacking_move[constants.BOOSTS].copy()
            for k, v in attacking_move[constants.BOOSTS].items():
                attacking_move[constants.BOOSTS][k] = -1*v
        if attacking_move[constants.SECONDARY] and constants.BOOSTS in attacking_move[constants.SECONDARY]:
            attacking_move[constants.SECONDARY] = attacking_move[constants.SECONDARY].copy()
            attacking_move[constants.SECONDARY][constants.BOOSTS] = attacking_move[constants.SECONDARY][constants.BOOSTS].copy()
            for k, v in attacking_move[constants.SECONDARY][constants.BOOSTS].items():
                attacking_move[constants.SECONDARY][constants.BOOSTS][k] = -1*v
    elif constants.SELF in attacking_move and constants.BOOSTS in attacking_move[constants.SELF]:
        attacking_move = attacking_move.copy()
        attacking_move[constants.SELF] = attacking_move[constants.SELF].copy()
        attacking_move[constants.SELF][constants.BOOSTS] = attacking_move[constants.SELF][constants.BOOSTS].copy()
        for k, v in attacking_move[constants.SELF][constants.BOOSTS].items():
            attacking_move[constants.SELF][constants.BOOSTS][k] = -1 * v

    elif attacking_move[constants.SECONDARY] and constants.SELF in attacking_move[constants.SECONDARY]:
        if constants.BOOSTS in attacking_move[constants.SECONDARY][constants.SELF]:
            attacking_move = attacking_move.copy()
            attacking_move[constants.SECONDARY] = attacking_move[constants.SECONDARY].copy()
            attacking_move[constants.SECONDARY][constants.SELF] = attacking_move[constants.SECONDARY][constants.SELF].copy()
            attacking_move[constants.SECONDARY][constants.SELF][constants.BOOSTS] = attacking_move[constants.SECONDARY][constants.SELF][constants.BOOSTS].copy()
            for k, v in attacking_move[constants.SECONDARY][constants.SELF][constants.BOOSTS].items():
                attacking_move[constants.SECONDARY][constants.SELF][constants.BOOSTS][k] = -1 * v

    return attacking_move


def hustle(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if attacking_move[constants.CATEGORY] == constants.PHYSICAL:
        attacking_move = attacking_move.copy()
        attacking_move[constants.ACCURACY] *= 0.8
        attacking_move[constants.BASE_POWER] *= 1.5
    return attacking_move


def ironfist(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if "punch" in attacking_move[constants.FLAGS]:
        attacking_move = attacking_move.copy()
        attacking_move[constants.BASE_POWER] *= 1.2
    return attacking_move


def megalauncher(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if "pulse" in attacking_move[constants.FLAGS]:
        attacking_move = attacking_move.copy()
        attacking_move[constants.BASE_POWER] *= 1.5
    return attacking_move


def noguard(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    attacking_move = attacking_move.copy()
    attacking_move[constants.ACCURACY] = True
    return attacking_move


def pixilate(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if attacking_move[constants.TYPE] == 'normal':
        attacking_move = attacking_move.copy()
        attacking_move[constants.BASE_POWER] = int(attacking_move[constants.BASE_POWER] * 1.30)
        attacking_move[constants.TYPE] = 'fairy'
    return attacking_move


def refrigerate(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if attacking_move[constants.TYPE] == 'normal':
        attacking_move = attacking_move.copy()
        attacking_move[constants.BASE_POWER] = int(attacking_move[constants.BASE_POWER] * 1.30)
        attacking_move[constants.TYPE] = 'ice'
    return attacking_move


def scrappy(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    # this logic is technically wrong, but it at least allows the move to hit
    # for example, a fighting move on ice/ghost should technically be super-effective
    # this logic would make it do neutral damage instead
    if 'ghost' in defending_pokemon.types:
        attacking_move = attacking_move.copy()
        attacking_move[constants.TYPE] = "typeless"
    return attacking_move


def serenegrace(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if attacking_move[constants.SECONDARY]:
        attacking_move = attacking_move.copy()
        attacking_move[constants.SECONDARY] = attacking_move[constants.SECONDARY].copy()
        attacking_move[constants.SECONDARY][constants.CHANCE] *= 2
        if attacking_move[constants.SECONDARY][constants.CHANCE] > 100:
            attacking_move[constants.SECONDARY][constants.CHANCE] = 100
    return attacking_move


def sheerforce(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if attacking_move[constants.SECONDARY]:
        attacking_move = attacking_move.copy()
        attacking_move[constants.SECONDARY] = False
        attacking_move[constants.BASE_POWER] *= 1.3
    return attacking_move


def strongjaw(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if "bite" in attacking_move[constants.FLAGS]:
        attacking_move = attacking_move.copy()
        attacking_move[constants.BASE_POWER] *= 1.5
    return attacking_move


def technician(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if attacking_move[constants.BASE_POWER] <= 60:
        attacking_move = attacking_move.copy()
        attacking_move[constants.BASE_POWER] *= 1.5
    return attacking_move


def toughclaws(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if "contact" in attacking_move[constants.FLAGS]:
        attacking_move = attacking_move.copy()
        attacking_move[constants.BASE_POWER] *= 1.3
    return attacking_move


def toxicboost(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if attacking_move[constants.CATEGORY] == constants.PHYSICAL:
        if attacking_pokemon.status in [constants.POISON, constants.TOXIC]:
            attacking_move = attacking_move.copy()
            attacking_move[constants.BASE_POWER] *= 1.5
    return attacking_move


def hugepower(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if attacking_move[constants.CATEGORY] == constants.PHYSICAL:
        attacking_move = attacking_move.copy()
        attacking_move[constants.BASE_POWER] *= 2
    return attacking_move


def guts(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if attacking_pokemon.status is not None and attacking_move[constants.CATEGORY] == constants.PHYSICAL:
        attacking_move = attacking_move.copy()
        attacking_move[constants.BASE_POWER] *= 1.5
        if attacking_pokemon.status == constants.BURN:
            attacking_move[constants.BASE_POWER] *= 2
    return attacking_move


def reckless(attacking_move, attacking_pokeon, defending_pokemon, first_move):
    if constants.RECOIL in attacking_move:
        attacking_move = attacking_move.copy()
        attacking_move[constants.BASE_POWER] *= 1.2
    return attacking_move


def rockhead(attacking_move, attacking_pokeon, defending_pokemon, first_move):
    if constants.RECOIL in attacking_move:
        attacking_move = attacking_move.copy()
        del attacking_move[constants.RECOIL]
    return attacking_move


def parentalbond(attacking_move, attacking_pokeon, defending_pokemon, first_move):
    attacking_move = attacking_move.copy()
    attacking_move[constants.BASE_POWER] *= 1.25
    return attacking_move


def tintedlens(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if is_not_very_effective(attacking_move[constants.TYPE], defending_pokemon.types):
        attacking_move = attacking_move.copy()
        attacking_move[constants.BASE_POWER] *= 2
    return attacking_move


def skilllink(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if attacking_move[constants.ID] in ['bulletseed', 'iciclespear', 'pinmissile', 'rockblast', 'tailslap', 'watershuriken']:
        attacking_move = attacking_move.copy()
        attacking_move[constants.BASE_POWER] *= 5
    return attacking_move


def waterbubble(attacking_move, attacking_pokemon, defending_pokemon, first_move):
    if attacking_move[constants.TYPE] == 'water':
        attacking_move = attacking_move.copy()
        attacking_move[constants.BASE_POWER] *= 2

    return attacking_move


ability_lookup = {
    'waterbubble': waterbubble,
    'adaptability': adaptability,
    'analytic': analytic,
    'aerilate': aerilate,
    'compoundeyes': compoundeyes,
    'contrary': contrary,
    'hustle': hustle,
    'ironfist': ironfist,
    'megalauncher': megalauncher,
    'noguard': noguard,
    'pixilate': pixilate,
    'refrigerate': refrigerate,
    'scrappy': scrappy,
    'serenegrace': serenegrace,
    'sheerforce': sheerforce,
    'strongjaw': strongjaw,
    'technician': technician,
    'hugepower': hugepower,
    'purepower': hugepower,
    'reckless': reckless,
    'rockhead': rockhead,
    'guts': guts,
    'parentalbond': parentalbond,
    'toxicboost': toxicboost,
    'speedboost': speedboost,
    'tintedlens': tintedlens,
    'skilllink': skilllink
}


def ability_modify_attack_being_used(ability_name, attacking_move, attacking_pokemon, defending_pokemon, first_move):
    ability_func = ability_lookup.get(ability_name)
    if ability_func is not None:
        return ability_func(attacking_move, attacking_pokemon, defending_pokemon, first_move)
    else:
        return attacking_move
