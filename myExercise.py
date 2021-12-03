import sys
f=open(sys.argv[1])

d={ a.split(":")[0]: (a.split(":")[1].split(",")[0], a.split(":")[1].split(",")[1]) for a in f.read().splitlines()}

names=sys.argv[2]
for i in names.split(","):
    try:
        print("Name: ", i, ", University: ", d[i][0], ",", d[i][1], sep="")
    except KeyError:
        print("No record of '", i, "' was found!", sep="")