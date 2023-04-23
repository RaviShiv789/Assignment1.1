# Define a variable named "raise_salary_percentage" and get the salary raise percentage from the user, Now apply the raise to an employeewith harcoded data Name= 'gaurav' existing_salary = 900 INR and print the incremented salary to the consol using function

def my_salary(existing_salary,raised_salary_percentage):    
     return (existing_salary + (existing_salary*raised_salary_percentage/100 ))

Name= 'ravi'
existing_salary = 900

raised_salary_percentage = int(input("Please enter the percentage"))
     
incrementd_salary = my_salary(existing_salary,raised_salary_percentage)
print("The incremented salary is " ,incrementd_salary )
    