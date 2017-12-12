import re
import csv
from collections import Counter
import glob
import unidecode

output_file='keywords_list_2.csv'
input_file="competences2.csv"


def words_in_string(word_list, a_string):
  return set(word_list).intersection(a_string.split())
  
  
# ------ gerer le mot "R'  
  
def find_R_word(text,writer):
 
    text=unidecode.unidecode(text)
    text_subbed=re.sub("[^a-zA-Z.+3]"," ", text)
    
    cnt = Counter()
      
    for word in words_in_string( ['R'],text_subbed): # detecter si 'R' apparait dans le texte
      cnt[word] += 1
      
    for word in words_in_string( ['R&D'],text): #mais l'enlever si 'R&D' est present
      cnt.clear()
    
    
    for key, value in dict(cnt).items():
      writer.writerow([key, value])#write to file
    return cnt  
    
    
# ------ chercher les expressions composes   
  
def find_multi_words(text,writer,multiple_list):
  text = re.sub("[^a-zA-Z.+3]"," ", text)    
  text = text.lower()
  cnt = Counter()
  
  for key in multiple_list:   
    if key in text: 
      cnt[key] += 1
      
  for key, value in dict(cnt).items():
    writer.writerow([key, value])
  return cnt    

  
# ------ chercher les mots simples 
  
def find_single_words(text,writer,key_list):
  text = re.sub("[^a-zA-Z.+3]"," ", text)    
  text = text.lower()
  cnt = Counter()
  for word in words_in_string( key_list,text): 
    cnt[word] += 1
    
  for key, value in dict(cnt).items():
    writer.writerow([key, value])  
  return cnt
  
  
  
# ------ chercher les combos de mots  
def find_words_combo(output_file,cnt):
  with open("combo_"+output_file, 'a',newline='') as csv_file:
    writer = csv.writer(csv_file)	
    words_list=[]
    for key, value in cnt.items():
      words_list.append(key)
    if(len(words_list)>1):
      writer.writerow(words_list)
    csv_file.close
  

# ------ fouiller dans l'annonce  
def find_keywords(filename, key_list, multiple_list):
  try:
    file=open( filename,'r')
    text=file.read()  
    if text.find('Apec')<0:
      with open(output_file, 'a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        cnt_R = Counter()
        cnt_s = Counter()
        cnt_m = Counter()       
        cnt_R=find_R_word(text,writer)##R
        cnt_m=find_multi_words(text,writer,multiple_list) ##multiple
        cnt_s=find_single_words(text,writer,key_list) #mot simple
        csv_file.close
        
      #### combos  
      with open("combo_"+output_file, 'a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        find_words_combo(output_file,cnt_R+cnt_s+cnt_m)
        csv_file.close
    file.close()
  except Exception as e:
    print("Erreur dans le traitement de "+filename)
    print(e)
    print('***')
    return 1
  return 0  

# ------ gerer fichier csv n'ayant qu'une seule colonne
def parse_keywords(filename):
  with open(filename, 'r') as f:
    return  f.read().splitlines()

# ------ separer les mots en groupes 'un seul mot' ou 'plusieurs mots'    
def split_lists(input_list):
  more_words_list=[]
  one_word_list=[]
  for key in input_list:
    if len(key.split()) >1:## multiples mots
      more_words_list.append(key)
    else:
      one_word_list.append(key) ##mot unique
  return one_word_list,more_words_list

  
# ----- boucle principale  
def map_keywords():	
  with open("combo_"+output_file, 'w',newline='') as csv_file: #creer le fichier de sortie pour les combos + header
    writer = csv.writer(csv_file)
    writer.writerow(['combo']) #header
    csv_file.close()
    
  # lister toutes les annonces dans le dossier ads/   
  filelist=glob.glob("ads/*.txt") 
  
  # separer competences.csv en deux listes "mots simples" 
    keylist,multiple_keylist=split_lists(parse_keywords(input_file)) "mots composes"
  
  with open(output_file, 'w',newline='') as csv_file: #creer le fichier de sortie + header
    writer = csv.writer(csv_file)
    writer.writerow(['word','count']) #header
  csv_file.close()
  
  i=0
  for f in filelist:
    i=i+find_keywords(f,keylist,multiple_keylist)#travail principal
    
  print("--------------")
  print(str(len(filelist))+" fichiers traites")
  print(str(len(filelist)-i)+" fichiers analyses")
  print(str(i)+" fichiers invalides")
  

map_keywords() # ---- appel principal





