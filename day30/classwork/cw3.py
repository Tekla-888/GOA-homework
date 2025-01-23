def manual_swap_case(main_str):
    res=""
    for char in main_str:
        if char.islower(): res+=char.upper()
        else:
             res+=char.lower()
             print(res)

manual_swap_case('HeLLo WoRlD')
print(manual_swap_case.swapcase())