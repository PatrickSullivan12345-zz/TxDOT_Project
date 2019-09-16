#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      patri
#
# Created:     02/11/2018
# Copyright:   (c) patri 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

    import csv

    from collections import defaultdict

    csv_location = r'D:\Final_Product\Export_Output.txt'

    new_csv = r'D:\Final_Product\Dictionary_CSV.csv'

    angles = []

    near_FID = []

    dictionary_list = []

    count = 0

    with open(csv_location) as file:
        reader = csv.reader(file, delimiter=',')

        for column in reader:

            angles.append(column[9])
            near_FID.append(column[3])

        angles.remove(angles[0])
        near_FID.remove(near_FID[0])

    near_FID_and_angles = zip(near_FID,angles)

    joined_dictionary = defaultdict(list)

    for k,v in near_FID_and_angles:
        joined_dictionary[k].append(v)

    str_dict = str(joined_dictionary)

    for key, value in sorted(joined_dictionary.items()):
        list_elements = [key,value]
        dictionary_list.append(list_elements)

    with open(new_csv,'w') as file2:
        file2.write('FID,Angle1,Angle2,Angle3,Angle4,Other_Angles'+'\n')

        for row in sorted(dictionary_list):
            file2.write(''.join(row[0])+','+','.join(row[1])+'\n')


if __name__ == '__main__':
    main()
