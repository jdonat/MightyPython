import re

def inv(stri):
   return stri[::-1]
def exo1():
   strn = str(input("Entrez une chaine de caracteres\n"))
   print(inv(strn))

def count(stri):
   #print(ord('a')) 97
   #print(ord('z')) 122
   key_dict = {}
   for x in range(97, 123):
      ind = cnt = 0
      for y in range(len(stri)):
         j = stri.find(chr(x), ind)
         if(j != -1):
            cnt+=1
            ind+=j+1
      if(cnt != 0):
         key_dict[chr(x)] = cnt
   print(key_dict)

def input_line():
   strn = str(input("Entrez une chaine de caracteres\n"))
   return strn.lower()

def exo2():
   strn = input_line()
   count(strn)

def is_palindrom(stri):
   if(stri == inv(stri)):
      return True
   return False

def exo3():
   strn = input_line()
   resp = is_palindrom(strn)
   print(resp)

def exo4():
   strn = str(input("Entrez une phrase\n"))
   strn = strn.replace(" ", "-")
   print(strn)

def exo5():
   strn = str(input("Entrez une phrase\n"))
   words = strn.split()
   longest_word = ""
   max_cnt = 0
   for w in words:
      if(len(w)>=max_cnt):   
         max_cnt = len(w)
         longest_word = w
   print(longest_word)

def exo6():
   strn = str(input("Entrez une phrase contenant une date au format JJ/MM/AAAA\n"))
   dates = []
   pattern = r"\d{1,2}\/\d{2}\/\d{2,4}"
   p = re.compile(pattern)
   dates = p.findall(strn)
   print(dates)

def inv_list(liste):
   ret = []
   for x in range(len(liste)-1, -1, -1):
      ret.append(liste[x])
   print(ret)
   return ret

def exo7():
   inv_list([1, 2, 3, 4, 5])

def liste_commune(list1, list2):
   ret = []
   cnt = 0
   for x in list1:
      cnter = 0
      for y in list2:
         if(x == y):
            if(cnt == 0):
               for z in ret:
                  if(z == x):
                     cnter+=1
               if(cnter == 0):
                  ret.append(x)
            cnt+=1
         cnt = 0
   print(ret)

def exo8():
   liste_commune([1, 1, 2, 2, 3, 4], [2, 2, 4, 4, 6, 8])

def count_occ(liste, occ):
   cnt = 0
   for x in liste:
      if x == occ:
         cnt+=1
   print(cnt)

def exo9():
   count_occ([1, 4, 2, 7, 4, 4, 3, 4], 4)

def long_asc(liste):
   coord_start = []
   coord_end = []
   start = end = long = last = next = 0
   for x in range(len(liste)):
      start = x
      last = liste[x]
      next = last +1
      if(x < len(liste)-1):
         for y in range(start+1, len(liste)):
            if(liste[y] == next):
               long += 1
               last = liste[y]
               next = last + 1
               end = y
            else:
               long = 0
               coord_start.append(start)
               coord_end.append(end)
               break
   ind = 0
   longueur = []
   long = 0
   for x in range(len(coord_start)):
      longueur.append(coord_end[x]-coord_start[x])
   for x in range(len(longueur)):
      if(longueur[x] > long):
         long = longueur[x]
         ind = x
   arr = []
   start = coord_start[ind]
   end = coord_end[ind]
   for x in range(start, end+1):
      arr.append(liste[x])
   return arr

def exo10():
   arr = long_asc([1, 2, 2, 3, 2, 3, 4, 1, 2, 3, 4, 5, 3, 5, 7])
   print(arr)

def exo11():
   

menu = int(input("Entrez 1 pour l Exo 1\n2 pour l Exo 2\n3 pour l Exo 3\n4 pour l Exo 4\n5 pour l Exo 5\n6 pour l Exo 6\n7 pour l Exo 7\n8 pour l Exo 8\n9 pour l Exo 9\n10 pour l Exo 10\n"))
match menu:
   case 1:
      exo1()
   case 2:
      exo2()
   case 3:
      exo3()
   case 4:
      exo4()
   case 5:
      exo5()
   case 6:
      exo6()
   case 7:
      exo7()
   case 8:
      exo8()
   case 9:
      exo9()
   case 10:
      exo10()
   case 11:
      exo11()
   case _:
      print("Erreur : Veuillez rentrer un chiffre compris entre 1 et 2\n")

