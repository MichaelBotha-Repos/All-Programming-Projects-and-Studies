'''
import random

class Lottery:
  def shuffle(self):
    results = []
    for i in range(5):
      results.append(random.randint(1, 20))
    return results

Use the Lottery class above as the parent class. Create the PowerBall class as a child class of Lottery.
Override the shuffle method so that it returns a list of six random integers between 1 and 99.
'''
import random

class Lottery:
  def shuffle(self):
    results = []
    for i in range(5):
      results.append(random.randint(1, 20))
    return results

class PowerBall(Lottery):
    def shuffle(self):
        results = []
        for i in range(5):
          results.append(random.randint(1, 99))
        return results

ticket1 = Lottery()
ticket2 = PowerBall()
for lst in [ticket1.shuffle(), ticket2.shuffle()]:
    for num in lst:
        print(num)
