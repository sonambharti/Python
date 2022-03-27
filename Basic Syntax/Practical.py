#single astric in formal arguement is used to take inputs as tuples

def WelcomeUsers(*user):
    #print(user)
    for i in user:
        print(i)

#calling Function
WelcomeUsers('ram','umar','abhay')
WelcomeUsers('ram','umar')
WelcomeUsers('ram','umar','abhay','rajeev','subham')