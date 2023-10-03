#!/usr/bin/python3
"""
This module contains a function
which prints the exact text as
'My name is <first_name> <last_name>'
The full information about the
function(prototype, declaration and definition)
is contained its the function documentation
"""


def say_my_name(first_name, last_name=""):
  if not isinstance(first_name, str):
  raise TypeError("first_name must be a string")
  elif not isinstance(last_name, str):
  raise TypeError("last_name must be a string") 
  else:
    print("My name is {} {}".format(first_name, last_name))
