
def outerFun(greet):
    # simple curry...
    def innerFun(gname):

        # print("Hello World.....")
        print(greet, gname)

    return innerFun

engGrt = outerFun("Hello")
hndGrt = outerFun("Namaskar")


engGrt("Virat")
engGrt("Messi")

hndGrt("Jadeja")
hndGrt("Axar")