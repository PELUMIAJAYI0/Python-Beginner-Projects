
while True:
    USSDCode = input("Input the USSD code to purchase data on your network---> ")

    if USSDCode == '*312#':
        first = input('1. Data Plans \n2. Social Plans \n3. Business Plans \n4. Borrow Credit/package\n Input the number---> ')

        if first == '1':
                print("...Purchase Data Plans...")

                second = input('1. Daily Plans \n2. Weekly Plans \n3. Monthly Plans \n4. Manage Data Plans\n Input the number---> ')
                if second == "1":
                    print("...Select Any Daily Plans...")
                    
                    third = input('1. 50 Naira for 40MB \n2. 100 Naira for 100MB \n3. 200 Naira for 200MB \n4.300 Naira for 1GB\n Input the number---> ')
                    if third in ["1", "2", "3", "4"]:
                        print("...You have Successfully purchased your dataplans...")
                    else:
                        print("...Invalid input code, Please retry again...")

                elif second == "2":
                    print("...Select Any Weekly Plans...")
                    fourth = input('1. 350 Naira for 350MB \n2. 600 Naira for 1GB \n3. 1000 Naira for 1.5GB\n Input the number---> ')
                    if fourth in ["1", "2", "3", "4"]:
                        print("...You have Successfully purchased your dataplans...")
                    else:
                        print("...Invalid input code, Please retry again...")
                
                elif second == "3":
                    print("...Select Any Weekly Plans...")
                    fifth = input('1. 350 Naira for 350MB \n2. 600 Naira for 1GB \n3. 1000 Naira for 1.5GB\n Input the number---> ')
                    if fifth in ["1", "2", "3"]:
                        print("...You have Successfully purchased your dataplans...")
                    else:
                        print("...Invalid input code, Please retry again...")
                
                elif second =="4":
                    print("...Select Any Weekly Plans...")
                    sixth = input('1. 350 Naira for 350MB \n2. 600 Naira for 1GB \n3. 1000 Naira for 1.5GB\n Input the number---> ')
                    if sixth in ["1", "2", "3"]:
                        print("...You have Successfully purchased your dataplans...")
                    else:
                        print("...Invalid input code, Please retry again...")
                else:
                    print("...Invalid number, please enter correct number...")

        elif first == "2":
            print("...Purchase Social Plans...")

            s = input('1. Daily Plans \n2. Weekly Plans \n3. Monthly Plans \n4. Manage Data Plans\n Input the number---> ')
            if s == "1":
                    print("...Select Any Daily Plans...")
                    
                    t = input('1. 50 Naira for 40MB \n2. 100 Naira for 100MB \n3. 200 Naira for 200MB \n4.300 Naira for 1GB\n Input the number---> ')
                    if t in ["1", "2", "3", "4"]:
                        print("...You have Successfully purchased your dataplans...")
                    else:
                        print("...Invalid input code, Please retry again...")

            elif s == "2":
                    print("...Select Any Weekly Plans...")
                    f = input('1. 350 Naira for 350MB \n2. 600 Naira for 1GB \n3. 1000 Naira for 1.5GB\n Input the number---> ')
                    if f in ["1", "2", "3"]:
                        print("...You have Successfully purchased your dataplans...")
                    else:
                        print("...Invalid input code, Please retry again...")
                
            elif s == "3":
                    print("...Select Any Weekly Plans...")
                    fi = input('1. 350 Naira for 350MB \n2. 600 Naira for 1GB \n3. 1000 Naira for 1.5GB\n Input the number---> ')
                    if fi in ["1", "2", "3"]:
                        print("...You have Successfully purchased your dataplans...")
                    else:
                        print("...Invalid input code, Please retry again...")
                
            elif s =="4":
                    print("...Select Any Weekly Plans...")
                    si = input('1. 350 Naira for 350MB \n2. 600 Naira for 1GB \n3. 1000 Naira for 1.5GB\n Input the number---> ')
                    if si in ["1", "2", "3"]:
                        print("...You have Successfully purchased your dataplans...")
                    else:
                        print("...Invalid input code, Please retry again...")
            else:
                    print("...Invalid number, please enter correct number...")

        elif first == "3":
            print("...Business Plans...")

            B = input('1. Daily Plans \n2. Weekly Plans \n3. Monthly Plans \n4. Manage Data Plans\n Input the number---> ')
            if B == "1":
                    print("...Select Any Daily Plans...")
                    
                    d = input('1. 50 Naira for 40MB \n2. 100 Naira for 100MB \n3. 200 Naira for 200MB \n4.300 Naira for 1GB\n Input the number---> ')
                    if d  in ["1", "2", "3", "4"]:
                        print("...You have Successfully purchased your dataplans...")
                    else:
                        print("...Invalid input code, Please retry again...")

            elif B == "2":
                    print("...Select Any Weekly Plans...")

                    h = input('1. 350 Naira for 350MB \n2. 600 Naira for 1GB \n3. 1000 Naira for 1.5GB\n Input the number---> ')
                    if h in ["1", "2", "3"]:
                        print("...You have Successfully purchased your dataplans...")
                    else:
                        print("...Invalid input code, Please retry again...")
                
            elif B == "3":
                    print("...Select Any Weekly Plans...")
                    th = input('1. 350 Naira for 350MB \n2. 600 Naira for 1GB \n3. 1000 Naira for 1.5GB\n Input the number---> ')
                    if th in ["1", "2", "3"]:
                        print("...You have Successfully purchased your dataplans...")
                    else:
                        print("...Invalid input code, Please retry again...")
                
            elif B =="4":
                    print("...Select Any Weekly Plans...")
                    six = input('1. 350 Naira for 350MB \n2. 600 Naira for 1GB \n3. 1000 Naira for 1.5GB\n Input the number---> ')
                    if six in ["1", "2", "3"]:
                        print("...You have Successfully purchased your dataplans...")
                    else:
                        print("...Invalid input code, Please retry again...")
            else:
                    print("...Invalid number, please enter correct number...")

        elif first == "4":
            print("...Borrow Credit and Recharge...")

            nd = input('1. Daily Plans \n2. Weekly Plans \n3. Monthly Plans \n4. Manage Data Plans\n Input the number---> ')
            if nd == "1":
                    print("...Select Any Daily Plans...")
                    
                    thi = input('1. 50 Naira for 40MB \n2. 100 Naira for 100MB \n3. 200 Naira for 200MB \n4.300 Naira for 1GB\n Input the number---> ')
                    if thi in ["1", "2", "3", "4"]:
                        print("...You have Successfully purchased your dataplans...")
                    else:
                        print("...Invalid input code, Please retry again...")

            elif nd == "2":
                    print("...Select Any Weekly Plans...")
                    fou = input('1. 350 Naira for 350MB \n2. 600 Naira for 1GB \n3. 1000 Naira for 1.5GB\n Input the number---> ')
                    if fou in ["1", "2", "3"]:
                        print("...You have Successfully purchased your dataplans...")
                    else:
                        print("...Invalid input code, Please retry again...")
                
            elif nd == "3":
                    print("...Select Any Weekly Plans...")
                    fif = input('1. 350 Naira for 350MB \n2. 600 Naira for 1GB \n3. 1000 Naira for 1.5GB\n Input the number---> ')
                    if fif in ["1", "2", "3"]:
                        print("...You have Successfully purchased your dataplans...")
                    else:
                        print("...Invalid input code, Please retry again...")
                
            elif nd =="4":
                    print("...Select Any Weekly Plans...")
                    sixt = input('1. 350 Naira for 350MB \n2. 600 Naira for 1GB \n3. 1000 Naira for 1.5GB\n Input the number---> ')
                    if sixt in ["1", "2", "3"]:
                        print("...You have Successfully purchased your dataplans...")
                    else:
                        print("...Invalid input code, Please retry again...")
            else:
                    print("...Invalid number, please enter correct number...")
        else: 
            print("...Invalid number, Input the valid number")


    else:
        print("...Inputted the wrong Code!!!...")
        
    cont = input("Do you want to continue? (yes/no)---> ")
    if cont.lower() == "no":
        quit()








        
