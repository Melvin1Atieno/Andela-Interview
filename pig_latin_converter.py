
def pig_latin_converter(string_parameter):
    pig_latin = True
    for current_value in string_parameter:
        if current_value.isdigit():
            index_of_current_value = string_parameter.index(current_value)
            for next_value in string_parameter[index_of_current_value+1:]:
                if next_value.isdigit():
                    index_of_next_value = string_parameter.index(next_value)
                    total = int(current_value) + int(next_value)
                    if total == 10:
                        question_mark_count = string_parameter.count('?',index_of_current_value,index_of_next_value)
                        if not pig_latin and len(string_parameter[index_of_next_value:]) < 1:
                            return False
                        if pig_latin and len(string_parameter[index_of_next_value:]) < 1:
                            return True
                        if question_mark_count == 3 and len(string_parameter[index_of_next_value:])> 1:
                            pig_latin = True
                            new_string_parameter = string_parameter[index_of_next_value:]
                            pig_latin_converter(new_string_parameter)
                        if question_mark_count != 3:
                             return False
   

print(pig_latin_converter("5??aaaaaaaaaaaaaaaaaaa?5???5"))
# print(len('5???5'))
