import pip
fo = open("C:/SALHI OMAR/requir", "r")
inp = fo.read()
ls =inp.split()

for i in ls:
    pip.main(['install',i])