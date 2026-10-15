# D1
labels= ["R-001", "R-002", "R-003"]
print(labels[0])
print(labels[-1])
print(len(labels))


# D2
"""use slicing to print parts of a list."""
values=[5,10,15,20,25,30]
print(values[1:5])
print(values[:2])
print(values[3:])


# D3
"""modify a list remove an item and print each value."""
values={10,20,30}
values[0] = 99
print(values)
values.append(40)
print(values)
values.remove(20)
print(values)


# D4
"""it shows turples cannot change."""
point=(3,7)
print(point)
print(point[0])

#point[0]=5
#this causes a type error because turples do not change.

# D5
record_id="R-001"
print(record_id[0])
print(record_id[-1])
print(record_id[2:])


# D6
"""filter your values"""
values=[40,55,70,25]
doubled=[value*2]
print(doubled)
filtered=[values>=50]
print(filtered)


# D7
record={"label":"R-001","value":87.0,"limit":100.0}
print(record["label"])
record["status"]="OK"
record["value"]=90.0
print(record)


# D8
record={"label": "R-001","value":90.0,
        "limit":100.0,"status":"OK"}
print(record.get("status"))
print(record.get("owner"))
print(record.get("owner", "n/a"))



# D9
for key in record:
    print(key)
    for value in record.values():
        print(value)
        for key, value in record.items():
            print(f"{key}: {value}")


            # D10
hostnames=["srv-01","srv-02","srv-03"]
used=[87,45,120]


# D11
ips=["10.0.0.5","10.0.0.9","10.0.0.5","10.0.0.7"]
print("10.0.0.9","10.0.0.1")


# D12
"""write two lines to a file then read them."""
f.write("R-001\n")
f.write("R-002\n")


# D13
"""read records from a file and print each field"""
with open("records_sample.txt","r") as f:
    for line in f:
        line=line.strip()
        value=float(value)
        limit=float(limit)
        print(label,value,limit)



        # D14
text= "abc"
try:
    number=float(text)
    print(number)
except ValueError:
    print("Not a number:ABC")
    text="42"
    try:
        number=float(text)
        print(number)
    except ValueError:
        print("Not a number:42")




        # D15
try:
    with open("missing.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("missing.txt not found")



    # D16
records=[{"label": "R-001", "value":87,"limit":100},
         {"label": "R-002", "value":120,"limit":100},
         {"label":"R-003","value":45.0,"limit":100}
]
for record in records
    if record["value"]>record["limit"]:
        status= "OVERLIMIT" 
    else:
        status= "OK"
        print(record["label"], status)