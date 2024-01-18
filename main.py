import pandas


## Iegūst failu kuru rediģēt
Fails = input("norādiet lūdzu failu: ")
## iegūst slaidu(sheet) kuru rediģēt
sheet = input("norādiet lūdzu sheetu: ")

## atver excel failu un iegūst vērtības
Atvert = pandas.read_excel(Fails, sheet_name=sheet,header=None)
info_list = Atvert.values.tolist()

## izveido sarakstus kurus uzglabās katras rindas iformāciju
vecums=[]
speletaji=[]
sazina=[]

## iziet curi visiām rindām un tiek vaļā no duplikātiem
for x in range(len(info_list)):
    vards = info_list[x][0]
    gads = info_list[x][1]
    e_pasts = info_list[x][2]
    if e_pasts not in sazina:
        if vards not in speletaji:
            sazina.append(e_pasts)
            speletaji.append(vards)
            vecums.append(gads)

## izveido divas kolonas kuras satāv no vecuma un e-pasta areses
d={"gads":vecums,"e-pasts":sazina}

## izveido un ievieto visu jaunajā tabulā 
df1 = pandas.DataFrame(index=speletaji,data=d)

## iegūst kā vēlas nosaukt jauno failu un saglabā to
nosaukums=input("kā nosaukt failu: ")
df1.to_excel(nosaukums+".xlsx")
