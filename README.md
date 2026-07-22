---

## What this repo covers

| # | Project | Core Skills |
|---|---|---|
| 1 | Titanic — First Look | `.shape`, `.dtypes`, `.describe()`, `.head()`/`.tail()`, `.unique()` |
| 2 | Titanic — Missing Data | `.isna().sum()`, fillna (median/mode), dropping columns |
| 3 | Titanic — Filtering | boolean filtering, `.isin()`, `.loc[]`, negation |
| 4 | Titanic — GroupBy & Aggregation | `.groupby()`, `.agg()`, `.size()` vs `.count()`, `.reset_index()` |
| 5 | Titanic — Columns, Apply, Pivot | new columns, `.apply()`, `.sort_values()`, `pivot_table` |
| 6 | Tips — Calculated Columns | ratio columns, `.idxmax()`/`.idxmin()` |
| 7 | Tips — Multi-Level GroupBy | multi-column groupby, `.agg()` with dict |
| 8 | Tips — Concat & Merge | `pd.concat()`, `pd.merge()`, join types (`left` vs `inner`) |
| 9 | Tips — Ranking & Binning | `.rank()`, `pd.cut()` vs `pd.qcut()` |
| 10 | Tips — Correlation & Pivot | `.corr()`, pivot tables with `margins=True` |
| 11 | Messy Sales — Diagnosing | spotting dtype/whitespace/casing issues before touching data |
| 12 | Messy Sales — String Cleaning | `.str.strip()`, `.str.lower()`, `.str.title()` |
| 13 | Messy Sales — Numeric Cleaning | stripping currency symbols, `pd.to_numeric(errors='coerce')` |
| 14 | Messy Sales — Date Parsing | `pd.to_datetime(errors='coerce')`, `.dt` accessor |
| 15 | Messy Sales — Duplicates & Export | `.duplicated()`, `.apply(axis=1)`, `.to_csv()`/`.to_excel()` |

## Datasets used

- **Titanic** — loaded via `seaborn.load_dataset('titanic')`, no download needed
- **Tips** — loaded via `seaborn.load_dataset('tips')`, no download needed
- **Messy Sales** — synthetic dataset generated in-script (intentionally messy: inconsistent casing, currency symbols, mixed date formats, duplicates)
