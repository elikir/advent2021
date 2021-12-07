



with open('01.txt') as f:
    fishies = [int(x) for x in f.read().split(",")]
    

    for x in range(80):
        for x in range(len(fishies)):
            fish = fishies[x]
            init = fish
            if init == 0:
                fishies[x] = 6
                fishies.append(8)
            else:
                fishies[x] = init - 1



    print(len(fishies))
