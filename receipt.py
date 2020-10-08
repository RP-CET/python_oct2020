
#
#Watermelon       $  5.00
#Apples           $  14.00
#Item B 0001      $  114.00
#

'''

print (items[0] + "     " + "$" + str(prices[0]) )
print (items[1] + "         " + "$" + str(prices[1]) )
print (items[2] + "         " + "$" + str(prices[2]) )
print (items[3] + "          " + "$" + str(prices[3]) )
'''

items = ["Watermelon", "Apples", "Mangos", "Pizza"]
prices = [5.00, 14.00, 140.33, 20.50]

for i in range( len(items)):
    line = "%-25s $ %.2f" % (items[i], prices[i])
    print (line)

print ("-" * 35)
print ("%-25s $ %.2f" % ("Total : ", sum(prices)) )

