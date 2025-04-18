
file_name = input("Ime datoteke: ")

try:
    
    with open(file_name, 'r') as file:
        total_confidence = 0
        count = 0

        
        for line in file:
            
            if line.startswith("X-DSPAM-Confidence:"):
              
                try:
                    confidence = float(line.split(":")[1].strip())
                    total_confidence += confidence
                    count += 1
                except ValueError:
                    continue

        if count > 0:
            average_confidence = total_confidence / count
            print(f"Average X-DSPAM-Confidence: {average_confidence}")
        else:
            print("Nema pronađenih linija oblika 'X-DSPAM-Confidence:'.")

except FileNotFoundError:
    print(f"Datoteka '{file_name}' nije pronađena.")
except Exception as e:
    print(f"Dogodila se greška: {e}")