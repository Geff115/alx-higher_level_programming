#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        temp = 0
        try:
            if (not isinstance(my_list_1[i], (int, float)) or
                    not isinstance(my_list_2[i], (int, float))):
                print("wrong type")
                result.append(0)
            else:
                temp = my_list_1[i] / my_list_2[i]
                result.append(temp)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        except TypeError:
            print("invalid type")
            result.append(0)
    return (result)
