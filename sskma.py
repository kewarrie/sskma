'''
Simple Shared Key Mutual Authentication

REG NO:   P15/55175/2012
COURSE:   CSC 411 - Computer Network Security
'''
##############
# Shared Key #
##############
privateKey = [38369,39203]
publicKey = [19625,39203]

########################
# Alice Challenges Bob #
########################
aliceHasAuthenticated = False

print('##########\nAlice Challenges Bob\n##########')

#Alice sends challenge to Bob
aliceSentChallenge = int(input("Alice, enter challenge: "))
aliceSentCypherChallenge =  pow(aliceSentChallenge, publicKey[0], publicKey[1]) # (pT ^ e) mod N
print('The encrypted challenge is: {}'.format(aliceSentCypherChallenge))

#Bob receives & decrypts challenge
bobReceivedCypherChallenge = int(input("Bob, enter the received encrypted challenge: "))
bobReceivedChallenge =  pow(bobReceivedCypherChallenge, privateKey[0], privateKey[1]) # (cT ^ d) mod N
print('The decrypted challenge is: {}'.format(bobReceivedChallenge))

# if Bob's received challenge == Alice's sent challenge
if aliceSentChallenge == bobReceivedChallenge:
  aliceHasAuthenticated = True
  print('Alice: Yes, it is you Bob!')
else:
  print('Alice: You are not Bob, who are you?')

print("\n")

########################
# Bob Challenges Alice #
########################
bobHasAuthenticated = False

print('##########\nBob Challenges Alice\n##########')

#Bob sends challenge to Alice
bobSentChallenge = int(input("Bob, enter challenge: "))
bobSentCypherChallenge =  pow(bobSentChallenge, publicKey[0], publicKey[1]) # (pT ^ e) mod N
print('The encrypted challenge is: {}'.format(bobSentCypherChallenge))

#Alice receives & decrypts challenge
aliceReceivedCypherChallenge = int(input("Alice, enter the received encrypted challenge: "))
aliceReceivedChallenge =  pow(aliceReceivedCypherChallenge, privateKey[0], privateKey[1]) # (cT ^ d) mod N
print('The decrypted challenge is: {}'.format(aliceReceivedChallenge))

# if Alice's received challenge == Bob's sent challenge
if bobSentChallenge == aliceReceivedChallenge:
  bobHasAuthenticated = True
  print('Bob: Yes, it is you Alice!')
else:
  print('Bob: You are not Alice, who are you?')

print("\n")

###################################
# Print success on authentication #
###################################
if aliceHasAuthenticated and bobHasAuthenticated:
  print('Both users have authenticated each others identity. Communication can resume.')
else:
  print('Authentication failed for both users.')