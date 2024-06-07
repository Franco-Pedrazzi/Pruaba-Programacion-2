import webbrowser,requests,os,json
Primos=[]
NoPrimos=[]

def nroDePostsRevicion():
    nroDePosts=input("inserte un numero entre el 1 y el 100 ")
    if nroDePosts.isdecimal()==True:
        nroDePosts=int(nroDePosts)
        if nroDePosts>0 and nroDePosts<101:
            return nroDePosts
        else:
            return nroDePostsRevicion()
    else:
        return nroDePostsRevicion()
    
def esPrimo(nro):
    for i in range(nro):
        if (nro%(i+1)==0 and (i+1)>1 and i<nro-1) or nro==1:
     
            return False
    return True

nroDePosts=nroDePostsRevicion()

for n in range(nroDePosts):
    post=requests.get(f"https://jsonplaceholder.typicode.com/posts/{n+1}")
    print(n+1)
    if esPrimo(n+1)==True:
        Primos.append(post.text)
    else:
        NoPrimos.append(post.text)

Primos=json.dumps(Primos)
NoPrimos=json.dumps(NoPrimos)

if os.path.exists("dir")==False:
    os.makedirs("dir")
os.chdir("dir")

Px=0
while os.path.exists(f"dl{Px}Primes.json"):
    Px+=1
NPx=0
while os.path.exists(f"dl{NPx}NotPrimes.json"):
    NPx+=1

Primosjson=open(f"dl{Px}Primes.json","w")
NoPrimosjson=open(f"dl{NPx}NotPrimes.json","w")

for post in Primos:
    Primosjson.write(post)
for post in NoPrimos:
    NoPrimosjson.write(post)
