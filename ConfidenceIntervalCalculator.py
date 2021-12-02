# This is the Statistic Calculator, for confidence intervals and hypothesis testing!
from math import *

problem = input("What problem would you like to solve?")

if problem == "Confidence Interval":
    def confidence_interval():
        print("This is to find out the confidence interval for a dataset.")
        confidence_interval = input("What is the confidence interval? ")
        total_number = input("What is the total number? ")
        working_number = input("What is the number that is successful? ")

        if confidence_interval == "90":
         critical_value = 1.645

       if confidence_interval == "95":
        critical_value = 1.96

        if confidence_interval == "80":
        critical_value = 1.28


        p_hat = int(working_number) / int(total_number)
        oneminus_phat = 1 - float(p_hat)

        standard_error = sqrt(float(p_hat * float(oneminus_phat) / int(total_number)))

        margin_error = float(critical_value) * float(standard_error)

        lower_interval = float(p_hat) - float(margin_error)
        upper_interval = float(p_hat) + float(margin_error)

        print("I am " + str(confidence_interval) + "% confident that the interval from " + str(
                round(lower_interval, 4)) + " to " + str(round(upper_interval, 4)) + "finish with problem information.")
    else
