class A:
    def reverse(self,n):
        s=str(n)
        return int(s[::-1])
class B(A):
    def palindrome(self,n):
        if self.reverse(n)==n:
            return "palindrome"
        else:
            return "not palindrome"
print(B().palindrome(121))



class A:
    def reverse(self,n):
        s=str(n)
        return s[::-1]
class B(A):
    def palindrome(self,n):
        if self.reverse(n)==n:
            return "palindrome"
        else:
            return "not palindrome"
print(B().reverse(121))