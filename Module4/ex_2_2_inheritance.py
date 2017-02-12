class Master1(object):
    pass

class Master2(object):
    pass

class Edureka(Master1,Master2):
    course = "Mastering Python"
    startDate = "04th June 2016"

if __name__ == "__main__":
    print Edureka.__bases__

