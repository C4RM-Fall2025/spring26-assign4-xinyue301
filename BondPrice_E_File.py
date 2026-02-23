

def getBondPrice_E(face, couponRate, yc):
   
    pvfcsum = 0
    cf = face * couponRate  

    n = len(yc)  

    for t, y in enumerate(yc, start=1):  
        pvfc = cf / (1 + y) ** t

        if t == n:  
            pvfc = pvfc + face / (1 + y) ** t

        pvfcsum = pvfcsum + pvfc

    return pvfcsum
