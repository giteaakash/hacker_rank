# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


s = "abcabcbb"

for idx in range(0,len(s)-1):
    print("idx--->",s[idx])
    for j in range(1,len(s)-1):
        if s[idx] == s[j]:

            print(s[:idx])
            break



abs()