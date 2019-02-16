file = open("FL/ALA_20151217.txt", "r")

for line in file:
   fields = line.split()
   parties = ['DEM', 'REP', 'NPA']
   person = []
   name = fields[2:4]
   if len(fields[4]) > 1:
       name.append(fields[4])
   person.append(name)
   for field in fields:
       if field in parties:
           person.append(field)

   print(person)

