import random     #first we import a library for generate a random passwd


upeercase = "ABCDEFGHIJKLMOPQRSTVUWXYZ"

lowercase = "abcdefghijklmnopqrstuvwxyz"

numbers = "1234567890"

special = "!@#$%&*.?\/~_"

use_this = upeercase + lowercase + numbers + special

lenght_for_passwd = 10

passwd = "".join(random.sample(use_this, lenght_for_passwd))

print("your Generated password", passwd)
