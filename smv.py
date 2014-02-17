# Example Preference Lists, Greater Value = Higher Preference
men   = {"1":{"A":4, "C":3, "B":2}, \
         "2":{"C":4, "A":3, "B":2}, \
         "3":{"A":4, "C":3, "B":2}}
women = {"A":{"2":4, "1":3, "3":2}, \
         "B":{"1":4, "2":3, "3":2}, \
         "C":{"1":4, "2":3, "3":2}}

# WOMEN MUST BE FIRST AND CANNOT CHANGE POSITION. (Its not robust, but this is just a little project for fun.)
pairing = (("A","1"),("B", "2"),("C","3"))

# Pretty self-explanatory
def is_stable(m, w, p):
    for i in p:
        for j in p:
            if not i == j:
                if w[i[0]][i[1]] < w[i[0]][j[1]] and m[j[1]][j[0]] < m[j[1]][i[0]]:
                    return False
    return True

# Pretty self-explanatory
def find_all_rogue_pairs(m, w, p):
    rogues = []
    for i in p:
        for j in p:
            if not i == j:
                if w[i[0]][i[1]] < w[i[0]][j[1]] and m[j[1]][j[0]] < m[j[1]][i[0]]:
                    rogues.append((i[0], j[1]))
    return rogues

# Swap the pairs in p such that ab is a pair in p.
def swap(ab, p):
    o = []
    s = ""
    t = ""
    for j in p:
        if j[0] == ab[0]:
            s = j[1]
        if j[1] == ab[1]:
            t = j[0]
    for i in p:
        if i[0] == ab[0]:
            o.append(ab)
        elif i[0] == t:
            o.append((t, s))
        else:
            o.append(i)
    return tuple(o)

# Generate Graph of Pairings as Nodes, Rogue Pairs as edges.
graph = {}
def populate_graph(g, m, w, p):
    g[p] = {}
    g[p]["marked"] = False
    r = find_all_rogue_pairs(m, w, p)
    for c in r:
        pn = swap(c, p)
        g[p][c] = pn
        if not pn in g:
            populate_graph(g, m, w, pn)

populate_graph(graph, men, women, pairing)

# Depth-First Search
def find_cycles(g, p):
    g[p]["marked"] = True
    o = False
    for k in g[p]:
        if not k == "marked":
            if g[g[p][k]]["marked"] == False:
                o = find_cycles(g, g[p][k])
            elif g[g[p][k]]["marked"] == True:
                return True
    return o

