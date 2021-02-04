def lengthOfLongestSubstring(s):
    ans = 0
    for i in range(len(s)):
        build_set, counter, j = set(), 0, i
        while j < len(s) and s[j] not in build_set:
            counter += 1
            build_set.add(s[j])
            j += 1
        ans = max(ans, counter)

    return ans


dict = {}
dict[0] = 1
dict[1] = 11
dict[2] = 40

# print(max(dict.values()))

print(lengthOfLongestSubstring('abcabcbb'))


