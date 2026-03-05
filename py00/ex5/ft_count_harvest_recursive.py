def ft_count_harvest_recursive():
    count = int(input("Days until harvest: "))

    def helper(day):
        if day > count:
            print("Harvest time!")
            return
        print("Day", day)
        helper(day + 1)
    helper(1)
