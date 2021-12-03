gamma_rate = ""
epsilon_rate = "" # inverse of epsilon_rate for uneven no of inputs


out = 0
with open("input.txt", "r") as f:
    lines = f.readlines()
    size = len(lines[0].strip())
    count = [0 for _ in range(size)]
    for line in lines:
        for i in range(size):
            count[i] += int(line[i]) 
    half = len(lines) // 2
    for number in count:
        gamma_rate += "1" if number > half else "0"
        epsilon_rate += "1" if number < half else "0" # what if they are equal? else epsilon_rate = ~gamma_rate

print(gamma_rate, epsilon_rate)
power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(power_consumption)