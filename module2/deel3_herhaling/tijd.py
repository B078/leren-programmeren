hour = 0  # Beginnen bij middernacht (0 uur)

while hour < 24:
    if hour < 12:
        print(f"{hour} AM")
    else:
        print(f"{hour - 12} PM")
    
    hour += 1

