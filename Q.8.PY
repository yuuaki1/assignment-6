class SumToZero:
    def __init__(self, numbers):
        self.numbers = numbers
        
    def find_triplets(self):
        result = []
        self.numbers.sort()
        for i in range(len(self.numbers)-2):
            if i > 0 and self.numbers[i] == self.numbers[i-1]:
                continue
            l, r = i+1, len(self.numbers)-1
            while l < r:
                s = self.numbers[i] + self.numbers[l] + self.numbers[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    result.append([self.numbers[i], self.numbers[l], self.numbers[r]])
                    while l < r and self.numbers[l] == self.numbers[l+1]:
                        l += 1
                    while l < r and self.numbers[r] == self.numbers[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return result

# test the class
numbers = [1, -2, 1, 0, 5, -1, -4]
s = SumToZero(numbers)
print(s.find_triplets())
