tekst=input("Ievadiet tekstu:" )
def replaceDivi(tekst):
  if tekst.count("2")>0:
    tekst=tekst.replace("2", "divi")
    print (tekst)
  else:
    tekst="Nekas netika aizveitots" 
    print(tekst)
  return tekst  
replaceDivi(tekst)
