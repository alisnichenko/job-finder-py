# Logging file. Probably not necessary.

def info(tag: str, data: object) -> None:
    """
    Accepts the type of the output and formats the output with the given
    message. More functionality will include formatting the data in a table
    and more. For now it's just printing out with a tag in front of it.

    Args:
        type: char variable from subset s = {"i", "e", "d", ...} that signifies 
        the type of the output and determines the information being shown.
        data: the data with implemented print() method to be shows in the
        console.
    Remarks:
        More functionality will come in the future.
    """
    if (tag == "i"):
        print("[INFO]", data)
    if (tag == "e"):
        print("[ERROR]", data)
    if (tag == "d"):
        if (type(data) is list):
            print("[DATA]", "Outputting ", len(data), " lines of data below:")
            for bit in data:
                print(bit)
        if (type(data) is dict):
            print("[DATA]", "Outputting ", len(data), " lines of data below:")
            for key, val in data:
                print(key, ": ", val)