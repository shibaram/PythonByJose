import math

age = input("Please enter your age : ")

age_in_secs = int(age) * 365 * 24 * 60 * 60
msg = "You lived for : {} seconds"
print(msg.format(age_in_secs))
diff = 1003968000 - age_in_secs
print("Difference = " + str(diff))
diff_in_days = (((diff / 60) / 60) / 24)
diff_in_months = (diff_in_days / 30)

print("Difference in {} days".format(diff_in_days))
print("Difference in {} months".format(diff_in_months))