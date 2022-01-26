def rep_num():
    int(num) = input("Enter the number: ")
    print(num)
    char_freq={}
    for i in num:
        if i in char_freq:
            char_freq[i]=char_freq[i]+1

        else:
             char_freq[i]=1

    result=max(char_freq)
    print(result)

  rep_string()