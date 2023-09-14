\version "2.21.80"
\pointAndClickOff

\include "anacarolina-violin.ily"
\include "anacarolina-viola.ily"
\include "anacarolina-violoncello.ily"

\header {
  dedication = \markup { \italic "A mi amada sobrina, en memoria" }
  title = "Ana Carolina"
  subtitle = "Juego de dados para trío de cuerdas"
  composer = "Pablo Herrera"
  instrument = "Partitura general"
  copyright = "©2023 Pablo Herrera - Todos los derechos reservados."
  tagline = ""
}


global = {
  \override Score.BarNumber.break-visibility = #end-of-line-invisible
  \override Score.BarNumber.font-size = #2
  \override Score.BarNumber.stencil = #(make-stencil-boxer 0.1 0.25 ly:text-interface::print)
  \override Score.BarNumber.self-alignment-X = #-1
  \set Timing.defaultBarType = "||"
}

trio = \new GrandStaff <<
  \override Score.MetronomeMark.stencil = ##f
  \set Score.barNumberVisibility = #all-bar-numbers-visible
  \new Staff { \bar "" \violin }
  \new Staff { \viola }
  \new Staff { \violoncello }
>>


\markup {
  \column {
    \vspace #2
    \fill-line {
      \justify  {\concat{\italic {Ana Carolina},} parte del proyecto \concat{\bold{Soy Legión},}
                 es un sistema generador de piezas en Re menor para trío de cuerdas
                 (violín, viola, violoncello), basado en el lanzamiento de dados
                 para definir, según la tabla que a continuación presentamos, qué
                 compases deben conformar una pieza producida por este sistema.
                 Cada trío constará de dieciséis compases, por lo que se hace
                 necesario lanzar un dado esa misma cantidad de veces, anotando en
                 cada ocasión el compás que en suerte haya tocado. \lower #5 {\null}
      }
    }
    \fill-line {
      \right-column {\hspace #3 }
      \right-column {\hspace #1 \hspace #1 \hspace #1 \hspace #1 \rotate#90 {\bold "Dado"} }
      \center-column {\bold {"Compás: " \hspace #1 1 2 3 4 5 6 }}
      %\right-column {\hspace #1 }
      \right-column {\bold c01 \hspace #1 22 79 39 50 84 11 }
      \right-column {\bold c02 \hspace #1 61 33 8 93 37 73 }
      \right-column {\bold c03 \hspace #1 57 46 81 15 59 25 }
      \right-column {\bold c04 \hspace #1 13 47 90 34 76 55 }
      \right-column {\bold c05 \hspace #1 44 1 77 94 3 63 }
      \right-column {\bold c06 \hspace #1 68 51 19 64 18 91 }
      \right-column {\bold c07 \hspace #1 26 41 66 4 43 70 }
      \right-column {\bold c08 \hspace #1 82 16 80 62 87 30 }
      \right-column {\bold c09 \hspace #1 9 60 40 23 74 96 }
      \right-column {\bold c10 \hspace #1 71 85 27 52 17 6 }
      \right-column {\bold c11 \hspace #1 35 24 56 12 95 69 }
      \right-column {\bold c12 \hspace #1 20 75 5 92 31 58 }
      \right-column {\bold c13 \hspace #1 49 72 86 28 36 14 }
      \right-column {\bold c14 \hspace #1 53 10 89 32 78 38 }
      \right-column {\bold c15 \hspace #1 65 29 48 88 2 21 }
      \right-column {\bold c16 \hspace #1 7 83 42 67 54 45 }
      \right-column {\hspace #3 }
    }
    \fill-line {
      \justify {
        \vspace #2
        Este juego está provisto con una plantilla que el jugador
        puede utilizar para anotar las composiciones que 
        \italic{Ana Carolina} es capaz de generar. Tal plantilla
        ya tiene impresos los signos de armadura de clave,
        indicador de compás, indicación de \italic{tempo} y
        barras de repetición.
      }
    }
    \vspace #3
  }
}

#(set-global-staff-size 20 )
\score {
  << \trio \global >>
  \layout {
     indent = 0\cm
  }
}

\paper {
  oddHeaderMarkup = \markup {
    \fill-line {
      " "
      \justify {
        \on-the-fly #not-first-page \bold \fromproperty #'header:instrument
        \on-the-fly #not-first-page " - "
        \on-the-fly #not-first-page \italic \fromproperty #'header:title
      }
      \on-the-fly #print-page-number-check-first \fromproperty #'page:page-number-string
    }
  }
  evenHeaderMarkup = \markup {
    \fill-line {
      \on-the-fly #print-page-number-check-first \fromproperty #'page:page-number-string
      \justify {
        \on-the-fly #not-first-page \bold \fromproperty #'header:instrument
        \on-the-fly #not-first-page " | "
        \on-the-fly #not-first-page \italic \fromproperty #'header:title
      }
      " "
    }
  }
}