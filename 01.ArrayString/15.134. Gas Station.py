# Greedy,
def gs(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    total = 0
    res = 0
    for i in range(len(gas)):
        total += (gas[i] - cost[i])

        if total < 0:
            total = 0
            res = i + 1

    return res


def gasStation(gas, cost):  # Too slow On^2
    for i in range(len(gas)):
        if gas[i] == 0:
            continue
        station = (i + 1) % len(gas)  # starting with the next one
        tank = gas[i]  # initializing it with the starting gas station units
        tax = cost[i]
        while station != i and tank - tax >= 0:
            tank += gas[station] - tax
            tax = cost[station]
            station = (station + 1) % len(gas)

        if tank - tax >= 0:
            return i
    return -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
cost_too_expensive = [3, 4, 5, 2, 2]

print(gasStation(gas, cost))  # 3
print(gasStation(gas, cost_too_expensive))  # -1
print(gs(gas, cost))
print(gs(gas, cost_too_expensive))

gas2 = [5, 1, 2, 3, 4]
cost2 = [4, 4, 1, 5, 1]
print(gs(gas2, cost2))
print(gasStation(gas2, cost2))
'''
set tank to 0
loop thr gas stations
    assume each starting gas station as a answer
    check from every gas station if u can make a circle
        calculate tank at each station 
        if tank < 0: continue to next starting gas station
    if u can make a cirlce
    return that index of the gstation because it will be only one answer
if here return -1, cause looped through all and no answer
'''
