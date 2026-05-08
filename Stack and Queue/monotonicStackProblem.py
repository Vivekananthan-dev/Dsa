#Given a list of daily temperatures, return an array where each element tells how many days you must wait for a warmer temperature.

def dailyTemperatures(temperature):
    n = len(temperature)
    res = [0]*n
    stack = []

    for i, temp in enumerate(temperature):
        while stack and temperature[i]>temperature[stack[-1]]:
            prev = stack.pop()
            res[prev] = i-prev
        stack.append(i)
    return res

t = list(map(int,input("Enter values: ").split()))
print(dailyTemperatures(t))