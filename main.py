@namespace
class SpriteKind:
    Finish = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    carnival.on_game_over_expanded(winTypes.MULTI)
sprites.on_overlap(SpriteKind.player, SpriteKind.Finish, on_on_overlap)

def on_player2_button_a_pressed():
    myHorse2.x += 1.5
    myHorse2.start_effect(effects.hearts, 100)
    info.player2.change_score_by(1)
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_player4_button_a_pressed():
    myHorse4.x += 1.5
    myHorse4.start_effect(effects.fountain, 100)
    info.player4.change_score_by(1)
controller.player4.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player4_button_a_pressed)

def on_player1_button_a_pressed():
    myHorse1.x += 1.5
    myHorse1.start_effect(effects.spray, 100)
    info.player1.change_score_by(1)
controller.player1.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player1_button_a_pressed)

def on_player3_button_a_pressed():
    myHorse3.x += 1.5
    myHorse3.start_effect(effects.confetti, 100)
    info.player3.change_score_by(1)
controller.player3.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player3_button_a_pressed)

myHorse4: Sprite = None
myHorse3: Sprite = None
myHorse2: Sprite = None
myHorse1: Sprite = None
scene.set_background_color(8)
scene.set_background_image(assets.image("""
    bgFrame
"""))
myHorse1 = sprites.create(img("""
        ........................bc....
            ......................bcccc...
            ......................cccccc..
            ....................cccccccc..
            .........cccccb....cccccccccc.
            .......bccccccccccccccccc.bccc
            .....ccccccccccccccccccc...bbc
            ...bccbcccccccccccccccc.......
            ccccc...ccccccccccccccb.......
            .ccc....bcccccccccccccc.......
            .........bccc..ccccccccc......
            ..........ccc....cccccccc.....
            ..........bccc.....ccc..bc....
            ..........cbcc......cc...cb...
            ..........b.bcc...ccc....bcb..
            ..............cc..bc..........
    """),
    SpriteKind.player)
myHorse1.set_position(20, 15)
myHorse2 = sprites.create(img("""
        ........................42....
            ......................42222...
            ......................222222..
            ....................22222222..
            .........222224....2222222222.
            .......422222222222222222.4222
            .....2222222222222222222...442
            ...42242222222222222222.......
            22222...222222222222224.......
            .222....422222222222222.......
            .........4222..222222222......
            ..........222....22222222.....
            ..........4222.....222..42....
            ..........2422......22...24...
            ..........4.422...222....424..
            ..............22..42..........
    """),
    SpriteKind.player)
myHorse2.set_position(20, 34)
myHorse3 = sprites.create(img("""
        ........................67....
            ......................67777...
            ......................777777..
            ....................77777777..
            .........777776....7777777777.
            .......677777777777777777.6777
            .....7777777777777777777...667
            ...67767777777777777777.......
            77777...777777777777776.......
            .777....677777777777777.......
            .........6777..777777777......
            ..........777....77777777.....
            ..........6777.....777..67....
            ..........7677......77...76...
            ..........6.677...777....676..
            ..............77..67..........
    """),
    SpriteKind.player)
myHorse3.set_position(20, 57)
myHorse4 = sprites.create(img("""
        ........................54....
            ......................54444...
            ......................444444..
            ....................44444444..
            .........444445....4444444444.
            .......544444444444444444.5444
            .....4444444444444444444...554
            ...54454444444444444444.......
            44444...444444444444445.......
            .444....544444444444444.......
            .........5444..444444444......
            ..........444....44444444.....
            ..........5444.....444..54....
            ..........4544......44...45...
            ..........5.544...444....545..
            ..............44..54..........
    """),
    SpriteKind.player)
myHorse4.set_position(20, 77)
finish = sprites.create(assets.image("""
    finish
"""), SpriteKind.Finish)
finish.set_position(150, 50)
textSprite2 = textsprite.create("Horse Race")
textSprite2.set_position(80, 108)