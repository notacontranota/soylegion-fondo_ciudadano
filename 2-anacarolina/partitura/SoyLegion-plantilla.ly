\version "2.21.80"
\pointAndClickOff

\header {
  title = "Ana Carolina"
  subtitle = "Trío de cuerdas"
  subsubtitle = "Dados: [__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __]"
  composer = \markup { \caps "Pablo Herrera" }
  instrument = "Partitura general"
  dedication = \markup { "de" \italic "«Soy Legión»" }
  copyright = \markup {\with-url #"http://lecturayescrituramusical.blogspot.com/" {
    \center-column {
      \concat { \epsfile #0 #15 #"../recursos/soyfondo.eps"
      \epsfile #0 #15 #"../recursos/soyncn.eps" }
      \bold {"Fondo Ciudadano de Desarrollo Cultural & Nota contra Nota"}
      "http://lecturayescrituramusical.blogspot.com/"
      \null
      }
    }
  }
  tagline = ##f
}
\layout  {
  indent = 3\cm
}


trio = \new StaffGroup <<
  \new Staff \with {
    instrumentName = \markup { \caps "Violín" }
  }{
    \clef treble
    \key d \minor
    \time 6/8
    \tempo "Lento"
    \repeat volta 2 {
      s2.*4 \break
      s2.*4 \break
    }
    \repeat volta 2 {
      s2.*4 \break
      s2.*4
    }
  }
  \new Staff \with {
    instrumentName = \markup { \caps "Viola" }
  }{
    \clef alto
    \key d \minor
    \time 6/8
    s2.*16
  }
  \new Staff \with {
    instrumentName = \markup { \caps "Violoncello" }
  }{
    \clef bass
    \key d \minor
    \time 6/8
    s2.*16
  }
>>

\markup { \vspace #1 }
\new Score \with {
  \override SpacingSpanner #'uniform-stretching = ##t
} { \trio }
