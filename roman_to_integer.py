class Solution(object):
    def romanToInt(self, s):
        sum = 0
        i=0
        length = len(s)

        while i<length:
            if s[i] == "I":
                if i < length-1 and s[i+1] == "V":
                    sum += 4
                    i=i+2
                    continue
                elif i < length-1 and s[i+1] == "X":
                    sum += 9
                    i=i+2
                    continue
                else:
                    sum += 1
                

            elif s[i] == "V":
                sum += 5

            elif s[i] == "X":
                if i < length-1 and s[i+1] == "L":
                    sum += 40
                    i=i+2
                    continue
                elif i < length-1 and s[i+1] == "C":
                    sum += 90
                    i=i+2
                    continue
                else:
                    sum += 10
                    #i=i+2

            elif s[i] == "L":
                sum += 50

            elif s[i] == "C":
                if i < length-1 and s[i+1] == "D":
                    sum += 400
                    i=i+2
                    continue
                elif i < length-1 and s[i+1] == "M":
                    sum += 900
                    i=i+2
                    continue
                else:
                    sum += 100

            elif s[i] == "D":
                sum += 500

            elif s[i] == "M":
                sum += 1000
            i=i+1

        return sum
