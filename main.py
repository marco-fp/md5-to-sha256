import hashlib

# Para crackear las passwords he utilizado: https://crackstation.net/

salt = "SUPER_SECURE_SALT"

with open("plain.txt") as f:
    passwords = f.readlines()
passwords = [x.strip() for x in passwords]
passwords = [x.split(" ") for x in passwords]

new_hashes = []
for raw_line in passwords:
  line = [x.split("\t") for x in raw_line][0]
  if 'md5' in line:
    plain_password = line[2]
    new_hash = hashlib.sha256( salt.encode() + plain_password.encode() ).hexdigest()
    new_hashes.append([plain_password, new_hash])
  else:
    print(line)
    new_hashes.append([line[0], "NOT FOUND"])

print(new_hashes)

with open('new_hashes.txt', 'w') as f:
    for new_hash in new_hashes:
      f.write(new_hash[0] + " " + new_hash[1] + '\n')