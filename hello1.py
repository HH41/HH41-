def readline(filename):
    with open(filename,'r',encoding='utf-8',errors='ignore') as fd:
        data = fd.readlines()
        total=ints=breaks=cases=returns=elses=ifs=defaults=switchs=doubles=longs=elses=dos=0
        for lines in data:
            if "break" in lines:
                total=total+1
            if "auto" in lines:
                total=total+1
            if "char" in lines:
                total=total+1
            if "const" in lines:
                total=total+1
            if "continue" in lines:
                total=total+1
            if "default" in lines:
                total=total+1
            if "do " in lines:
                total=total+1
            if "double" in lines:
                total=total+1
            if "else" in lines:
                total=total+1
            if "enum" in lines:
                total=total+1
            if "extern" in lines:
                total=total+1
            if "float" in lines:
                total=total+1
            if "for" in lines:
                total=total+1
            if "goto" in lines:
                total=total+1
            if "if" in lines:
                total=total+1
            if "int" in lines:
                total=total+1
            if "long" in lines:
                total=total+1
            if "register" in lines:
                total=total+1
            if "return" in lines:
                total=total+1
            if "static" in lines:
                total=total+1
            if "short" in lines:
                total=total+1
            if "signed" in lines:
                total=total+1
            if "sizeof" in lines:
                total=total+1
            if "struct" in lines:
                total=total+1
            if "switch" in lines:
                total=total+1
                switchs=switchs+1
            if "case" in lines:
                total=total+1
                cases=cases+1
            if "while" in lines:
                total=total+1
            if "volatile" in lines:
                total=total+1
            if "void" in lines:
                total=total+1
            if "unsigned" in lines:
                total=total+1
            if "union" in lines:
                total=total+1
            if "typedef" in lines:
                total=total+1
        fd.close()
        print("total num=",total) 
        print("switch num=",switchs)
filename,level=input().split()
readline(filename)