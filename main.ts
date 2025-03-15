input.onButtonPressed(Button.A, function on_button_pressed_a() {
    ship.move(-1)
})
function End_Sound() {
    for (let index = 0; index < 8; index++) {
        music.play(music.stringPlayable("C5 B A G F E D C ", 1200), music.PlaybackMode.UntilDone)
    }
}

input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    shoot = game.createSprite(ship.get(LedSpriteProperty.X), ship.get(LedSpriteProperty.Y))
    shoot.change(LedSpriteProperty.Brightness, 80)
    for (let index2 = 0; index2 < 4; index2++) {
        shoot.change(LedSpriteProperty.Y, -1)
        basic.pause(100)
        if (shoot.isTouching(enemy)) {
            game.addScore(1)
            enemy.delete()
            shoot.delete()
            music.play(music.tonePlayable(330, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        }
        
    }
    shoot.delete()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    ship.move(1)
})
let enemy : game.LedSprite = null
let shoot : game.LedSprite = null
let ship : game.LedSprite = null
ship = game.createSprite(2, 4)
game.setScore(0)
basic.forever(function on_forever() {
    
    enemy = game.createSprite(randint(0, 4), 0)
    enemy.change(LedSpriteProperty.Direction, 1)
    basic.pause(100)
    enemy.turn(Direction.Right, 90)
    for (let index3 = 0; index3 < 4; index3++) {
        enemy.move(1)
        basic.pause(500)
    }
    if (enemy.isTouchingEdge()) {
        enemy.delete()
    }
    
})
basic.forever(function on_forever2() {
    if (enemy.isTouching(ship)) {
        game.gameOver()
    }
    
})
basic.forever(function on_forever3() {
    if (enemy.isTouching(ship)) {
        End_Sound()
        music.stopAllSounds()
    }
    
})
