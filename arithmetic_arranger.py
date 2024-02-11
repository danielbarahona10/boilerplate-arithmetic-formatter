def arithmetic_arranger(problems):

  arranged_problems = ""
  
  if len(problems) > 5:
    return "Error: Too many problems."
  
  a = problems[0].split(' + ')
  length = max(len(a[0]), len(a[1]))+2
  spaces_first_line = length - len(a[0])
  spaces_second_line = length - len(a[1])-1
  
  print(' '*spaces_first_line+a[0]+'\n+'+' '*spaces_second_line+a[1]+'\n'+'-'*length)
  
  return arranged_problems