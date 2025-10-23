from classes import GameState, Player

from actions import train

# rudimentary test for train()
def test_four_trains_equal_level(gamestate: GameState):
    starting_level = gamestate.player.level
    for i in range(4):
        train(gamestate)
    ending_level = gamestate.player.level
    assert starting_level - ending_level == 1
    
def test_train_gives_quarter_xp(gamestate: GameState):
    starting_xp = gamestate.player.xp
    train(gamestate)
    ending_xp = gamestate.player.xp
    assert ending_xp - starting_xp == gamestate.player.calc_lvl_cost / 4