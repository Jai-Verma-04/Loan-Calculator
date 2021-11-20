principal = int(input("Enter Loan Amount: "))
rate = float(input("Enter Rate of interest: "))/12/100
tenure = int(input("Enter the loan tenure(in years): "))*12
div1 = (1+rate)**tenure
div2 = ((1+rate)**tenure) - 1
mulltiply_by = principal*rate

print("-------------------------------------")

EMI_per_month = mulltiply_by*(div1/div2)
print("Monthly EMI Payment: Rs.",round(EMI_per_month, 2))

intereset_per_month = EMI_per_month - (principal/tenure)
print("Interest per month: Rs.",round(intereset_per_month, 2))

Total_amount = EMI_per_month*tenure
print("Total amount payable: Rs.",round(Total_amount,2))

Total_interest_amount = Total_amount-principal
print("Total interest to be paid: Rs.", round(Total_interest_amount,2))

print("-------------------------------------")
