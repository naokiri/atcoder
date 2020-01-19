import copy

def get_greedy_pay(arbeits, dones, worklen):
    works = arbeits.get(worklen, [])
    done = dones.get(worklen, 0)
    if len(works) <= done:
        return -999
    else:
        return works[done]

counts, maxday = map(int, input().split())
arbeits = {}
days = set()

for i in range(counts):
    a, b = map(int, input().split())
    adays = arbeits.get(a, [])
    adays.append(b)
    adays.sort(reverse=True)
    #print("{}".format(adays))
    arbeits[a] = adays
    days.add(a)

#print("{}".format(arbeits))


rewards = [0]
plans = [{}]
for i in range(maxday):
    day = i + 1
    candlen = -1
    max_pay = -1
    for worklen in days:
        candday = day - worklen
        if candday >= 0:
            pay = get_greedy_pay(arbeits, plans[day-1], worklen)
            if max_pay < pay:
                max_pay = pay
                candlen = worklen
    if max_pay > 0:
        plan = copy.copy(plans[day-1])
        plan[candlen] = plan.get(candlen, 0) + 1
        plans.append(plan)
        reward = rewards[day - 1]
        reward = reward + max_pay
        rewards.append(reward)
    else:
        plan = copy.copy(plans[day-1])
        plans.append(plan)
        reward = rewards[day-1]
        rewards.append(reward)
    #print("{}".format(rewards))
    #print("{}".format(plans))

print("{}".format(rewards[maxday]))


