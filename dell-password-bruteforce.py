import subprocess

def next(password, pos=0):
  index = chars.index(password[pos])
  if chars[-1] == chars[index]:
    if pos + 1 >= len(password):
      password.append(chars[0])
      for password_char in range(len(password)):
        password[password_char] = chars[0]
      ipassword = next(password, 0)
    else:
      password[pos] = chars[0]
      password = next(password, pos+1)
  else:
    password[pos] = chars[index +1]
  return password


if __name__ == '__main__':
  minimum_password_length = 8
  maximum_password_length = 100

  chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

  password = []

  while len(password) < minimum_password_length:
    password.append(chars[0])

  cmd = ['C:\\Progam Files (x86)\\Dell\CCTK\\X86_64\\cctk.exe', '--setuppassword=""', '--vaultsetuppwd=""'] 
  result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  
  while len(password) < maximum_password_length or result.returncode == 0:
    cmd[1] = f'--setuppassword={"".join(password)}'
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(password, result)
    password = next(password)

  with open('output.txt', a) as stream:
    stream.write(password)
  print(password)

  # for i in range(3845):
  #   print(password)
  #   password = next(password)
  
  # char_length = len(chars)
  # print(char_length**minimum_password_length)
