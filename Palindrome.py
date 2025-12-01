
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # we can reverse an integer in python using slicing but first we need to convert it into string bcz slicing works only for string
        
        # --> Method - 1

        # if x<0:
        #     return False
        # return str(x) == str(x)[::-1]

        # --> Method - 2 (Using while loop)
        original_num = x
        rev_num = 0
        while x > 0:
            last_digit = x % 10
            rev_num = rev_num * 10 + last_digit
            x = x//10 #remove the last digit
        return rev_num == original_num


if __name__ == "__main__":
    obj = Solution()

    x = int(input("Enter a number: "))
    result = obj.isPalindrome(x)

    if result:
        print("Palindrome")
    else:
        print("Not Palindrome")
