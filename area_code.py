
#!/usr/bin/python
import sys

with open(sys.argv[1],'r')as file:
    for each_line in file:
        area_code = each_line[1:4]
        print(area_code)
