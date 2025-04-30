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
- Această idee funcționează deoarece se bazează pe echivalența dovedită dintre expresiile regulate și automate finite nedeterministe (NFA). Orice limbaj descris printr-o expresie regulată poate fi recunoscut de un NFA, iar orice NFA poate fi construit pentru a simula comportamentul unei expresii regulate. Prin transformarea expresiei într-o formă postfixată, putem construi recursiv un NFA pentru fiecare operator (concat, alternare, stea, plus, prezență opțională) și combină automatul final. Apoi, simularea NFA-ului, care include și explorarea tuturor tranzițiilor lambda, permite verificarea completă a tuturor căilor posibile prin care un șir poate fi acceptat. Acest mecanism este corect din punct de vedere teoretic și reflectă fidel regulile limbajelor regulate.

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



