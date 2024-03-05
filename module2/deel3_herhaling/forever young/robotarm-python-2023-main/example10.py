from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
# Jouw python instructies zet je vanaf hier:
rechts = 9
links = 8
blokje = 4
while blokje >= 0:
    robotArm.grab()
    for _ in range(rechts):
        robotArm.moveRight()
    robotArm.drop()
    for _ in range(links):
        robotArm.moveLeft()
    rechts -= 2
    links -= 2
    blokje -= 1



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()