def input_temperature(temp_str: str) -> int:
	return int(temp_str)


def test_temperature() -> None:
	print("Input data is '25'")
	try:
		temp = input_temperature("25")
	except Exception as error:
		print(f"Caught input_temperature error: {error}")
	else:
		print(f"Temperature is now {temp}°C\n")

	print("Input data is 'abc'")
	try:
		temp = input_temperature("abc")
	except Exception as error:
		print(f"Caught input_temperature error: {error}")
	else:
		print(f"Temperature is now {temp}°C\n")


if __name__ == "__main__":
	print("=== Garden Temperature ===")
	print()
	test_temperature()
	print()
	print("All tests completed - program didn't crash!")
