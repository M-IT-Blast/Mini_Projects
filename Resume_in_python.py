name = ('''\nMUSTAFA SANJIV PINJARI\n
MECHANICAL ENGINEERING GRADUATE [GATE & IPATE Qualified]\n''')
Career_objective  = ('''\nSeeking an Opportunity which allows me to utilize 
the Combination of my Technical and Management skills for  
the upliftment of Organization and Personal Growth.\n''')
Experience = ('''\nSiddhivinayak Process Equipment Pvt.Ltd, Thane — Intern
4 Weeks Training in Production Practices in Works.\n
Sports Secretary, Gymkhana Committee.
Managed 3 days sports events (12+) for 600+ participants with 45+ volunteers\n
Co-founder and Secretary, MESA.
Organized Guest  lectures,Project Exhibition, Industrial visits 
and arranged Tech fest, Annual gathering, Freshers and Farewell party. etc\n
Core Committee Member, ISHRAE Mumbai Chapter.\n'''
)
Qualification = ('''\nAnjuman-I- Islam’s M. H. Saboo Siddik COE, Mumbai— Degree in Mechanical Engineering (Mumbai University)                                  
JULY 2017 -  OCT 2020
Awarded Degree with First Class Distinction ( 8.76 CGPI) by Mumbai University \n
Government Polytechnic Thane — Diploma in Mechanical Engineering ( MSBTE )
AUG  2014 - MAY 2017
Awarded Diploma with First Class Distinction (84.18 %)\n
Gurunanak English High School, kalyan —SSC 
MAY 2014
Passed Secondary School Certificate Examination with 90.60 %\n''')
Projects = ('''\nPerformance Based Analysis of Micro Hydro Power Plant — 
CFD Analysis of Kaplan Turbine   (Delayed due to Covid crisis )
Parameterization for a Kaplan turbine of a micro hydro power plant.\n
Design and Fabrication of Fire Extinguishing Rover — 
Remote Fire fighting mini vehicle
A Solution to Prevent Direct Human contact with  the accident Zone\n
''')
Skills = ('''\nManagement Skills and Experience\n
Programming basics, Python, Sql, Java\n
Engineering Software Basic skills  (Autocad, ProE, Solidworks, Ansys Fluent) (fluid sim).\n
Systems, Applications & Products (SAP01 Training Program) in Data Processing.\n
M S Office \n
''')
Achievements = ('''\nFire Extinguishing Rover -  Consolation Prize in National Level Project Exhibition\n 
Qualified GATE 2020 with 38.01 marks and Score being 398.\n
Qualified IPATE 2020 with 43  marks out of 100.\n
''')
Languages = ('''\nBasic level of C , C ++.\n
Moderate level of Python\n''')
Contact = ('''\nMobile No - +91 8691982080
            +91 7977940899\n
Email - mspinjari7867@gamil.com\n''')


ask = input("Ask for the details: ").lower()
while ask != "":
    if "name" in ask:
        print (name)
    
    elif "career objective" in ask:
        print(Career_objective)
    
    elif "experience" in ask:
        print(Experience)

    elif "internship" in ask:
        print('''\nSiddhivinayak Process Equipment Pvt.Ltd, Thane — Intern
4 Weeks Training in Production Practices in Works.\n''')
    
    elif "qualification" in ask or "education" in ask:
        print (Qualification)

    elif "degree pointer" in ask or "degree marks" in ask:
        print ("\n8.76 cgpa (First class Distinction) \n")

    elif "diploma marks" in ask or "diploma percentage" in ask:
        print ("\n84.18 % (First class Distinction)\n ")
    
    elif "degree" in ask  and "project" in ask:
        print('''\nPerformance Based Analysis of Micro Hydro Power Plant — 
CFD Analysis of Kaplan Turbine   (Delayed due to Covid crisis )
Parameterization for a Kaplan turbine of a micro hydro power plant.\n''')

    elif "diploma" in ask and "project" in ask:
        print('''\nDesign and Fabrication of Fire Extinguishing Rover — 
Remote Fire fighting mini vehicle
A Solution to Prevent Direct Human contact with  the accident Zone\n''')

    elif "project" in ask:
        print(Projects)

    elif "programming"in ask and "skill" in ask:
        print('''\nBasic concepts of Programming\n
        Basic level of  C, Java and sql\n
        Moderate level of Python\n''')

    elif "skill" in ask:
        print(Skills)

    elif "achievements" in ask:
        print(Achievements)

    elif "programming" in ask or "language" in ask:
        print(Languages)

    elif "mobile" in ask or "phone" in ask:
        print('''\n+91 8691982080
+91 7977940899\n''' )

    elif "email" in ask or "e-mail" in ask:
        print("\nEmail :- mspinjari7867@gmail.com\n")
    
    elif "contact" in ask:
        print(Contact)

    else:
        print( "\nI will improve on this\n ")
        

    ask = input("Ask for the details: ").lower()
