"""

2 Teilaufgaben

    leerzeichen vorne und hinten weg
    zeilenumbrüche vorne und hinten weg
    doppelte leerzeichen entfernen

    die menge der wörter zählen

Rückgabe

{
    "data" : "Hallo Welt von Python",
    "word_count" : 4
}

"""

def text_verarbeiter(text):

    def cleanup(text):
        #return text.strip().replace("\n", "").replace( "  ", " ")
        return " ".join(text.strip().lower().split())


    def count_words(text):
        return len(cleanup(text).split(" "))

    return {
        "data": cleanup(text),
        "word_count": count_words(text)
    }


def text_cleaner(text):

    def cleanup(t):
        return " ".join(t.strip().lower().split())

    def count_words(t):
        return len(t.split())

    clean_text = cleanup(text)
    word_count = count_words(clean_text)

    return {
        "data": clean_text,
        "word_count": word_count
    }


# Test
ergebnis = text_verarbeiter("   Hallo Welt  von  Python   ")
print(ergebnis)
"""
Erwartete Ausgabe

{
    "data" : "Hallo Welt von Python",
    "word_count" : 4
}
"""