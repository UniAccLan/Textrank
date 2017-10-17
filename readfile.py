col_num = None
with open('anything.txt','r') as fr, open('positive.txt','w') as fw:
    for line in fr:
        data = line.split('\t')
        if col_num is None:
            col_num = len(data)
        else:
            pass
        if len(data) == col_num:
            fw.write(line+'\n')
        else:
            print(data)

col_num = None
with open('alternative.txt','r') as fr, open('negative.txt','w') as fw:
    for line in fr:
        data = line.split('\t')
        if col_num is None:
            col_num = len(data)
        else:
            pass
        if len(data) == col_num:
            fw.write(line+'\n')
        else:
            print(data)
