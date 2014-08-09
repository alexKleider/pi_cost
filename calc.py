#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
# Copyright 2014 Alex Kleider; All Rights Reserved.

# file: 'calc.py'
"""
Put your docstring here.
"""
print("Running Python3 script: 'calc.py'.......")

tax_rate = 0.072

costs = {"32G card": 17.60,  # Choose SD card capacity.
         "64G card": 32.15,
        "128G card": 66.99,
     "raspberry pi": 35.49,  # The 'pi' itself.
      "usb charger": 7.00,   # Need this!
  "usb wifi dongle": 5.20,   # To provide Access Point capability.
"ethernet patch cable": 7.99,  # If you expect to have local access.
# A variety of enclosures are available:
     "ModMyPi Case": 13.46,
# https://www.modmypi.com/shop 
         "Tux Case": 38.53,
# http://www.makershed.com/products/tux-case-for-raspberry-pi
     "Bud Pi Plate": 14.87,  
# http://www.budind.com/view/Plastic+Boxes/Microcomputer+Enclosures
     "SB R Pi Case":  7.49,  # from Amazon
          }
print("\n\n")
total = 0
for k in (
        "32G card",
        "raspberry pi",
        "usb charger",
        "usb wifi dongle",
        "Bud Pi Plate",
        "ethernet patch cable",
        ):
    cost_string = "${0:.2f}".format(costs[k])
    print("Cost of {0:<20} : {1:>6s}.".format(k, cost_string))
    total += costs[k]
    #print("..running total is {0:.2f}.".format(total))

print("\nTotal cost (includes {0:.3f} sales tax) is ${1:.2f}.\n".\
            format(tax_rate, total) )

price_of_32G_card = 17.60
#card_price = 17.60   # 32GB
card_price = 66.99   # 128GB
#card_price = 32.15   # 64GB
pi_price = 35.49
charger_price = 7.00
both_price = price_of_32G_card + pi_price
cost = (pi_price + 2 * price_of_32G_card)
paid = 75.79
tax_rate = (paid - cost) /cost
adapter_cost = 5.20
enclosure_cost = 13.46
#print("Tax rate is {0:.3f}.".format(tax_rate))
#print
#rachel_cost = (card_price + pi_price + charger_price) * (1 + tax_rate)\
#                        + adapter_cost\
#                        + enclosure_cost
#print("Total cost of Rachel is ${:03.2f}.".format(rachel_cost))
#print("cost of Rspberry Pi: {:.2f}.".format(pi_price * (1 + tax_rate)))
#print("cost of SD Card: {:.2f}.".format(card_price * (1 + tax_rate)))
#print("cost of USB charger: {:.2f}.".format(charger_price * (1 + tax_rate)))
#print("cost of USB AP adapter: {:.2f}.".format(adapter_cost))
#print("cost of enclosure (from ModMyPi Ltd.): {:.2f}."\
#                                                   .format(enclosure_cost))
#print("Total cost of Rachel is ${:.2f}.".format(rachel_cost))
