# easy

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<j:
            if s[i].isalpha() is False and s[i].isdigit() is False:
                i+=1
                continue
            if s[j].isalpha() is False and s[j].isdigit() is False:
                j-=1
                continue
            if s[i].lower()==s[j].lower():
                i+=1
                j-=1
            else:
                break
        return True if i>=j else False

        
if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))

