## Descrierea proiectului

Acest proiect citește expresii regulate dintr-un fișier JSON, le convertește în Automate Finite Nedeterministe (NFA) și verifică dacă un set de șiruri de caractere sunt acceptate de lambda-NFA-ul generat. Procesul implică conversia expresiei regulate în notație postfix, construirea unui lambda-NFA pentru fiecare expresie și simularea NFA-ului pentru a valida dacă șirurile de intrare sunt acceptate.

 Forma unui test din fișierul JSON este următoarea: 
 ```
    {
        "name": "R2",
        "regex": "(ab)*",
        "test_strings": [
          { "input": string1, "expected": "" },
          { "input": string2, "expected": "" }
    ]
      } 
 ``` 
## Execuția programului:
- Expresia regulată de intrare este mai întâi transformată în notație postfix (forma poloneză).
- Construire lambda-NFA:
Se construiesc automat NFA-uri pentru simboluri și se combină folosind:

    - concatenarea → concat(nfa1, nfa2)

    - alternarea → OR(nfa1, nfa2)
    
    - zero sau mai multe repetări → star(nfa)
    
    - una sau mai multe repetări → plus(nfa)
    
    - prezență opțională → question(nfa)


- Pentru fiecare șir de intrare, simularea NFA-ului este rulată, iar rezultatul este comparat cu valoarea așteptată.

## Rularea programului

Scriptul se rulează direct prin următoarea comandă:
```
python3 tema.py
```
Outputul va indica pentru fiecare test dacă rezultatul este cel așteptat:
```
R2: (ab)*
The result is the expected result
The result is the expected result
The result is not the expected result
```
La final, dacă toate testele au trecut, va fi afișat următorul mesaj:
```
The result is the expected result
```



