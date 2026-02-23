

def getBondPrice_Z(face, couponRate, times, yc):

    cf_coupon = face * couponRate   
    bondPrice = 0

    for t, y in zip(times, yc):

        pvcf = cf_coupon / (1 + y) ** t

        if t == max(times):
            pvcf = pvcf + face / (1 + y) ** t

        bondPrice = bondPrice + pvcf

    return bondPrice
