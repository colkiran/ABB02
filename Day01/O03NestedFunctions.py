def outerFun():
    gname = "Sachin"        # Local Variable

    def innerFun():

        nonlocal gname      # only local variables can be converted to nonlocal
        gname += " Tendulkar"
        print("Hello World......")
        print(f"Greetings Mr.{gname}")

    innerFun()
    print(f"outerFun :{gname}")

outerFun()

