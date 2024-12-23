import geocoder, time

def get_current_location():
    while 1:
        try:
            # Get your current location using the 'ipinfo.io' provider
            location = geocoder.ip('me')
            if location.latlng[0],==48.14827 and location.latlng[1]==19.554161:
                print("Hajnáčka Depo \nNasledujuce stanica: Hajnácka Zel. Stanica")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka Zel. Stanica \nNasledujuce stanica: Hajnácka Ipelské Tehelna")
            elif location.latlng[0]==48.144310 and location.latlng[1]==19.56830:
                print("Hajnácka Ipelské Tehelna \nNasledujuce stanica: Hajnácka cast Zel. Stanica")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.56355:
                print("Hajnácka cast Zel. Stanica \nNasledujuce stanica: Hajnácka Sasbik")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka Sasbik \nNasledujuce stanica: Hajnácka Gortva")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka Gortva \nNasledujuce stanica: Hajnácka Gortva do Zabodou")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka Gortva do Zabodou \nNasledujuce stanica: Hajnácka Kolónia")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka Kolónia \nNasledujuce stanica: Hajnácka Kolónia do Pose")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Kolónia do Pose \nNasledujuce stanica: Hajnácka do Kolónia")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka do Kolónia \nNasledujuce stanica: Hajnácka do Doh.")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka do Doh. \nNasledujuce stanica: Hajnácka do Ostrá skala")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka do Ostrá skala \nNasledujuce stanica: Hajnácka Doh.")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka Doh. \nNasledujuce stanica: Hajnácka Durenda")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka Durenda \nNasledujuce stanica: Hajnácka do Hrad")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka do Hrad \nNasledujuce stanica: Hajnácka Nové Cintorín")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka Nové Cintorín \nNasledujuce stanica: Hajnácka do Ragácou")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka do Ragácou \nNasledujuce stanica: Hajnácka ulica Nového")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka ulica Nového \nNasledujuce stanica: Hajnácka ulica Na Hradu")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka ulica Na Hradu \nNasledujuce stanica: Hajnácka ulica Selecov")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka ulica Selecov \nNasledujuce stanica: Hajnácka Zabovy")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka Zabovy \nNasledujuce stanica: Hajnácka Pekáren")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka Pekáren \nNasledujuce stanica: Hajnácka Lekáren")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka Lekáren \nNasledujuce stanica: Hajnácka Futbal Stadion")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka Futbal Stadion \nNasledujuce stanica: Hajnácka ulica Pesov")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka ulica Pesov \nNasledujuce stanica: Hajnácka Centrum")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka Centrum \nNasledujuce stanica: Hajnácka do Centrum")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka do Centrum \nNasledujuce stanica: Hajnácka Doh.")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka Doh. \nNasledujuce stanica: Hajnácka Posa")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka Posa \nNasledujuce stanica: Hajnácka do Tilic")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka do Tilic \nNasledujuce stanica: Hajnacka Do Tenkes")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnacka Do Tenkes \nNasledujuce stanica: Hajnácka Tenkes")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka Tenkes \nNasledujuce stanica: Hajnácka do S.J.R.D.")
            elif location.latlng[0]==48.14489 and location.latlng[1]==19.555331:
                print("Hajnácka do S.J.R.D.")
        # Print the latitude and longitudeprint("železničná stanica \nNasledujuce stanica: ip teh")
            if location:
                print("Latitude:", location.latlng[0])
                print("Longitude:", location.latlng[1])
            else:
                print("Location not found")
    
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1)

if __name__ == "__main__":
    get_current_location()
