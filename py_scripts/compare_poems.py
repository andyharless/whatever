"""
Script to compare the lines of two poems to see if the first
is a correct transcription of the second
"""

POEM1 = '/home/andy/temp_poem1.txt'
POEM2 = '/home/andy/temp_poem2.txt'

LINE_NUMBER_MARKER = '<-'

POEM1_HEADER_LINES = 0
POEM2_HEADER_LINES = 2

replaces = {    # Punctuation &c that is allowed to differ
        '.': '',
        ',': '',
        ';': '',
        '’': "'",
        '—': ' ',
        ':': ''
        }
        

def do_replaces(t):
    """Replace stuff that is allowed to differ"""
    t = t.lower()
    for old, new in replaces.items():
        t = t.replace(old, new)
    return t
    
def do_all_replaces(lines):
    """Process poem for comparison"""
    result = []
    for line in lines:
        if not line.startswith(LINE_NUMBER_MARKER):
            result.append(do_replaces(line).strip())
    return result

with open(POEM1) as p:
    poem1 = p.readlines()
    
with open(POEM2) as p:
    poem2 = p.readlines()

count = 0
for line1, line2 in zip(
                       do_all_replaces(poem1[POEM1_HEADER_LINES:]),
                       do_all_replaces(poem2[POEM2_HEADER_LINES:])
                       ):
 
    if line1:  # Blank lines don't count
        count += 1
 
    if line1 != line2:
        print(f'{count}\n{line1}\n{line2}\n')
