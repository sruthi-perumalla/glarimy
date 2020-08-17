str=input()
def deduplicate(str):
 uniue_char = []
 for c in str:
    if not c in uniue_char:
        uniue_char.append(c)
 print(uniue_char)
deduplicate(str)
