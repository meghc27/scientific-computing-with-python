import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
       self.contents.extend([key] * value)

  def draw(self, balls):
    if balls > len(self.contents):
      return self.contents
    balls_drawn = []

    for _ in range(balls):
      d = random.choice(range(len(self.contents)))
      # print(self.contents[d])
      balls_drawn.append(self.contents.pop(d))
    return balls_drawn
  
      

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for _ in range(num_experiments):
    hat_exp = copy.deepcopy(hat)
    balls_drawn = hat_exp.draw(num_balls_drawn)
    # print(balls_drawn)
    flag = True
    for key, value in expected_balls.items():
      if balls_drawn.count(key) < value:
        flag = False
        continue
    if flag:
      M += 1
  return M / num_experiments

  
    