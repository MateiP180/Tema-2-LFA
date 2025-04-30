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

    - . (concat) → concat(nfa1, nfa2)

    - | (alternare) → OR(nfa1, nfa2)
    
    - * (zero sau mai multe repetări) → star(nfa)
    
    - + (una sau mai multe repetări) → plus(nfa)
    
    -? (prezență opțională) → question(nfa)


- Pentru fiecare șir de intrare, simularea NFA-ului este rulată, iar rezultatul este comparat cu valoarea așteptată.

Scriptul se rulează direct prin comanda python 3. Acesta va procesa expresiile regulate și șirurile de test, afișând dacă fiecare șir corespunde rezultatului așteptat.

