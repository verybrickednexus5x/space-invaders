#when a is pressed, move the ship left
def on_button_pressed_a():
    ship.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

#play a sound at death
def End_Sound():
    for index in range(8):
        music.play(music.string_playable("C5 B A G F E D C ", 1200),
            music.PlaybackMode.UNTIL_DONE)

#when both a and b are pressed, shoot a bullet and if the bullet hits the enemy, add a point.
def on_button_pressed_ab():
    global shoot
    shoot = game.create_sprite(ship.get(LedSpriteProperty.X), ship.get(LedSpriteProperty.Y))
    shoot.change(LedSpriteProperty.BRIGHTNESS, 80)
    for index2 in range(4):
        shoot.change(LedSpriteProperty.Y, -1)
        basic.pause(100)
        if shoot.is_touching(enemy):
            game.add_score(1)
            enemy.delete()
            shoot.delete()
            music.play(music.tone_playable(330, music.beat(BeatFraction.QUARTER)),
                music.PlaybackMode.UNTIL_DONE)
    shoot.delete()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

#on button b being pressed, move the character right
def on_button_pressed_b():
    ship.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

#create sprites
enemy: game.LedSprite = None
shoot: game.LedSprite = None
ship: game.LedSprite = None
ship = game.create_sprite(2, 4)
game.set_score(0)

#create an enemy and make sure it spawns in the right place.
def on_forever():
    global enemy
    enemy = game.create_sprite(randint(0, 4), 0)
    enemy.change(LedSpriteProperty.DIRECTION, 1)
    basic.pause(100)
    enemy.turn(Direction.RIGHT, 90)
    for index3 in range(4):
        enemy.move(1)
        basic.pause(500)
    if enemy.is_touching_edge():
        enemy.delete()
basic.forever(on_forever)

#end the game if the enemy hits the ship
def on_forever2():
    if enemy.is_touching(ship):
        game.game_over()
basic.forever(on_forever2)

def on_forever3():
    if enemy.is_touching(ship):
        End_Sound()
        music.stop_all_sounds()
basic.forever(on_forever3)
