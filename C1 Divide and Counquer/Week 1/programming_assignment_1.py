# programming_assignment_1 (gradeschool multiplication algorithm)
class multiplication:

    def naive_multiply(self, num1: str, num2: str) -> str:
        ## if either of the numbers are 0, return 0
        if num1 == '0' or num2 == '0':
            return '0'

        ## find n, size of the answer from n size of the input
        ## initialize array of index n to hold answer 
        n = len(num1) + len(num2)
        answer = [0] * n

        ## reverse string array of integers to multiply
        first_num = num1[::-1]
        sec_num = num2[::-1]

        for j, digit2 in enumerate(sec_num):
            for i, digit1 in enumerate(first_num):
                num_zeros = i+j
                carry = answer[num_zeros]
                partial_sum = int(digit1) * int(digit2) + carry

                answer[num_zeros] = partial_sum % 10
                answer[num_zeros + 1] += partial_sum // 10
        if answer[-1] == 0:
            answer.pop()

        return ''.join(str(digit) for digit in reversed(answer))

    def recursive_multiply(self, x: int, y: int) -> int:
        if x < 10 or y < 10: return x*y 
        if x < y: x, y, = y, x

        i, j = len(str(x)), len(str(y))
        n = min(i, j)//2
        x, y = str(x), str(y)
        x, y = x.zfill(max(i, j)), y.zfill(max(i, j))

        a, b = int(x[:i-n]), int(x[i-n:i])
        c, d = int(y[:i-n]), int(y[i-n:i])

        u = self.recursive_multiply(a, c)
        v = self.recursive_multiply((a + b), (c + d))
        w = self.recursive_multiply(b, d)

        return ( ((10**(2*n))*u) + ((10**(n))*(v-w-u)) + w)

x = 123
y = 4567
m = multiplication()
print('product:  ', f'{m.recursive_multiply(x,y):,}')