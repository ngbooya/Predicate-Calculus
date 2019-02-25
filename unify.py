def remove_char(str,n):
    first_part = str[:n]
    last_part = str[n+1:]
    return first_part + last_part

def unify(E1, E2):
    E1_Variable = E1[0].isupper()
    E2_Variable = E2[0].isupper()
    SUBSET = ""
    if not E1_Variable and not E2_Variable or(len(E1) == 0 and len(E2) == 0):
        if E1[0] == E2[0]:
            E1 = remove_char(E1,0)
            E2 = remove_char(E2,0)
        else:
            print("FAIL")
            return "FAIL"
    if E1_Variable:
        if E1[0] in E2[0]:
            print("FAIL")
            return "FAIL"
        else:
            SUBSET = E2[0] + "/" + E1[0]
            return SUBSET
    if E2_Variable:
        if E2[0] in E1[0]:
            print("FAIL")
            return "FAIL"
        else:
            SUBSET = E1[0] + "/" + E2[0]
            return SUBSET
    if E1[0] == "" or E2[0] == "":
        print("FAIL")
        quit()
    else:
        HE1 = E1[0]
        HE2 = E2[0]
        SUBS1 = unify(HE1,HE2)
        if SUBS1 == "FAIL":
            print("SUBS1: FAILED")
            quit()
        temp = SUBS1.split("/")
        if temp[1] == E1[1]:
            TE1 = temp[0]
        if temp[1] != E1[1]:
            TE1 = E1[1]
        if temp[1] == E2[1]:
            TE2 = temp[0]
        if temp[1] != E2[1]:
            TE2 = E2[1]
        SUBS2 = unify(TE1,TE2)
        if SUBS2 == "FAIL":
            quit()
        else:
            print(SUBS1 + ", " + SUBS2 )

list1 = "pXX"
list2 = "pab"
unify(list1, list2)
