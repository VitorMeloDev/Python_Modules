def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
	print("Input data is '25'")
	try:
		temp = input_temperature("25")
	except Exception as error:
		print(f"Caught input_temperature error: {error}\n")
	else:
		print(f"Temperature is now {temp}°C\n")

	print("Input data is 'abc'")
	try:
		temp = input_temperature("abc")
	except Exception as error:
		print(f"Caught input_temperature error: {error}\n")
	else:
		print(f"Temperature is now {temp}°C\n")

	print("Input data is '100'")
	try:
		temp = input_temperature("100")
	except Exception as error:
		print(f"Caught input_temperature error: {error}\n")
	else:
		print(f"Temperature is now {temp}°C\n")
	
	print("Input data is '-50'")
	try:
		temp = input_temperature("-50")
	except Exception as error:
		print(f"Caught input_temperature error: {error}\n")


if __name__ == "__main__":
	print("=== Garde Temperature Checker")
	print()
	test_temperature()
	print("All tests completed - program didn't crash!")