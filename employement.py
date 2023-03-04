class employees:
    def __init__(self, name, last):
        self.name=name
        self.last=last
class supervisors(employees):
    def __init__(self,name,last,password):
        super().__init__(name,last)
        self.password=password
class chefs(employees):
    def leave_req(self,days):
        return "May I take a leave for "+str(days)+" days"
adrian=supervisors("Adrian","A","apple")
emily=chefs("Emily","E")
juno=chefs("Juno","J")

print(emily.leave_req(3))
print(adrian.password)
print(emily.name)