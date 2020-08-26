import random

SUMMARY = "Start scores = ({s0}, {s1}).\nPlayer {w} rolls {nr} dice and gets outcomes {rv}.\nEnd scores = ({e0}, {e1})"

def describe_game(hog, hog_gui, test_number, score0, score1, goal, feral_hogs):
    strat_seed0, strat_seed1, dice_seed = run_with_seed(test_number, lambda: [random.randrange(2**32) for _ in range(3)])
    strategy0 = random_strat(strat_seed0)
    strategy1 = random_strat(strat_seed1)
    dice = get_dice(dice_seed)
    s0last, s1last, game_trace = hog_gui.trace_play(
        hog.play,
        strategy0,
        strategy1,
        score0=score0,
        score1=score1,
        dice=dice,
        goal=goal,
        say=hog.silence,
        feral_hogs=feral_hogs)

    end_of_turn = [(turn["s0_start"], turn["s1_start"]) for turn in game_trace[1:]]
    end_of_turn.append((s0last, s1last))
    summary = []
    for turn, end in zip(game_trace, end_of_turn):
        summary.append(SUMMARY.format(
            s0=turn["s0_start"],
            s1=turn["s1_start"],
            w=turn["who"],
            nr=turn["num_dice"],
            rv=turn["dice_values"],
            e0=end[0],
            e1=end[1]
        ))
    summary.append("Game Over")
    return summary

def random_strat(seed):
    """
    Makes a random strategy from based on the given seed
    """
    def random_strat(score, opponent_score):
        # Save the state of the random generator, so strategy calls don't
        # impact dice rolls.
        # using this because python's hash function is NOT CONSISTENT ACROSS OSs!!!!!!!!!!!!11!!22!!2!
        conditional_seed = score * 314159265358979 + opponent_score * 27182818284590452353602874713527 + seed * 161803398874989484820
        return run_with_seed(conditional_seed % (2 ** 32), lambda: random.randrange(0, 11))
    return random_strat

def run_with_seed(seed, fn):
    state = random.getstate()
    random.seed(seed)
    result = fn()
    random.setstate(state)
    return result

def get_dice(seed):
    def dice():
        nonlocal seed
        seed, value = run_with_seed(seed, lambda: (random.randrange(0, 2**32), random.randrange(1, 7)))
        return value
    return dice
