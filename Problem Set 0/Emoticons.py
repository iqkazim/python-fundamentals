def main():
    msg= input('Say something!')
    convert(msg)

def convert(to):
   smiley =to.replace (':)','🙂').replace (':(','🙁')
   print (smiley)

main()
