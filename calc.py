#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
# Copyright 2014 Alex Kleider; All Rights Reserved.

# file: 'calc.py'
"""
A simple script to quickly calculate cost of a Raspberry Pi installation.

Simply comment out all items in 'costs' that you _don't_ want included,
(and be sure none of the ones you do want are still commented out,)
and then run the script.
Oh, and don't forget the sales 'tax_rate' variable which can be set to 0 if
appropriate.
"""
print("Running Python3 script: 'calc.py'.......")

tax_rate = 0.072

costs = {
          "32G card": 17.60,  # Choose SD card capacity.
#         "64G card": 32.15,
#        "128G card": 66.99,
#     "raspberry pi": 35.49,  # The 'pi' itself.
       "usb charger": 7.00,   # Need this!
   "usb wifi dongle": 5.20,   # To provide Access Point capability.
 "ethernet patch cable": 7.99,  # If you expect to have local access.
# A variety of enclosures are available:
#     "ModMyPi Case": 13.46,
# https://www.modmypi.com/shop 
#         "Tux Case": 38.53,
# http://www.makershed.com/products/tux-case-for-raspberry-pi
      "Bud Pi Plate": 14.87,  
# http://www.budind.com/view/Plastic+Boxes/Microcomputer+Enclosures
#     "SB R Pi Case":  7.49,  # from Amazon
          }
print("\n\n")
total = 0
for k in costs:
    cost_string = "${0:.2f}".format(costs[k])
    print("Cost of {0:<20} : {1:>6s}.".format(k, cost_string))
    total += costs[k]
    #print("..running total is {0:.2f}.".format(total))

tax_notice = ""
if tax_rate:
    tax_notice = "(includes {0:.3f} sales tax) ".format(tax_rate)
    total += tax_rate * total

print("\nTotal cost is {0} ${1:.2f}.\n".\
            format(tax_notice, total) )

