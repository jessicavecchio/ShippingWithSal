weight = 5
price_per_pound = 0

#ground shipping
ground_flat_charge = 20
if weight <= 2:
  price_per_pound = 1.50 
elif weight > 2 and weight <= 6:
  price_per_pound = 3.00
elif weight > 6 and weight <= 10:
  price_per_pound = 4.00
elif weight > 10:
  price_per_pound = 4.75

ground_cost = price_per_pound*weight+ground_flat_charge

print("To ship a package with ground shipping that is", weight, "pounds, it costs:", ground_cost, "dollars.")

#premium ground shipping
print("")
premium_cost = 125.00
print("To ship a package with premium ground shipping that is", weight, "pounds, it costs:", premium_cost, "dollars.")

#drone shipping
if weight <= 2:
  price_per_pound = 4.50 
elif weight > 2 and weight <= 6:
  price_per_pound = 9.00
elif weight > 6 and weight <= 10:
  price_per_pound = 12.00
elif weight > 10:
  price_per_pound = 14.25

drone_cost = price_per_pound*weight

print("")
print("To ship a package with drone shipping that is", weight, "pounds, it costs:", drone_cost, "dollars.")

print("")
if ground_cost < premium_cost and ground_cost < drone_cost:
  print("Ground shipping is the cheapest option for you!")
elif premium_cost < ground_cost and premium_cost < drone_cost:
  print("Premium ground shipping is the cheapest option for you!")
elif drone_cost < ground_cost and drone_cost < premium_cost:
  print("Drone shipping is the cheapest option for you!")
