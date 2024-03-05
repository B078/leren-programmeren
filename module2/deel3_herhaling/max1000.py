total_sum = 0
current_number = 51 
trede = 1

while total_sum <= 1000:
    total_sum += current_number
    som = " + ".join([str(i) for i in range(50, current_number + 1)])
    print(f"{trede}. {som} = {total_sum}")
    current_number += 1
    trede += 1