
def getBondDuration(y, face, couponRate, m, ppy = 1):
    
    pvcfsum = 0        
    sumProduct = 0     

    if ppy == 1:
        cf = face * couponRate

        for t in range(1, m + 1):
            pvcf = cf * (1 + y) ** (-t)

            if t == m:
                pvcf = pvcf + face * (1 + y) ** (-t)

            pvcfsum += pvcf
            sumProduct += t * pvcf

        bondDuration = sumProduct / pvcfsum

    else:
        y = y / ppy
        couponRate = couponRate / ppy
        m = m * ppy

        cf = face * couponRate

        for t in range(1, m + 1):
            pvcf = cf * (1 + y) ** (-t)

            if t == m:
                pvcf = pvcf + face * (1 + y) ** (-t)

            pvcfsum += pvcf
            sumProduct += t * pvcf

        bondDuration = (sumProduct / pvcfsum) / ppy

    return bondDuration

