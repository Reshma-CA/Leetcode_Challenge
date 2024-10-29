class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        List2 = []
        for i in range(1,n+1):

            if n%3==0 and n%5 ==0:
                ans = "FizzBuzz"

            elif n%3==0:
                ans = "Fizz"

            elif n%5 ==0:
                ans = "Buzz"

            else:
                ans = str(i)
            output = List2.append(ans)

                

        return List2