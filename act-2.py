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

Clave=input("inserte una palabra clave ")
Posts=Primos+NoPrimos
cont=[0,0]
contforPost=[]
id=[]
for post in Posts:
    cont[0]=cont[1]
    post=eval(post)
  
    
    title_palabras=post["title"].split()

    for palabra in title_palabras:
        print(palabra," ",Clave)
        if palabra==Clave:
            contforPost.append(1)
            id.append(post["id"])
            cont[0]+=1

            break
    print(" ")
    body_palabras=post["body"].split()
    for palabra in body_palabras:
        print(palabra," ",Clave)
        if palabra==Clave  :
           
            if cont[0]==cont[1]:
                
                contforPost.append(1)
                id.append(post["id"])
            else:
                contforPost[cont[0]]+=1
            cont[0]+=1
            break
print(f"Post      Ocurrencias de {Clave}")
for i in range(cont[0]):
    print(f"{id[i]}            {contforPost[i]}")
print(f"Total de Ocurrencias de {Clave}: {cont[0]}")
    



