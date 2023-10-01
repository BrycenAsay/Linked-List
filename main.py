"""driver file"""
from courselist import CourseList
from course import Course

def main():
    """main function that is run"""
    with open('data.txt', 'r') as file:
        data = file.read()
        data = data.split('\n')
        lyst = CourseList()
        for values in data:
            complete_values = values.split(',')
            course = Course(*complete_values)
            lyst.insert(course)
    print(f'Current List: {lyst.size()}')
    for vals in lyst:
        print(vals)
    print('\n')
    print(f'Cumulative GPA: {lyst.calculate_gpa()}')

if __name__ == '__main__':
    main()
