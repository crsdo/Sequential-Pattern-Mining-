from collections import defaultdict

def mine_contiguous_patterns(filename, min_support):
    # Read data
    sequences = []
    with open(filename, 'r') as f:
        for line in f:
            sequences.append(line.strip().split())
    
    # First pass: find all frequent length-1 patterns
    freq_1 = defaultdict(int)
    for seq in sequences:
        for word in set(seq):  # Count each word only once per sequence
            freq_1[word] += 1
    
    # Filter by minimum support
    patterns = { (word,): count for word, count in freq_1.items() 
                if count >= min_support }
    
    # Find longer patterns
    k = 1
    while True:
        new_patterns = defaultdict(int)
        # For each frequent pattern of length k
        for pattern in [p for p in patterns if len(p) == k]:
            # Find all possible extensions
            extensions = defaultdict(set)
            for seq_id, seq in enumerate(sequences):
                # Find first occurrence of pattern in sequence
                for i in range(len(seq) - k + 1):
                    if tuple(seq[i:i+k]) == pattern:
                        if i + k < len(seq):
                            next_word = seq[i + k]
                            extensions[next_word].add(seq_id)
                        break  # Only count once per sequence
            
            # Add extensions that meet support
            for word, seq_ids in extensions.items():
                if len(seq_ids) >= min_support:
                    new_pattern = pattern + (word,)
                    new_patterns[new_pattern] = len(seq_ids)
        
        if not new_patterns:
            break
            
        patterns.update(new_patterns)
        k += 1
    
    # Sort patterns by length, then by support (descending), then lexicographically
    sorted_patterns = sorted(patterns.items(),
                           key=lambda x: (len(x[0]), -x[1], x[0]))
    
    # Write output file
    with open('patterns.txt', 'w') as f:
        for pattern, support in sorted_patterns:
            f.write(f"{support}:{';'.join(pattern)}")
            print(f"{support}:{';'.join(pattern)}")
