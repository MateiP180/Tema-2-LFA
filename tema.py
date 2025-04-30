import json

def validstring(Q, Sigma, D, q0, F, cuv):
    cuv = "~" + "~".join(cuv) + "~"
    current_states = [q0]

    for symbol in cuv:
        next_states = []

        for state in current_states:
            if symbol == '~':
                stack = [state]
                visited = set()

                while stack:
                    st = stack.pop()
                    if st not in visited:
                        visited.add(st)
                        next_states.append(st)
                        for next_st in D.get((st, '~'), []):
                            stack.append(next_st)
            else:
                next_states.extend(D.get((state, symbol), []))

        current_states = next_states

    for state in current_states:
        if state in F:
            return True
    return False



def concat(nfa1, nfa2):
    nfa = [[], [], {}, -1, []]
    n = len(nfa1[0])
    m = len(nfa2[0])

    nfa[0] = [i for i in range(n + m)]
    nfa[1] = list(set(nfa1[1]) | set(nfa2[1]))
    nfa[2] = nfa1[2]
    nfa[3] = nfa1[3]
    nfa[4] = [i + n for i in nfa2[4]]

    for transition in nfa2[2]:
        nfa[2][(transition[0] + n, transition[1])] = [i + n for i in nfa2[2][transition]]

    for q in nfa1[4]:
        key = (q, "~")
        if key in nfa[2]:
            nfa[2][key].append(nfa2[3] + n)
        else:
            nfa[2][key] = [nfa2[3] + n]
    return nfa


def star(nfa):

    n = len(nfa[0])
    nfa[0].append(n)
    nfa[2][(n, "~")] = [nfa[3]]
    nfa[3] = n
    for q in nfa[4]:
        key = (q, "~")
        if key in nfa[2]:
            nfa[2][key].append(n)
        else:
            nfa[2][key] = [n]
    
    nfa[4] = [n]
    return nfa

def plus(nfa):
    n = len(nfa[0])
    nfa[0].append(n)
    nfa[2][(n, "~")] = [nfa[3]]
    nfa[3] = n
    for q in nfa[4]:
        key = (q, "~")
        if key in nfa[2]:
            nfa[2][key].append(n)
        else:
            nfa[2][key] = [n]
    
    return nfa

def OR(nfa1, nfa2):
    nfa = [[], [], {}, -1, []]

    n = len(nfa1[0])
    m = len(nfa2[0])

    nfa[0] = [i for i in range(n + m + 1)]
    nfa[1] = list(set(nfa1[1]) | set(nfa2[1]))
    nfa[2] = nfa1[2]
    nfa[3] = n
    nfa[4] = nfa1[4] + [i + n + 1 for i in nfa2[4]]

    for transition in nfa2[2]:
        nfa[2][(transition[0] + n + 1, transition[1])] = [i + n + 1 for i in nfa2[2][transition]]
    
    nfa[2][(n, "~")] = [nfa1[3], nfa2[3] + n + 1]
    return nfa

def question(nfa):
    nfa[4].append(nfa[3])

    return nfa

with open("data.json", "r") as file:
    infile = json.load(file)
op = ".|*+?()"
priority = {
    "(" : 0, ")" : 0,
    "|" : 1,
    "." : 2,
    "+" : 3, "*" : 3, "?" : 3
}

nrgood = 0 

for test in infile:
    print(test["name"] + ": ", end="")
    string = test["regex"]
    print(string)
    i = 1
    while i < len(string):
        if string[i] not in ".|*+?)" and string[i - 1] not in ".|(":
            string = string[:i] + "." + string[i:]
        i += 1

    
    stack = []
    output = []
    for char in string:
        if char not in op:
            output.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop() 
        else:
            while stack and priority[char] < priority[stack[-1]]:
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    string = "".join(output)
    Regex = []
    for char in string:
        if char in op:
            Regex.append(char)
        else:
            nfa = [[0, 1], [char], {(0, char) : [1]}, 0, [1]]
            Regex.append(nfa)

        stack_op = []
        stack_nfa = []
        for regex in Regex:
            if regex == ".":
                nfa1 = stack_nfa.pop()
                nfa2 = stack_nfa.pop()
                nfa = concat(nfa2, nfa1)
                stack_nfa.append(nfa)
            elif regex == "|":
                nfa1 = stack_nfa.pop()
                nfa2 = stack_nfa.pop()
                nfa = OR(nfa2, nfa1)
                stack_nfa.append(nfa)
            elif regex == "*":
                nfa = stack_nfa.pop()
                nfa = star(nfa)
                stack_nfa.append(nfa)
            elif regex == "+":
                nfa = stack_nfa.pop()
                nfa = plus(nfa)
                stack_nfa.append(nfa)
            elif regex == "?":
                nfa = stack_nfa.pop()
                nfa = question(nfa)
                stack_nfa.append(nfa)
            else:
                stack_nfa.append(regex)

    nfa = stack_nfa.pop()
    Q = nfa[0]
    Sigma = nfa[1]
    D = nfa[2]
    q0 = nfa[3]
    F = nfa[4] 


 
    for word in test["test_strings"]:
        if validstring(Q, Sigma, D, q0, F, word["input"]) == word["expected"]:
            print("The result is the expected result", end="\n")
            nrgood += 1
            
        else:
            print("The result is not the expected result", end="\n")

if nrgood == 86:
    print("Everything worked as expected")
else:
    print(nrgood)
