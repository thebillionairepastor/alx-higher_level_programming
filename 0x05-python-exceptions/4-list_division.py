#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists"""
    div = []
    tmp_result = 0
    for i in range(0, list_length):
        try:
            tmp_result = my_list_1[i] / my_list_2[i]
        except TypeError:
            tmp_result = 0
            print("wrong type")
        except ZeroDivisionError:
            tmp_result = 0
            print("division by 0")
        except IndexError:
            tmp_result = 0
            print("Out of range")
        finally:
            pass
        div.append(tmp_result)
    return div
