\version "2.22.0"
\pointAndClickOff

\include "minue-violin.ily"
\include "minue-viola.ily"
\include "minue-violoncello.ily"

\header {
  dedication = \markup { "de" \italic "«Soy Legión»"}
  title = "Minué"
  subtitle = "Juego de dados para trío de cuerdas"
  composer = \markup { "Germán Mercado" }
  instrument = "Partitura general"
  copyright = "©2023 Germán Mercado - Todos los derechos reservados."
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
  \overrideTimeSignatureSettings 3/4 1/4 1,1,1 #'() %para dividir beats.
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
      \justify  {\concat{\italic {Minué},} parte del proyecto \concat{\bold{Soy Legión},}
                 es un sistema generador de piezas en Do mayor para trío de cuerdas
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
      \right-column {\bold c01 \hspace #1 43 48 38 34 4 26 }
      \right-column {\bold c02 \hspace #1 58 14 51 8 64 45 }
      \right-column {\bold c03 \hspace #1 12 37 18 57 71 82 }
      \right-column {\bold c04 \hspace #1 69 81 94 1 17 75 }
      \right-column {\bold c05 \hspace #1 54 10 21 95 60 30 }
      \right-column {\bold c06 \hspace #1 78 93 13 42 88 61 }
      \right-column {\bold c07 \hspace #1 65 84 80 85 76 53 }
      \right-column {\bold c08 \hspace #1 19 24 46 29 6 32 }
      \right-column {\bold c09 \hspace #1 50 66 9 31 36 56 }
      \right-column {\bold c10 \hspace #1 87 49 77 90 2 40 }
      \right-column {\bold c11 \hspace #1 91 72 67 27 83 33 }
      \right-column {\bold c12 \hspace #1 15 3 23 92 86 89 }
      \right-column {\bold c13 \hspace #1 70 68 47 44 11 79 }
      \right-column {\bold c14 \hspace #1 25 20 5 59 73 7 }
      \right-column {\bold c15 \hspace #1 39 28 52 22 41 63 }
      \right-column {\bold c16 \hspace #1 55 35 74 96 62 16 }
      \right-column {\hspace #3 }
    }
    \fill-line {
      \justify {
        \vspace #2
        Este juego está provisto con una plantilla que el jugador
        puede utilizar para anotar las composiciones que 
        \italic{Minué} es capaz de generar. Tal plantilla
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