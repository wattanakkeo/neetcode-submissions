class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #map to track the window, and char needed
        #loop r thru s
            #add into window map
            #if r in needMap and window[r] == needMap[r]
                #haveCount++
            #while  haveCount == needCount
                #if length of window < windowLen (init inf)
                    #res = min(res, r - l + 1)
                    #windowLen = r - l + 1
                #if l in needMap and window[l] < needMap[l]
                    #haveCount--
                #l++

        window, needMap = {}, {}
        windowLen = float('inf')
        l = 0
        res = [-1, -1]

        for c in t:
            needMap[c] = needMap.get(c, 0) + 1

        haveCount, needCount = 0, len(needMap)

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in needMap and window[c] == needMap[c]:
                haveCount += 1
            
            while haveCount == needCount:
                if (r - l + 1) < windowLen:
                    res = [l, r]
                    windowLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in needMap and window[s[l]] < needMap[s[l]]:
                    
                    haveCount -= 1
                l += 1
        
        l, r = res
        return s[l:r + 1] if windowLen != float('inf') else ''

                