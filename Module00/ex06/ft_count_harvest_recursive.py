def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count_days(days, 1)


def count_days(days, current):
    if current <= days:
        print(f"Day {current}")
        count_days(days, current + 1)
    else:
        print("Harvest time!")
