def decode_ways(self,index=0,current_decoding="",results=None):
    if results is None:
        results=[]
    if index==len(self):
        results.append(current_decoding)
        return
    num1=int(self[index])
    if 1<=num1<=9:
        decode_ways(self,index+1,current_decoding+chr(num1+64),results)
    if index+1<len(self):
        num2=int(self[index:index+2])
        if 10<=num2<=26:
            decode_ways(self,index+2,current_decoding+chr(num2+64),results)
    return results
def main():
    encoded_message=input("Enter encoded message: ")
    decoded_messages=decode_ways(encoded_message)
    print("Possible Decodings:")
    for msg in decoded_messages:
        print(msg)
if __name__=='__main__':
    main()