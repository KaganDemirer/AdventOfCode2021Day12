with open("12_Advent.txt") as input_file:
    lines = input_file.readlines()

connections = []
points = 0
ways = []

for x in lines:
    x = x.replace("\n","").split("-")
    connections.append(x)
    connections.append([x[1],x[0]])

print(connections)

def gofrom(begin, visited):
    visited_new = visited.copy()
    global points
    if begin in visited_new and begin == begin.lower():
        print("I was in", begin, "so I go back")
        return "visited once"
    visited_new.append(begin)
    if begin == "end":
        points += 1
        print("I finished so I get one point and go back")
        ways.append(visited_new)
        return True
    for x in connections:
        if x[0] == begin:
            print("I am", begin, "and I go to", x[1], "   My Path was:", visited_new)
            gofrom(x[1], visited_new)

def gofrom_new(begin, visited, twice):
    visited_new = visited.copy()
    twice_new = twice
    global points
    if begin in visited_new and begin == begin.lower() and twice_new==False:
        return "visited once"
    elif begin in visited_new and begin == begin.lower() and twice_new:
        if begin == "start" or begin == "end":
            return "visited once"
        twice_new=False
    visited_new.append(begin)
    if begin == "end":
        points += 1
        ways.append(visited_new)
        return True
    for x in connections:
        if x[0] == begin:
            gofrom_new(x[1], visited_new, twice_new)

gofrom_new("start",[],True)

for x in ways:
    print(x)
print(points)