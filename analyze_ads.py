import re
import csv
from stop_words import get_stop_words
from collections import Counter
import glob

output_file='keywords_list.csv' ### fichier final


def chunk_space(chunk):
  chunk_out = chunk + ' ' # Need to fix spacing issue
  return chunk_out  
  
# -------- Compter les mots d'un article
def filter_ad(filename):
  try:
    file=open( filename,'r')
    print('analyzing '+filename)
    lines = (line.strip() for line in file.read().splitlines()) 
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = ''.join(chunk_space(chunk) for chunk in chunks if chunk).encode('utf-8') 
    text=text.decode('utf-8')
      if text.find('Apec.fr')<0: ### les annonces Apec ne sont pas correctements aspirees, ne pas les traiter
      
#--- nettoyage de l'annonce      
        text = re.sub("[^a-zA-Z.+3]"," ", text)
        text = text.lower().split() 
        stop_words = get_stop_words('french')
        text = [w for w in text if not w in stop_words]
        text=' '.join(word for word in text if len(word)<20).split()
#--- Comptage de chaque mot        
        cnt = Counter()
        for word in text:
          cnt[word] += 1
          with open(output_file, 'a',newline='') as csv_file:
            writer = csv.writer(csv_file)	
            for key, value in dict(cnt).items():
              writer.writerow([key, value])
            csv_file.close()
  except Exception as e:
    print("Erreur dans le traitement de "+filename)
    print(e)
    print('***')
		
# ------ Boucle principale
def run():
  filelist=glob.glob("ads/*.txt") ### les annonces sont stockees dans ads/
  with open(output_file, 'w',newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['word','count']) #header
  csv_file.close()
  for f in filelist:# pour chaque annonce
    filter_ad(f)
  print("Termine")
	
run()  # Appel principal