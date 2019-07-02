import string
import collections

def caesar(rotate_string, num_to_rotate_by):

  upper = collections.deque(string.ascii_uppercase)
  lower = collections.deque(string.ascii_lowercase)

  upper.rotate(num_to_rotate_by)
  lower.rotate(num_to_rotate_by)

  upper = ''.join(list(upper))
  lower = ''.join(list(lower))

  return rotate_string.translate(string.maketrans(string.ascii_uppercase, upper)).translate(string.maketrans(string.ascii_lowercase, lower))
print caesar("This is easy!", 1)
