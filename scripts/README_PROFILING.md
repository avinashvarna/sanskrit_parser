# Profiling Sanskrit Parser

This directory contains scripts and instructions for profiling the performance of the Sanskrit Parser.

## Profiling Script: `profile_kiss.py`

This script allows you to run the parser on CONLL files (like those in the KISS dataset) and profile the execution.

### Usage

```bash
python3 scripts/profile_kiss.py tests/KISS/KISS_Sanskrit_Parsing_Data/dataset/STBC_Dev.conll -n 1
```

Options:
- `-n`, `--num-tests`: Number of tests to run from each file (default: 1).
- `-s`, `--skip`: Number of tests to skip (default: 0).
- `--max-splits`: Maximum number of lexical splits to explore (default: 1).
- `--max-parses`: Maximum number of parses to explore for each split (default: 1).
- `--pyinstrument`: Use `pyinstrument` for profiling.

### 1. Using `pyinstrument`

`pyinstrument` is a statistical profiler that provides a nice hierarchical view of where time is spent.

```bash
python3 scripts/profile_kiss.py tests/KISS/KISS_Sanskrit_Parsing_Data/dataset/STBC_Dev.conll -n 1 --pyinstrument
```

### 2. Using `scalene`

`scalene` provides high-precision CPU and memory profiling.

```bash
scalene run scripts/profile_kiss.py tests/KISS/KISS_Sanskrit_Parsing_Data/dataset/STBC_Dev.conll -n 1
```

To view the results in the terminal:
```bash
scalene view --cli scalene-profile.json
```

### 3. Using `line_profiler`

`line_profiler` is useful for seeing line-by-line execution time.

To use it with `profile_kiss.py`, you can use the `kernprof` tool. Note that you may need to add the `@profile` decorator to the functions you want to profile in the source code.

Example:
```bash
kernprof -l -v scripts/profile_kiss.py tests/KISS/KISS_Sanskrit_Parsing_Data/dataset/STBC_Dev.conll -n 1
```

## Tips for Profiling

- Start with a small number of tests (`-n 1`) as some sentences can take a long time to parse.
- Use `--skip` to profile specific sentences if you find one that is particularly slow.
- The first run might be slower due to database initialization and caching.
