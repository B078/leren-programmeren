from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
for lengte in range(5):
    for blokje in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for rechts in range(2):
        if lengte >= 4:
            break
        else:
         robotArm.moveRight()




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()