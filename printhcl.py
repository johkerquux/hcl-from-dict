
def printhcl(mydict, ident=False):
    """
    Produces a multi-line string for use in terraform tfvars file from a dictionary
    :param mydict: Dict
    :param ident: Should the lines be idented or not
    :return s: Multi-line String in hcl format
    """

    s = ""
    for key, val in mydict.items():
        if ident:
            s += '\t'
        if isinstance(val, dict):
            if len(val) > 0:
                s += '{0} = {1}\n'.format(key, '{\n' + str(printhcl(val, ident=True)) + '\n}')
        elif isinstance(val, str):
            if ident:
                if key != 'value':
                    k = '"{}"'.format(key)
                else:
                    k = key
            else:
                k = key
            s += '{0} = {1}\n'.format(k, '"' + str(val) + '"')
        elif isinstance(val, list):
            s += key + ' = [\n'
            for i in val:
                if ident:
                    s += '\t'
                if isinstance(i, dict):
                    s += '\t{' + str(printhcl(i, ident=True)).strip() + '},\n'
                else:
                    s += '\t"{}",\n'.format(i)
            s = s[0:-2]
            s += '\n]\n'
        elif val is None:
            if ident:
                s += '"{0}" = {1}\n'.format(key, '""')
            else:
                s += '{0} = {1}\n'.format(key, '""')
        else:
            if ident:
                k = '"{}"'.format(key)
            else:
                k = key
            s += '{0} = {1}\n'.format(k, str(val).lower())
    return s

