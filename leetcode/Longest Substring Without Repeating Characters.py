# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=featured-list&envId=top-interview-questions
from intake.util_tests import temp_conf
from pexpect.ANSI import term


def lengthOfLongestSubstring(s):
    longest_substring = 0
    temp_substring = ''

    # initial definition of temp_substring for comparisons, end function if s is empty
    if s:
        temp_substring = s[0]
        s = s[1:]
    else:
        return 0

    for c in s:
        if c not in temp_substring:  # Check if current char exists in temp_substring
            temp_substring += c  # Not a repeating character, add to substring
        else:  # repeating character found, perform comparison to current longest substring for possible switch

            if longest_substring < len(temp_substring):  # check for new longest substring
                longest_substring = len(temp_substring)

            # restart substring testing from last non-duplicate
            print(temp_substring)
            temp_substring = temp_substring[temp_substring.rindex(c):]
    print(temp_substring)

    # Final comparison after the loop is over with the remaining temp_substring
    if longest_substring < len(temp_substring):
        return len(temp_substring)
    return longest_substring


# s = "jbpnbwwd"  # jpbn - pnbw - wd = 4 longest substring
s = "aab"  # a - ab = 2 longest substring
# s = "aabaab!bb"  # a - ab - ba - ab! - !b - b = 3 longest substring

result = lengthOfLongestSubstring(s)
print(result)
