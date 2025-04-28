
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):

            from emojis import emojis
            emojized = emojis.encode (greet + " :" + sep + ": " + gname)
            print(emojized)

        return innerMostFun

    return innerFun

kanGrt = outerFun("Hello")

kanGrtTgr = kanGrt("tiger")
kanGrtLin = kanGrt("lion")
kanGrtBer = kanGrt("bear")

kanGrtTgr("Prabhakar")
kanGrtLin("Prabhakar")
kanGrtBer("Prabhakar")




"""
engGrt = outerFun("Hello")


engGrtSngArw = engGrt("----->")
engGrtDblArw = engGrt("=====>>")

engGrtSngArw("Rahul")
engGrtDblArw("Rohit")
"""