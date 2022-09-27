class Category:

  def __init__(self, cat):
    self.category = cat
    self.ledger = []
  
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})

  def get_balance(self):
    return sum([d['amount'] for d in self.ledger])
  
  def withdraw(self, amount, description = ""):
    funds = self.check_funds(amount)
    if funds:  
      self.ledger.append({"amount": -amount, "description": description})
    return funds

  def transfer(self, amount, cat):
    # funds = self.check_funds(amount)
    success = self.withdraw(amount, "Transfer to " + cat.category)
    if success:
      cat.deposit(amount, "Transfer from " + self.category)
    return success

  def __str__(self):
    stars = (30 - len(self.category)) // 2 * '*'
    out = stars + self.category + stars + '\n'
    for items in self.ledger:
      desc = items['description'][:23]
      amt = "{:.2f}".format(items['amount'])
      out += desc + ' ' *  (30 - len(desc) - len(amt)) + amt + '\n'
    out += "Total: " + str(self.get_balance())
    return out
  

  def check_funds(self, amount):
    return amount <= self.get_balance()

  
    

def create_spend_chart(categories):
  cat = [c.category for c in categories]
  expenditure =  [-sum([d['amount'] for d in c.ledger if d['amount'] < 0]) for c in categories]
  
  expenditure = [int(e / sum(expenditure) * 10) for e in expenditure]
  
  string = "Percentage spent by category\n"

  bars = [((e + 1) * 'o').rjust(11) for e in expenditure]

  for i, perc in enumerate(range(100,-10,-10)):
    string += str(perc).rjust(3) + '| ' 
    for j in range(len(bars)):
      string += bars[j][i] + '  '
    string += '\n'

  string += ' ' * 4 + '-' * (3 * len(cat) + 1) + '\n'

  maxima = max(len(s) for s in cat)

  cat = [c.ljust(maxima) for c in cat]

  for i in range(maxima):
    string += 5 * ' '
    for c in cat:
      string += c[i] + 2 * ' '
    if i != maxima - 1:
      string +=  '\n'
  
  return string