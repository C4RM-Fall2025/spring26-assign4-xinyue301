

def getBondPrice_E(face, couponRate, yc):
    pvcf=0
    cf=face*couponRate
    for i, y in enumerate(yc)
    pvcf=cf/(1+y)**i
    if i==m:
        pvcf=pvcf+face/(1+y)**i
    pvcfsum=pvcfsum+pvcf
return(pvcfsum)
