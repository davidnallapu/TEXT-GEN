"""Generates a random word based on your input"""
import random
vowels='aeiou'
consonants='bcdfghjklmnpqrstvwxyz'
letters=vowels+consonants
name=''

def plot(linput):
	if linput=='V':
		return random.choice(vowels)
	elif linput=='C':
		return random.choice(consonants)
	elif linput=='L':
		return random.choice(letters)
	else:
		return linput

n=input('How many letters do you want in the name?')
choice=''
for i in range(int(n)):
	linput=input("What letter do you want? V for vowel, C for consonant, L for any letter:")
	choice+=linput
for i in range(10):
	for i in choice:
		name+=plot(i)
	print (name)
	name=''



    





