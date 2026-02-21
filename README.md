## What is this project?

We are building a tool that predicts **where a meteorite lands** after it stops
glowing and falls invisibly through the atmosphere ("dark flight"). The tool will:

1. Simulate the physics of a falling rock under gravity, drag, and wind
2. Pull real wind data from NOAA
3. Run thousands of simulations to produce a **probability map** of where to search

This is a 4-week sprint across four team members. This README will grow each week.

---

## Folder Structure

```
meteor-dark-flight/
├── .github/
│   └── workflows/
│       └── ci.yml         
├── src/
│   └── metrec/             
│       ├── physics/        
│       ├── data/          
│       ├── core/           
│       └── viz/          
├── tests/
├── notebooks/        
├── examples/              
├── data/                   ← raw data goes here (git-ignored, not uploaded)
├── docs/                   ← documentation (future)
├── paper/                  ← manuscript draft (future)
├── requirements.txt        ← Python packages everyone needs to install
└── pyproject.toml          ← makes `metrec` pip-installable
```

---

## Setup (do this first — everyone)

You need Python 3.10 or newer. Check with:
```bash
python --version
```

### Step 1 — Clone the repo
```bash
git clone https://github.com/Fuad1711/METREC
cd METREC
```

### Step 2 — Create a virtual environment

This keeps the project's packages separate from your system Python.
```bash
python -m venv .venv

# On Mac/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

You should see `(.venv)` appear in your terminal prompt.

### Step 3 — Install dependencies
```bash
pip install -e ".[dev]"
```

The `-e` means "editable install" — changes you make to the source files take
effect immediately without reinstalling.

### Step 4 — Verify everything works
```bash
pytest tests/ -v
```

You should see something like:
```
tests/test_week1.py::test_package_is_importable PASSED
tests/test_week1.py::test_placeholder_always_passes PASSED
```

---

## Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run just the Week 1 tests
pytest tests/test_week1.py -v
```

Tests also run **automatically on GitHub** every time anyone pushes a commit.
Check the Actions tab on GitHub to see results.

---

## How to Contribute (Week 1 version — keep it simple)

1. Make a branch for your work:
   ```bash
   git checkout -b week1/your-name-or-task
   ```
2. Do your work, commit often:
   ```bash
   git add .
   git commit -m "short description of what you did"
   ```
3. Push and open a Pull Request:
   ```bash
   git push origin week1/your-name-or-task
   ```
4. Check that the CI badge goes green on your PR before asking for review.

---

## Where to put Week 1 work

- **Zarin** → `notebooks/week1_terminal_velocity.ipynb`
- **Ovi** → `scripts/week1_fetch_wind.py`
- **Fuad** → (`tests/test_week1.py`)
- **Iftekhar** → `scripts/week1_map_points.py`

*(The `scripts/` folder doesn't exist yet — B or D can create it when they push their work.)*

---

## License

MIT — see [LICENSE](LICENSE).