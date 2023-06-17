import itertools
# answer: 20313839404245
# (20, 31, 38, 39, 40, 42, 45)

def is_special_sum(b, c):
#    print(b, " -- ", c)
#    print(c)
#    print("")
    
    if sum(b) == sum(c): return False
    if len(b) > len(c):
        return sum(b) > sum(c)
    if len(c) > len(b):
        return sum(c) > sum(b)
    #print(b, " -- ", c)
    return True

def generate_set(lst, minus):
    nlst = [x for x in lst if x not in minus]
    back = []
    for size in range (1, len(nlst)+1):
       back += list(itertools.combinations(nlst, size))
    return back


def generate_set(lst, minus):
    nlst = [x for x in lst if x not in minus]
    back = []
    for size in range (1, len(nlst)+1):
       back += list(itertools.combinations(nlst, size))
    return back


def generate_sets(lst):
    return [(b,c) for b in generate_set(lst, []) for c in generate_set(lst, b)]


def generate_candidates(lst, *, epsilon = 0):
    seed = lst[len(lst)//2]
    back = [(seed,b,c,d,e,f,g)
            for b in range(seed + lst[0] - epsilon, seed + lst[0] + epsilon + 1) if  seed + b > seed
            for c in range(seed + lst[1] - epsilon, seed + lst[1] + epsilon + 1) if  c > b
            for d in range(seed + lst[2] - epsilon, seed + lst[2] + epsilon + 1) if  d > c
            for e in range(seed + lst[3] - epsilon, seed + lst[3] + epsilon + 1) if  e > d
            for f in range(seed + lst[4] - epsilon, seed + lst[4] + epsilon + 1) if  f > e
            for g in range(seed + lst[5] - epsilon, seed + lst[5] + epsilon + 1) if  g > f
        ]
    return back


def renderer(lst):
    st = ""
    for val in lst:
        st += str(val)

    print(f'{lst} -> {st}')

#lst = [2, 3, 4]
#lst = [3, 5, 6, 7]
#lst = [6, 9, 11, 12, 13]
lst = [11, 18, 19, 20, 22, 25]
candidates = []

for candidate in generate_candidates(lst, epsilon = 2):
    #print(candidate)
    is_special_set = True
    for b_c in generate_sets(candidate):
        #print(b_c[0], " -- ", b_c[1])
        if not is_special_sum(b_c[0], b_c[1]):
            is_special_set = False
            #print("STOP:", b_c[0], " -- ", b_c[1])
            break

    if is_special_set: candidates.append(candidate)

values = []
for candidate in candidates:
   values.append(sum(candidate))
   print(candidate, " -> ", sum(candidate))



if len(candidates) == 0:
    print(f"nothing found for {lst}")
else:
    renderer(candidates[values.index(min(values))])