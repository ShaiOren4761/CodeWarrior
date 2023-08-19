#  https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

def domain_name(url):
    if url.count('www'):  # //if there's a 'www' we can find the first dot.
        url = url[url.index('.') + 1:]
        return url[:url.index('.')]

    elif url.count('//'):  # if there is no 'www', we go by the '//'
        return url[url.index('/') + 2: url.index('.')]

    # if there is no 'www' nor '//', the first dot must follow after the domain name.
    else:
        return url[:url.find('.')]


def domain_name_ultimate(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

