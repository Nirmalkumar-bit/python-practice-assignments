# Task: Implement repeat_char(ch, times) to return ch repeated 'times' times.
# Implement box_line(width) that calls repeat_char('-', width) and wraps with '+' at ends.
# Example: width=4 -> "+----+"
# Expected outcome: print(box_line(4)) outputs exactly: +----+

def repeat_char(ch, times):
    return ch * times

    # TODO
    pass


def box_line(width):
    return "+" + repeat_char("-", width) + "+"
    # TODO: call repeat_char('-', width)


print(box_line(4))
