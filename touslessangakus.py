TAILLE=500
pourcentage=0.05
from math import *

def decalage(c,percent=pourcentage):
    return "\"translate("+str(c*percent)+","+str(c*percent)+")\""

#grouper deux rectangles pour définir le cadre
def rectangle(c=TAILLE,percent=pourcentage,transform=""):
    s="<g> <rect x=\""+str(percent*c)+"\" y=\""+str(c*percent)+"\" width=\""+str(c)+"\" height=\""+str(c)+"\" fill=\"none\" stroke=\"red\" transform="+transform+ "/>\n"
    print(s)
    sprime="<rect x=\"0\" width=\""+str(c*(1+2*percent))+"\" height=\""+str(c*(1+2*percent))+"\" rx=\"25\" fill=\"none\" stroke=\"red\" transform="+transform+ "/></g>\n"
    print(sprime)
    return s+"<rect x=\"0\" width=\""+str(c*(1+2*percent))+"\" height=\""+str(c*(1+2*percent))+"\" rx=\"25\" fill=\"none\" stroke=\"red\" transform="+transform+ "/></g>\n"

def simplerectangle(c=TAILLE,percent=pourcentage,transform=""):
    s="<rect x=\""+str(0)+"\" y=\""+str(0)+"\" width=\""+str(c)+"\" height=\""+str(c)+"\" fill=\"none\" stroke=\"red\" transform="+transform+ "/>\n"
    return s

def ligne(debut,fin,transform=""):
     s="<line x1=\""+str(debut[0])+"\" y1=\""+str(debut[1])+"\" x2=\""+str(fin[0])+"\" y2=\""+str(fin[1])+"\" stroke=\"red\"   transform="+transform+" />\n"
     return s
    

def equilateral(c=TAILLE,transform=""):
    hauteur=c*sqrt(3)/2
    return "<polygon points=\"0 "+str(c)+" ,"+str(c/2)+" "+str(c-hauteur)+" , "+str(c)+" "+str(c)+"\" fill=\"none\" stroke=\"red\" transform="+transform+"/>\n"

def cercle(cx,cy,rayon,transform=""):
    return "<circle cx=\""+str(cx)+"\" cy=\""+str(cy)+"\"  r=\""+str(rayon)+"\" transform="+transform+" fill=\"none\" stroke=\"red\"/>\n"


def distance(p1,p2):
    difx=(p1[0]-p2[0])*(p1[0]-p2[0])
    dify=(p1[1]-p2[1])*(p1[1]-p2[1])
    return sqrt(difx+dify)

def resoutCercle(p1,p2,p3):
    #retourne centre et rayon du cercle inscrit dans un triangle de sommets p1,p2,p3
    #longueur du cote oppose au point point1
    dist1=distance(p2,p3)
    dist2=distance(p1,p3)
    dist3=distance(p1,p2)
    denom=dist1+dist2+dist3
    #coordonnees du centre
    cx=(dist1*p1[0]+dist2*p2[0]+dist3*p3[0])/denom
    cy=(dist1*p1[1]+dist2*p2[1]+dist3*p3[1])/denom
    #rayon du cercle
    s=(dist1+dist2+dist3)/2
    radius=sqrt(s*(s-dist1)*(s-dist2)*(s-dist3))/s
    return (cx,cy),radius
    


def equilateralPenche(c=TAILLE,transform=""):
    a=(2-sqrt(3))*c
    b=c-a
    return "<polygon  points=\""+str(c)+" 0 ,"+str(b)+" "+str(c)+" ,  0 "+str(a)+" \" fill=\"none\" stroke=\"red\" transform="+transform+"/>\n"

def sangakupb36page114(a=TAILLE):
    entete="<svg viewBox=\"0 0 "+str(2*a)+" "+str(2*a)+"\" xmlns=\"http://www.w3.org/2000/svg\">\n"
    pied="</svg>\n"
    image=open("sangakuPB36page114test.svg","w")
    image.write(entete)
    image.write(rectangle(a))
    translation=decalage(a)
    image.write(equilateral(a,translation))
    r=a*sqrt(3)/6
    t=(sqrt(3)-1)*r
    petitr=(2-sqrt(3))/4*a
    image.write(cercle(a/2,a-r,r,translation))
    image.write(cercle(a-t,t,t,translation))
    image.write(cercle(t,t,t,translation))
    image.write(cercle(a/2,petitr,petitr,translation))


    image.write(pied)
    image.close()


def readSteiner(c=TAILLE,filename="steiner.txt"):
    echelle=475
    translation="\"translate("+str(c+2*c*pourcentage)+","+str(c+2*c*pourcentage)+")\""
    entete="<svg viewBox=\"0 0 "+str(2*c)+" "+str(2*c)+"\" xmlns=\"http://www.w3.org/2000/svg\">\n <g>"
    pied="</g></svg>\n"
    image=open("steinerxx.svg","w")
    image.write(entete)
    image.write(rectangle(c=2*TAILLE))
    entree=open(filename,"r")
    lignes=entree.readlines()
    image.write("<g>")
    for l in lignes[:-2]:
        t=l.split(' ')
        tf=[float(u) for u in t]
        image.write(cercle(tf[0]*echelle,tf[1]*echelle,tf[2]*echelle,translation))
    image.write("</g>")
    
    image.write(pied)
    image.close()
    

def sangakupb9Page96(a=TAILLE):
    entete="<svg viewBox=\"0 0 "+str(2*a)+" "+str(2*a)+"\" xmlns=\"http://www.w3.org/2000/svg\">\n"
    pied="</svg>\n"
    image=open("sangakupb9Page96test.svg","w")
    image.write(entete)
    image.write(rectangle(a))
    translation=decalage(a)
    r=sqrt(2)/(1+3*sqrt(2))*a
    image.write(simplerectangle(2*r,transform=translation))
    print("step")
    image.write(cercle(a-r,a-r,r,translation))
    image.write(ligne([4*r-a,a],[a,4*r-a],translation))
    image.write(pied)
    image.close()

def sangakupb10Page152(a=TAILLE):
    entete="<svg viewBox=\"0 0 "+str(2*a)+" "+str(2*a)+"\" xmlns=\"http://www.w3.org/2000/svg\">\n"
    pied="</svg>\n"
    image=open("sangakuPB10page152test.svg","w")
    image.write(entete)
    image.write(rectangle(a))
    translation=decalage(a)
    alpha=atan(sqrt(3)-sqrt(2))
    tan2alpha=tan(2*alpha)
    p1=(0,a)
    p2=(a,a)
    p3=(a/2,a-(a/2*tan2alpha))
    centre,rayon=resoutCercle(p1,p2,p3)
    print(rayon," ",a)
    image.write(cercle(centre[0],centre[1],rayon,translation))
    centrey=(1-sqrt(3)/2)*a+2*rayon
    image.write(cercle(a/2,centrey,rayon,translation))
    #calcul du point D
    coef=1+tan2alpha*sqrt(3)/3
    ux=a/coef
    hauteur=ux*tan2alpha
    image.write(ligne((0,a),(ux,a-hauteur),translation))
    image.write(ligne((a,a),(a-ux,a-hauteur),translation))
    image.write(equilateral(a,translation))
    image.write(pied)
    image.close()
    
	
    		
     	

def sangaku(c=TAILLE):
    entete="<svg viewBox=\"0 0 "+str(2*c)+" "+str(2*c)+"\" xmlns=\"http://www.w3.org/2000/svg\">\n"
    pied="</svg>\n"
    image=open("sangakuOriginaltest.svg","w")
    image.write(entete)
    image.write(rectangle(c))
    translation=decalage(c)
    
    image.write(equilateralPenche(c,translation))
    

    # Des petites verifications intermediaires et des calculs de coordonnees
    
    # coordonnees du sommet h
    a1=(sqrt(3)-1)/(sqrt(3)+1)*c
    h=2*(sqrt(3)-1)/(sqrt(3)+1)*c
    #image.write(cercle(a1,h,5,translation))
    #coordonnees du sommet h1
    b1=c*sqrt(3)/(2*(3-sqrt(3)))
    b2=c-b1
    h1=sqrt(3)/3*b2
    #image.write(cercle(c-h1,b1,5,translation))
    
    #resolution du grand cercle
    point1=(a1,h)
    point2=((sqrt(3)-1)*c,c)
    point3=(0,c)
    centre,rayon=resoutCercle(point1,point2,point3)
    grandR=rayon
    image.write("<g>")
    image.write(cercle(centre[0],centre[1],rayon,translation))
    image.write(equilateral(c,translation))
    image.write("</g>")

    #resolution du petit cercle
    point1=(c-h1,b1)
    point2=(c,0)
    point3=(c,c)
    centre,rayon=resoutCercle(point1,point2,point3)
    petitR=rayon
    print(grandR,petitR,petitR/grandR)
    image.write(cercle(centre[0],centre[1],rayon,translation))

    """
    #longueur du cote oppose au point point1
    dist1=distance(point2,point3)
    dist2=distance(point1,point3)
    dist3=distance(point1,point2)
    denom=dist1+dist2+dist3
    #coordonnees du centre
    cx=(dist1*point1[0]+dist2*point2[0]+dist3*point3[0])/denom
    cy=(dist1*point1[1]+dist2*point2[1]+dist3*point3[1])/denom
    #rayon du cercle
    s=(dist1+dist2+dist3)/2
    radius=sqrt(s*(s-dist1)*(s-dist2)*(s-dist3))/s
    image.write(cercle(cx,cy,radius,translation))
    """
    image.write(pied)
    image.close()
    
sangaku()
sangakupb10Page152()
sangakupb9Page96()
sangakupb36page114()
print("fini")