# Raw Source Protocols (Archive — German)

Optional-read appendix: verbatim working protocols of the practitioner-video and platform research this skill was distilled from (sources [A], [P1–P16]). Content is German-language by origin and intentionally left untranslated — consult only when tracing a rule back to its source; all actionable knowledge lives in the English reference files.

---

# Quellen-Archiv: Rohprotokolle (Academy + P1–P16)

Rohmaterial der Konsolidierung in den Task-Dateien (production-pipeline / video-prompting / platforms-models / post-audio-legal). Nur bei Quellen-Rückfragen lesen.

Quelle: higgsfield.ai/academy, Kurs „The AI Filmmaking Pipeline" (Volltext der Lektionen, Stand Aug 2026).

### Die vier Stufen und ihre Übergaben

Think (Brief mit Claude) → Setup (Projekt, Ordner, Namensvertrag `@loc_`/`@char_`/`@prop_`) → Generation (Stills) → Seedance (Motion) → Review. Eine Stufe ist erst fertig, wenn sie eine konkrete, geprüfte Übergabe liefert. Kernsätze des Kurses:

- **„A still is only a hypothesis."** Erst der Seedance-Motion-Test beweist ein Asset.
- **„Proof, not promises."** Modellbeschreibung + selbstbewusster Prompt sind Versprechen; nur Pixel sind Beweis.
- **„A defect handed over here will be multiplied in motion."** Slop im Standbild vervielfacht sich in Bewegung — deshalb Gate vor Seedance, nicht danach.
- **Review-Loop:** Immer die früheste kaputte Übergabe reparieren. Geografie schmilzt → Location fixen. Identität driftet → Character Sheet fixen. Assets sauber, Aktion falsch → Seedance-Regie ändern. Shot beantwortet die falsche Idee → Brief neu öffnen. Downstream-Symptome polieren versteckt nur die Quelle.
- **Location vor Charakter:** Der Ort ist Fundament und Testbett zugleich — nur auf sauberer Location lässt sich beurteilen, ob der Charakter hält.

### Slop-Erkennung: die vier universellen Tells

| Tell | Symptom | Folge in Motion |
|---|---|---|
| **Licht ohne Übergänge** | Flach-schwarze Löcher statt Schattenverlauf | Überträgt sich auf jeden Charakter im Frame |
| **Kaputt-aber-plausible Objekte** | Kisten, Geländer, Hardware „fast lesbar" | Wird zu Brei und multipliziert sich |
| **Lokale Logikbrüche** | Effekt nur in einem Frame-Teil (Regen kratzt eine Ecke) | Seedance-Logik bricht mit |
| **Ölige Texturen** | Seifige Oberflächen ohne Materialcharakter | Reflexionen „kriechen", Plate hält keine Kontinuität |

Regel: Sichtbarer Standbild-Defekt = Stopp. Seedance nur nutzen, um unsichere Kanten/Reflexionen/Objekte in Motion zu verifizieren. Zwei weitere Location-Killer: übergeschärfte ölige Flächen (schwimmen/schmieren bei Bewegung) und fehlender atmosphärischer Dunst (ohne Haze liest alles gleich scharf = flach = sofort als Slop erkennbar).

### Bildmodell-Auswahl (Stills-Phase; Modell-„Slop-Akzente")

| Modell | Einsatz | Typischer Slop-Akzent |
|---|---|---|
| **Soul Cinema** | Erste Wahl: Locations mit Atmosphäre, filmische Textur, menschliche Charaktere from scratch | Kompositionsvarianz (mehrere Runs nötig); schwach bei exakten Props/Text; keine Multi-Referenz-Edits |
| **GPT Image 2** | Lesbarer Text, Prop-Geometrie, Reverse-Angles, Kreaturen, präzise Add-ons | „GPT-Slop": Überschärfung, Halos, alles im Fokus, gelbstichig, Plastik-Materialien; auf Menschenhaut ungeeignet |
| **Nano Banana Pro** | Nur Edits fertiger Bilder (Umkleiden, Objekt-Tausch); nie from scratch | „Banana-Slop": Lineal-Symmetrie, flaches Licht, Stock-Foto-Leblosigkeit, 3D-Render-Anmutung; hyperbolisiert Edits; kann Gesamtbild tinten → nur maskierte Region zurückkompositieren |
| **Seedream 4.5** | Character-Sheet-Edits, wenn Haut-/Stofftextur erhalten bleiben muss | Kann Pose/Winkel verschieben oder Teil des Auftrags ignorieren |

Entscheidungsregel: Pro Pass **ein Must-Preserve-Kriterium** benennen, Output im Ziel-Crop inspizieren, das Modell wählen, das dieses Kriterium beweist — Rankings nie in die nächste Modellgeneration mitnehmen.

### Location-Regeln

1. **Geografie vor Stil:** Eingänge, bespielbare Wege, drei Tiefenebenen benennen — versteckte Geometrie ist das, was spätere Winkel neu erfinden.
2. **Ein motiviertes Licht:** eine Quelle, eine Richtung, ein Falloff. Widersprüchliche Quellen = widersprüchliche Schatten oder abgesoffene Regionen.
3. **3/4-Master, dann Reverse-Test:** 3/4 zeigt Seitengeometrie und Tiefenebenen; frontal wird zur Kulisse („Charaktere stehen davor, nie darin"). Reverse ist eigene Generierung + Kontinuitätstest: Anker, Öffnungen, Lichtseite, Materialien, Palette müssen matchen.
4. **Blocking-Anker:** Aktionen an ein fixes Objekt binden („zwischen Sofalehne und Fenster"), nie an Screen-Richtungen — die driften beim Kamerawechsel.
5. **Ein Wide reicht nur für B-Roll/Montage,** wenn kein Cut von Off-Frame-Geografie abhängt.
6. Claude darf Prompts formulieren, aber nicht still Regie führen: **Decision-Log verlangen** und gegen die Locks prüfen; verschwundene Locks wiederherstellen.

### Character-Sheet-Regeln (Seedance liest das Sheet wörtlich)

- Layout: tiefes Neutralgrau (#3a3a3c) als Plate (Weiß blutet ins Video, Schwarz frisst Detail), Spalten-Layout mit **dominantem Porträt (25–30 % der Fläche)** — daraus liest Seedance das Gesicht.
- Porträt leicht angewinkelt (nie dead-on) oder zusätzliches ¾-Porträt; **Iris nie schwarz**, immer Catchlight („no catchlight = dead eyes").
- **Symmetrie brechen:** perfekt gespiegelte Gesichter lesen sich als KI und werden von Seedance so weitergetragen.
- **Kopf auf Ganzkörper-Panels abschneiden** — sonst konkurrieren zwei Gesichter und die Identität driftet; Seedance soll gezwungen sein, das Gesicht nur aus dem Porträt-Panel zu nehmen.
- **Kein 3D-Game-Look:** Seedance erkennt die Game-Anmutung und animiert entsprechend „wie Spielgrafik".
- **Edits maskiert aufs Original kompositieren, nie das ganze Sheet neu generieren** — gestapelte Re-Generierungen schichten Grime und konkurrierende Identitäten ein.

### Seedance-Motion-Test: Diagnose-Protokoll

- Baseline sauber halten: Charakter auf einer Location testen, die Geometrie/Tiefe/Licht bereits beweisbar hält — kaputte Plate gibt jedem Charakterfehler eine zweite plausible Ursache.
- **Eine Variable pro Rerun ändern.** Defekt existiert in der Quelle oder bleibt bei Richtungswechsel am selben Feature → Quell-Asset schuld. Quelle sauber, Defekt ändert sich mit der Motion-Klausel → Regie schuld. Weder noch → Test enger fassen.
- Diagnose gilt für dieses Asset + diese Regie — keine Universalaussage übers Modell; ein gelungener Rerun garantiert nicht den nächsten.

**Konsequenz fürs Treatment:** Assets (Locations, Figuren, Props) sind eigene Produktionsposten mit eigenem Abnahme-Gate — als „Set-Build"- und „Casting"-Phase vor dem ersten Shot einplanen; pro Location Reverse-Tauglichkeit klären (oder bewusst als B-Roll-only deklarieren).

Quelle: higgsfield.ai/academy, Kurs „The AI Filmmaking Pipeline" (Hell-Grind-Team), Lektionen „The pipeline, end to end", „Choosing your image model", „Generating locations", „Generating characters", „Test in Seedance", „Spot the slop".


---

## Praxis-Protokoll: Kompletter Kurzfilm-Workflow (Adil, „Ultra Realistic AI Short Film Using Seedance 2.0 in 4K", Volltranskript)

Quelle: YouTube 0HIRIT7px9Y, vollständiges Transkript. Ein 2-Minuten-Drama, komplett mit Higgsfield Cinema Studio + Claude (Fable 5) + Seedance 2.0 4K produziert. Ergänzt die Academy-Lektionen um erprobte Detail-Regeln:

### Skript & Struktur
- Skript-Auftrag an Claude: konkrete Prämisse + Figuren-Backstory + Ende, **jeder Shot max. 15 Sekunden** — denn **eine Seedance-Generation = ein 15-s-Take**. Das Skript kommt als Shot-by-Shot-Breakdown zurück.
- Klassische Struktur explizit anfordern: Setup → Rising Action → Climax → Resolution.
- Eine 15-s-Generation kann **2–3 interne Shots mit echten Kamerawinkel-Wechseln** enthalten (im Prompt als Shot 1/2/3 beschrieben). Wenn eine Szene gehetzt wirkt: in zwei Generationen splitten. Große Finalszenen: vollen Prompt schreiben lassen, dann in 8A/8B/8C-Teilszenen splitten.
- Nach einem Flashback nie direkt in Dialog schneiden — 1–2 s Verarbeitungspause für die Figur einbauen.

### Character Sheets & Assets (ergänzend zu oben)
- Sheet-Layout aus der Praxis: Graue Fläche, **Front, Rücken, separates Close-up-Headshot**.
- Abnahmekriterium Licht: weich, **keine harten Schatten im Gesicht, kein Glanz im Haar** — Sheets mit abgesoffener Gesichtshälfte oder Glare verwerfen. Das hochwertige Charakterbild ist „the main secret" der Filmqualität.
- Soul Cinema für Sheets: liefert pro Run eine andere Person für <0,5 Credit → mehrere Runs, beste wählen, locken.
- Element speichern (benannt) → Claude referenziert den Namen im Prompt → Higgsfield zieht das Asset automatisch.
- **Sheet lockt auch die Stimme:** Seedance generiert pro Charakter-Sheet eine passende, konsistente Stimme. Visuals locken = Voice locken.
- Prop-Edits & Kombinationen mit GPT Image 2: Trikotnummer/Logo ändern („change the logo and swap the number 7 to 23"); Kit + Charakter-Sheet hochladen → „create a character in this uniform". Wiederkehrende Props (Ball) brauchen ein eigenes Prop-Sheet auf Grau.
- Kind-/Alters-Variante einer Figur: bestehendes Sheet anhängen, Umwandlung prompten (z. B. 7-Jähriger, Name auf dem Shirt).
- **Einmal-Figuren brauchen kein Sheet:** Wer nur in einem einzigen Prompt auftaucht (Zuschauer, Passant), kann direkt aus dem Prompt kommen.

### Location & Stimmung
- Mood im Location-Prompt steuern: warme/kalte Töne, Wetter, Tageszeit. Flashbacks per Palette differenzieren (kalte Erinnerung vs. warmes Golden-Hour-„old film"-Flair).
- „3/4 angle" wörtlich in den Location-Prompt schreiben → Volumen, Tiefe, Objektabstände.

### Seedance-Regie (Video-Prompts)
- **Keine Negativ-Prompts.** Seedance versteht sie nicht und macht eher das Gegenteil („he's not crying" → Verwirrung). Immer das Gewünschte positiv formulieren („an anxious look").
- **Positions-Lock:** Video mit Wide-Establishing-Shot beginnen → Seedance platziert alle Figuren korrekt und hält die Positionen für die gesamte Generation. Fixt Sitzposition-Drift zwischen Szenen.
- Wenn alle 4 Takes eines Batches falsch sind → Fehler liegt im Prompt: konkretere Bewegungen und Emotionen beschreiben.
- Handheld-Movement prompten (Operator-Atmung/Gehen) für Realismus; optische Flares + Fog als Stimmungsträger.
- Match Cut zwischen Szenen: letzten Frame der Vorszene anhängen → Folgeszene startet aus identischer Position.
- **Whip Pan:** Dauer angeben + Subjekte als A/B/C labeln; muss auf demselben Shot-Typ enden, auf dem er startet (Medium→Medium) — Medium→Close-up bricht.
- **Speed Ramp** promptbar: Slow-mo im entscheidenden Moment, Snap-back beim Impact.
- Dutch Angle für Spannung; Figur fast ohne Abstand zur Framekante = Gefühl von Gefangensein.
- Voice-Direction gehört in den Prompt: Ton, Mikropausen, „trembling voice", Emotion.
- **Voiceover-Trick:** Für reine Sprachzeilen einen separaten Wegwerf-Shot generieren (Figur spricht im vertrauten Setting), nur die Audiospur verwenden und über die Zielszene legen.

### Auswahl & Schnitt
- Pro Generation die besten Teil-Shots ernten und über Generationen hinweg kombinieren; brauchbare Takes als Backup behalten.
- Ausschusskriterien aus der Praxis: spontan auftauchende Objekte (dritter Stuhl), Location-Wechsel mitten im Take, falsche Proportionen, Figuren zu dicht beieinander, wanderndes Eye-Tracking, Text-Gekritzel im Bild (Notizbuch) → Shot neu generieren.
- Emotions-Kontinuität über Szenen prüfen: Wer in Szene 4 weint, darf in Szene 5 nicht grundlos lächeln — Kontext an Claude zurückgeben und Prompt anpassen.

---

## Praxis-Protokoll 2: AI-Commercial-Workflow (Adil, „AI Commercial", Volltranskript)

Quelle: YouTube 3rDs6FhFoUQ, vollständiges Transkript. Ein Werbespot (Kopfhörer) mit Cinema Studio + GPT Image 2.0 + Soul Cinema + Seedance 2.0. Drei Stufen: Assets → Shotlist (Claude-Skill) → Szenengenerierung. Neue Regeln gegenüber Protokoll 1:

### Assets bauen UND testen (Stage 1)
- **Produkt-Sheet:** Eigenes Produktfoto in GPT Image 2.0 → „product sheet with front and 3/4 perspective views". Ein einziges Bild reicht nicht — ohne Rundum-Ansicht halluziniert das Modell das Produkt mitten in der Szene.
- **Sheet-Layout-Variante:** Zwei Panels — Close-up + Ganzkörper (Front/Rücken) auf Grau. Grau ist Pflicht: ohne Hintergrund-Clutter ist die Win-Rate messbar höher.
- **Stills nie trauen — Kandidaten in Motion testen:** 2+ Charakter-Kandidaten behalten; ein Gesicht, das als Still trägt, kann in Bewegung zerfallen. Test: identischer Simpel-Prompt, **nur eine Variable pro Run tauschen** (Held A/B × Location A/B), Sieger locken. Gilt auch für Locations. Kostet vorab wenig, spart später massenhaft Credits.
- **Soul Cinema:** 8 Bilder = 1 Credit → viele Batches, scrollen bis ein Gesicht „stoppt".
- **AI Cast für Nebenfiguren:** Instant-Sheets mit Styling-Optionen aus einem Prompt. Nebenfiguren bekommen nicht die Held-Sorgfalt.
- **Location-Edits per GPT Image 2.0:** gezielt umbauen („clear the island, add a gas stove left, remove the TV, put a door there, keep everything else") statt neu generieren.
- **Gesicht-Löschen-Trick:** Mehrere Gesichter in einem Sheet → Videomodell weiß nicht, welches es greifen soll → Drift. Fix: „erase the face from the full body panel" (GPT Image 2.0) → genau ein Gesicht zum Locken. (Alternative zur Academy-Regel „Kopf abschneiden" — gleiches Prinzip.)
- **Qualitätsverlust bei Edits maskieren:** Jeder GPT-Image-Edit weicht das Bild auf → Plastik-Slop. Fix: Original (Soul, scharf) als obere Ebene, Edit darunter, im Bildeditor nur das Outfit ausmaskieren — Gesicht/Haut/Hintergrund bleiben vom Original.
- **Outfit-Findung:** Claude um 10 Outfit-Prompts bitten, alle in GPT Image 2.0 rennen, Teile kombinieren („shirt from look 2 in pink + jeans from look 1").
- **Zustands-Doppel-Sheets:** Ändert sich der Charakterzustand (trocken → verschwitzt), zweites Sheet bauen statt den Wandel zu prompten — Seedance improvisiert sonst und „das Gesicht tropft weg". Regel: „Images are cheap, videos aren't." Claude sagen, welches Sheet in welchem Cut gilt.
- **Wiederkehrende Props** (auch Kleinzeug wie Tasse/Mokkakanne) als Referenz-Elemente locken — in Close-ups fällt Prop-Drift zuerst auf. Props brauchen keine Motion-Tests.
- Organisation: Canvas als Workspace — Kandidaten nebeneinander, Sieger nach oben, gelockt. Element-Namen in Claude und Higgsfield identisch halten (Auto-Attach).

### Shotlist als verbundenes Dokument (Stage 2)
- Claude bekommt drei Dinge: fertiges Skript, **alle gelockten Assets als Bilder hochgeladen** (nicht beschrieben!), jedes benannt.
- Output ist **ein Dokument, keine Einzelprompts**: oben ein **Style-Prefix** (Licht, Kamera, Farbe) — an jeden Prompt „geklebt", eine Änderung wirkt überall. Jeder Prompt hat einen Namen (1A, 1B, 2A …) → „edit prompt 1A" ändert exakt einen.
- **Per-Szene-Override:** Prefix ist Default; braucht eine Szene eigenes Licht (Stadion: harte Mittagssonne), nur für diese Szene overriden.
- Schlechte Momente aus einem Prompt herauslösen und als Zwischen-Prompt (1B) eigenständig bauen, statt einen Prompt zu überladen.

### Szenengenerierung (Stage 3)
- **Layout-Map-Trick (wichtigster Hack):** Wenn Text die Geografie nicht pinnt (Figur läuft jede Generation woanders hin, Objekt springt in Größe/Position): in GPT Image 2.0 ein **Schematic** bauen — Positionen markieren, Größen relativ definieren („two times a person's height, on the same line") — und als Input an den Prompt hängen. Ersetzt 20 Lotterie-Generationen. Schematic in späteren Szenen wiederverwenden.
- **Objekt-Anker zusätzlich im Text** („hero stands under the tree on the left") und hartes Prop-Locking pro Cut („lock the backpack on both shoulders in every single cut") gegen inkonsistente Batches.
- **Choreografie ausschreiben, nie „he dances":** Generische Bewegungsbegriffe bedeuten Seedance nichts → mushy Flailing. Move für Move benennen: „two head nods, shoulder roll one at a time, knee dip, finger snap, quarter spin at the door". Gilt für jede komplexe Bewegung, pro Cut.
- **Musik-Track als Input mitgeben** („add the music track as an input, have him dance in time with its beat") → Bewegungen landen auf dem Beat.
- **Match Cut über Szenengrenzen:** Öffnenden Cut explizit an den schließenden der Vorszene binden („match the opening tap to the closing tap of 1C — same hand, same motion").
- Unmögliche Rig-Shots sind promptbar: Snorricam/Body-Rig („camera bolted to his body, ear cup dead center, background ripping past in motion blur").
- Diagnose-Reihenfolge bei kaputten Takes: erst Licht (Prefix), dann Kamera (statisch?), dann Überladung (Moment in eigenen Prompt auslagern).
- **Iterations-Philosophie:** Einen Prompt 3× verfeinern schlägt drei parallele Prompts. Endprodukt = die besten Sekunden aus ~100 Versuchen; pro Take „Keeper-Phasen" ernten und on action schneiden. „Iteration is the skill."

---

## Praxis-Protokoll 3: Seedance 2.5 vs. 2.0 (Adil, Sechs-Kategorien-Vergleich, Volltranskript)

Quelle: YouTube jvkdHdeWICM, vollständiges Transkript. Identische Prompts auf beiden Modellen in sechs Kategorien. Seedance 2.5 kommt „soon" zu Higgsfield.

### Die zwei harten Eckdaten
- **Seedance 2.5: bis 30 s pro Generation** (2.0: 15 s) — ein 2-Minuten-Musikvideo in vier Generationen. Alle 2.5-Beispiele: ein Prompt, eine Generation, kein Editing/Comping/Post.
- **Der Haken: 2.5 rendert nur 720p** (2.0: natives 4K). Auf dem Phone kaum sichtbar; auf TV oder im Wide werden Gesichter weich/verschmiert.

### Modellwahl pro Shot (abgeleitete Regel)
| Shot-Typ | Modell |
|---|---|
| Komplexe kontinuierliche Kamera (Whip Pan→Push-in→Low-Angle-Orbit in einem Take, Vertigo/Dolly-Zoom) | 2.5 — 2.0 konnte Vertigo nie |
| Choreografie, schnelle Moves, Zwei-Personen-Sync | 2.5 (Gewicht, kein Limb-Clipping) |
| Transformationen/VFX in-shot | 2.5 (Anatomie hält, Trümmer/Embers mit Objektpermanenz; 2.0 teleportiert zwischen Formen, Hintergrund flackert, Gegner werden frame-zu-frame „gelöscht") |
| Drama-Szenen mit Peak am Ende | 2.5 — bei 2.0 läuft die 15-s-Uhr exakt am dramatischen Höhepunkt ab |
| 4K-Deliverable, Hero-Close-ups, TV/Kino-Auswertung | 2.0 (oder 2.5 + Upscale-Pfad testen) |
| UGC | Beide; 2.0 bleibt solide (Heimatdisziplin), 2.5 versteht die Kamera als physisches Phone (abgelegt auf Fels: Handheld-Wobble davor, Locked-off danach; Pan bewegt sich „wie ein Handgelenk, nicht wie ein Kran") |

### Neue diagnostische Tells (modellunabhängig nützlich)
- **Quick-Cut-Verstecken:** Hektische Schnitte mit neuem Winkel jede Sekunde = das Modell kaschiert, dass es die Bewegung darunter nicht animieren kann. Schneidet ein Take genau dann weg, wenn die Motion schwer wird → Take verwerfen, nicht feiern.
- 2.0-Failure-Katalog bei schneller Bewegung: Gliedmaßen clippen durcheinander, Haltung „resettet" zwischen Sets auf eine Standardpose, Schimmer-Makeup wird bei Kopfdrehung zu Brei, Fisheye ist nur Kantenfilter statt echter Linsenphysik.
- Schrei-Test für Gesichter: Schreien zwingt das ganze Gesicht zum Commitment (Kiefer, Halsspannung) — klassische Bruchstelle; 2.5 besteht ihn.
- Reflexionen (Tänzerinnen im Glossy Floor) waren ein Dead Giveaway — bei 2.5 korrekt. Bei 2.0 weiterhin als Risiko behandeln.
- Licht-Rhythmus als Qualitätsmerkmal: Kerzenflackern, das über alle Winkel synchron bleibt (2.5), vs. flaches Licht, das den Plastik-Look erzeugt (2.0-Beispiel).

### Konsequenzen für Skript/Shotlist
- Generationseinheit ist modellabhängig: **2.0 = 15-s-Takes, 2.5 = 30-s-Takes.** Shot-Planung (interne Shots pro Take, Pacing, wo der Peak liegt) ans Zielmodell anpassen — Drama-Peaks nie ans Ende eines 15-s-2.0-Takes legen.
- 2.5 erlaubt In-Shot-Transformationen als „einen Satz im Prompt" — was bisher zwingend per Ellipse/Schnitt gelöst wurde (siehe Rote Liste), wird mit 2.5 pro Fall testbar. Ellipse bleibt der sichere Default.
- Musikvideo-Konsistenz (gleiche Gesichter/Outfits über mehrere Sets, Cuts auf den Beat) ist mit 2.5 in einer Generation machbar — mit 2.0 weiterhin Set-für-Set + manueller Schnitt.

---

## Praxis-Protokoll 4: Seedance 2.0 in 4K (Adil, „Is 4K Worth It", Volltranskript)

Quelle: YouTube bY8RDKoBwU0, vollständiges Transkript. Werbenaher Test (Higgsfield-affiliiert, Showcase-Charakter) — Aussagen als Tendenz werten, nicht als verifizierte Grenzen. Kernthese: **die Auflösungsstufe selbst ist ein Anti-Slop-Faktor.**

### 4K als Anti-Slop-Hebel
- In 720p/1080p morphen Wide Shots mit vielen bewegten Teilen oder erstarren; in 4K hält dieselbe Komposition. Detailsprung auf allen Ebenen (Haut, Wasser, Hintergründe).
- **Crowds:** „Armee aus Tausenden" in Ultra-Wide 21:9 hält in 4K — Hintergrundfiguren zerlaufen nicht mehr zu Pixelbrei. Per Text-to-Video generiert. ⚠️ Widerspricht der Roten Liste (Crowds meiden) — Einstufung: in Seedance-4K pro Fall testbar, bei niedrigeren Auflösungen und anderen Modellen bleibt die Rote Liste gültig.
- **Bildtext:** 4K rendert Text „way sharper" — Ad-Beispiele mit gezielten Text-Inputs funktionierten; im Gaming-Test blieben HUD/Health-Bars/Quest-Text scharf (Image-to-Video). ⚠️ Gleiche Einordnung: Rote-Liste-Regel „kein Bildtext" wird für Seedance-4K zur Gelb-Regel (testen, Text-Referenz als Input mitgeben), nicht aufgehoben — Protokoll 1 dokumentiert Text-Gekritzel als realen 4K-Ausschussgrund (Notizbuch-Szene).
- Weniger Rerolls nötig → Credit-Ersparnis trotz teurerer Generationen.

### VFX auf Realfootage
- Workflow: echtes Video (auch simpler Screen-/Handyclip) in Seedance droppen + Effekt prompten → Cyber-Effekt, Reptilienhand, komplettes Weg-Radieren der Hand. **Kein Greenscreen** — Masking passiert automatisch im Shot.
- 4K-spezifisch: Effekte werden addiert, ohne Details/Objekte des Originals zu verändern — in 1080p veränderte VFX regelmäßig Kleindetails und machte Shots unbrauchbar.
- Konsequenz: Hybrid-Produktionen (Realdreh + generierte VFX) sind ein planbarer Produktionspfad, nicht nur Vollgenerierung.

### Stile & Technik
- Cartoon/2D: hohe Farbqualität, kinotauglich; Kamera/Dynamik entsteht ohne Per-Scene-Kamera-Prompting.
- CGI/3D: schnelle Kamerafahrten durch Partikelmassen halten; Physik-/Gewichtssimulation spürbar (Monster-Roar mit Masse) — das übliche „Floaty"-Problem entfällt weitgehend.
- **10-bit-Farbe:** Seedance gibt 10 bit aus (>1 Mrd. Farben) → kein Banding in Smoke/Verläufen. In Higgsfield Bitrate auf „high" stellen, sonst verschenkt.
- High-Speed + Tiefe (Kamerajagd mit greifenden Händen): 4K-Modell versteht 3D-Raum — für solche Shots ist 4K „Necessity, nicht Option".

### Bildmodell-Pairing mit Seedance 4K (bestätigt/ergänzt Protokoll-Regeln)
- Soul Cinema: Charaktere, Locations, Keyframes (8 Bilder/1 Credit, cinematischer Default-Look).
- GPT Image 2: Text, Motion-Vorgaben, **Storyboards**.

---

## Praxis-Protokoll 5: Action-Kurzfilm über vier Settings (Adil, „Action Short Film in Seedance 4K", Volltranskript)

Quelle: YouTube CHHH8tNioSc, vollständiges Transkript. Piratenschiff → Wüste → Dschungel → Wohnzimmer; ~400 Generationen über 2 Wochen. Neue Regeln gegenüber Protokoll 1–4:

### Skript-Entwicklung
- Nie „write me a script" — **Idee von Claude expandieren lassen**: Claude fragt zurück (Laufzeit? Settings? Plot-Twist-Vorschläge?), Skript entsteht im Dialog Schritt für Schritt. „Nothing good comes out of one lazy request."

### Assets
- **Reale Person als Held:** Eigene Referenzfotos (Front + linkes/rechtes Profil) → GPT Image 2.0 baut daraus das fotoreale Charakter-Sheet (Kostüm, Grime, Kratzer). GPT Image 2 ist erste Wahl für Sheets, **wenn bereits eine Referenz existiert**; Soul Cinema, wenn from scratch.
- Ein-Gesicht-Regel drastisch bestätigt: Mehrere Gesichter im Sheet → Drift kumuliert, „by scene five, our hero is a stranger."
- **Ordnerdisziplin:** Pro Szene ein Ordner mit Unterordnern pro Asset — bei 400 Generationen überlebenswichtig.
- Location-Abnahme konkret: Lichtquellen müssen der Prompt-Intention entsprechen (eine Laterne + Tageslichtstrahlen — nicht plötzlich zwei Lampen), Schlüsselobjekt (Karte) zentral und lesbar. Kleindetails wie Lichtstrahlen sind das, was Generationen „real" macht.
- Prop-Routine: **Soul Cinema = Raw-Pass** (Varianten, Front/Back/¾), **GPT Image 2.0 = Edits + finales Clean Sheet** (Segel öffnen, schwarz färben, Logo drauf).
- **Sub-Locations als eigene Assets:** Braucht die Story einen Ort im Ort (Oase in der Wüste), eigenes Location-Asset generieren — sonst sieht er in jeder Generation anders aus.
- **Asset-Tausch mitten in der Produktion ist normal:** Wirken Elemente cartoonish/plastisch (Mandrills mit Leuchtnasen), gegen simplere, realistischere Variante tauschen (weiße Makaken). Asset-Varianten vorhalten.
- Zustandswechsel-Sheets erneut bestätigt (zerrissene Hose als zweites Sheet nach dem Jaguar-Riss — sonst „reparieren" sich die Hosen magisch); Objektpermanenz zusätzlich im Prompt festschreiben („device stays in his hands as he falls", „jaguar stays on top of the cliff").

### Szenengenerierung
- Standard-Setup: 21:9, 4K, 15 s, **4 Batches pro Prompt** — beste Teile über Batches mischen.
- Iterationsschleife: Run → präzise benennen, was falsch ist (Tisch-Clutter, Pacing, Tageszeit hinter der Tür, fehlende Reaktion) → exakte Änderungen an Claude → erneut. **Reaktions-Beats machen Shots real** (Karte auf den Tisch knallen, zur Tür bewegen, sobald die Nachricht kommt).
- Interne Shots löschbar: stört ein Shot den Fluss, Claude sagen „delete shot 3".
- **Zeichnung als Geometrie-Input:** Wo Worte die Geometrie nicht pinnen (Kanonenkugel-Einschlag, Positionen), eine simple Skizze mitgeben — „one drawing tells the model what 10 sentences can't." (Erweitert den Layout-Map-Trick auf Handzeichnungen.)
- **POV-Shots:** Multi-Shot-POV scheitert (Modell schob die Spinne „ins Auge") → auf **einen kontinuierlichen POV-Shot** reduzieren; Augen öffnen „like shutters"; Schreckobjekt seitlich statt mittig — wirkt natürlicher.
- Chase-Staging explizit: Laufrichtung festschreiben („always run toward the oasis"), Verfolger-Distanz definieren (sonst kleben sie am Helden und es gibt keinen Raum für die Jagd), „almost makes it" als dramaturgische Regel.
- Setting-Übergänge in den Prompt schreiben (Sprung ins Meer → Wüste; Klippensturz → Aufprall aufs Sofa) für Match-Transitions zwischen Welten.

### Dialogszenen (wichtigster Block dieses Protokolls)
- **Reverse-Angle-Environment-Referenzen sind Pflicht:** Für Schuss/Gegenschuss beide Raumseiten als Bilder generieren und dem Modell mitgeben — erst mit diesem „Blueprint" hört der Hintergrund auf, zwischen Cuts zu springen.
- Prop-Locks in Dialogszenen: exakte Objektgröße festschreiben (Device schrumpfte/wuchs), Positionen fixieren (Papagei AUF dem Käfig, nicht darin).
- **180°-Regel im Prompt erzwingen:** Kamera komplett statisch, Figur A immer aus demselben Winkel bei ihren Lines, Cut auf Figur B über As linker Schulter bei seinen. Achsenbrüche zerstören die Raumlogik. Auch dann mehrere Batches nötig — Kamera-Lock gelingt nicht immer.
- Stimm-Regie pro Line justierbar („annoyed disbelieving tone" statt Schrei).

---

## Praxis-Protokoll 6: 1-Minuten-4K-Film, Meta-Story „TV im TV" (Adil, Volltranskript) — nur Deltas

Quelle: YouTube HSON-SoFz7s. Bestätigt weitgehend Protokoll 1–5; hier nur Neues:

- **Prop-Sheets brauchen Tiefe:** Flache Frontansichten ohne Schatten/Highlights animiert Seedance wie 2D-Objekte. Abnahmekriterium: sichtbares Volumen, Kantenverjüngung, Studio-Reflexionen. Praxisfall: GPT Image 2 lieferte nur flache Remote-Sheets, **Nano Banana Pro löste es mit demselben Prompt** — ⚠️ widerspricht der Academy-Regel „Banana nie from scratch"; für Props gilt: kein Modell ist überall bestes, bei Fehlschlag Modell wechseln statt nur Prompt tweaken.
- **Video-als-Input (Screen-in-Screen):** Generierten Clip (z. B. erste 6 s) als Video-Referenz anhängen und prompten, dass er auf dem TV im Shot läuft — VFX-frei. **Generationsdauer exakt auf die Referenzlänge setzen**, sonst erfindet Seedance Inhalte. TV-Größe im Prompt locken, Screen-Glare für Realismus ergänzen.
- **Bildschirminhalte nie freilassen:** Frei generierte TV-Kanäle produzieren Text-/Kanal-Slop. Exakt festschreiben, was läuft; letzter Kanal = Eröffnungsbild der Folgeszene (Location als Asset anhängen) → schnittfreie Transition.
- **Roter-Pfeil-Trick:** Interagiert die Figur wiederholt mit dem falschen Detail (falsche Taste in jedem Take), Pfeil direkt aufs Prop-Sheet zeichnen, der das richtige Element markiert — löste das Problem sofort. (Asset-Annotation als dritte Geometrie-Input-Form neben Layout-Map und Skizze.)
- **Klon-Armeen vermeiden:** Ein Einzel-Charakter-Sheet für eine Menge → identische Klone. Fix: Multi-Varianten-Sheet (mehrere unterschiedliche Figuren in einem Sheet) laden → diverse Crowd.
- **Location-Asset optional bei Einmal-Nutzung:** Für simple Settings, die nur in einem Video vorkommen, reicht die Prompt-Beschreibung — Seedance 4K baut sie selbst. Assets nur für Wiederkehrendes.
- Referenzbilder in höchster Qualität generieren (GPT Image 2 auf 4K): Input-Schärfe vererbt sich ins Video.
- VO-Workflow: Video hochladen → analysieren lassen → Doku-Voiceover im Stil schreiben + Stimme wählen (Higgsfield-Feature) → Audio überlagern.

---

## Praxis-Protokoll 7: Animation mit Seedance 2.0 (unabhängiger Reviewer, ArtList-gesponsert, Volltranskript) — nur Deltas

Quelle: YouTube aAGZM2aoq1Q. Erste Nicht-Adil-Quelle; testet 2D-Zeichentrick, Pixar-3D, Anime, Comic. Ton kritischer als die Higgsfield-Showcases.

- **Stil-Adjektive entscheiden:** T2V-Prompt „3D animation" driftet Richtung Realismus („alle AI-Videos sind technisch 3D-Animation"). Erst „whimsical Pixar-style 3D animation" liefert echten Stilisierungs-Look. Stilbegriffe präzise und redundant setzen.
- Anime ist eine Seedance-Stärke: Speed Lines, Anime-Motion-Blur, Action-Kamera werden verstanden; High-Action-Anime = Sweet Spot.
- Comic-Stil ab Startframe: Stiltreue ~10/10 (Speed Lines, Textur, SFX-Sticker), **Logik ~3/10** — wer wen jagt, bleibt unklar; überladener Prompt verschlechtert. Abhilfe laut Reviewer: Shot-for-Shot-Prompting (deckt sich mit unserer Shot-first-Doktrin).
- ⚠️ **Emotions-Schwäche als Modell-Eigenschaft:** Reviewer findet konsistent, dass Seedance 2.0 bei komplexen Emotionen/Charakter-Animation steif und flach wird (Pixar-Romantik-Szene „lacks life") — und Nach-Tweaken dort teuer ist, weil die Schwäche inhärent ist. Spannung zu Protokoll 1/5 (Drama-Acting gelang): Auflösung vermutlich — Emotionen tragen bei fotorealen Figuren mit starken Sheets + expliziter Acting-/Voice-Regie, brechen bei stilisierten Figuren und T2V ohne Referenz. Für emotionale Beats in Animation: mehr Batches einplanen oder auf Reaktions-Schnitte ausweichen.
- Ungefragte Genre-Injektionen möglich (Abenteurer bekam Zelda-artige Elfenohren) — Stilreferenzen locken das ab.
- **Scene Extension:** Seedance akzeptiert Video-Referenzen und generiert Fortsetzungen. Limit: 15-s-Clips werden als Extension-Input abgelehnt — **Input muss <15 s sein** (14 s funktionierte; notfalls im Editor kürzen). Extension hielt Stil und Details konsistent. Reviewer-Empfehlung für Langform: Anime-Stil + konsistente Charaktere + Scene Extension.
- Konsistenz-Nebenbefund: identischer Prompt, zweite Generation = anderes Action-Blocking, aber Detailtreue teils besser (Skelette behielten blaue Flammen) — Re-Roll ist auch ein Qualitätshebel, nicht nur Fehlerkorrektur.
- Stylized Startframes: Nano Banana Pro/2 erneut erfolgreich from scratch für Grafisches — stützt die Protokoll-6-Ausnahme (Banana für Nicht-Fotoreales/Props tauglich).

---

## Praxis-Protokoll 8: VFX auf Realfootage in drei Stufen (Adil, Volltranskript) — nur Deltas

Quelle: YouTube Yte-UGhYkPQ. Vertieft den Hybrid-Pfad aus Protokoll 4 (Realdreh + Seedance-VFX, kein Greenscreen/Masking). Neu:

- **Keep-List als Prompt-Architektur:** Der VFX-Prompt besteht aus drei Teilen — (1) explizite Lock-Liste alles Unveränderlichen (Gesicht, Gang, Ringe, Gesten, exakter Handheld-Move; bei Fahraufnahmen auch Auto, Gurt, Rig-Framing, Fahrbewegung), (2) die EINE gewünschte Änderung, (3) der exakte Zeitpunkt/Trigger. Je bewegter die Kamera, desto länger muss die Keep-List sein.
- **Trigger an Aktion oder Dialog binden:** „right when he snaps his fingers", „right when I say the line …" — Mid-Clip-Effekte an sichtbare/hörbare Momente koppeln.
- Claude liest angehängte Videos als Frame-Serie → versteht Shot-Inhalt, Licht und Kamerabewegung als Kontext für den Prompt.
- **Relighting ist automatisch:** Seedance zieht Licht aus der generierten Umgebung und wirft es auf die reale Person (Neon auf Auto, Lava unters Kinn, Feuerschein auf Shirt) — kein Grading nötig; das ist der Realismus-Verkäufer.
- **Virtuelle Kamerabewegung auf Realfootage:** Kamerafahrten prompten, die nie gefilmt wurden (Zoom-out-Reveal: erst tight auf den Effekt, dann Pullback auf die Person, Lip-Sync erhalten).
- **Mit Absicht drehen:** Raw-Clips schon mit dem geplanten Effekt im Kopf filmen (Monkey-Bars → kollabierender Tempel; Treppe → Kraken-Sturm). Die Bewegung im Realmaterial muss zur späteren Fiktion passen.
- Kreaturen-Referenz statt Beschreibung: Gewünschtes Wesen vorab als Bild bauen (GPT Image 2.0) und anhängen — „show, don't describe", sobald die Vorstellung konkret ist.
- Physik-Ergänzungen kommen ungefragt und korrekt (Wind im Haar auf Bergflug, obwohl im Original windstill) — als Realismus-Bonus einkalkulieren.
- Handheld ist die Königsdisziplin (Parallaxe/Shake müssen getrackt werden) und funktioniert; Locked-off/Steady ist der einfache Einstieg für Welt-Swaps.
- Wardrobe-Swap auf Realfootage promptbar; mehrere Welt-Varianten in einem Auftrag anforderbar.

---

## Praxis-Protokoll 9: Seedance 2.5 vs. 2.0 vs. MiniMax H3, 30-Video-Vergleich (unabhängiger Reviewer, plattform-gesponsert, Volltranskript) — nur Deltas

Quelle: YouTube ViKIlLMn99A. Zweite unabhängige Quelle; nüchternes Fazit als Korrektiv zu Protokoll 3.

- **2.5 vs. 2.0 relativiert:** „In many cases very very much the same." Echte 2.5-Vorteile: Länge (30 s) + mehr Inputs. Mehrfach gewann 2.0 im Direktvergleich (Commercial-Ending, Cartoon-Ending, Face-Rendering aus Einzelbild). Protokoll-3-Begeisterung ist damit auf „situativ besser" herunterzustufen — pro Shot testen, nicht pauschal 2.5 wählen.
- **Preisrelation:** 2.5 kostet doppelt (15 s / 720p = 300 Credits vs. 150 bei 2.0 inkl. besserer Auflösung). MiniMax H3: 120 Credits, bis 2K.
- **Wasserglas-Test bleibt verloren:** Weder 2.5 noch 2.0 füllen ein Weinglas randvoll — die klassische Physik-Grenze besteht fort (beide stoppen beim „üblichen" Füllstand). MiniMax H3 bestand den Test. Merksatz: Flüssigkeits-Zielzustände, die vom Trainings-Normal abweichen, bleiben rote Liste — modellübergreifend testpflichtig.
- **MiniMax H3 als dritte Option:** Großer Sprung; macht Celebrity-/TV-Likenesses ohne Moderationsblock (rechtlich heikel, Bestand unklar); Schwächen: plastisch/cartoonish bei Realismus-Anspruch, Audio-Loops (repetitives Schreien), schwache Kampfszenen, verweigerte Edits.
- **Video-Edit auf generierten Clips** (Modell-Feature „edit video"): Elemente entfernen/hinzufügen (Stuhl weg, Langhaar+Bart, Katze dazu) funktioniert — aber **Element-Verlust-Risiko**: 2.5 löschte ungefragt eine zweite Person; 2.0 behielt alles, dafür Audio-Verzerrungen. Nach jedem Edit alle Keep-Elemente einzeln verifizieren (deckt sich mit der Keep-List-Doktrin aus Protokoll 8).
- **Audio-to-Video:** Song als Input + „lip sync perfectly" → Lip-Sync exzellent (2.5 und 2.0). Instrumenten-Hände nur approximativ: Akkorde grob plausibel, Fingerpicking wird zu Strumming — Musiker-Nahaufnahmen auf Griffhände bleiben Gelb.
- Platzierungs-Anweisungen („place me in this chair") werden nicht zuverlässig befolgt — Re-Roll einplanen statt Prompt aufblähen.

---

## Praxis-Protokoll 10: Storyboard-to-Sequence-Workflow (Jack, VFX-Veteran, Higgsfield-affiliiert, Volltranskript) — nur Deltas

Quelle: YouTube Is4wgEpPMJQ. Alternativer Produktionspfad: **ein Multi-Panel-Storyboard-Bild als Input → Seedance 2.0 generiert die ganze Sequenz.**

- **Workflow:** Character-Sheets (optional, aber mehr Kontrolle/weniger Rerolls) → Storyboard in GPT Image 2 (Sheet als Bildreferenz, 4K — Input-Fidelity vererbt sich, 16:9, Batch 2 zum Vergleichen) → Seedance 2.0 mit Storyboard (+optional Sheet) und Minimal-Prompt: „use the reference storyboards to make a full animation movie."
- **Seedance liest Panel-Annotationen:** Im Storyboard eingebetteter Text wird extrahiert und als Regie verstanden — die Detailarbeit steckt im Board, nicht im Video-Prompt.
- **Nicht frame-genau:** Seedance nutzt Panels als Inspiration und trifft die wichtigsten Story-Beats; der Stil überträgt sich stark, die exakte Shot-Abfolge nicht. Trade-off explizit: Speed/Einfachheit vs. Präzision. Hybrid-Empfehlung: Storyboard-Pfad als Basis, ultra-spezifische Shots einzeln nachgenerieren.
- **Panel-Stil-Drift:** Einzelne Panels können aus dem Stil fallen (Panel 5 wurde fotoreal) → per GPT-Image-Edit gezielt fixen („ensure panel 5 has the same … style as the rest") statt neu generieren.
- **Audio-Spezifikation im Video-Prompt:** „diegetic sound only, natural ambience, environmental foley, subject-driven sound" — sonst legt Seedance ungefragt Musik drunter. Immer „no text" anhängen.
- **Stil-Varianten eines Charakters billig:** identische Foto-Referenzen + ein Stil-Tag am Prompt-Ende („Pixar animation style", „rubber hose animation style") = derselbe Mensch in jedem Look.
- **Accessoire-Zustands-Lücke:** Skibrille abgesetzt → Gesicht brach, weil das Modell die Figur nie ohne Brille gesehen hat. Erweitert die Zustands-Sheet-Regel (Protokoll 2/5) auf An/Ab-Zustände von Accessoires.
- **Eligibility-Check:** Higgsfield scannt Referenzbilder vor Videonutzung auf Copyright/IP — bei realen Personen/Produkten einplanen.
- Dauer-Anpassung: LLM den fertigen Prompt für andere Länge umschreiben lassen („reword for a 10-second generation") statt selbst zu kürzen.
- Ökonomie: 1080p als Default, 720p für Proofs; Produkt-Ads funktionierten mit Storyboard allein (ohne Produkt-Sheet).

---

## Praxis-Protokoll 11: Seedance 2.5 Hands-on via Dreamina (unabhängiger Reviewer, Volltranskript) — nur Deltas

Quelle: YouTube xjyuNokwAPw. Dritte 2.5-Quelle; Fazit deckt sich mit Protokoll 9: „a .5 improvement, not a complete overhaul" — „best model für Physik/Emotion, aber nicht für Preis/Fidelity".

- **Bis 50 Referenzen** in 2.5 (2.0: 12), inklusive **Referenz-Video und -Audio** — laut Reviewer der eigentliche Hauptwert des Updates: größeres Kontextfenster = mehr Kontrolle. Zugang aktuell über Dreamina (ByteDance-Aggregator), dort nur 480p/720p.
- **30-s-Takes sind nicht produktionsreif:** Mit der Länge steigt der Logikverlust (unmotivierte Aktionen, falsche Blickrichtungen, absurde Objekt-Interaktionen). Empfehlung des Reviewers deckt sich mit unserer Doktrin: in kürzere Takes aufbrechen; 30 s eher als Prototyping.
- **Qualitäts-Artefakte in 2.5:** eingebackenes Artifacting („low-compression-Look eines High-Budget-Films"), vertikales Banding, Jitter wie wechselnde Shutter Speed. Für Profi-Nutzung ist ein **AI-Upscaler (z. B. Topaz) fest einzuplanen** — versteckte Zusatzkosten zur ohnehin ~2× teureren Generation ($2,18 vs. $1,14 pro 5 s/720p; 30 s = $13,10). „Is it twice as good? No."
- Direktvergleiche erneut gemischt: Moped-Test und Asteroiden-Physik gingen an **2.0**; Haut-Textur an **2.5** (2.0 plastischer); Kling fiel bei Lip-Sync/Hintergrund-Morphing deutlich ab.
- **Nebenfiguren-Intelligenz:** 2.5 platziert hochgeladene Nebencharaktere korrekt als Umgebung (unscharf im Hintergrund, nicht zur Hauptfigur befördert) — Realismus-Gewinn für belebte Szenen.
- Referenzen werden eingebaut, aber **kreativ umarrangiert** (Objekte an anderen Orten, ungefragte Verwandlungen) — Keep-List-/Layout-Disziplin bleibt auch mit 50 Refs nötig.
- **Extension-Ketten bis 3 Minuten** (30 s je Schritt): driftet zunehmend ins Absurde, Figur wechselte ins Chinesische (Trainingsdaten-Bias) — nur mit Kuratierung je Segment nutzbar.
- **Emotionale Dialogszene überzeugte** (fotoreal, mit Personen-Referenzen) — stützt die Protokoll-7-Auflösung: Emotion trägt bei Fotorealismus + starken Referenzen, nicht bei stilisiert/T2V.
- Bildtext bleibt auch in 2.5 kaputt.

---

## Praxis-Protokoll 12: Hyperrealismus mit Seedance 2.5 in Higgsfield (Tutorial-Quelle, Volltranskript) — nur Deltas

Quelle: YouTube 70I52_Ex6H4. Status-Update: **2.5 ist jetzt in Higgsfield Cinema Studio live** (P3 sagte noch „coming soon").

- **Realismus-Prompting umgestellt:** Die generische Formel (Subjekt/Aktion/Szene/Stil) produziert Plastik. 2.5 verarbeitet und belohnt Hyper-Detail: Alter, Ethnie, Gesichtsstruktur, explizit „realistic skin texture", Augen, Haar, Kleidung, Körperbau.
- **Kleine Gesichter bleiben ein Tell:** Entfernte/winzige Gesichter wirken „wie mit Bleistift gezeichnet" — für Hyperrealismus nah kadrieren. (Ergänzt die Rote/Gelbe Liste: Distanz-Gesichter sind auch in 2.5 riskant, unabhängig vom 4K-Crowd-Claim aus P4.)
- **Realismus-Deckel von Charakter-Sheets:** KI-Sheets tragen Studio-Licht und zu glatte Haut — das Video erbt beides. Für maximalen Realismus: erst ein **fotorealistisches In-Scene-Einzelbild** generieren (Szenenlicht, echte Textur), davon I2V — statt sheet-getrieben. ⚠️ Nuanciert die Sheet-Doktrin: **Sheets = Konsistenz-Werkzeug, realistische In-Scene-Stills = Realismus-Werkzeug**; je Shot nach Ziel wählen bzw. kombinieren (Sheet für Identität + In-Scene-Still als Startframe).
- **Multi-Stage-Emotionen:** Emotions-Storyboard mit Timestamps; pro Abschnitt Mikro-Cues statt Emotionslabels („chin lifts slightly, shoulders squaring", „jaw clenches, brow drops, nostrils flare"). 2.5-Stärke: Emotions-Übergänge innerhalb eines 30-s-Takes.
- ⚠️ **Negativ-Prompt-Widerspruch:** Diese Quelle nutzt für 2.5 explizit Negativ-Sektionen („no exaggerated crying movements, no fast cuts, no music, no cartoonish expressions") mit Erfolg — direkter Widerspruch zu Protokoll 1 („keine Negativ-Prompts bei Seedance", 2.0, Adil). Einstufung: Für 2.0 gilt weiter positiv formulieren; für 2.5 ist eine Negativ-Sektion testwürdig, keine gesicherte Regel.
- **Dialog-Pacing:** Figuren Zeit zum Atmen zwischen den Lines geben statt Skript in kurze Clips zu pressen — 30 s nutzen; Sprachen/Akzente steuerbar.
- **Kontinuierliche Multi-Move-Kamera bricht auch in 2.5:** 4 Kamerabewegungen in einem 30-s-Take kollabierten (Overhead-Flug zerfiel, zweiter Fahrer erschien). Empfehlung der Quelle = unsere Doktrin: Schnitte statt einer langen Fahrt; Kamera-Storyboard mit Timestamps, ein Move pro Abschnitt.

---

## Praxis-Protokoll 13: Strukturierter 2.5-Kurs, Teil 1 — Animierter 1-Minüter (Kurs-Quelle, node-basiertes „Spaces"-UI, Volltranskript) — nur Deltas

Quelle: YouTube LD55SB10ChA. Didaktisch sauberste Quelle bisher; liefert die klarste Begriffstrennung.

- **Input-Taxonomie (Kernstück):** **Start-Image** = wie der Clip beginnt. **End-Image** = wie er endet. **Referenzen** = halten Aussehen von Figuren/Objekten/Orten über die ganze Generation. **Prompt** = was passiert. Referenzen = wer, wo, wie es aussieht. Gezielte Korrekturen einzelner Momente laufen über Start/End-Images statt Neugenerierung der Sequenz.
- **Charakter-in-Umgebung-Referenzen:** Nach den Sheets zusätzlich Bilder der Figuren **in ihren Umgebungen** generieren und als Referenzen mitgeben — Brücke zwischen Sheet (Identität) und Szene (Licht/Kontext); deckt sich mit der P12-Nuance.
- **Dauer-Strategie trotz 30-s-Fähigkeit: bewusst 4×15 s.** Begründung der Quelle: Längere Generationen geben dem Modell mehr Zeit, von den Referenzen zu **driften**, Details zu ändern, Unerwartetes einzubauen. Kürzere Abschnitte = besserer Trade-off aus Konsistenz, Kontrolle und billiger Iteration. Dauer ist ein Tuning-Parameter je nach Aktionskomplexität — nicht maximieren, weil möglich. (Dritte unabhängige Bestätigung der Kurz-Take-Doktrin.)
- **Auflösungs-Ökonomie-Leiter:** Exploration bei 480p (Prompt/Komposition/Aktion billig testen) → Auswahl → finale Version höher auflösen/upscalen. 1080p als Arbeits-Default; 4K für Iteration unpraktisch (Zeit + Credits).
- **Musik-Regel mit Begründung:** Nativen Sound aktivieren (Dialog, SFX, Ambience), aber **Musik im Prompt explizit ausschließen** — vier Clips erzeugen sonst vier zusammenhanglose Soundtracks. Score entsteht in der Post über den Gesamtfilm. (Erweitert die Diegetic-only-Regel aus P10 um das Warum.)
- **Batch-Bewertung als Protokoll:** 4 Outputs pro Setup; jeden Clip **vollständig** ansehen, nie nach Einzelframe urteilen. Checkliste: bleiben Figuren nach jedem internen Cut wiedererkennbar? Folgen Orte den Referenzen? Bleibt die Aktion beim Shot-Wechsel klar lesbar?
- **Prompt-Länge ist zielabhängig:** Bei klaren Referenzen genügen konzise Prompts (Aktion, Kamera, Atmosphäre, Sound) — Gegenpol zu P12s Hyper-Detail. Auflösung: Hyper-Detail für fotorealistische Menschen ohne/mit schwachen Referenzen; konzise Prompts, wenn Referenzen die Last tragen (stilisiert/animiert).
- Multi-Shot-Prompting definiert Schnitte, indem der Prompt die Ereignisfolge erzählt („dann erreicht er die Lichtung, das Haus wird enthüllt …") — der Wechsel im Geschehen ist das Schnittsignal.

---

## Praxis-Protokoll 14: Long-Video-Mode (60 s) in Dreamina, Musikvideo-B-Roll (unabhängiger Creator, Volltranskript) — nur Deltas

Quelle: YouTube 8lhYCnCNT-Y. Experimente mit dem 2.5-Long-Video-Modus jenseits der 30 s.

- **60-s-Generationen existieren** (Dreamina Long-Video-Mode, 720p; ~4.000 Credits pro Minute ohne Rabatt — teuer). Referenz-Handling hielt bei ~30 angehängten Bildern („spot-on", besonders Charaktere).
- **Timestamp-Prompting bricht bei Langform (A/B/C-Test):** (1) Strikte Timestamps pro Aktion → erste 18 s brauchbar, danach „wonky". (2) Hybrid aus Timestamps + Beschreibung → Zeitsprünge, Szene loopt zum Anfang zurück. (3) **Ohne Timestamps, rein deskriptive Ereignisfolge → klar bestes Ergebnis.** Einordnung: Timestamps funktionieren in kurzen Takes (P3/P12, ≤30 s); für 60-s-Montagen deskriptiv prompten.
- **Padding-Effekt:** 2.5 legt ein paar Sekunden „Dead Space" um gepromptete Aktionen — Aktionen landen später als getimestampt; Timing-Erwartungen entsprechend locker planen.
- **Label-Disziplin bei vielen Referenzen:** Asset-Labels im Prompt müssen den Labels der angehängten Referenzen exakt entsprechen (spart das Neu-Verknüpfen); **einmalige Erwähnung reicht** — das Modell erinnerte Assets über mehrere Szenen der Generation, ohne sie pro Szene erneut zu referenzieren.
- **Montage-Denke:** Für B-Roll/Musikvideo-Montagen Übergänge nicht erzwingen — in der Post schneiden; auch „gescheiterte" Runs liefern verwertbare Einzelstücke für den Schnitt. Long-Video lohnt für Montage-Material, nicht für präzise erzählte Szenen.

---

## Praxis-Protokoll 15: Gezeichneter Kamera-Pfad (Creator „Nova", LoomFlow-affiliiert, Volltranskript) — nur Deltas

Quelle: YouTube tVPNCk2O-yQ. Vierte Geometrie-Input-Form neben Layout-Map (P2), Skizze (P5) und Pfeil-Annotation (P6): **die Kamera-Pfad-Linie.**

- **Workflow:** Sauberes Environment-Bild generieren (ohne Markierung) → grobe Linie für die Kameraroute direkt aufs Bild zeichnen (muss nicht präzise sein) → markiertes Bild dem LLM geben, das den Seedance-Prompt zur Bewegung schreibt → markiertes Bild als Input + Prompt generieren. In manchen UIs wird das Bild per **@-Tag im Prompt** referenziert.
- **Linie + Text arbeitsteilig:** Die Linie gibt die generelle Richtung, der Text disambiguiert das Wie („punch through the gap instead of flying over it"). Ohne Text-Präzisierung interpretiert das Modell frei.
- **Winkelwechsel entlang des Pfads:** Nummerierte Schritte, die dem gezeichneten Pfad folgen, erlauben Kamera-Wechsel innerhalb der Fahrt — POV → Tracking → Close-up → Slow-mo — statt reinem POV-Flythrough; Charakter-Referenzen bleiben dabei konsistent. Seedance liest 3D-Tiefe aus dem 2D-Bild (Vertikal-Drops, Dach-Tracking funktionieren).
- **Pfadlänge budgetieren:** Zu langer Pfad → Engine schafft in 15 s nur ~die Hälfte der Route. Pfadlänge an Take-Dauer anpassen.
- Einsatz: POV-Flythroughs, Establishing-Fahrten durch Locations, Verfolgungs-Tracking — überall, wo Kamerarouten in Textform scheitern.

---

## Praxis-Protokoll 16: Sheet-Minimalismus, Storyboard-Adhärenz, Plattform-Ökonomie (unabhängiger Instagram-Creator, Volltranskript) — nur Deltas

Quelle: YouTube DosWo7GplD4. Wertvoll als Entzauberung der „schönen" Sheets.

- **Sheet-Minimalismus:** Fancy Multi-Panel-Sheets mit Beschriftungen sind großteils „looking pretty" — verschwendeter Platz. Es reicht: **Front, Seite, Rücken, Gesichts-Close-up, Kleidung.** Text auf Sheets liest das Modell vermutlich nicht. Aber: **kleine Kleidungs-Details brauchen ein eigenes Close-up-Panel**, sonst werden sie falsch gerendert. ⚠️ Relativiert die aufwendigen Adil-/Academy-Sheet-Layouts: Inhalt schlägt Ästhetik.
- **Location-Kontinuität bleibt ungelöst:** Je komplexer die Location (Basketball-Linien!), desto schwerer die Kontinuität — „haven't figured out location sheet continuity yet" (ehrlichste Aussage der ganzen Serie). Faustregeln: Durch-die-Stadt-Videos dürfen frei schneiden (jeder Shot neue Kulisse ok); Ein-Ort-Videos brauchen die Kontinuität wirklich. **Workaround: Screenshots aus einer gelungenen Generation als Location-Referenzen** für Folge-Generationen — Video-Stills statt Location-Sheet.
- **Storyboard-Adhärenz quantifiziert: ~70–80 %.** Storyboard und reiner Prompt funktionieren beide; Storyboard-Vorteil ist die **billige visuelle Vorab-Prüfung** (gleichförmige Shots erkennen und fixen, bevor Video-Credits fließen).
- **Adhärenz ist auflösungsunabhängig:** Das Modell folgt dem Storyboard bei 480p genauso — deshalb Shot-Flow bei 480p testen, erst bei Gefallen 720/1080 generieren (unabhängige Bestätigung + Begründung der P13-Leiter). Seedance-„Fast"-Variante für Tests brauchbar.
- Durchschnitt **4–5 Generationen pro Storyboard**, dann Cherry-Picking; die Musik auf der Timeline diktiert Schnittbedarf und Nach-Prompts („mehr Close-Cuts am Anfang").
- Charakter-Findung: MidJourney-Explore-Seite (Charaktere entdecken, Prompts sichtbar) → Edits dann in GPT Image/Banana (MJ editiert schlecht).
- Crowd-Klone unabhängig bestätigt: Ein Bild mit vielen unterschiedlichen Gesichtern als Referenz würde die identischen Statisten fixen (deckt sich mit P6-Multi-Varianten-Sheet).
- **Plattform-Ökonomie:** Runway, ArtList, Magnific, Higgsfield, LoomFlow etc. sind Aggregatoren derselben Modell-APIs — nach Preis wählen, nicht nach Features; Modellverhalten ist plattformunabhängig identisch.

---

## Praxis-Protokoll 17: Pixar-Animations-Kurzfilm mit Seedance 2.5 (Creator-Tutorial, Volltranskript) — nur Deltas

Quelle: YouTube-Tutorial (Klassenzimmer-Kurzfilm "This is my family", Seedance 2.5 + Higgsfield). Bestätigt weitgehend P1–P16 + [PP]; hier nur Neues:

- **Voice-Harvest-Workflow (Kernstück):** Die erste Generation setzt die Stimm-Baseline pro Charakter — Konsistenz danach ist die eigentliche Herausforderung. Fix: alle Sprechzeilen eines Charakters aus den Takes schneiden, pro Charakter zu EINER Referenz kompilieren (kombiniert <30 s), als **MP4 mit Schwarzbild exportieren (nicht MP3)** und als Video-Referenz neben dem Character-Sheet an jede Folge-Generation hängen → Stimmen halten über Generationen und Extends.
- **Animations-Sheet-Variante:** Für Animation funktioniert das übliche Multi-View-Sheet schlechter — animierte Videos tragen viel mehr Mimik als Cinematic. Layout: Full-Body-Pose + 8 Expression-Panels.
- **Seedream 5.0 Pro** auf Higgsfield verfügbar; lieferte für ein Character-Sheet das beste Ergebnis (Einzelfall). GPT Image 2: Grain-/Noise-Tell bei stilisierten Renders — Grund für Nano Banana Pro bei der Location.
- **Mix and match pro Asset:** Kein Bildmodell gewinnt projektweit; pro Asset vergleichen. "Credits for images are quite cheap — spend more time getting the best image than trying to fix it with your video generations."
- **Doppel-Generierung bei 30-s-Takes:** Zwei Batches desselben Prompts, beste Teile über Generationen schneiden (Beispiel: Tür-Durchbruch aus Take 2 ersetzt Wand-Glitch aus Take 1). Aber: erste Generation komplett Müll → Prompt überarbeiten, nicht erneut würfeln.
- **Style-Reverse-Engineering:** Referenzen zuerst vom LLM analysieren lassen (Hauttexturen, Materialien) → wiederverwendbare Basis-Prompt-Struktur; pro Charakter mit weiteren Referenzen iterieren ("rinse and repeat").
- Extend-UI: Richtungswahl **Sequel/Prequel**; Referenzen erneut anhängen, Dauer angeben (~29–30 s), nahtlose Fortsetzung bestätigt.
- 12-Segment-Charakter-Prompt-Format (Face/Subject/Skin/Hands/Silhouette/Hair/Wardrobe/Pose/Camera/Background) als Portrait-Variante.
- Finger-Zählen-Szene scheiterte teilweise (falsche Fingerzahl) — bestätigt die Hände-Regel der Roten Liste auch in 2.5.

---

## Praxis-Protokoll 18: Blender-Blockout-Workflow mit Higgsfield-Plugin (Adil, Volltranskript) — nur Deltas

Quelle: YouTube OiULPvTJ-0E. Neuer Produktionspfad: 3D-Blocking in Blender steuert Seedance-Kamera exakt.

- **Setup:** Higgsfield-Plugin (frei) + Bridge-URL als LLM-Connector + Plugin in Blender ziehen; Higgsfield-Panel im Viewport (Assets/Modelle/Szenen direkt einsetzbar). Empfehlung des Creators: Cowork-Modus, Reasoning hoch.
- **Kern-Workflow:** Szene + Shotliste in Sprache → LLM baut editierbare Gray-Boxes, Kamera-Rails, Cuts → Iteration in Sprache ("mehr Handheld", "Textur", "Scene 3 recutten") → Viewport-Render 1080p/24/MP4 → Render anhängen + "write a 30-second prompt based on this video blocking, second by second matching the camera moves" → Generation mit Dauer = Blocking-Länge.
- **Belegte Ergebnisse:** Orbit→Profil→Top-Down in einem Move · Floor-Rise · Robo-Arm-Whip — first try; 6-Personen-Dialog, 4 Cuts, 30 s, null Platztausch, jede Line auf dem richtigen Gesicht. Identischer Prompt OHNE Blockout: Platztausch pro Take, 180°-Bruch, ~5.000 Credits ohne brauchbaren Take.
- **Gray-Box-Regeln:** Blockout = Kamera+Timing, Referenzen = Visuals (Trennung im Prompt benennen). Unblockbares (Flüssigkeit) schwarz/leer lassen — Modell füllt. Kamera folgt separatem Offset-Target neben dem Kopf (Realismus). Handheld als subtiler Nach-Pass. Pfad mit Kontrollpunkten ist drag-editierbar — Winkel in Blender ziehen statt reprompten.
- **Zwei-Hälften-Prinzip:** Struktur-Hälfte (Blocking-Video: Cuts/Kamera/Timing, unveränderlich) + Stil-Hälfte (Welt). Client-Notes → Blocking recutten; Restyle → Stil-Hälfte tauschen: ein Edit als 2.5D / 2D ink / Toy-Box-3D, Kamera frame-identisch. Pitch: drei Welten auf einem approbierten Edit an einem Tag.
- Previs-Framing: entspricht Studio-Previs (Kamerapositionen, Schulter-Frames, Eyelines vor dem ersten Licht) — als Ein-Satz-Auftrag.
- Speed-Ramps über Blocking-Änderung statt Prompt ("slams in, pauses, accelerates into next cut") — Cut gleitet auf der Rampe.
