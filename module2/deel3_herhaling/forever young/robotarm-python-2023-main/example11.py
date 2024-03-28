from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
for blokje in range(9):
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == "white":
       robotArm.moveRight()
       robotArm.drop()
    else:
        robotArm.drop()
    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()