
import re

def main():

    E1 = ["p","X","X"]
    E2 = ["p","a","b"]
    unifyresults = []


    for count in range(len(E1)):

        print("unify(" + E1[count][0] + ", " + E2[count][0] + ")")
        E1_Variable = E1[count][0].isupper()
        E2_Variable = E2[count][0].isupper()
        # print(str(E1_Variable) + str(E2_Variable))

        if not E1_Variable and not E2_Variable or (len(E1) == 0 and len(E2)== 0):
            if E1[count] == E2[count]:
                unifyresults.append("EMPTY")
            else:
                unifyresults.append("FAIL")
        if E1_Variable:
            if E1[count] in E2[count]:
                unifyresults.append("FAIL")
            else:
                unifyresults.append(E2[count]+"/"+E1[count])
        if E2_Variable:
            if E2[count] in E1[count]:
                unifyresults.append("FAIL")
            else:
                unifyresults.append(E1[count]+"/"+E2[count])



    print(unifyresults)

main()
