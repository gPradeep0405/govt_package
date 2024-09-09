def check_eligibility(gender, marital_status, annual_income):
    if gender.lower() == "female" and marital_status.lower() == "married" and annual_income < 450000:
        return True
    else:
        return False

def calculate_monthly_allowance(eligible):
    if eligible:
        return 5000
    else:
        return 0

# Example usage:
gender = input("Enter gender (Male/Female): ")
marital_status = input("Enter marital status (Single/Married): ")
annual_income = float(input("Enter family's annual income: "))

eligibility = check_eligibility(gender, marital_status, annual_income)
monthly_allowance = calculate_monthly_allowance(eligibility)

if eligibility:
    print("Congratulations! You are eligible for 'Magalir Urimai Thogai' and will receive Rs.5000 per month.")
else:
    print("Sorry, you do not meet the eligibility criteria for 'Magalir Urimai Thogai'.")
