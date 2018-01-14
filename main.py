import sys
import random
import string

def genpass(pwlen):
	letters = string.ascii_letters
	numbers = '234567890'
	symbols = '!@#$%^&*()_-+=|}]{[:;"?/>.<,'

	allchars = list(''.join([letters, numbers, symbols]))
	random.shuffle(allchars)

	result = []

	for i in range(0, int(pwlen)):
		result.append(random.choice(allchars))

	return ''.join(result)

def main(pwlen):
	passwd = genpass(pwlen)
	print passwd

if __name__ == '__main__':
	if len(sys.argv) == 1:
		passwd_len = random.randint(8, 16)
	elif len(sys.argv) == 2:
		passwd_len = sys.argv[1]
	else:
		print 'Usage: python main.py [password_length]'
		sys.exit(0)

	main(passwd_len)
