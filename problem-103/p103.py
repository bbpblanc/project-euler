import itertools
# answer: 20313839404245

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
    back = [] # [(b, c)]
    #[a, b, c] => a, ab, ac, abc, b, bc, c
    #[a, b, c, d] => a, ab, ac, ad, abc, abd, abcd, b, bc, bd, bcd, c, cd
    for b in generate_set(lst, []):
        for c in generate_set(lst, b):
            #if not is_special_sum(b, c): continue
            back.append((b, c))

    return back



def generate_candidates(lst, *, epsilon = 0):
    back = [] # [(b, c)]
    seed = lst[len(lst)//2]
    # {2, 3, 4} => {3, 5, 6,7}
    # {a, b, c, d} => {c, c+a +/- epsilon, c+b +/- epsilon, ..., c+d +/- epsilon}
    for b in range(lst[0]-epsilon, lst[0]+epsilon+1):
        if seed + b <= seed: 
            #print("ABORT", b, seed)
            continue
        #print("KEEP", b, seed)
        for c in range(lst[1]-epsilon, lst[1]+epsilon+1):
            if c <= b: continue
            for d in range(lst[2]-epsilon, lst[2]+epsilon+1):
                if d <= c: continue
                for e in range(lst[3]-epsilon, lst[3]+epsilon+1):
                    if e <= d: continue
                    for f in range(lst[4]-epsilon, lst[4]+epsilon+1):
                        if f <= e: continue
                        #back.append((seed, seed + b, seed + c, seed + d, seed + e, seed + f))
                        for g in range(lst[5]-epsilon, lst[5]+epsilon+1):
                            if g <= f: continue
                            back.append((seed, seed + b, seed + c, seed + d, seed + e, seed + f, seed + g))
    
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
    is_special_set = True
    for b_c in generate_sets(candidate):
        #if b_c[0] == (65, 87, 88): print(b_c[0], " -- ", b_c[1])
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
    print("nothing found")
else:
    renderer(candidates[values.index(min(values))])