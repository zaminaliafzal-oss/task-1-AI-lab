class FizzBuzz:
    def __init__(self, start=1, end=100):
        self.start = start
        self.end = end
    def check_number(self, num):
        if num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        else:
            return num
    def run(self):
        for i in range(self.start, self.end + 1):
            print(self.check_number(i))
game = FizzBuzz()
game.run()