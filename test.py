import csv
ADDRESSES=[]
with open('exercise/master_data/13tokyo.csv',encoding="utf-8", errors="ignore") as f:
        reader = csv.reader(f)
        with open('coors_new.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            mydict = {rows[0]:rows[1] for rows in reader}

input_file = csv.DictReader(open("exercise/master_data/13tokyo.csv", errors="ignore"))
        # data=list(reader)
        # i=0
        # for row in reader:
            # _, created = Teacher.objects.get_or_create(
            #     first_name=row[0],
            #     last_name=row[1],
            #     middle_name=row[2],
            #     )
            # ADDRESSES.append(row[i])
        # print(data["字丁目"])
            # data=row[16]
            # size=len(row)
# for row in input_file:
#     print(row)

print(next(input_file))