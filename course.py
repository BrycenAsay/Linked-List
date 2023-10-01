"""course.py is a python file with the intent of constructing a course node object for a linked list"""
class Course:
    """this class is to init a course"""
    def __init__(self,number=0,name="",credit_hr=0.0,grade=0.0,next=None):
        """initalizes class variables and tests if variables are valid, otherwise throws value error"""
        if not str(number).isnumeric():
            raise ValueError
        if int(number) < 0:
            raise ValueError
        self._number = int(number)

        if isinstance(name, str):
            self._name = str(name)
        else:
            raise ValueError

        if float(credit_hr) < 0:
            raise ValueError
        if isinstance(credit_hr, float):
            self._credit_hr = credit_hr
        elif str(credit_hr).replace('.', '').isnumeric():
            self._credit_hr = float(credit_hr)
        else:
            raise ValueError

        if float(grade) < 0:
            raise ValueError
        if isinstance(grade, float):
            self._grade = grade
        elif str(grade).replace('.', '').isnumeric():
            self._grade = float(grade)
        else:
            raise ValueError
        
        self.next = next

    def number(self):
        """inits the number (e.g. 2420 in cs2420) for the course object"""
        return self._number
    def name(self):
        """inits the name (e.g. introduction to computers) for the course object"""
        return self._name
    def credit_hr(self):
        """inits the credit horus (e.g. 3 credit hours) for the course object"""
        return self._credit_hr
    def grade(self):
        """inits the grade (e.g. 3.7) for the course object"""
        return self._grade
    def __str__(self):
        sn = str(self.number())
        sg = str(self.grade())
        str_cred_hr = str(self.credit_hr())
        """returns a representation of the course that is easy to read for user convienece"""
        return 'cs' + sn + ' ' + self.name() + ' Grade:' + sg + ' Credit Hours: ' + str_cred_hr
