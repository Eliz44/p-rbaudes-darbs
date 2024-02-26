def lasit_un_drukaj_failu(faila_cele):
    try:
        with open(faila_cele, 'r', encoding='utf-8') as fails:
            saturs = fails.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Faila '{faila_cele}' nav atrasts.")
    except Exception as e:
        print(f"Ir radusies kļūda: {e}")

faila_cele = 'aka.txt'
lasit_un_drukaj_failu(faila_cele)
import csv

def lasit_un_drukaj_ceturtas_kolonnas(faila_cele):
    try:
        with open(faila_cele, 'r', newline='', encoding='utf-8') as fails:
            lasitajs = csv.reader(fails)
            
            
            kolonnu_nosaukumi = next(lasitajs)
            
            
            if len(kolonnu_nosaukumi) < 4:
                print("Failā nav pietiekami daudz kolonnu.")
                return
            
            ceturta_kolonna = [rinda[3] for rinda in lasitajs]
            
            print("Ceturta kolonna:")
            for elements in ceturta_kolonna:
                print(elements)
    except FileNotFoundError:
        print(f"Faila '{faila_cele}' nav atrasts.")
    except Exception as e:
        print(f"Ir radusies kļūda: {e}")

csv_faila_cele = 'aka.csv'
lasit_un_drukaj_ceturtas_kolonnas(csv_faila_cele)
def lasit_un_drukaj_rindas(faila_cele):
    try:
        with open(faila_cele, 'r', encoding='utf-8') as fails:
            rindas = fails.readlines()
            
           
            if len(rindas) < 4:
                print("Failā nav pietiekami daudz rindu.")
                return
            
            
            print("Trešās rindas saturs:")
            print(rindas[2].strip())  
            
            print("\nCeturtās rindas saturs:")
            print(rindas[3].strip())
            
    except FileNotFoundError:
        print(f"Faila '{faila_cele}' nav atrasts.")
    except Exception as e:
        print(f"Ir radusies kļūda: {e}")


faila_cele = 'aka.txt'
lasit_un_drukaj_rindas(faila_cele)
def lasit_un_drukaj_failu_saturs():
    try:
        
        faila_nosaukums = input("Ievadiet faila nosaukumu: ")
        paplasinajums = input("Ievadiet faila paplašinājumu (piemēram, txt): ")
        
        
        faila_cele = f"{faila_nosaukums}.{paplasinajums}"
        
        with open(faila_cele, 'r', encoding='utf-8') as fails:
            saturs = fails.read()
            print(f"Faila '{faila_cele}' saturs:")
            print(saturs)
            
    except FileNotFoundError:
        print(f"Faila '{faila_cele}' nav atrasts.")
    except PermissionError:
        print(f"Nav atļaujas lasīt failu '{faila_cele}'.")
    except Exception as e:
        print(f"Ir radusies kļūda: {e}")


lasit_un_drukaj_failu_saturs()
def ievadit_un_ierakstit_vardu():
    try:
       
        lietotaja_vards = input("Ievadiet savu vārdu: ")
        
        
        faila_nosaukums = "aka.txt"
        
        
        with open(faila_nosaukums, 'w', encoding='utf-8') as fails:
            fails.write(lietotaja_vards)
        
        print(f"Vārds '{lietotaja_vards}' veiksmīgi ierakstīts failā '{faila_nosaukums}'.")
            
    except PermissionError:
        print(f"Nav atļaujas rakstīt failā '{faila_nosaukums}'.")
    except Exception as e:
        print(f"Ir radusies kļūda: {e}")


ievadit_un_ierakstit_vardu()
def ievadit_un_ierakstit_vardu():
    try:
        
        lietotaja_vards = input("Ievadiet savu vārdu: ")
        
        
        faila_nosaukums = "lietotajs.txt"
        
        
        with open(faila_nosaukums, 'w', encoding='utf-8') as fails:
            fails.write(lietotaja_vards)
        
        print(f"Vārds '{lietotaja_vards}' veiksmīgi ierakstīts failā '{faila_nosaukums}'.")
            
    except PermissionError:
        print(f"Kļūda: Nav atļaujas rakstīt failā '{faila_nosaukums}'.")
    except Exception as e:
        print(f"Ir radusies kļūda: {e}")


ievadit_un_ierakstit_vardu()







