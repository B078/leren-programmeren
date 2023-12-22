for uren in range(24):
    bereken_uur = uren % 12 or 12
    periode = 'AM' if uren < 12 else 'PM'

    print(f"{bereken_uur}{periode}")

    volgende_uur = (uren + 1) % 24
    volgende_periode = 'AM' if volgende_uur < 12 else 'PM'

    if volgende_uur == 0:
        print("12AM")
