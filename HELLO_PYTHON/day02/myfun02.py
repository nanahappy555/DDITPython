def showDan(dan):
    print("***" + str(dan) + "단***")
    for i in range(1,9+1):
        print("{} * {} = {}".format(dan,i,dan*i))

    

showDan(5)