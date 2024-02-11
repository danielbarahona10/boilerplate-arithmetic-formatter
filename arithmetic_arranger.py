def arithmetic_arranger(problems):

  arranged_problems = ""
  
  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:
    problem = problem.split()
    if problem[1] != '+' and problem[1] != '-':
      return "Error: Operator must be '+' or '-'."
    if len(problem[0]) > 4 or len(problem[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    try:
      int(problem[0])
      int(problem[2])
    except Exception:
      return "Error: Numbers must only contain digits."
    
    length = max(len(problem[0]), len(problem[2]))+2
    spaces_first_line = length - len(problem[0])
    spaces_second_line = length - len(problem[2])-1
  
    first_line = ' '*spaces_first_line+problem[0]
    second_line = ' '*spaces_second_line+problem[2]
    third_line = '-'*length
    
    print(first_line+'\n+'+second_line+'\n'+third_line+'\n')
  
  return arranged_problems