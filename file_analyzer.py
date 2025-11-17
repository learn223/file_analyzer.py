def read_file(file_contents):
    '''
        Reads the file
    '''
    with open(file_contents, "r") as file:
        data = file.readlines()
    return data


def read_total_lines(total_lines):
    '''
        1. Reads the file
        2. Calculates the total length of each of line
        3. Returns the total
    '''
    with open(total_lines, "r") as lfile:
        lines = lfile.readlines()
        total = len(lines)
    return total


def read_even_and_odd_num_lines(file_name):
    '''
        1. opens the file
        2. calculates the even and odd lines
        3. appends the words to its respective list (even_line and odd_line)
        4. Then returns the even and odd list
    '''
    even_line = []
    odd_line = []

    with open(file_name, "r") as in_file:
        for index, lst in enumerate(in_file, 1):
            if index % 2 == 0:
                even_line.append(lst)
            else:
                odd_line.append(lst)

    return even_line, odd_line


def average_num_word_per_line(file_name):
    '''
        Calculates the average number of words per line in the file
    '''
    with open(file_name) as average_file:
        lines = average_file.readlines()
        
        if len(lines) == 0:
            return 0
        
        total_words = 0
        for line in lines:
            words = line.split()
            total_words += len(words)
        
        average = total_words / len(lines)
        return average


def total_words(file_contents):
    '''
        This calculates the total words in the file content
    '''
    with open(file_contents) as file:
        text = file.read()
        word = text.split()
        total_words = len(word)
    return total_words


def reverse_file_contents(file_reverse, output_file="reversed.txt"):
    '''
        This reverses the file content and writes it to another file.
    '''
    with open(file_reverse, "r") as r_file:
        lines = r_file.readlines()
    
    # Write reversed lines to output file
    with open(output_file, "w") as out_file:
        for line in reversed(lines):
            out_file.write(line)
    
    return output_file


def save_summary(file_name, summary_file="summary.txt"):
    '''
        Generates a summary of file statistics and saves to summary.txt
    '''
    # Collect all statistics
    total_lines = read_total_lines("file.txt")
    even_lines, odd_lines = read_even_and_odd_num_lines("file.txt")
    avg_words = average_num_word_per_line("file.txt")
    total_word_count = total_words("file.txt")
    
    # Create summary text
    summary = f"""File Analysis Summary for: {"file.txt"} 
{'=' * 50}

Total Lines: {total_lines}
Even-numbered Lines: {len(even_lines)}
Odd-numbered Lines: {len(odd_lines)}
Total Words: {total_word_count}
Average Words per Line: {avg_words:.2f}

Even-numbered lines content:
{'-' * 50}
{''.join(even_lines)}

Odd-numbered lines content:
{'-' * 50}
{''.join(odd_lines)}
"""
    
    # Write to summary file
    with open(summary_file, "w") as s_file:
        s_file.write(summary)
    
    print(f"Summary saved to {summary_file}")
    return summary_file


# Example usage:
if __name__ == "__main__":
    # Uncomment to create test file
    # with open("file.txt", "w") as file:
    #     file.writelines([
    #         "A crust of bread and a corner to sleep in,\n",
    #         "A minute to smile and an hour to weep in,\n",
    #         "A pint of joy to a peck of trouble,\n",
    #         "And never a laugh but the moans come double;\n",
    #         "And that is life!"
    #     ])
    
    # Run analysis
    file_to_analyze = "file.txt"
    
    # Generate summary
    save_summary(file_to_analyze)
    
    # Reverse file
    reverse_file_contents(file_to_analyze, "reversed.txt")
    print("File reversed and saved to reversed.txt")