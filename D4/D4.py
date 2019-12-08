import re


passwords = []
for num in range(171309, 643603+1):
    num_to_check = str(num)

    if not ''.join(sorted(num_to_check)) == num_to_check:
        continue
    num_to_check = re.sub(r'(\d)\1{2,}', '', num_to_check)

    if not ('11' in num_to_check or '22' in num_to_check or '33' in num_to_check or '44' in num_to_check or '55' in num_to_check or '66' in num_to_check or '77' in num_to_check or '88' in num_to_check or '99' in num_to_check or '00' in num_to_check):
        continue
      
    passwords.append(num)

print(len(passwords))