"""helps to implement a list to link course node objects"""
class CourseList:
    """The point of this is to implement a linked' list to hold course node objects"""
    def __init__(self, head=None, current_node=None, next_node=None, number='this is useless'):
        """inits the head"""
        self.head = head
        self.current_node = current_node
        self.next_node = next_node
        self.number = number
    def insert(self, course):
        """inserts a course object into linked list"""
        curr = self.head
        if curr is None:
            nani = course
            self.head = nani
            return
        if curr.number() > course.number():
            nani = course
            nani.next = curr
            self.head = nani
            return
        while curr.next is not None:
            if curr.next.number() > course.number():
                break
            curr = curr.next
        nani = course
        nani.next = curr.next
        curr.next = nani
        return

    def is_sorted(self):
        """looks through list, if sorted from smallest to greatest returns true otherwise returns false"""
        if self.head is not None:
            curr = self.head
        else:
            return True
        while curr.next is not None:
            if curr.number() > curr.next.number():
                return False
            curr = curr.next
        return True

    def remove(self,number):
        """removes a specific instance in the list"""
        if self.head is not None:
            curr = self.head
        if curr.number() == number:
            self.head = curr.next
            curr = None
        while curr is not None:
            if curr.number() == number:
                break
            prev = curr
            curr = curr.next
        if curr is None:
            return
        prev.next = curr.next

    def remove_all(self,number):
        """removes all instance of a course identified by the particular course number"""
        def keep_removing(_self,_number):
            if _self.head is not None:
                curr = _self.head
            if curr.number() == _number:
                _self.head = curr.next
                curr = None
            while curr is not None:
                if curr.number() == _number:
                    break
                prev = curr
                curr = curr.next
            if curr is None:
                return
            prev.next = curr.next

        def is_num_present(_self,number):
            """returns true if the course of specified number exists in the list, otherwise returns false"""
            if _self.head is not None:
                curr = self.head
            else:
                curr = None
            while curr is not None:
                if curr.number() == number:
                    return True
                curr = curr.next
            return False
        while is_num_present(self,number) is not False:
            keep_removing(self,number)

    def find(self,number):
        """finds the specific course of specified course number and returns it"""
        if self.head is not None:
            curr = self.head
        else:
            curr = None
        while curr is not None:
            if curr.number() == number:
                return curr
            curr = curr.next
        return -1

    def size(self):
        """returns the number of items in the list"""
        size_count = 0
        if self.head is not None:
            curr = self.head
        else:
            curr = None
        while curr is not None:
            size_count += 1
            curr = curr.next
        return size_count

    def print_vals(self):
        """prints the values of the list"""
        curr = self.head
        while curr is not None:
            print(curr.number())
            curr = curr.next

    def calculate_gpa(self):
        """calculates the cumulative GPA of courses in course list"""
        def size(self):
            size_count = 0
            if self.head is not None:
                curr = self.head
            else:
                curr = None
            while curr is not None:
                size_count += curr.credit_hr()
                curr = curr.next
            return size_count
        the_size = size(self)
        if the_size == 0:
            return 0.0
        all_gpas_sum = 0
        curr = self.head
        while curr is not None:
            all_gpas_sum += curr.grade() * curr.credit_hr()
            curr = curr.next
        return all_gpas_sum / the_size

    def __str__(self):
        """returns string object in a readable user-friendly format"""
        soon = str(self.number())
        soog = str(self.grade())
        sooch = str(self.credit_hr())
        return 'cs' + soon + ' ' + self.name() + ' Grade:' + soog + ' Credit Hours:' + sooch

    def __iter__(self):
        self.current_node = None
        self.next_node = self.head
        return self

    def __next__(self):
        """moves to the next node"""
        if self.next_node is None:
            raise StopIteration
        self.current_node = self.next_node
        self.next_node = self.next_node.next
        return self.current_node

def main():
    pass

if __name__ == '__main__':
    main()