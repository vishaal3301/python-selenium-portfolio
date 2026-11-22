# User define exception
class InvalidAgeError(Exception):
	"""Raised when an age is outside the accepted range."""


def check_age(age):
	if age < 0:
		raise InvalidAgeError("Age cannot be negative.")
	print(f"Age {age} is valid.")


try:
	check_age(-10)
except InvalidAgeError as error:
	print(f"Error: {error}")
