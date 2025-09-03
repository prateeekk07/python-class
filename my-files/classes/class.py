from faker import Faker

#create a faker instance
fake = Faker()

class student:
    def __init__(self,sid,nm,job,mob,email,addr,dob):
        self.sid = sid
        self.name = nm
        self.job = job
        self.date_of_birth = dob
        self.mobile = mob
        self.email = email
        self.address = addr

    def __str__(self):
        return f"\n{self.__dict__}"
    
    def __repr__(self):
        return str(self)

# s1 = student(nm="A",job="Test Job",mob="+91-3216549870",email="abc@abc.com",addr="Pune",dob="26-05-1996")
# s2 = student(nm="B",job="Test Job",mob="+91-8954549870",email="cef@abc.com",addr="Pune",dob="26-05-1996")
# lst = [s1,s2]
# # print(s1)
# # print(s2)
# print(lst)

def generate_students(num):
    fake = Faker()
    student_list = []
    for i in range(1,num+1):
        name = fake.name()
        email = name.replace(" ",".")
        obj = student(sid=100+i,nm=name,job=fake.job(),mob=fake.phone_number(),email=f"{email}@gmail.com",addr=fake.address(),dob=fake.date_of_birth(minimum_age=18,maximum_age=70))
        student_list.append(obj)
    return student_list

stds = generate_students(50)
print(stds)
    

# #gentrate some fake data
# fake.name()
# fake.address()
# fake.email()
# fake.phone_number()
# fake.job()
# fake.date_of_birth()

# st1 = student("prateek",salary=8500,surename="patil")
# st1.name = "abhijeet"
# print(st1.__dict__)
