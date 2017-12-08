import csv
from collections import Counter

# fichier a trier
input_file="reduced_combos.csv"

# ---- categories de competences classees par fichier 
base_file="competences_base.csv"
outil_file="competences_outil.csv"
big_file="competences_big.csv"
lang_file="competences_langage.csv"
visu_file="competences_visual.csv"
tech_file="competences_technique.csv"

output_file="sorted_combos.csv" # fichier de sortie
 
# --- astuce pour lire fichier csv sur une seule colonne 
def parse_keywords(filename):
  with open(filename, 'r') as f:
    return  f.read().splitlines()


#travail principal    
def sort():
  with open(output_file, 'w',newline='') as csv_file: #creation fichier de sortie + header
    writer = csv.writer(csv_file)
    writer.writerow(['combo'])
    csv_file.close
    
    
  #--- lecture des competences    
  base,outil,big,lang,visu,tech=read_lists()
  

  # ---- Denombrement  
  cnt_base = Counter()
  cnt_outil = Counter()
  cnt_big = Counter()
  cnt_lang = Counter()
  cnt_visu = Counter()
  cnt_tech = Counter()
  with open(output_file, 'a',newline='') as csv_file: # ouverture fichier de sortie
    writer = csv.writer(csv_file)	
    with open(input_file, 'r') as file:# ouverture fichier a trier
      input=csv.reader(file, delimiter=',') 
      for row in input:
        for word in row:
          if word in base:
            cnt_base["base de donnees"]+=1
          
          
          if word in outil:
            cnt_outil["outils"]+=1
          
          
          if word in big:
            cnt_big["big data"]+=1
         
        
          if word in lang:
            cnt_lang["langage"]+=1
       
          
          if word in visu:
            cnt_visu["visualisation"]+=1
         
          
          if word in tech:
            cnt_tech["techniques"]+=1
      
        words_list=[]
        cnt=cnt_base+cnt_outil+cnt_big+cnt_lang+cnt_visu+cnt_tech
        for key, value in cnt.items():
          words_list.append(key)
        if(len(words_list)>0):  
          writer.writerow(words_list)
          
     
        cnt_base.clear()
        cnt_outil.clear()
        cnt_big.clear()
        cnt_lang.clear()
        cnt_visu.clear()
        cnt_tech.clear()
      csv_file.close        

# ---- lecture de tous les fichiers de competences      
def read_lists():

  base = parse_keywords(base_file)
  outil = parse_keywords(outil_file)
  big = parse_keywords(big_file)
  lang = parse_keywords(lang_file)
  visu = parse_keywords(visu_file)
  tech = parse_keywords(tech_file)
    
      
  return base,outil,big,lang,visu,tech
  
  

sort() # appel principal