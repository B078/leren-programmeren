# example:
def increment(nr2: float) -> float:
  return nr2 + 1

def decrement(nr2: float) -> float:
  return nr2 - 1
  
def add(nr1: float, nr2: float) -> int:
  return nr1 + nr2 

def substract(nr1: float, nr2: float) -> int:
  return nr1 - nr2

def multiply(nr1: float, nr2: float) -> int:
  return nr1 * nr2

def divide(nr1: int, nr2: int) -> int:
  try:
    result = nr1 / nr2
    return result
  except ZeroDivisionError:
    print("kan niet dor 0 delen")
    return None

