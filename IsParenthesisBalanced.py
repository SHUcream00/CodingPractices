class stack():
    def __init__(self, stack = []):
        self.stack = stack

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            return False
        return self.stack[len(self.stack)-1]

    def isempty(self):
        return True if len(self.stack) == 0 else False

def checkpair(opening, closing):
    openings = ["(", "[", "{"]
    closings = [")", "]", "}"]
    if openings.index(opening) == closings.index(closing):
        return True
    return False

def isparenthesesbalanced(stringtocheck):
    openings = ["(", "[", "{"]
    closings = [")", "]", "}"]

    s = stack()

    for i in stringtocheck:
        print(i, s.stack)

        if i in openings:
            s.push(i)
        elif i in closings:
            if s.isempty() == True or checkpair(s.top(), i) == False:
                return False
            else:
                s.pop()
    print(s.isempty())
    return True if s.isempty() else False


if __name__ == "__main__":

    text = input("please type string to check: ")
    print(isparenthesesbalanced(text))
