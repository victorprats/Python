# Caesar Cipher Hacker
# http://inventwithpython.com/hacking/chapter7.html

# http://inventwithpython.com/hacking (BSD Licensed)


 message = 'GUVF VF ZL FRPERG ZRFFNTR.'

 LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



 # loop through every possible key

for key in range(len(LETTERS)):


10.     # It is important to set translated to the blank string so that the

11.     # previous iteration's value for translated is cleared.

12.     translated = ''

13.

14.     # The rest of the program is the same as the original Caesar program:

15.

16.     # run the encryption/decryption code on each symbol in the message

17.     for symbol in message:

18.         if symbol in LETTERS:

19.             num = LETTERS.find(symbol) # get the number of the symbol

20.             num = num - key

21.

22.             # handle the wrap-around if num is 26 or larger or less than 0

23.             if num < 0:

24.                 num = num + len(LETTERS)

25.

26.             # add number's symbol at the end of translated

27.             translated = translated + LETTERS[num]

28.

29.         else:

30.             # just add the symbol without encrypting/decrypting

31.             translated = translated + symbol

32.

33.     # display the current key being tested, along with its decryption

34.     print('Key #%s: %s' % (key, translated))
