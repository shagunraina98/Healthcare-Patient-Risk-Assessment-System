name = input("Enter Patient Name: ")
age = int(input("Enter Age: "))
temperature = float(input("Enter Body Temperature (°C): "))
heart_rate = int(input("Enter Heart Rate (BPM): "))
oxygen = int(input("Enter Oxygen Level (SpO2): "))

print("\n----- Patient Report -----")
print("Patient Name:", name)

if oxygen < 0 or oxygen > 100:
    print("Invalid Oxygen Level")
elif temperature < 30 or temperature > 45:
    print("Invalid Temperature")
elif oxygen < 90 or temperature > 40:
    print("Risk Level: Critical")
    print("Recommendation: Immediately transfer the patient to ICU.")
elif (90 <= oxygen <= 94) or (38 <= temperature <= 40):
    print("Risk Level: High")
    print("Recommendation: Doctor consultation and hospital admission required.")
elif heart_rate > 100 or age > 60:
    print("Risk Level: Medium")
    print("Recommendation: Keep the patient under observation.")
else:
    print("Risk Level: Low")
    print("Recommendation: Patient is healthy and can go home after consultation.")
if age >= 75:
  print("Senior Citizen")
  print("Priority Consultation Required")