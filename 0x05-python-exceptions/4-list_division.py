#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            if i < len(my_list_1) and i < len(my_list_2):
                try:
                    if (not isinstance(my_list_1[i], (int, float)) or
                            not isinstance(my_list_2[i], (int, float))):
                        print("wrong type")
                        result.append(0)
                    else:
                        temp = my_list_1[i] / my_list_2[i]
                        result.append(temp)
                except ZeroDivisionError:
                    result.append(0)
                    print("division by 0")
            else:
                result.append(0)
                print("out of range")
    except IndexError:
        print("out of range")
    except Exception as e:
        print("Error: {}".format(e))
    return (result)
