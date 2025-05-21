while True:
  password=input("Enter the password: ")
  if len(password)<8:
     print("Password is too short,(no less than 8 characters)")
     continue
  elif password.isdigit():
     print("Password should contain letters")
     continue   
  elif password.islower():
     print("Password must contain an uppercase letter ")
     continue
  else:
    print("Password is strong.")
    break
