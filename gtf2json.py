#!/usr/bin/python
import sys
import fileinput
import re
import json

my_gene=sys.argv[1]
Lookup_gene=[]
#with open(sys.argv[1],'r') as my_gene:
#for each_line_my_gene in my_gene:
for each_line_my_gene in fileinput.input(my_gene):   #re.match
    geneName=re.findall(r'^\w+.*\sgene\s+\w+\s+\w+\s\.\s.\s\.\s+[\w-]+\s\"[\w-]+\"\;\s+[\w-]+\s\"+([\w\.\w-]+)',each_line_my_gene,re.I|re.M)
    chr1=re.findall(r'(^\w)+.*\sgene\s+\w+\s+\w+\s\.\s.\s\.\s+[\w-]+\s\"[\w-]+\"\;\s+[\w-]+\s\"+[\w\.\w-]+',each_line_my_gene,re.I|re.M)
    startPos=re.findall(r'^\w+.*\sgene\s+(\w+)\s+\w+\s\.\s.\s\.\s+[\w-]+\s\"[\w-]+\"\;\s+[\w-]+\s\"+[\w\.\w-]+',each_line_my_gene,re.I|re.M)
    endPos=re.findall(r'^\w+.*\sgene\s+\w+\s+(\w+)\s\.\s.\s\.\s+[\w-]+\s\"[\w-]+\"\;\s+[\w-]+\s\"+[\w\.\w-]+',each_line_my_gene,re.I|re.M)
    if geneName:
        if chr:
            if startPos:
                if endPos:
                    for each_line_my_dic_geneName in geneName:
                        for each_line_my_dic_chr in chr1:
                            for each_line_my_dic_startPos in startPos:
                                for each_line_my_dic_endPos in endPos:
                                    Lookup_gene_geneName={"geneName":each_line_my_dic_geneName}
                                    Lookup_gene.append(Lookup_gene_geneName)
                                    Lookup_gene_chr={"chr":each_line_my_dic_chr}
                                    Lookup_gene_startPos={"startPos":each_line_my_dic_startPos}
                                    Lookup_gene_endPos={"endPos":each_line_my_dic_endPos}
                                    Lookup_gene_geneName.update(Lookup_gene_chr)
                                    Lookup_gene_geneName.update(Lookup_gene_startPos)
                                    Lookup_gene_geneName.update(Lookup_gene_endPos)
                                    #Lookup_gene_json=json.dumps(Lookup_gene)

#print(Lookup_gene_json)

with open("Result.json","w") as f:
    json.dump(Lookup_gene,f)
    
