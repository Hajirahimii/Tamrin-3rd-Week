# Hamid HajiRahimi
# Tamrin: 3-1
# Remove Duplicate Elements From The List

############################################################

Element_List = [8, 0, 3, 0, 4, 1, 8, 8, 10, 7]

print ("The Initial List: " , str(Element_List))

############################################################

# Remove Duplicate Elements From The List

result = []

for i in Element_List:

    if i not in result:

        result.append(i)

print ("The list After Removing Duplicate Elements : " , str(result))
