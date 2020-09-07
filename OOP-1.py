""" DECORATORS IN PYTHON"""


def decdist(result):
    def distinction(marks):
        for m in marks:
            c = marks.count(m)
            if m >= 75:
                print("Wow! You've got",c,"distinction(s)")

        else:
            result(marks)

    return distinction


def decper(result):
    def percentage(marks):
        percent = (sum(marks) / 500) * 100
        print("Percentage secured:", percent, "%")
        result(marks)

    return percentage


@decdist
@decper
def result(marks):
    for m in marks:
        if m >= 32:
            pass
        else:
            print("Sorry your result is FAILED!")
            break
    else:
        print("Congratulations you're PASSED!")
        print("Your Score:", sum(marks), "out of 500")


marks = [eval(x) for x in input("Enter your marks in 5 subjects: ").split(',')]

result(marks)
