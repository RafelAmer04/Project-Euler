sol = 0
for a in range(0, 2):
    value = 2*a
    for b in range(0, 3):
        value += b
        if value > 2:
            break
        elif value == 2:
            sol += 1
        for c in range(0, 5):
            value += c*0.5
            if value > 2:
                break
            elif value == 2:
                sol += 1
            for d in range(0, 11):
                value += d*0.2
                if value > 2:
                    break
                elif value == 2:
                    sol += 1
                for e in range(0, 21):
                    value += e*0.1
                    if value > 2:
                        break
                    elif value == 2:
                        sol += 1
                    for f in range(0, 41):
                        value += f*0.05
                        if value > 2:
                            break
                        elif value == 2:
                            sol += 1
                        for g in range(0, 101):
                            value += g*0.02
                            if value > 2:
                                break
                            elif value == 2:
                                sol += 1
                            for h in range(0, 201):
                                value += h*0.01
                                if value > 2:
                                    break
                                if value == 2:
                                    sol += 1

print(sol)








0.01






