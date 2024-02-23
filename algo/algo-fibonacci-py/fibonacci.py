def fibonacci(n):
  # F(n) = F(n - 1) + F(n - 2)
  # a and b relat to the F(n-1) and F(n-2)
  a = 0
  b = 1
  #c variable is a place holder
  c = 0
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
  # This starts the pattern
    while n > 1:
      c = a + b # current F(n)
      a = b # Becomes next F(n-1)
      b = c # Becomes next F(n-2)
      n = n-1 # Decrement to progress to next step
  return c

print(fibonacci(7))

#commment added
