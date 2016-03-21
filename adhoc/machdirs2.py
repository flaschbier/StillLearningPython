import os,pprint,sys
while True:
    print()
    oq=input('Press the first directory:   ')
    print()
    print()
    ow=input('Press the next directory/name:   ')
    print()
    p2=input('Continue with next directory? yes or no: ').lower()
    if p2=='no':
        break
    print()
    oe=input('Press the next directory/name:   ')
    print()
    p3=input('Continue with next directory? yes or no: ').lower()
    if p3=='no':
        break
    print()
    oee=input('Press the next directory/name:   ')
    print()
    p4=input('Continue with next directory? yes or no: ').lower()
    if p4=='no':
        break
    print()
    ot=input('Press the next directory/name:   ')
    print()
    p5=input('Continue with next directory? yes or no: ').lower()
    if p5=='no':
        break
    print()
    oy=input('Press the next directory/name:   ')
    print()
    p6=input('Continue with next directory? yes or no: ').lower()
    if p6=='no':
        break
    print()
    ou=input('Press the next directory/name:   ')
    print()
    p7=input('Continue with next directory? yes or no: ').lower()
    if p7=='no':
        break
    print()
    if p2=='no':
        os.makedirs(oq+'\\'+ow)
    if p3=='no':
        os.makedirs(oq+'\\'+ow+'\\'+oe)
    if p4=='no':
        os.makedirs(oq+'\\'+ow+'\\'+oe+'\\'+oee)
    if p5=='no':
        os.makedirs(oq+'\\'+ow+'\\'+oe+'\\'+oee+'\\'+ot)
    if p6=='no':
        os.makedirs(oq+'\\'+ow+'\\'+oe+'\\'+oee+'\\'+ot+'\\'+oy)
    if p7=='no':
        os.makedirs(oq+'\\'+ow+'\\'+oe+'\\'+oee+'\\'+ot+'\\'+oy+'\\'+ou)
    ppp=input('Wannna continue???')
    if ppp=='no':
        sys.exit()
