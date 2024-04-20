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
   mon_tuple = (1, "chat", 3.14, True)
   print(mon_tuple[1])

def exo12():
    #A tuple is a collection which is ordered and unchangeable
    mon_tuple = (1, "chat", 3.14, True)
    mon_tuple[2] = "python"

def max_min_moy(tuple_t):
   moy = min = max = 0
   min = 60000
   for x in tuple_t:
      moy += x
      if(x < min):
         min = x
      if(x > max):
         max = x
   moy = moy/len(tuple_t)
   ret_tuple = (max, min, moy)
   return ret_tuple

def exo13():
   test_tuple = (10, 20, 30, 40, 50)
   print("Max, Min, Moyenne:", max_min_moy(test_tuple))

def sort_students(etuds):
   sort_studs = []
   for x in range(len(etuds)):
      max_ind = -1
      max_val = -1
      for y in range(len(etuds)):
         if(etuds[y][1]>max_val):
            max_ind = y
            max_val = etuds[y][1]
      sort_studs.append((etuds[max_ind][0], etuds[max_ind][1]))
      etuds.pop(max_ind)
   return sort_studs

def exo14():
   etudiants = [("Alice", 88), ("Bob", 95), ("Charlie", 78)]
   etudiants_tries = sort_students(etudiants)
   print(etudiants_tries)

def tri_actif(d):
   ret = []
   for x in d:
      if(x[2]=="actif"):
         ret.append(x)
   return ret

def tri_nb_desc(d):
   sort_tuple = []
   for x in range(len(d)):
      max_ind = -1
      max_val = -1
      for y in range(len(d)):
         if(d[y][1]>max_val):
            max_ind = y
            max_val = d[y][1]
      sort_tuple.append((d[max_ind][0], d[max_ind][1], d[max_ind][2]))
      d.pop(max_ind)
   return sort_tuple

def filtre_stat(d):
   tup = []
   for e in d:
      tup.append(e[0], e[1])
   return tup


def exo15():
   data = [("id1", 10, "actif"), ("id2", 15, "inactif"), ("id3", 20, "actif"), ("id4", 15, "inactif"), ("id5", 32, "actif"), ("id6", 26, "inactif")]
   ssmenu = input("Entrez A pour trier les actifs\nD pour trier par nombre décroissant\nS pour filtrer sans statut\n")
   match ssmenu:
      case 'A':
         print(tri_actif(data))
      case 'D':
         print(tri_nb_desc(data))
      case _:
         print(filtre_stat(data))

def exo16():
   livre = { "titre": "Les Misérables", "auteur": "Victor Hugo", "annee": "1862"}
   return livre["auteur"]

def exo17():
   livre = { "titre": "Les Misérables", "auteur": "Victor Hugo", "annee": "1862"}
   livre["annee"]="1865"
   livre["genre"]="Roman"
   return livre

def affiche_dict(d):
   for e in d.items():
      print(e)

def exo18():
   livre = exo17()
   affiche_dict(livre)

def exo19():
   dic1 = {"un": 1, "deux":2, "trois": 3}
   dic2 = {"quatre": 4, "cinq": 5, "six": 6}
   dico = {**dic1, **dic2}
   print(dico)

def exo20(d1, d2):
   d = []
   for x1, x2  in d2.items():
      for y1, y2 in d1.items():
         if (x2 == y1):
            z = {x1: y2}
            d.append(z)
   print(d)

def intersection_without_multiples_of_three(s1,s2):
   s = s1 & s2
   sr = {x for x in s if x%3!=0}
   #for x in s:
   #   if x % 3 != 0:
   #      sr 
   #print(sr)
   return sr

def exo21():
   set1 = {1, 2, 3, 4, 6, 9, 10}
   set2 = {2, 3, 5, 6, 7, 9, 10}
   print(intersection_without_multiples_of_three(set1, set2))

def union_excluding_n(lis, n):
   s = []
   for y in lis:
      s.append({x for x in y if(x != n)})
   return s

def exo22():
   list_of_sets = [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}]
   n = 5
   print(union_excluding_n(list_of_sets, n))

menu = int(input("Entrez un chiffre pour acceder a l exercice (de 1 a 22)\n"))
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
   case 12:
      exo12()
   case 13:
      exo13()
   case 14:
      exo14()
   case 15:
      exo15()
   case 16:
      print(exo16())
   case 17:
      print(exo17())
   case 18:
      exo18()
   case 19:
      exo19()
   case 20:
      exo20({"a": 1, "b": 2, "c": 3}, {"x": "a", "y": "b"})
   case 21:
      exo21()
   case 22:
      exo22()
   case _:
      print("Erreur : Veuillez rentrer un chiffre compris entre 1 et 2\n")

