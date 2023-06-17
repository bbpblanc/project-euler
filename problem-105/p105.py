import itertools
# answer: 73702



def is_special_sum(b, c):
 #   print(b, " -- ", c)
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


def generate_sets(lst):
    back = [] # [(b, c)]
    #[a, b, c] => a, ab, ac, abc, b, bc, c
    #[a, b, c, d] => a, ab, ac, ad, abc, abd, abcd, b, bc, bd, bcd, c, cd
    for b in generate_set(lst, []):
        for c in generate_set(lst, b):
            #if not is_special_sum(b, c): continue
            back.append((b, c))

    return back


special_sum_sets = []
with open("./0105_sets.txt") as fh:
    lst = []
    cpt = 0
    for line in fh.readlines():
        #if cpt == 2: break
        candidates = sorted([int(x) for x in line.strip().split(',')])
        #candidates = [42, 65, 75, 81]
        is_special_set = True
        for b_c in generate_sets(candidates):
           #if b_c[0] == (65, 87, 88): print(b_c[0], " -- ", b_c[1])
           if not is_special_sum(b_c[0], b_c[1]):
               is_special_set = False
               #print("STOP:", b_c[0], " -- ", b_c[1])
               break
        
        if is_special_set: special_sum_sets.append(candidates)
        #print(candidates)
        cpt += 1
        
print(sum([sum(x) for x in special_sum_sets]))
