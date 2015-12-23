poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# Open for 'w'riting
with open('poem.txt', 'w') as f:
    # Write text to file
    f.write(poem)

# If no mode is specified,
# 'r'ead mode is assumed by default
with open('poem.txt') as f:
    for line in f:
        # The `line` already has a newline
        # at the end of each line
        # since it is reading from a file.
        print(line),
