import sys
import re
import math

def sqrt(value):
  return math.sqrt(value)

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

def get_polynomial_term(term, coef_sign):



def check_term_validity(term):
  re.findall()

def lex(equation_part):
  terms = re.split(r"(\+|\-)", equation_part)

  actions = list()
  i = 0
  while i < len(terms):
    term = terms[i]
    coef_sign = "+"

    if term == "-":
      coef_sign = "-"
      i += 1
      term = terms[i]

    polynomial_term = get_polynomial_term(term, coef_sign)

    # operands = re.findall(r"[0-9]+\.?[0-9]*", term)
    # variables = re.findall(r"[a-zA-Z]", term)
    # variable = None if len(variables) == 0 else variables[0]

    # coefficient = 1
    # degree = 0

    # if len(operands) > 1:
    #   coefficient = float(operands[0])
    #   degree = int(operands[1] or 0)
    # else:
    #   coefficient =  float(operands[0]) if variable == None else 1
    #   degree = 0 if variable == None else int(operands[0])

    # polynomial_term = create_polynomial_term(variable, coefficient * coef_sign, degree)
    actions.append(polynomial_term)

    i += 1

  return merge_terms(actions)

def negate_coef_list(coefficients):
  actions = list()

  for coef in coefficients:
    coef["coefficient"] = coef["coefficient"] * -1
    actions.append(coef)

  return actions

def print_reduced_form(terms, polynomial_degree):
  if polynomial_degree > 2:
    return

  if polynomial_degree == 0:
    reduced_form = None
    for term in terms:
      if reduced_form == None:
        reduced_form = (str(term["coefficient"]) if term["coefficient"] >= 0 else " - " + str(term["coefficient"] * -1))
      else:
        reduced_form += (" + " + str(term["coefficient"]) if term["coefficient"] >= 0 else " - " + str(term["coefficient"] * -1))
    reduced_form += " = 0"
    print("Reduced form: " + reduced_form)
  else:
    reduced_form = None
    for term in terms:
      if reduced_form == None:
        reduced_form = (str(term["coefficient"]) if term["coefficient"] > 0 else " - " + str(term["coefficient"] * -1)) + " * " + ("x" if term["variable"] == None else term["variable"]) + "^" + str(term["root_degree"])
      else:
        reduced_form += (" + " + str(term["coefficient"]) if term["coefficient"] > 0 else " - " + str(term["coefficient"] * -1)) + " * " + ("x" if term["variable"] == None else term["variable"]) + "^" + str(term["root_degree"])
    reduced_form += " = 0"
    print("Reduced form: " + reduced_form)

def get_polynomial_degree(terms):
  polynomial_degree = 0
  for term in terms:
    if term["root_degree"] > polynomial_degree:
      polynomial_degree = term["root_degree"]

  print("Polynomial degree: " + str(polynomial_degree))
  return polynomial_degree

def solve_basic_equation(terms):
  x = terms[0]["coefficient"]

  if x != 0:
    print("This nomial is not solvable")
    exit(str(x) + " != 0")

  exit(str(x) + " = 0")

def solve_linear_polynomial(terms):
  x_coefficient = [x for x in terms if x["root_degree"] == 1][0]["coefficient"]
  constant_term = [x for x in terms if x["root_degree"] == 0][0]["coefficient"]

  solution = 0
  if x_coefficient > 1:
    solution = -constant_term / x_coefficient
  else:
    solution = -constant_term

  print("There is one solution to this linear equation:")
  print(solution)

def solve_quadratic_polynomial(terms):
  a = [x for x in terms if x["root_degree"] == 2][0]["coefficient"] if len([x for x in terms if x["root_degree"] == 2]) > 0 else 0
  b = [x for x in terms if x["root_degree"] == 1][0]["coefficient"] if len([x for x in terms if x["root_degree"] == 1]) > 0 else 0
  c = [x for x in terms if x["root_degree"] == 0][0]["coefficient"] if len([x for x in terms if x["root_degree"] == 0]) > 0 else 0

  discriminant = (b*b) - (4*a*c)

  if discriminant < 0:
    print("Discriminant strictly negative (" + str(discriminant) + "), the two solutions are complexes:")
    x1 = (-b - sqrt(discriminant * -1)) / (2*a)
    x2 = (-b + sqrt(discriminant * -1)) / (2*a)
    print(str(x1) + "i")
    print(str(x2) + "i")
    exit()

  if discriminant == 0:
    x = -b / 2*a
    exit("x is the only solution; x = " + str(x))

  if (discriminant > 0):
    x1 = (-b - sqrt(discriminant)) / (2*a)
    x2 = (-b + sqrt(discriminant)) / (2*a)
    print("Discriminant strictly positive (" + str(discriminant) + "), the two solutions are:")
    print(x1)
    print(x2)
    exit()

def main():
  if len(sys.argv) < 2:
    exit("You must provide an equation")

  equation = str(sys.argv[1])
  equation_parts = map(lambda value: value.replace(" ", ""), equation.split("="))

  terms = list()
  for part in equation_parts:
    terms.append(lex(part))

  merged_actions = list()
  for index in range(len(terms)):
    if index > 0:
      merged_actions += negate_coef_list(terms[index])
    else:
      merged_actions += terms[index]

  sorted_terms = merge_terms(merged_actions)
  sorted_terms.sort(reverse=True, key=lambda x: x["root_degree"])

  polynomial_degree = get_polynomial_degree(sorted_terms)
  if polynomial_degree > 2:
    exit("The polynomial degree is stricly greater than 2, I can't solve it.")

  print_reduced_form(sorted_terms, polynomial_degree)
  if polynomial_degree == 0:
    solve_basic_equation(sorted_terms)
  elif polynomial_degree == 1:
    solve_linear_polynomial(sorted_terms)
  elif polynomial_degree == 2:
    solve_quadratic_polynomial(sorted_terms)

main()