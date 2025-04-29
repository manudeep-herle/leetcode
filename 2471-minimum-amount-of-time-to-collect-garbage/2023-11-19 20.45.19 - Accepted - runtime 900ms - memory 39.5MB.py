class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel = [0] + travel
        metalMins, glassMins, paperMins = 0,0,0
        lastMetal, lastGlass, lastPaper = 0,0,0
        
        for i in range(len(garbage)):
            if "M" in garbage[i]:
                lastMetal = i
            if "G" in garbage[i]:
                lastGlass = i
            if "P" in garbage[i]:
                lastPaper = i
        
        for i in range(len(garbage)):
            if i <= lastMetal:
                metalMins += travel[i]
                metalMins += garbage[i].count("M")
            if i <= lastGlass:
                glassMins = glassMins + travel[i] + garbage[i].count("G")
            if i <= lastPaper:
                paperMins = paperMins + travel[i] + garbage[i].count("P")

        return metalMins + glassMins + paperMins

        