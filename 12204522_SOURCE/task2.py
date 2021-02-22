# Individual Project - Task 2

class Employees:
    companyName = "PiedPiper"

    def __init__(self, name, emp_ID, age, gender, adress, email, depart, expr, wHours):
        self.name = name
        self.emp_ID = int(emp_ID)
        self.age = int(age)
        self.gender = gender
        self.adress = adress
        self.email = email 
        self.depart = depart
        self.expr = int(expr)
        self.wHours = float(wHours)
    # Showing employee's personal information
    def show_info(self):
        print(f"Name: {self.name}\nID: {self.emp_ID}\nAge: {self.age}\nGender: {self.gender}\nAdress: {self.adress}\nEmail: {self.email}\nDepartment: {self.depart}\nWork experience: {self.expr} years\nWorking hours: {self.wHours} per week")
    # Raising and cutting salary
    def raise_wage(self, amount):
        self.salary += amount

    def cut_wage(self, amount):
        self.salary -= amount
    # Adding and cutting working hours
    def add_wHours(self, hours):
        self.wHours += hours
    
    def cut_wHours(self, hours):
        self.wHours -= hours

    def change_dept(self, new_dept):
        self.depart = new_dept

class Designers(Employees):
    def __init__(self, name, emp_ID, age, gender, adress, email, depart, expr, wHours, skill):
        super().__init__(name, emp_ID, age, gender, adress, email, depart, expr, wHours)
        self.skills = [skill] 
        # Assignment of salaries to designers by their experience and working hours
        if self.expr >= 4 and self.wHours > 30:
            self.salary = 8000
        else:
            self.salary = 4000
    
    def show_info(self):
        super().show_info()
        print(f"Skills: {self.skills}\nSalary: {self.salary}")
    # Adding skill to the designer's skill list
    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
    # Removing the skill from that list
    def remove_skill(self, skill):
        if skill in self.skills:
            self.skills.remove(skill)
    
class Marketers(Employees):
    def __init__(self, name, emp_ID, age, gender, adress, email, depart, expr, wHours, field):
        super().__init__(name, emp_ID, age, gender, adress, email, depart, expr, wHours)
        self.fields = [field]
        # Assignment of salaries to marketers by their experience and working hours
        if self.expr >=5 and self.wHours > 20:
            self.salary = 9000
        else:
            self.salary = 7000

    def show_info(self):
        super().show_info()
        print(f"Fields: {self.fields}\nSalary: {self.salary}")

    def add_field(self, field):
        if field not in self.fields:
            self.fields.append(field)
    
    def remove_field(self, field):
        if field in self.fields:
            self.fields.remove(field)

class Engineers(Employees):
    def __init__(self, name, emp_ID, age, gender, adress, email, depart, expr, wHours, tech, lang, lvl):
        super().__init__(name, emp_ID, age, gender, adress, email, depart, expr, wHours)
        self.techs = [tech]
        self.langs = [lang]
        self.lvl = lvl
        # Assignment of salaries to engineers by their level
        if self.lvl == 'Senior':
            self.salary = 10000
        elif self.lvl == 'Middle':
            self.salary = 7500
        elif self.lvl == 'Junior':
            self.lvl = 5000
        else:
            self.salary = 2500

    def show_info(self):
        super().show_info()
        print(f"Technologies: {self.techs}\nProgramming languages: {self.langs}\nLevel: {self.lvl}\nSalary: {self.salary}")
    # Adding technology that an engineer can work with 
    def add_tech(self, tech):
        if tech not in self.techs:
            self.techs.append(tech)
    # Removing the technology
    def remove_tech(self, tech):
        if tech in self.techs:
            self.techs.remove(tech)
    # Adding one more programming language in which engineer can code 
    def add_lang(self, lang):
        if lang not in self.langs:
            self.langs.append(lang)
    # Removing the programming language 
    def remove_lang(self, lang):
        if lang in self.langs:
            self.langs.remove(lang)
        
employee1 = Designers('Jony Ive', 91191, 29, 'Male', 'Moutain View', 'joIve@mail.com', 'Product & Interface Design', 11, 29.2, 'UI')        
employee2 = Marketers('Phil Schiller', 45151, 28, 'Male', 'Palo Alto', 'phil@icloud.com', 'Marketing & Advertisement', 10, 24, 'Digital Marketing')
employee3 = Engineers('Craig Federighi', 18818, 27, 'Male', 'Cupertino', 'craig@mail.com', 'Software Development', 9, 32, 'MacOS', 'Objective-C', 'Senior')

employee1.add_skill('Web-design')
employee1.add_skill('Adobe XD')
employee1.remove_skill('UI')
employee1.cut_wHours(10)
employee1.raise_wage(1800)

employee2.change_dept('Software Advertisement')
employee2.add_field('Social Media Marketing')
employee2.cut_wage(1200)

employee3.change_dept('System Engineering')
employee3.cut_wHours(10)
employee3.add_tech('iOS')
employee3.add_lang('Swift')
employee3.raise_wage(4200)

employee1.show_info()
employee2.show_info()
employee3.show_info()