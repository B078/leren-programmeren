uur = 1

while uur <= 24:
    if uur == 12:
        bereken_uur =12
        periode = 'PM'
    else:
        bereken_uur = uur % 12
    periode = 'AM' if uur < 12 else 'PM'
    if uur == 24:
        bereken_uur = 12
        periode = 'AM'

    print(f"{bereken_uur} {periode}")

    uur += 1