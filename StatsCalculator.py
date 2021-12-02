# This is the Statistic Calculator, for confidence intervals.
from math import *
import scipy.stats

cvlist = [1.282, 1.440, 1.645, 1.960, 2.576, 2.807, 3.291];

problem = input("What type of problem would you like to solve?")

if problem == "Confidence Interval":
    try:
        print("You are trying to find out the confidence interval for a dataset.")
        confidence_interval = input("What is the confidence interval? ")
        total_number = input("What is the total number? ")
        working_number = input("What is the number that is successful? ")

        if confidence_interval == "90":
            critical_value = cvlist[2]
        if confidence_interval == "95":
            critical_value = cvlist[3]

        p_hat = int(working_number) / int(total_number)
        oneminus_phat = 1 - float(p_hat)

        standard_error = sqrt(float(p_hat * float(oneminus_phat) / int(total_number)))

        margin_error = float(critical_value) * float(standard_error)

        lower_interval = float(p_hat) - float(margin_error)
        upper_interval = float(p_hat) + float(margin_error)

        print("I am " + str(confidence_interval) + "% confident that the interval from " + str(
            round(lower_interval, 4)) + " to " + str(round(upper_interval, 4)) + " contains (finish using problem).")
    except NameError:
        print("We do not support this confidence interval yet.")
    except ValueError:
        print(
            "Check the order you entered your total number and successful trials. The amount of successful trials must be lower than the total trials."
            )

elif problem == "Hypothesis Test":
    sample_mean = input("What is the sample mean? ")
    pop_mean = input("What is the population mean?")
    alpha = input("What is the significance level?")
    n = input("How many subjects are in the test?")
    tailed = input("Is the test one-tailed or two-tailed?")

    z = (float(sample_mean) - float(pop_mean)) / sqrt((float(pop_mean) * (1 - float(pop_mean))) / float(n))
    p = scipy.stats.norm.sf(abs(float(z)))
    if tailed == "One":
        if float(p) > float(alpha):
            print("Since p " + "(" + str(p) + ")" + "is greater than the significance level, we fail to reject the "
                                                    "null hypothesis.")
        else:
            print("Since p " + "(" + str(p) + ")" + "is less than the significance level, we will reject the null "
                                                    "hypothesis.")
    else:
        tailedp = 2 * int(p)
        if float(tailedp) > float(alpha):
            print("Since p " + "(" + str(tailedp) + ")" + "is greater than the significance level, we fail to "
                                                          "reject the null hypothesis.")
        else:
            print("Since p " + "(" + str(tailedp) + ")" + "is less than the significance level, we will reject the "
                                                          "null hypothesis.")
else:
    print("I am sorry, this type of problem is not yet supported.")
