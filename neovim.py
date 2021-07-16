#!/usr/bin/python3

import os.path
# import cProfile
from neovimh2h import NeoVimH2H
SECTION_BEGIN = r"""\addcontentsline{toc}{%s}{%s}
\markright{%s}
\begin{Verbatim}[commandchars=\\\{\},formatcom=\fixurl]
"""

CHAPTER_BEGIN = r"""\addcontentsline{toc}{%s}{%s}
\phantomsection{}
"""

SECTION_END = """
\\end{Verbatim}
\\cleardoublepage\\phantomsection{}
"""

DOC_END = r"""
\addcontentsline{toc}{%s}{About this pdf}
\markright{about this pdf}
"""

def main():
    print("Processing tags...")
    with open(os.path.join('doc', 'tags'), 'r') as input_file:
        h2h = NeoVimH2H(input_file.read())
    with open('contents.txt', 'r') as input_file:
        contents = input_file.read().split('\n')

    with open('body.tex', 'w') as output_file:
        level = "chapter"
        for row in contents:
            split_row = row.strip().split(None, 1)
            if len(split_row) != 2:
                continue
            filename, title = split_row
            if filename == "#":
                output_file.write(CHAPTER_BEGIN % ("chapter", title))
                level = "section"
                continue
            if filename == "##":
                output_file.write(CHAPTER_BEGIN % ("section", title))
                level = "subsection"
                continue

            print("Processing " + filename + "...")
            output_file.write(SECTION_BEGIN % (level, title, filename.replace('_', r'\_')))

            with open(os.path.join('doc', filename), 'r') as input_file:
                text = input_file.read()
            output_file.write(h2h.to_tex(filename, text))
            output_file.write(SECTION_END)

        output_file.write(DOC_END % level)

main()
# cProfile.run('main()')
