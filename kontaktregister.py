# ===================================================
# Ett enkelt kontaktregister
# ===================================================

def visa_kontakt(namn, kontakter):
    # Dictionaries använder 'in' för att kolla om en nyckel finns
    if namn in kontakter:
        info = kontakter[namn]
        print(f"\n--- {namn} ---")
        print(f"Telefon: {info['telefon']}")
        print(f"Email: {info['email']}")
    else:
        print(f"Kontakten '{namn}' finns inte.")


def visa_alla(kontakter):
    if not kontakter:
        print("Inga kontakter sparade.")
        return
    
    print("\n--- Alla kontakter ---")
    for namn, info in kontakter.items():
        print(f"{namn}: {info['telefon']}")


def lagg_till_kontakt(kontakter):
    # input() läser text från användaren
    namn = input("Namn: ")
    telefon = input("Telefon: ")
    email = input("Email: ")
    
    # Skapa en dictionary för denna kontakt
    kontakter[namn] = {
        "telefon": telefon,
        "email": email
    }
    print(f"'{namn}' tillagd!")


def ta_bort_kontakt(kontakter):
    namn = input("Vem vill du ta bort? ")
    
    if namn in kontakter:
        # 'del' tar bort från dictionary
        del kontakter[namn]
        print(f"'{namn}' borttagen!")
    else:
        print(f"'{namn}' finns inte.")


def redigera_kontakt(kontakter):
    namn = input("Vem vill du redigera? ")
    
    if namn in kontakter:
        print(f"Nuvarande telefon: {kontakter[namn]['telefon']}")
        print(f"Nuvarande email: {kontakter[namn]['email']}")
        
        telefon = input("Ny telefon (tryck Enter för att behålla): ")
        email = input("Ny email (tryck Enter för att behålla): ")
        
        if telefon:
            kontakter[namn]['telefon'] = telefon
        if email:
            kontakter[namn]['email'] = email
        
        print(f"'{namn}' uppdaterad!")
    else:
        print(f"'{namn}' finns inte.")

    def sok_kontakter(kontakter):
        sokterm = input("Sök: ").lower()
    
    hittade = []
    for namn in kontakter:
        if sokterm in namn.lower():
            hittade.append(namn)
    
    if hittade:
        print(f"\nHittade {len(hittade)} kontakt(er):")
        for namn in hittade:
            print(f"  - {namn}: {kontakter[namn]['telefon']}")
    else:
        print("Inga kontakter matchade sökningen.")
# ===================================================
# Huvudprogram med meny
# ===================================================

# En dictionary - som Dictionary<string, object> i C#
# Nyckel: namn, Värde: en till dictionary med info
kontakter = {
    "Anna": {"telefon": "070-1234567", "email": "anna@mail.se"},
    "Erik": {"telefon": "070-9876543", "email": "erik@mail.se"}
}

print("Välkommen till kontaktregistret!")

# En loop som körs tills användaren avslutar
while True:
    print("\n[1] Visa alla")
    print("[2] Sök kontakt")
    print("[3] Lägg till")
    print("[4] Ta bort")
    print("[5] Avsluta")
    Print("[6] Robin fyller åt")
    
    val = input("\nVälj (1-5): ")
    
    if val == "1":
        visa_alla(kontakter)
    elif val == "2":
        namn = input("Sök namn: ")
        visa_kontakt(namn, kontakter)
    elif val == "3":
        lagg_till_kontakt(kontakter)
    elif val == "4":
        ta_bort_kontakt(kontakter)
    elif val == "5":
        print("Hejdå!")
        break  # Avbryter while-loopen
    elif val =="6":
        print("Arvin gillar den nya noccon")

    else:
        print("Ogiltigt val, försök igen.")