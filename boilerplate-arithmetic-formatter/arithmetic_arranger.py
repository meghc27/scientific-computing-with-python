def arithmetic_arranger(problems, results = False):

  ## checking for the format of the input
  if len(problems) > 5:
    return "Error: Too many problems."

  width = []
  operand1 = []
  operand2 = []
  operator = []
  for i,p in enumerate(problems):
    operator.append(p.split(' ')[1])
    operand1.append(p.split(' ')[0])
    operand2.append(p.split(' ')[2])
    
    if operator[i] != '+' and operator[i] !='-':
      return "Error: Operator must be '+' or '-'."
    if not(operand1[i].isnumeric() and operand2[i].isnumeric()):
      return "Error: Numbers must only contain digits."
    if len(operand1[i]) > 4 or len(operand2[i]) > 4:
      return "Error: Numbers cannot be more than four digits."

    width.append(max(len(operand1[i]), len(operand2[i])) + 2)

  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  
  for i, w in enumerate(width):
    line1 += ' ' * (w - len(operand1[i])) + operand1[i]
    line2 += operator[i] + ' ' * (w - len(operand2[i]) - 1) + operand2[i]
    line3 += '-' * w

    if i != len(width) - 1:
      line1 += ' ' * 4
      line2 += ' ' * 4
      line3 += ' ' * 4
      
    if results:
      if operator[i] == '+':
        res = int(operand1[i]) + int(operand2[i])
      else:
        res = int(operand1[i]) - int(operand2[i])
      line4 += ' ' * (w - len(str(res))) + str(res)
      if i != len(width) - 1:
        line4 += ' ' * 4
    
  
  if results:
    arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
  
  else:
    arranged_problems = line1 + '\n' + line2 + '\n' + line3
    
  return arranged_problems