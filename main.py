import re

def spocitej_celkovou_utratu(text):
    """
    Spočítá celkovou útratu na základě nalezených částek ve formátu '-X,XX Kč'.
    """
    pattern = r"-\d+,\d+ Kč"
    matches = re.findall(pattern, text)
    total = sum(float(match.replace(' Kč', '').replace(',', '.')) for match in matches)
    return total

if __name__ == "__main__":
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            text = file.read()

        celkova_utrata = spocitej_celkovou_utratu(text)
        print("💰 Celková útrata: {:.2f} Kč".format(celkova_utrata))

    except FileNotFoundError:
        print("❌ Soubor 'data.txt' neexistuje. Vytvoř ho.")
    except Exception as e:
        print(f"⚠️ Nastala chyba: {e}")
