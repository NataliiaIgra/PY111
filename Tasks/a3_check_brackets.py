def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    skobochka = 0
    for bracket in brackets_row:
        if bracket == "(":
            skobochka += 1
        else:
            skobochka -= 1
        if skobochka < 0:
            return False
    if skobochka == 0:
        return True
    else:
        return False
