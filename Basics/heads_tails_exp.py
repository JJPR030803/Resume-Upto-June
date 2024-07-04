import random
number_of_streaks = 0
monedas = [] 


for experimentNumber in range(10000):
# Generate the coin flips
    for i in range(100):
        monedas.append(random.randint(0, 1))
    for i in range(6, 100):
    # Get the last 6 flips
        if monedas[i] == monedas[i-1] == monedas[i-2] == monedas[i-3] == monedas[i-4] == monedas[i-5]:
            print(monedas[i],monedas[i-1],monedas[i-2],monedas[i-3],monedas[i-4],monedas[i-5])
            number_of_streaks += 1

print(f"Number of streaks: {number_of_streaks}")

