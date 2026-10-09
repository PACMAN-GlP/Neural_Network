import xml.etree.ElementTree as ET
import re
import html

INPUT_FILE = "dewiki-latest-pages-articles.xml"
OUTPUT_FILE = "wikipedia.txt"

# XML-Namespace
NS = "{http://www.mediawiki.org/xml/export-0.11/}"

def clean_wikitext(text):
    if text is None:
        return ""

    # HTML-Entities dekodieren (&lt;ref&gt; → <ref>)
    text = html.unescape(text)

    # Kommentare entfernen
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)

    # Ref-Tags entfernen
    text = re.sub(r'<ref.*?>.*?</ref>', '', text, flags=re.DOTALL)
    text = re.sub(r'<ref.*?/>', '', text)

    # Überschriften == Geschichte ==
    text = re.sub(r'=+', '', text)

    # [[Link|Anzeigetext]] → Anzeigetext
    text = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]', r'\1', text)

    # Externe Links [https://... Text] → Text
    text = re.sub(r'\[https?://\S+\s+([^\]]+)\]', r'\1', text)

    # Fett/Kursiv-Markierungen entfernen
    text = text.replace("'''", "")
    text = text.replace("''", "")

    # Vorlagen {{...}} grob entfernen
    text = re.sub(r'\{\{.*?\}\}', '', text, flags=re.DOTALL)

    # Mehrere Leerzeilen zusammenfassen
    text = re.sub(r'\n\s*\n+', '\n\n', text)

    return text.strip()


with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    context = ET.iterparse(INPUT_FILE, events=("end",))

    count = 0

    for event, elem in context:
        if elem.tag == NS + "page":
            text_elem = elem.find(".//" + NS + "text")

            if text_elem is not None and text_elem.text:
                text = clean_wikitext(text_elem.text)

                if len(text) > 100:
                    out.write(text)
                    out.write("\n\n")

                count += 1

                if count % 10000 == 0:
                    print(f"{count} Artikel verarbeitet")

            # Speicher freigeben
            elem.clear()

print("Fertig!")