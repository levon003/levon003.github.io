#!/bin/bash
# this script doesn't work (although it works in Overleaf)
# not sure why it doesn't
# see: https://tex.stackexchange.com/questions/171793/bibtex-to-html-markdown-etc-using-pandoc

BIBTEX_FILEPATH="gaied_sources.bib"

cat <<EOF > "sources.tex"
\documentclass{article}
\usepackage{biblatex}
\bibliography{${BIBTEX_FILEPATH}}

\begin{document}
\nocite{*}
\printbibliography
\end{document}
EOF

pandoc sources.tex -o sources.md

#--bibliography "${BIBTEX_FILEPATH}"
echo "Finished."