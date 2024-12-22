"""
# Qualification Possibility

RCP is participating in a cricket tournament where each team plays a total of 14 matches. 
To qualify for the semifinals, a team must win at least 8 matches.

The RCP team has already completed the first n matches, and the outcomes of these matches are 
given as a string s of length n. Each character in the string represents the result of a match:

* 'W' indicates that the team won the match.

* 'L' indicates that the team lost the match.

The remaining matches (if any) are yet to be played. You need to determine if it is still possible for
the RCP team to qualify for the semifinals. In other words, can RCP secure at least 8 wins by the end 
of the tournament, considering the results of the matches already played and the matches yet to be played?

Examples:

Input: n = 8, s = WLWLLLLL

Output: true

Explanation: There are 6 matches remaining, if RCP wins all 6 of them, they would win a total of 8 matches 
and they would qualify for semi-finals. As there is still a possibilty to qualify for semi-finals, we 
would return true.
"""

def isPossible(s):
    n = len(s)
    countWin = 0
    totalMatch = 14
    
    for i in range(n):
        if(s[i]=='W'):
            countWin += 1
            
    matchLeft = totalMatch - n
    if(countWin == 8):
        return True
    
    elif(countWin + matchLeft >= 8):
        return True
    
    return False

if __name__ == "__main__":
    s = "WLWLLLLL"
    print(isPossible(s))
