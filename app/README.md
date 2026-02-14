# FounderOS Local App

Browser-based local console for FounderOS.

## Run

```bash
python3 app/server.py --port 8787
```

Then open:

- `http://127.0.0.1:8787`

## What You Get

- Chat-style interface with FounderOS commands
- Auto-router and command switching
- Live editor for `memory/*.md`
- Quick prompts for planning, MVP launch, and postmortems

## Notes

- No third-party Python packages required.
- Uses repo memory files directly, so changes persist to `memory/`.
