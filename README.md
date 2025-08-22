# Contiguous Sequential Pattern Mining in Text Data
## 📋 Project Overview
This project implements an efficient algorithm for mining contiguous sequential patterns from text data, specifically applied to a corpus of 10,000 stemmed Yelp reviews. The algorithm identifies meaningful phrase candidates that appear consecutively across multiple reviews with a minimum support threshold of 0.01 (100 occurrences).

## 🎯 Algorithm Implementation
### Core Approach
The implementation uses a breadth-first search strategy to efficiently discover contiguous sequential patterns of increasing length:

1. Initialization: Identifies all frequent single words (length-1 patterns)

2. Pattern Extension: Iteratively extends existing patterns by one word while maintaining contiguity

3. Support Counting: Uses sequence-level counting where each pattern is counted at most once per review

4. Pruning: Eliminates candidate patterns that fall below the minimum support threshold

### Key Features
- Contiguous Pattern Mining: Ensures all elements in discovered patterns appear consecutively in the original text

- Efficient Counting: Uses sequence IDs to avoid redundant counting of multiple occurrences in the same review

- Progressive Extension: Builds longer patterns from verified shorter ones, minimizing unnecessary computations

- Comprehensive Output: Includes all patterns from length 1 to maximum supported length

## 🛠 Technical Implementation
### Data Structures
DefaultDict: For efficient frequency counting and pattern extension tracking

Tuples: Used as immutable pattern representations for dictionary keys

Sets: For efficient sequence ID tracking during pattern extension

Algorithm Complexity
The implementation efficiently handles the pattern mining problem with:

O(n) initial pass for length-1 patterns

O(k × m × n) for pattern extension, where k is maximum pattern length, m is number of patterns, and n is number of sequences

Memory-efficient pattern storage using tuple representations

## 📊 Results
The algorithm successfully mines contiguous sequential patterns from the Yelp review dataset, identifying:

- Single-word patterns (common stemmed terms)

- Multi-word phrases that frequently appear together

- Meaningful combinations that represent common review phrases

Output Format
Patterns are written to patterns.txt in the format:

text
support:item_1;item_2;item_3
Example:

text
133:parking;lot
215:good;service
## 🚀 How to Use
- Requirements
- Python 3.6+

No external dependencies

Execution
bash
python pattern_miner.py
Parameters
filename: Path to input text file (default: "reviews_sample.txt")

min_support: Minimum absolute support threshold (default: 100)

Customization
The algorithm can be easily adapted for:

Different support thresholds

Alternative text preprocessing approaches

Various input formats and domains

## 📈 Applications
This pattern mining approach has practical applications in:

- Natural Language Processing: Phrase extraction and candidate generation

- Recommendation Systems: Identifying common product feature combinations

- Market Basket Analysis: Discovering frequently co-occurring items

- Text Analytics: Uncovering common patterns in user-generated content

## 🎓 Academic Context
This project was developed as part of the Master of Computer Science in Data Science program at the University of Illinois Urbana-Champaign, demonstrating practical implementation of sequential pattern mining algorithms on real-world text data.

The implementation showcases understanding of:

- Fundamental data mining concepts

- Efficient algorithm design

- Text processing techniques

- Pattern evaluation and selection

## 📝 Future Enhancements
Potential improvements include:

- Incorporation of constraint-based mining

- Integration with statistical significance testing

- Parallelization for large-scale datasets

- Interactive visualization of pattern relationships
