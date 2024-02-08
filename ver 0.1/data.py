def input_data():
    data= [[],[]]
    data_dict = { }

    texting = True
    while texting:
        note = []
        keynote = []
        note_num = 0
        key_num = 0
        condition = input('What the condition?\n 1. note\n 2. keynote\n 3. done\n : ')

        try:
            if condition == '1':
                taking_note = True
                while taking_note:
                    if data[0] == []:
                        print(f"your keynote is: \n none")
                    else:
                        if note_num > len(data[0]) - 1:
                            print(f"your keynote is: \n none")
                        else:
                            print(f"your note is: \n {data[0][note_num]}")
                    text = input('Tulis catatan: ')
                    if text.lower() == 'done':
                        taking_note = False
                    else:
                        note.append(text)
                        note_num += 1

            elif condition == '2':
                taking_key = True
                while taking_key:
                    if data[1] == []:
                        print(f"your note is: \n none")
                    else:
                        if key_num > len(data[1]) - 1:
                            print(f"your note is: \n none")
                        else:
                            print(f"your note is: \n {data[1][key_num]}")
                    text = input('Tulis keynote: ')
                    if text.lower() == 'done':
                        taking_key = False
                    else:
                        keynote.append(text)
                        key_num += 1 

            elif condition == '3':
                texting = False
            else:
                raise ValueError("Invalid condition") 
        except Exception as e:
            print(f"Error: {e}")

        for key in keynote:
            data[0].append(key)
        for nt in note:
            data[1].append(nt)

    for key,note in zip(data[0],data[1]):
        data_dict[f'{key}'] = note
    
    return data_dict