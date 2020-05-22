def findEmailDomain(address):
    # for i in range(len(address)-1, 0, -1):
    #     if address[i] == "@":
    #         return address[i+1:]

    return address.split("@")[-1]
