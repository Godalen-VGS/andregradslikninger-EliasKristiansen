a=2
b=2
c=2


if b**2-4*a*c<0:
    print("ingen løsning")
  elif b**2-4*a*c==0:
    print("svaret er",(-b+(b**2-4*a*c)**0.5)/2*a)
  else:
    print("svarene er",(-b+(b**2-4*a*c)**0.5)/2*a,"og",(-b-(b**2-4*a*c)**0.5)/2*a)