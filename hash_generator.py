import random,string,crypt

randomsalt = ''.join(random.sample(string.ascii_letters,8))

print crypt.crypt('TestPassword456!', '\$6\$%s\$' % randomsalt)