def defanging_ip(adress):
    adress = adress.replace('.', '[.]')
    return print(adress)


defanging_ip(input('input IP adress\n'))