def readline(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as fd:
        
        data = fd.readlines()
        num=nums=0
        total = ints = breaks = returns = elses = ifs = defaults = switchs = doubles = longs = elses = dos = cases = ies=ieis=0
        
        for lines in data:
            if '//' in lines:    #删除单行注释
                temp = lines.index('//')
                lines = lines[:temp]
            if '/*' in lines:   #删除多行注释
                first_lines = lines.index(line)
                for new_lines in lines[first_line:]:
                    if '*/' not in new_line:
                        del lines[first_line]
                    else:
                        del lines[first_line]
                        break

        for lines in data:   #total计数
            if "break" in lines:
                total = total + 1
            if "auto" in lines:
                total = total + 1
            if "char" in lines:
                total = total + 1
            if "const" in lines:
                total = total + 1
            if "continue" in lines:
                total = total + 1
            if "default" in lines:
                total = total + 1
            if "do " in lines:
                total = total + 1
            if "double" in lines:
                total = total + 1
            if "else" in lines:
                total = total + 1
            if "enum" in lines:
                total = total + 1
            if "extern" in lines:
                total = total + 1
            if "float" in lines:
                total = total + 1
            if "for" in lines:
                total = total + 1
            if "goto" in lines:
                total = total + 1
            if "if" in lines:
                total = total + 1
            if "int" in lines:
                total = total + 1
            if "long" in lines:
                total = total + 1
            if "register" in lines:
                total = total + 1
            if "return" in lines:
                total = total + 1
            if "static" in lines:
                total = total + 1
            if "short" in lines:
                total = total + 1
            if "signed" in lines:
                total = total + 1
            if "sizeof" in lines:
                total = total + 1
            if "struct" in lines:
                total = total + 1
            if "switch" in lines:
                total = total + 1
                switchs = switchs + 1
            if "case" in lines:
                total = total + 1
            if "while" in lines:
                total = total + 1
            if "volatile" in lines:
                total = total + 1
            if "void" in lines:
                total = total + 1
            if "unsigned" in lines:
                total = total + 1
            if "union" in lines:
                total = total + 1
            if "typedef" in lines:
                total = total + 1
        print("total num:", total)  
        print("switch num:", switchs)  
        for lines in data:  #switch-case计数
            num+=1
            if "switch" in lines:
                num1=num
                while(num1<len(data)):
                    if 'case' in data[num1]:
                        cases+=1
                    if 'switch' in data[num1]:
                        print('case num:',cases,end=" ")
                        cases=0
                        break
                    num1+=1
        print(cases)
        num = nums1 = 0
        ies=ieis=0
        lenn=len(data)
        for lines in data:  #if-else 与 if-else-if 计数
            num += 1
            if "if" in lines and "else if" not in lines:
                flag = 0  # 0:if-else     1:if-else-if
                suojin = lines.find("if")
                for nums1 in range(num,lenn):
                    if "else" in data[nums1] and data[nums1].find("else") == suojin:
                        if "else if" in data[nums1]:
                            flag = 1
                        else:
                            if flag == 0:
                                ies += 1
                            else:
                                ieis += 1
                            break
        print("if-else num:", ies)
        print("if-else-if num:", ieis)
        fd.close()

filename, level = input().split()
readline(filename)