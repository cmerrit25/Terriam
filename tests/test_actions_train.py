from classes import GameState, Player

from actions import train

def test_train_gives_quarter_xp(gamestate: GameState):
    starting_xp = gamestate.player.xp  # default 100
    train(gamestate)
    assert gamestate.player.xp_gained == starting_xp / 4
    assert gamestate.player.xp == starting_xp + starting_xp / 4