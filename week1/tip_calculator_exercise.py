bill_str=input("Please enter the bill amount: ")
bill=float(bill_str)
tip_str=input("Please enter the tip percentage: ")
tip=float(tip_str)


print(f"Tip Percentage: {tip:.2f} % \nTip Amount= ${(tip/100)*bill:.2f} \nTotal= ${bill+(tip / 100)*bill:.2f}")
#:.2f to make sure it shows two decimal places.
#:.0f would show zero decimal places and will approximate to the nearest number