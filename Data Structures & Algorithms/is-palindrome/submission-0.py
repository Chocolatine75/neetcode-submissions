class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.lower()
        j=len(st)-1
        i = 0
        while i < j :
            if st[i]==st[j]:
                i +=1
                j -=1
            
            else:
                a  =ord(st[i])
                if (a < ord('a') or a > ord('z')) and (a < ord('0') or a >ord('9')):
                    i+=1
                else:
                    b= ord(st[j])
                    if (b < ord('a') or b > ord('z')) and (b < ord('0') or b >ord('9')):
                        j-=1
                    else:
                        return False

        return True
