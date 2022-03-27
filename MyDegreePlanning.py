
courses_dict={"CSC1402":["Computer Programming",4,[],-1,-2],
                  "CSC2309":["Data Analysis",3,["CSC1402"],-1,-2],
                  "EGR2201":["Introduction to Engineering and Design",2,[],30,-2],
                  "EGR2210":["Computer Aided Engineering",2,["EGR2201"],-1,-2],
                  "EGR2301":["Statics",3,["PHY1401","MTH2301"],-1,-2],
                  "EGR2302":["Engineering Economics",3,["MTH1303"],-1,-2],
                  "EGR2311":["Dynamics",3,["EGR2301"],-1,-2],
                  "EGR2312":["Mechanics of Materials",3,["EGR2301"],-1,-2],
                  "EGR2402":["Electric Circuits",4,["EGR2210","PHY1402"],-1,-2],
                  "EGR3302":["Thermodynamics",3,["EGR2311"],-1,-2],
                  "EGR3331":["Digital Design",3,["EGR2201"],-1,-2],
                  "EGR3301":["Fluid Mechanics",3,["EGR3302"],-1,-2],
                  "EGR3304":["Materials Science",3,["CHE1302"],-1,-2],
                  "EGR3305":["Signals and Systems",3,["EGR2402"],-1,-2],
                  "EGR3306":["Instrumentation and Mechatronics",3,["EGR2402","EGR3331"]],
                  "EGR3310":["Microcontrollers",3,["EGR3331"]],
                  "EGR4300":["Internship",3,["ENG2303","FRN3210"],75,125],
                  "EGR4402":["Capstone Design",4,["ENG2303","FRN3210"],105,120],'FYE1101':['First year experience 1',1,[],-1,-2],
       'FYE1102':['First year experience 2',1,['FYE1101'],-1,-2],
       'FAS0210':['Foundations for Academic Success 1',0,[],-1,-2],
       'FAS1220':['Foundation for Academic Success',2,['FAS0210'],-1,-2],
       'ENG1301':['English Composition',3 ,[],-1,-2],
       'ENG2303':['Technical writing',3 ,['ENG1301'],-1, -2],
       'FRN3210':['French',2 ,[],-1,-2],
       'COM1301':['Public Speaking',3 ,['ENG1301'],-1 ,-2],
       'XXX****SL':['Civic Engagement',1,[], 60, 90],
       'CIP1001':['Civic Engagement',0,[], 60, 90],
       'CIP1002':['Civic Engagement',0,[], 60, 90],'MTH1303':['Calculus 1 : Differential and Integral Calculus',3,[],-1, -2],
                        'MTH2301':['Multivariable Calculus',3,['MTH1303'],-1, -2],
                        'MTH2320':['Linear Algebra',3 ,['MTH2301'],-1, -2],
                        'MTH2304':['Differential Equations',3 ,['MTH2320'],-1, -2],
                        'MTH3301':['Probability and Statistics for Engineers',3 ,['MTH2301'],-1, -2],
                        'PHY1401':['Physics 1',4 ,['MTH1303'],-1, -2],
                        'PHY1402':['Physics 2',4 ,['PHY1401'],-1, -2],
                        'CHE1401':['Chemistry 1',4, [],-1, -2],
                        'CHE1302':['Chemistry 2',3 ,['CHE1401'],-1, -2]}

##print('welcome to your degree planing')
##print('First enter your credentials',end='\n')
##_id=input('enter your ID:')
##_pswrd=input('enter your password:')
##_school=input('enter your school:')
##_major=input('enter your major initial [for eg computer science(CS)]:')
semester=int(input("enter your semester's number [foe eg 1st semester is 1]:"))
total_sch=138
print('welcome to aui')

#here is the functions that return both the transcript and his cummulated credits so far and the remaining credits 
def final_transcript(codes):
    def mytranscript(codes):
        courses=''
        for c in codes:
            courses+=c
        transcript=courses.split(',')
        return transcript
    mytranscript=mytranscript(codes)
    def mysch():
        sch=0
        for course_code in mytranscript:
            sch+=int(course_code[4])
        return sch
    def remaining_sch():
        earned_sch=mysch()
        remaining_sch=total_sch-earned_sch
        return remaining_sch
    return {'transcript':mytranscript,'earned_credits':mysch(),'remaining_credits':remaining_sch()}
def checkprerequisite(course_code,courses_dict,mypassedcourses):
    prerequisite=courses_dict.get(course_code)[2]
    for element in prerequisite:
        return element in mypassedcourses

#we will combine the 2 functions in 1
def checks(course_code,courses_dict,mypassedcourses):
    min_credits=courses_dict.get(course_code)[3]
    condition=checkprerequisite(course_code,courses_dict,mypassedcourses)
    print(condition)
    if course_code in courses_dict.keys():
        earned_sch=final_transcript(codes)['earned_credits']
        if earned_sch>=min_credits:
            if condition==True or condition==None:
                return True
            elif condition==False:
                print("you do not have the prerequisite to take this course")
                course_code=input("please re-enter another course code:")
        else:
            print("you do not have the minimum credits to take this course")
            course_code=input("please re-enter another course code:")
    else:
        return True

#this is a function that creates a semester to a student by returning the list of courses and credits

def create_semester_gpa(gpa):
    if gpa>2.5:
        list_coursecode=[]
        sem_sch=0
        while sem_sch<20:
            course_code=input('enter the coursecode of the class you want to take next semester:')
            if checks(course_code,courses_dict,mypassedcourses)==True or checks(course_code,courses_dict,mypassedcourses)==None:
                list_coursecode.append(course_code)
                sem_sch=0
                for ccode in list_coursecode:
                    sem_sch+=int(ccode[4])
            else:
                print("the course you entered is invalid")
                list_coursecode.append(course_code)
                sem_sch=0
                for ccode in list_coursecode:
                    sem_sch+=int(ccode[4])
    elif gpa<2.5 and gpa>0:
        list_coursecode=[]
        sem_sch=0
        while len(list_coursecode)<4:
            course_code=input('enter the coursecode of the class you want to take next semester:')
            if checks(course_code,courses_dict,mypassedcourses)==True:
                list_coursecode.append(course_code)
                sem_sch=0
                for ccode in list_coursecode:
                    sem_sch+=int(ccode[4])
            else:
                print("the course you entered is invalid")
                course_code=input('re-enter a valid coursecode:')
    elif gpa==None:
        list_coursecode=[]
        sem_sch=0
        while sem_sch<20:
            course_code=input('enter the coursecode of the class you are take next semester:')
            if checks(course_code,courses_dict,mypassedcourses)==True:
                list_coursecode.append(course_code)
                sem_sch=0
                for ccode in list_coursecode:
                    sem_sch+=int(ccode[4])
            else:
                print("the course you entered is invalid")
                course_code=input('re-enter a valid coursecode:')                
    return {"semester's_transcript":list_coursecode,"semester's_credits":sem_sch}

#this block of code makes sure that a student with a gpa higher than 2.5 registers for a max of 20 credits unless he takes only 4 courses
#these students aren't newcomers so we have to ask for their background transcript
if semester>1:
    codes=input('Please enter the codes of the courses you took seperated by comma[for eg: ABC1234,DEF5678...etc]:')
    mypassedcourses=final_transcript(codes)['transcript']
    gpa=float(input('please enter your GPA:'))
    data=create_semester_gpa(gpa)
    print(data)
else:
    codes=input('Please enter the codes of the courses you are taking seperated by comma[for eg: ABC1234,DEF5678...etc]:')
    mypassedcourses=final_transcript(codes)['transcript']
    student_data=final_transcript(codes)
    print(student_data)



