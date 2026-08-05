# PLAN.md — bank-data-pipeline

> Osobisty projekt portfolio (Data Engineering → MLOps / Analytics Engineering).
> Cel realny: **udowodnić sobie nawyk przez 2 tygodnie → dopiero potem kupić MacBooka.**
> Dowód nie do oszukania: publiczna historia commitów na GitHubie.
> **Kod piszę ja. Claude = rubber duck / review / odblokowywanie, nie wykonawca.**

---

## Zasada kosztu (to jest ten "wysiłek", o który chodzi)
- **3 sesje / tydzień, po 60–90 min.** Wpisane do kalendarza jako stałe bloki. Bronione jak spotkanie z klientem.
- Ochota nie przyjdzie — blok owszem.
- **Nigdy dwa razy z rzędu.** Jeden opuszczony blok to życie, dwa to wzorzec.
- **Done > perfect.** Commituj brzydkie, potem poprawiaj.
- Pierwsza sesja ma być śmiesznie mała. Momentum > intensywność.

---

## Stack
Python · BigQuery (sandbox / free tier — 0 zł) · Terraform · dbt · GitHub Actions · Looker Studio / Streamlit

---

## Struktura repo (stawiasz w sesji 1)
```
bank-data-pipeline/
├── README.md
├── PLAN.md              <- ten plik
├── .gitignore          <- venv, dane, *.pdf, sekrety
├── requirements.txt
├── data/               <- lokalne dane, NIE commitowane
├── src/
│   ├── parse.py        <- PDF wyciągu -> czyste transakcje + kategorie
│   └── load.py         <- transakcje -> BigQuery
├── infra/              <- Terraform (dataset BQ jako IaC)
├── dbt/                <- projekt dbt (staging + marty)
│   ├── models/staging/
│   └── models/marts/
├── dashboard/          <- link/screeny Looker Studio albo mały Streamlit
└── .github/workflows/  <- CI: parser + dbt test przy każdym pushu
```

---

## TYDZIEŃ 1 — fundament + ingest

**Sesja 1 (mała, rozgrzewkowa)**
- [ ] Publiczne repo na GitHubie, `git init`, pierwszy commit
- [ ] `README.md` — jedno zdanie co to jest, szkielet katalogów
- [ ] `.gitignore` (venv, `data/`, `*.pdf`, sekrety), `requirements.txt`, `venv`
- [ ] Wrzucić ten `PLAN.md` do repo

**Sesja 2**
- [ ] `src/parse.py` — wczytanie PDF, wyciągnięcie transakcji (data, kwota, opis)
- [ ] Reconciliation: suma obciążeń z parsera == suma z wyciągu (test poprawności)

**Sesja 3**
- [ ] Kategoryzacja merchantów (Glovo / Żabka / fast food / paliwo / spożywczy / mieszkanie / subskrypcje / transfery)
- [ ] Zapis wyniku do `parquet`/`csv`
- [ ] **Kamień milowy:** `python src/parse.py wyciag.pdf` → czysta, skategoryzowana tabela. Push.

---

## TYDZIEŃ 2 — hurtownia + transformacje

**Sesja 4**
- [ ] BigQuery sandbox, projekt, poświadczenia lokalnie (poza repo!)
- [ ] `infra/` — Terraform stawiający dataset (IaC — Twoja działka)

**Sesja 5**
- [ ] `src/load.py` — załadowanie transakcji do BQ (tabela raw)
- [ ] Projekt dbt wpięty w BQ, warstwa `staging` (czyszczenie, typy, standaryzacja)

**Sesja 6**
- [ ] Marty: wydatki wg kategorii/miesiąca, metryka "wycieku", częstotliwość merchantów
- [ ] `dbt test` (not_null, accepted_values na kategoriach)
- [ ] **Kamień milowy:** `dbt run` + `dbt test` na zielono, wszystko w repo.

---

## 🚦 BRAMKA PO 2 TYGODNIACH — to jest właściwy test
Sprawdzasz szczerze:
- [ ] Jest zielona historia z ~5–6 odbytych sesji?
- [ ] Parser działa i dane są w BigQuery?

**TAK →** nawyk udowodniony. Kupujesz MacBooka z czystym sumieniem. Tygodnie 3–4 robisz już NA nim (pierwsze zadanie na nowym sprzęcie).
**NIE →** dostałeś szczerą odpowiedź, oszczędziłeś ~10k, dowiedziałeś się czegoś prawdziwego. W obie strony wygrywasz.

---

## TYDZIEŃ 3 — wgląd + wizualizacja

**Sesja 7**
- [ ] Looker Studio wpięte w BQ (albo mały Streamlit)
- [ ] Wykresy: trend kategorii w czasie, miesięczny wyciek

**Sesja 8**
- [ ] Licznik Glovo + top merchantów wg częstotliwości
- [ ] **Kamień milowy:** link do dashboardu / screeny w README. Tu zobaczysz WŁASNE dane.

---

## TYDZIEŃ 4 — polish + automatyzacja

**Sesja 9**
- [ ] GitHub Actions: CI odpalające parser + `dbt test` przy każdym pushu
  (robiłeś już Actions przy katalogu pojazdów — znajomy teren)

**Sesja 10**
- [ ] README dopieszczony: diagram architektury + sekcja "czego się nauczyłem"
      (to jest artefakt na rozmowę typu Medicover)
- [ ] **Stretch:** Cloud Scheduler (harmonogram) albo drugie źródło danych

---

## Kotwica-nawyk obok (opcjonalna, mierzalna)
Skoro "dom to piękna ruina, nie mam siły":
- [ ] Doprowadzić kuchnię do stanu, w którym da się ugotować
- [ ] Domowe Glovo → maks. 1×/tydzień
- [ ] Metryka nieoszukiwalna: **licznik Glovo w apce banku**
- Efekt uboczny: ~700 zł/mc mniej wycieku + odzyskana przestrzeń. Dodatek, nie kręgosłup.

---

## Definicja sukcesu
Nie "idealny projekt". Sukces = **dowód, że wpisany blok wygrywa z brakiem ochoty.**
Repo albo ma zielone kwadraty, albo nie ma. Reszta to szczegóły.
