def arithmetic_arranger(problems, solution= False):
  arranged_problems=''
  if len(problems)>5:
    return("Error: Too many problems.")
  a=[]
  b=[]
  c=[]
  d=[]
  for x in problems:
    sh=x.split()[1]
    ph=x.split()[2]
    ch=x.split()[0]
    b.append(ph)
    c.append(ch)
    a.append(sh)
  for i in a:
    if i=="*" or i=="/":
      arranged_problems="Error: Operator must be '+' or '-'."
      return arranged_problems
  d=b+c
  for i in d:
    if i.isdigit()!=True:
      arranged_problems="Error: Numbers must only contain digits."

      return arranged_problems
  for i in d:
    if len(i)>4:
      arranged_problems="Error: Numbers cannot be more than four digits."
      return arranged_problems

  sum=""
  f_sum=""
  first_line=""
  second_line=""
  line_str=""
  final_string=""
  for var in problems:
    first_no=var.split()[0]
    second_no=var.split()[2]
    operator=var.split()[1]

    if(operator=="+"):
      sum=str(int(first_no)+int(second_no))
    elif (operator=="-"):
      sum=str(int(first_no)-int(second_no))

    length=max(len(first_no),len(second_no))+2
    first_obj=str(first_no).rjust(length)
    second_obj=operator+str(second_no).rjust(length-1)
    new_line=""
    rest= str(sum).rjust(length)
    for l in range(length):
      new_line+="-"

    if var !=problems[-1]:
      first_line+=first_obj+'    '
      second_line+=second_obj+'    '
      line_str+=new_line+'    '
      f_sum+=rest+'    '
    else:
      first_line+=first_obj
      second_line+=second_obj
      line_str+=new_line
      f_sum+=rest

  if solution:
    final_string=first_line+"\n"+second_line+"\n"+line_str+"\n"+f_sum
  else:
    final_string=first_line+"\n"+second_line+"\n"+line_str

  return(final_string)