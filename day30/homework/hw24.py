def swap_case_each_letter(text):

    result = ""

    for char in text:
       
        if char.isupper():
           
            result += char.lower()

        else:

            result += char.upper()

            return result
        
text = "PrInT tHiS iN a DiFfErEnT cAsE"
result = swap_case_each_letter(text)
print(result)  