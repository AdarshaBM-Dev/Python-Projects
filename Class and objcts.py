class Team:
    name = ""
    capt = "" 
    ban = 0

    def winRCBFansReview (self):
        if self.name == "RCB":
            return "Ee sala cup namde...."
        elif self.name == "CSK":
            return "Eradu sala ban agilla"

t1 = Team()
t1.name = "RCB"
t1.capt = "VK"

t2 = Team()
t2.name = "CSK"
t2.capt = "MSD"

print(t1.winRCBFansReview())
print(t2.winRCBFansReview())