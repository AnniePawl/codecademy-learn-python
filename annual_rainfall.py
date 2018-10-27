# Figure out how much it rained in the past year! Update the annual_rainfall variable to include the values from September to December.

january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall


# july_rainfall = 1.05
# annual_rainfall += july_rainfall
# august_rainfall = 4.91
# annual_rainfall += august_rainfall

july_to_august_rainfall = 1.05 + 4.91
print (july_to_august_rainfall)
annual_rainfall += july_to_august_rainfall

# september_rainfall = 5.16
# october_rainfall = 7.20
# november_rainfall = 5.2
# december_rainfall = 4.3

september_to_december_rainfall = 5.16 + 7.2 + 5.2 + 4.3
annual_rainfall += september_to_december_rainfall

print (annual_rainfall)
