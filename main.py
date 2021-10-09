import sys
import re
import math

SUM_ACTION = 'SUM_ACTION'
SUBSTRACTION_ACTION = 'SUBSTRACTION_ACTION'
OPERAND_ACTION = 'OPERAND_ACTION'
SQRT_ACTION = 'SQRT_ACTION'
MULTIPLICATION_ACTION = 'MULTIPLICATION_ACTION'
VARIABLE_ACTION = 'VARIABLE_ACTION'

def create_sum_action():
  return {
    "action": SUM_ACTION,
    "next_authorized_action": [OPERAND_ACTION]
  }

def create_substraction_action():
  return {
    "action": SUBSTRACTION_ACTION,
    "next_authorized_action": [OPERAND_ACTION]
  }

def create_operand_action(operand):
  return {
    "action": OPERAND_ACTION,
    "value": operand,
    "next_authorized_action": [SUM_ACTION, SUBSTRACTION_ACTION, VARIABLE_ACTION, MULTIPLICATION_ACTION]
  }

def create_variable_action(variable):
  return {
    "action": VARIABLE_ACTION,
    "value": variable,
    "next_authorized_action": [SQRT_ACTION, SUM_ACTION, SUBSTRACTION_ACTION]
  }

def create_sqrt_action(degree):
  return {
    "action": SQRT_ACTION,
    "value": degree,
    "next_authorized_action": [SUM_ACTION, SUBSTRACTION_ACTION, MULTIPLICATION_ACTION],
  }

def creation_multiplication_action():
  return {
    "action": MULTIPLICATION_ACTION,
    "next_authorized_action": [OPERAND_ACTION, VARIABLE_ACTION]
  }

def create_polynomial_term(variable, coefficient, root_degree):
  return {
    "variable": variable,
    "coefficient": coefficient,
    "root_degree": root_degree
  }

def merge_terms(terms):
  ordered_terms = {}

  for i in range(len(terms)):
    term = terms[i]

    if ordered_terms.get(term.get("root_degree")) == None:
      ordered_terms[term.get("root_degree")] = list()

    ordered_terms[term.get("root_degree")].append(term)

  merged_terms = list()
  for key, value in ordered_terms.items():
    first_item = value[0]
    for i in range(1, len(value)):
      first_item["coefficient"] += value[i]["coefficient"]
    merged_terms.append(first_item)

  return merged_terms

def lex(equation_part):
  equation_part.split()
  terms = re.split(r"(\+|\-)", equation_part)
  print(terms)

  actions = list()
  i = 0
  while i < len(terms):
    term = terms[i]
    term_value_sign_coef = 1

    if term == "+" or term == "-":
      term_value_sign_coef = 1 if term == "+" else -1
      i += 1
      term = terms[i]

    operands = re.findall(r"[0-9]+\.?[0-9]*", term)
    variables = re.findall(r"[a-zA-Z]", term)
    variable = None if len(variables) == 0 else variables[0] 

    coefficient = 1
    degree = 0

    if len(operands) > 1:
      coefficient = float(operands[0])
      degree = float(operands[1] or 0)
    else:
      coefficient =  float(operands[0]) if variable == None else 1
      degree = 0 if variable == None else float(operands[0])

    polynomial_term = create_polynomial_term(variable, coefficient * term_value_sign_coef, degree)
    actions.append(polynomial_term)

    i += 1

  return merge_terms(actions)
  #   while equation_part[i] != "*" and equation_part[i] != "+" and equation_part[i] != "-":
  #     i += 1
    
  #   if equation_part[i] == "*":
  #     term_degree = 0 if equation_part[i + 3] == None else int(equation_part[i + 3])
  #     term_value = 1 if equation_part[i - 1] == None else int(equation_part[i - 1])

  #     actions.append(create_polynomial_term(term_value, term_degree))
    
  #   if 

  # action_list = list()
  # i = 0
  # while i < len(equation_part):
  #   char = equation_part[i]
  #   last_action = None if len(action_list) == 0 else action_list[len(action_list) - 1]
  #   action = None

  #   if char == '+':
  #     action = create_sum_action()
  #   elif char == '-':
  #     action = create_substraction_action()
  #   elif char == '^':
  #     next_char = equation_part[i + 1]
  #     if next_char != None and next_char.isdigit():
  #       action = create_sqrt_action(int(next_char))
  #       i += 1
  #   elif char == '*':
  #     action = creation_multiplication_action()
  #   elif char == " ":
  #     action = None
  #   elif char.isdigit():
  #     action = create_operand_action(int(char))
  #   elif char.isalpha():
  #     action = create_variable_action(char)
    
  #   if action != None and last_action != None:
  #     in_auth_action = False
  #     for auth_action in last_action.get('next_authorized_action'):
  #       if action.get("action") == auth_action:
  #         in_auth_action = True

  #     if in_auth_action == False:
  #       return False
  #     else:
  #       action_list.append(action)
    
  #   if action != None and last_action == None:
  #     action_list.append(action)

  #   i += 1

  # return action_list
    
def parse_actions(actions):
  # ADD SECURITY
  # ORDER DE ACTIONS

  for action in actions:
    action_type = action.get("action")
    print(action)

  #   if action_type == SUM_ACTION:
      
  #   elif action_type == SUBSTRACTION_ACTION:

  #   elif action_type == TIME_ACTION:

  #   elif action_type == OPERAND_ACTION:

  #   elif action_type == VARIABLE_ACTION:

  #   elif action_type == SQRT_ACTION:

  # return

def negate_coef_list(coefficients):
  actions = list()

  for coef in coefficients:
    coef["coefficient"] = coef["coefficient"] * -1
    actions.append(coef)

  return actions

def print_reduced_form(terms):
  reduced_form = None
  for term in terms:
    if reduced_form == None:
      reduced_form = (str(term["coefficient"]) if term["coefficient"] > 0 else " - " + str(term["coefficient"] * -1)) + " * " + ("x" if term["variable"] == None else term["variable"]) + "^" + str(term["root_degree"])
    else:
      reduced_form += (" + " + str(term["coefficient"]) if term["coefficient"] > 0 else " - " + str(term["coefficient"] * -1)) + " * " + ("x" if term["variable"] == None else term["variable"]) + "^" + str(term["root_degree"])


  reduced_form += " = 0"
  print("Reduced form: " + reduced_form)

def check_polynomial_validity(terms):
  is_quadratic_or_less = True
  for term in terms:
    if term["root_degree"] > 2:
      is_quadratic_or_less = False

  if (is_quadratic_or_less == False):
    exit("The polynomial degree is stricly greater than 2, I can't solve it.")

def solve_quadratic_polynomial(terms):
  print("Polynomial degree: 2")
  a = filter(lambda x: x["root_degree"] == 2, terms)[0]["coefficient"] if len(filter(lambda x: x["root_degree"] == 2, terms)) > 0 else 0
  b = filter(lambda x: x["root_degree"] == 1, terms)[0]["coefficient"] if len(filter(lambda x: x["root_degree"] == 1, terms)) > 0 else 0
  c = filter(lambda x: x["root_degree"] == 0, terms)[0]["coefficient"] if len(filter(lambda x: x["root_degree"] == 0, terms)) > 0 else 0

  discriminant = (b*b) - (4*a*c)

  if discriminant < 0:
    exit("The solutions of this polynomial are complex")

  if discriminant == 0:
    x = -b / 2*a
    exit("x is the only solution; x = " + str(x))

  if (discriminant > 0):
    x1 = (-b - math.sqrt(discriminant)) / (2*a)
    x2 = (-b + math.sqrt(discriminant)) / (2*a)
    print("Discriminant is strictly positive, the two solutions are")
    print(x1)
    print(x2)
    exit()


# def solve_linear_polynomial(terms):

# def solve_constant_polynomial(terms):

def main():
  if len(sys.argv) < 2:
    exit("You must provide an equation")

  equation = str(sys.argv[1])
  equation_parts = map(lambda value: value.replace(" ", ""), equation.split("="))

  actions = list()
  for part in equation_parts:
    actions.append(lex(part))

  merged_actions = list()
  for index in range(len(actions)):
    if index > 0:
      merged_actions += negate_coef_list(actions[index])
    else:
      merged_actions += actions[index]

  sorted_terms = merge_terms(merged_actions)
  sorted_terms.sort(reverse=True, key=lambda x: x["root_degree"])

  print_reduced_form(sorted_terms)
  check_polynomial_validity(sorted_terms)
  solve_quadratic_polynomial(sorted_terms)

main()