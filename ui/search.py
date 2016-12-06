import pickle
import csv

def autocomp(name, src, no):
    with open('/home/neel/Desktop/csci_548/proj/drive_data/final_data/'+name) as infile:
        reader = csv.reader(infile)
        next(reader, None)  #skip header
        for row in reader:
            src[row[no]]=1
    infile.close
    return src

src = {}
file_name = ['6pm_eb_jw_85.csv',
             '6pm_za_jw_85.csv',
             'z-eb-dup_rem_85_imdesc.csv',
             '6pmEb_za_jw_85.csv']

rno = [3, 1, 2, 3, 1, 1, 3]
ptr=0
for i in file_name:
    src = autocomp(i, src, rno[ptr])
    ptr+=1

print(len(src))

with open('src.pickle','wb')as f:
    pickle.dump(src,f)
print('done')

