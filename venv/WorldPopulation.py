currentPopulation = 790_000_000
rate = 0.0105

for i in range(100):
    populationIncrease = currentPopulation * rate
    currentPopulation += populationIncrease
    print(currentPopulation)