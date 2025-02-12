def check_if_pangram(str):
    import string
    alphabets=list(string.ascii_lowercase)
    for i in range(len(str)):
        if str[i] in alphabets:
            alphabets.remove(str[i])
    if not alphabets:
        print("pangram")
    else:
        print("not pangram")
def main():
    st=input("Enter string:")
    st=st.lower()
    check_if_pangram(st)
if __name__=='__main__':
    main()