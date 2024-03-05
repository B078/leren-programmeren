from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for i in range(7):
    robotArm.grab()
    for _ in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for _ in range(8):
        if i >= 6:
            break
        else:
            robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()