#### 2D Plot with Gnuplot Lines

set terminal cairolatex standalone

set title   'Title' font 'CMU-Serif'
set xlabel  'X-Label $x$' font 'CMU-Serif'
set ylabel  'Y-Label' font 'CMU-Serif'
set xrange  [-0.1: 4.1]
set yrange  [-0.1: 2.1]
set xtics   0.0,0.5,4.0 font 'CMU-Serif'
set ytics   0.0,0.5,4.0 font 'CMU-Serif'
set key     font 'CMU-Serif'
set output  '2DLines.tex'

plot    '../Data/data00.dat'    using 1:2 with lines linecolor '#F0140A' linewidth 2 title 'Function 1',\

set output

system 'pdflatex 2DLines.tex'
system 'start 2DLines.pdf'
system 'rm *.aux *.log *.tex *-inc.eps *-to.pdf'