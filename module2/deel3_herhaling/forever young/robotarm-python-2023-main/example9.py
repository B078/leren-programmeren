from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')
# Jouw python instructies zet je vanaf hier:

for stapel in range(5):
    for blokje in range(stapel):
        robotArm.grab()
        for _ in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for _ in range(4 if stapel == (blokje + 1) else 5):
            robotArm.moveLeft()

        
            
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()