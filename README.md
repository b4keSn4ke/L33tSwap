# L33tSwap
Set of cracking rule for Hashcat that swap vowels from words in L33t format.

You can customize the list by commenting/uncommenting the sets of characters you want to use to generate the rules list. 

By default only `lowercase letters` are generated since it can get quite big.

```
#!/usr/bin/python3 

# Lowercase and uppercase letters
# Uncomment the array below if you want to permutate lowercase and uppercase letters - comment the array below if using another sets of character.
#char = ['sa@','sa4','si1','si!','se#','se3','se£','se€','suv','so0','ss$','ss5','sA@','sA4','sI1','sI!','sE#','sE3','sE£','sE€','sUV','sO0','sS$','sS5']

# Only lowercase letters - comment the array below if using another sets of character.
char = ['sa@','sa4','si1','si!','se#','se3','se£','se€','suv','so0','ss$','ss5']

# Only uppercase letters - comment the array below if using another sets of character.
#char = ['sA@','sA4','sI1','sI!','sE#','sE3','sE£','sE€','sUV','sO0','sS$','sS5']
```

After having selected your sets of characters you can simply generate the list by running the following command

```
python3 L33tSwap-generator.py > L33tSwap.rule
```


Here are examples of permuttation that can be achieved using this sets of rule (`Lowercase and uppercase letters`) with the input word `Sequoia`

```
Sequoia -> 5equoia
Sequoia -> $equoia
Sequoia -> 53quoia
Sequoia -> $3quoia
Sequoia -> 5#quoia
Sequoia -> $#quoia
Sequoia -> 5£quoia
Sequoia -> $£quoia
Sequoia -> 5€quoia
Sequoia -> $€quoia
Sequoia -> $3qvoia
Sequoia -> 5#qvoia
Sequoia -> $#qvoia
Sequoia -> 5£qvoia
Sequoia -> $£qvoia
Sequoia -> 5€qvoia
Sequoia -> $€qvoia
Sequoia -> $3qu0ia
Sequoia -> 5#qu0ia
Sequoia -> $#qu0ia
Sequoia -> 5£qu0ia
Sequoia -> $£qu0ia
Sequoia -> 5€qu0ia
Sequoia -> $€qu0ia
Sequoia -> $3qv0ia
Sequoia -> 5#qv0ia
Sequoia -> $#qv0ia
Sequoia -> 5£qv0ia
Sequoia -> $£qv0ia
Sequoia -> 5€qv0ia
Sequoia -> $€qv0ia
Sequoia -> $3quo1a
Sequoia -> 5#quo1a
Sequoia -> $#quo1a
Sequoia -> 5£quo1a
Sequoia -> $£quo1a
Sequoia -> 5€quo1a
Sequoia -> $€quo1a
Sequoia -> $3qvo1a
Sequoia -> 5#qvo1a
Sequoia -> $#qvo1a
Sequoia -> 5£qvo1a
Sequoia -> $£qvo1a
Sequoia -> 5€qvo1a
Sequoia -> $€qvo1a
Sequoia -> $3qu01a
Sequoia -> 5#qu01a
Sequoia -> $#qu01a
Sequoia -> 5£qu01a
Sequoia -> $£qu01a
Sequoia -> 5€qu01a
Sequoia -> $€qu01a
Sequoia -> $3qv01a
Sequoia -> 5#qv01a
Sequoia -> $#qv01a
Sequoia -> 5£qv01a
Sequoia -> $£qv01a
Sequoia -> 5€qv01a
Sequoia -> $€qv01a
Sequoia -> $3quo!a
Sequoia -> 5#quo!a
Sequoia -> $#quo!a
Sequoia -> 5£quo!a
Sequoia -> $£quo!a
Sequoia -> 5€quo!a
Sequoia -> $€quo!a
Sequoia -> $3qvo!a
Sequoia -> 5#qvo!a
Sequoia -> $#qvo!a
Sequoia -> 5£qvo!a
Sequoia -> $£qvo!a
Sequoia -> 5€qvo!a
Sequoia -> $€qvo!a
Sequoia -> $3qu0!a
Sequoia -> 5#qu0!a
Sequoia -> $#qu0!a
Sequoia -> 5£qu0!a
Sequoia -> $£qu0!a
Sequoia -> 5€qu0!a
Sequoia -> $€qu0!a
Sequoia -> $3qv0!a
Sequoia -> 5#qv0!a
Sequoia -> $#qv0!a
Sequoia -> 5£qv0!a
Sequoia -> $£qv0!a
Sequoia -> 5€qv0!a
Sequoia -> $€qv0!a
Sequoia -> $3quo14
Sequoia -> 5#quo14
Sequoia -> $#quo14
Sequoia -> 5£quo14
Sequoia -> $£quo14
Sequoia -> 5€quo14
Sequoia -> $€quo14
Sequoia -> $3qvo14
Sequoia -> 5#qvo14
Sequoia -> $#qvo14
Sequoia -> 5£qvo14
Sequoia -> $£qvo14
Sequoia -> 5€qvo14
Sequoia -> $€qvo14
Sequoia -> $3qu014
Sequoia -> 5#qu014
Sequoia -> $#qu014
Sequoia -> 5£qu014
Sequoia -> $£qu014
Sequoia -> 5€qu014
Sequoia -> $€qu014
Sequoia -> $3qv014
Sequoia -> 5#qv014
Sequoia -> $#qv014
Sequoia -> 5£qv014
Sequoia -> $£qv014
Sequoia -> 5€qv014
Sequoia -> $€qv014
Sequoia -> $3quo!4
Sequoia -> 5#quo!4
Sequoia -> $#quo!4
Sequoia -> 5£quo!4
Sequoia -> $£quo!4
Sequoia -> 5€quo!4
Sequoia -> $€quo!4
Sequoia -> $3qvo!4
Sequoia -> 5#qvo!4
Sequoia -> $#qvo!4
Sequoia -> 5£qvo!4
Sequoia -> $£qvo!4
Sequoia -> 5€qvo!4
Sequoia -> $€qvo!4
Sequoia -> $3qu0!4
Sequoia -> 5#qu0!4
Sequoia -> $#qu0!4
Sequoia -> 5£qu0!4
Sequoia -> $£qu0!4
Sequoia -> 5€qu0!4
Sequoia -> $€qu0!4
Sequoia -> $3qv0!4
Sequoia -> 5#qv0!4
Sequoia -> $#qv0!4
Sequoia -> 5£qv0!4
Sequoia -> $£qv0!4
Sequoia -> 5€qv0!4
Sequoia -> $€qv0!4
Sequoia -> $3quo1@
Sequoia -> 5#quo1@
Sequoia -> $#quo1@
Sequoia -> 5£quo1@
Sequoia -> $£quo1@
Sequoia -> 5€quo1@
Sequoia -> $€quo1@
Sequoia -> $3qvo1@
Sequoia -> 5#qvo1@
Sequoia -> $#qvo1@
Sequoia -> 5£qvo1@
Sequoia -> $£qvo1@
Sequoia -> 5€qvo1@
Sequoia -> $€qvo1@
Sequoia -> $3qu01@
Sequoia -> 5#qu01@
Sequoia -> $#qu01@
Sequoia -> 5£qu01@
Sequoia -> $£qu01@
Sequoia -> 5€qu01@
Sequoia -> $€qu01@
Sequoia -> $3qv01@
Sequoia -> 5#qv01@
Sequoia -> $#qv01@
Sequoia -> 5£qv01@
Sequoia -> $£qv01@
Sequoia -> 5€qv01@
Sequoia -> $€qv01@
Sequoia -> $3quo!@
Sequoia -> 5#quo!@
Sequoia -> $#quo!@
Sequoia -> 5£quo!@
Sequoia -> $£quo!@
Sequoia -> 5€quo!@
Sequoia -> $€quo!@
Sequoia -> $3qvo!@
Sequoia -> 5#qvo!@
Sequoia -> $#qvo!@
Sequoia -> 5£qvo!@
Sequoia -> $£qvo!@
Sequoia -> 5€qvo!@
Sequoia -> $€qvo!@
Sequoia -> $3qu0!@
Sequoia -> 5#qu0!@
Sequoia -> $#qu0!@
Sequoia -> 5£qu0!@
Sequoia -> $£qu0!@
Sequoia -> 5€qu0!@
Sequoia -> $€qu0!@
Sequoia -> $3qv0!@
Sequoia -> 5#qv0!@
Sequoia -> $#qv0!@
Sequoia -> 5£qv0!@
Sequoia -> $£qv0!@
Sequoia -> 5€qv0!@
Sequoia -> $€qv0!@
```
