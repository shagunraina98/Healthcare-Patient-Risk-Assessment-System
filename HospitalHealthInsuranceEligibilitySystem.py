name = input("Enter Patient Name: ")
age = int(input("Enter Patient Age: "))
insurance = input("Enter Insurance Status (Yes/No): ").lower()
policy = input("Enter Policy Status (Active/Expired): ").lower()
cost = float(input("Enter Estimated Treatment Cost: "))

print("\n----- Patient Insurance Report -----")
print("Patient Name:", name)

if insurance == "yes" and policy == "active" and cost <= 500000:
    print("Insurance Status: Approved")
    print("Approval Status: Approved")
    print("Decision: Patient is eligible for Cashless Treatment.")

elif insurance == "yes" and policy == "active" and cost <= 1000000:
    print("Insurance Status: Pending Approval")
    print("Approval Status: Pending")
    print("Decision: Additional approval from the insurance company is required.")

elif insurance == "yes" and policy == "expired":
    print("Insurance Status: Rejected")
    print("Approval Status: Rejected")
    print("Decision: Insurance policy has expired. Cashless treatment is not available.")

elif insurance == "no":
    print("Insurance Status: Not Available")
    print("Approval Status: Self Payment")
    print("Decision: Patient must pay the treatment cost.")

else:
    print("Invalid patient information entered.")
if age >= 65 and insurance == "yes" and policy == "active" and cost <= 500000:
    print("Senior Citizen Benefit Applied")
    print("5% Discount on Hospital Service Charges")