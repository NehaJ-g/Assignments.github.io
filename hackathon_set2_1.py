def isPallindrome(S):
    if S==S[::-1]:
        return 1
    else:
        return 0


S=input()
print(isPallindrome(S))