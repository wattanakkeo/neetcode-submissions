class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #use a map to store what we NEEDMAP and what we need WINDOW
        #populate HAVE map
        #loop R thru S
            #populate the WINDOW
            #check if char at R is in NEEDMAP and R at WINDOW == R at NEEDMAP
                #HAVECOUNT++

            #while HAVECOUNT >= NEEDCOUNT
                #if (R - L + 1) > RESLEN
                    #RES = [L, R]
                    #RESLEN = R - L + 1
                #if WINDOW at L in NEEDMAP
                    #HAVECOUNT--
                #L++
        #L, R = res
        #return [L:R+1] if HAVECOUNT != "infinity"
        
        needMap, window = {}, {}

        for c in t:
            needMap[c] = needMap.get(c, 0) + 1
        
        haveCount, needCount = 0, len(needMap)
        resLen = float("infinity")
        res = [-1, -1]
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if (c in needMap and window[c] == needMap[c]):
                haveCount += 1
            while haveCount >= needCount:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in needMap and needMap[s[l]] > window[s[l]]:
                    haveCount -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""

