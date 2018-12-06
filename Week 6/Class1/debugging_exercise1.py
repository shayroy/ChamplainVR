"""DEBUGGING EXERCISE 1
Expected result
Expected BMI values are 21.604938, 22.160665 and 51.903114.
Step 1
Copy the code and run the application and make note of the problem(s). There will be two distinct problems.
Step 2
Place a debugging breakpoint at line 8. Investigate the values weight and height. Allow the process to run through
these 3 times by pressing play. What do you notice? How do you fix this?
Step 3
Place a debugging breakpoint at line 4. Again, Investigate the values weight and height. What is this problem
now? How do you fix it?
Brendan said there are two bugs. The first was [0] after patients, and the second was the order of height, weight
in the function. He did not show us %f, which is another way to format printing. It would be more familiar to us to
use {0}".format(bmi))"""

patients = [[70, 1.8], [80, 1.9], [150, 1.7]]
def calculate_bmi(height, weight):
    return weight / (height ** 2)
for patient in patients:
    weight, height = patient
    bmi = calculate_bmi(height, weight)
    print("Patient's BMI is: %f" % bmi)