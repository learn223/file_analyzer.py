# File Analyzer

A Python utility for analyzing text files with comprehensive statistics and content manipulation features.

## Overview

File Analyzer is a lightweight Python tool that provides detailed insights into text files. It calculates various metrics including line counts, word counts, and averages, while also offering functionality to separate even and odd lines, reverse file contents, and generate comprehensive summary reports.

## Features

- **Line Count Analysis**: Calculate total number of lines in a file
- **Word Statistics**: Compute total words and average words per line
- **Even/Odd Line Separation**: Extract and separate lines based on their position
- **File Reversal**: Reverse the order of lines in a file
- **Summary Generation**: Create detailed analysis reports saved to a text file
- **Simple API**: Easy-to-use functions with clear parameters

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Installation

1. Clone or download the repository:
```bash
git clone https://github.com/yourusername/file_analyzer.git
cd file_analyzer
```

2. Ensure you have Python installed:
```bash
python --version
```

## Usage

### Basic Usage

Create a text file named `file.txt` in the same directory, then run:

```bash
python file_analyzer.py
```

This will:
- Generate a summary report (`summary.txt`)
- Create a reversed version of the file (`reversed.txt`)

### Individual Functions

#### 1. Read File Contents
```python
from file_analyzer import read_file

contents = read_file("file.txt")
# Returns a list of lines from the file
```

#### 2. Count Total Lines
```python
from file_analyzer import read_total_lines

total = read_total_lines("file.txt")
print(f"Total lines: {total}")
```

#### 3. Separate Even and Odd Lines
```python
from file_analyzer import read_even_and_odd_num_lines

even_lines, odd_lines = read_even_and_odd_num_lines("file.txt")
print(f"Even lines: {len(even_lines)}")
print(f"Odd lines: {len(odd_lines)}")
```

#### 4. Calculate Average Words Per Line
```python
from file_analyzer import average_num_word_per_line

avg = average_num_word_per_line("file.txt")
print(f"Average words per line: {avg:.2f}")
```

#### 5. Count Total Words
```python
from file_analyzer import total_words

word_count = total_words("file.txt")
print(f"Total words: {word_count}")
```

#### 6. Reverse File Contents
```python
from file_analyzer import reverse_file_contents

reverse_file_contents("file.txt", "output_reversed.txt")
# Creates a new file with lines in reverse order
```

#### 7. Generate Complete Summary
```python
from file_analyzer import save_summary

save_summary("file.txt", "my_summary.txt")
# Creates a comprehensive analysis report
```

## Example

Given a file `file.txt` with the following content:

```
A crust of bread and a corner to sleep in,
A minute to smile and an hour to weep in,
A pint of joy to a peck of trouble,
And never a laugh but the moans come double;
And that is life!
```

Running the analyzer will produce:

**summary.txt**:
```
File Analysis Summary for: file.txt 
==================================================

Total Lines: 5
Even-numbered Lines: 2
Odd-numbered Lines: 3
Total Words: 40
Average Words per Line: 8.00

Even-numbered lines content:
--------------------------------------------------
A minute to smile and an hour to weep in,
And never a laugh but the moans come double;

Odd-numbered lines content:
--------------------------------------------------
A crust of bread and a corner to sleep in,
A pint of joy to a peck of trouble,
And that is life!
```

**reversed.txt**:
```
And that is life!
And never a laugh but the moans come double;
A pint of joy to a peck of trouble,
A minute to smile and an hour to weep in,
A crust of bread and a corner to sleep in,
```

## Function Reference

| Function | Parameters | Returns | Description |
|----------|-----------|---------|-------------|
| `read_file()` | `file_contents` (str) | list | Reads and returns all lines from a file |
| `read_total_lines()` | `total_lines` (str) | int | Returns the total number of lines |
| `read_even_and_odd_num_lines()` | `file_name` (str) | tuple | Returns two lists: even lines and odd lines |
| `average_num_word_per_line()` | `file_name` (str) | float | Returns average words per line |
| `total_words()` | `file_contents` (str) | int | Returns total word count |
| `reverse_file_contents()` | `file_reverse` (str), `output_file` (str) | str | Reverses file and returns output filename |
| `save_summary()` | `file_name` (str), `summary_file` (str) | str | Generates summary report and returns filename |

## Output Files

The tool generates two output files by default:

1. **summary.txt**: Contains comprehensive file statistics and content analysis
2. **reversed.txt**: Contains the original file content in reverse line order

## Error Handling

- The tool handles empty files gracefully (returns 0 for averages)
- Ensure input files exist before running the analyzer
- All functions require read permissions for input files
- Output operations require write permissions in the directory

## Use Cases

- **Text Analysis**: Analyze structure and composition of text documents
- **Data Validation**: Verify line counts and word counts in data files
- **Content Processing**: Extract even or odd lines for alternating data patterns
- **File Manipulation**: Quickly reverse log files or ordered lists
- **Report Generation**: Create automated summaries of text file contents

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Author

Your Name - Obed Udem(mailto:your.obedudem@gmail.com)

## Acknowledgments

- Built with Python standard library
- Inspired by common text processing needs
- Thanks to all contributors

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository or contact the maintainer directly.