---
## What this repo covers
| # | Project | Core Skills | Chart Added |
|---|---|---|---|
| 1 | First Look | `.shape`, `.dtypes`, `.describe()`, `.head()`/`.tail()`, `.unique()` | Age distribution histogram |
| 2 | Missing Data | `.isna().sum()`, fillna (median/mode), dropping columns | Bar chart of missing values by column |
| 3 | Filtering | boolean filtering, `.isin()`, `.loc[]`, negation | Children vs adult survival bar chart |
| 4 | GroupBy & Aggregation | `.groupby()`, `.agg()`, `.size()` vs `.count()`, `.reset_index()`, `.unstack()` | Grouped bar chart: survival by sex & class |
| 5 | Columns, Apply, Pivot | new columns, `.apply()`, `.sort_values()`, `pivot_table()`, exporting to csv/xlsx | Pivot chart + family type distribution, saved as PNG |

## Dataset used
- **Titanic** — loaded via `seaborn.load_dataset('titanic')`, no download needed
