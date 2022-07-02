def q468(queryIP):
    if queryIP.find(':') < 0:
        queryIP = queryIP.split('.')
        if len(queryIP) != 4:
            return 'Neither'
        for i in range(len(queryIP)):
            if not str(queryIP[i]).isdigit():
                return 'Neither'
            if int(queryIP[i]) < 0 or int(queryIP[i]) > 255:
                return 'Neither'
            if len(queryIP[i]) > 1:
                if queryIP[i][0] == '0':
                    return 'Neither'
        return 'IPV4'
    else:
        queryIP = queryIP.split(':')
        if len(queryIP) != 8:
            return 'Neither'
        for i in range(len(queryIP)):
            if len(queryIP[i]) <= 0 or len(queryIP[i]) >= 5:
                return 'Neither'
            if not queryIP[i].isalnum():
                return 'Neither'
        return 'IPV6'


print(q468("12.12.12.12.12"))
