
class Team:

    grpHead = ""

    @classmethod
    def setGrpHead(cls, gname):
        cls.grpHead = gname

    @classmethod
    def getGrpHead(cls):
        print(cls.grpHead)

Team.setGrpHead("Jack")
Team.getGrpHead()
