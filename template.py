"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def check_record(value, limit):
    """calculate difference and percentage"""
    difference = value - limit
    percent=(value/limit)*100 
    return difference, percent
def print_report(label,value,limit,difference,percent,status):
    print"="*34
    print("Label:",label)
    print(f"Value:{value:.2f}")
    print(f"Limit:{limit:.2f}")
    print(f"Difference:{difference:.2f}")
    print(f"Percentage:{percent:.2f}%")
    print("Status:", status)
    print"="*34




records=[
    {"label":"R-001,"value":87, "limit":100},
    {"label":"R-002", "value":120,"limit":100},
    {"label": "R-003","value":45.0,"limit":100}
]


# =============================================================== PROCESS + OUTPUT
for record in records:
laabel=record["label"]
value=record["value"]
limit=record["limit"]
difference, percent=check_record(value,limit)
status="OVERLIMI" if value > limit else "OK"
print_report(label,value,limit,difference,percent, status)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
