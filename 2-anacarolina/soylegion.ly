%Generado automáticamente por 'soylegion.py'
%para el juego "Ana Carolina", de Pablo Herrera.
\version "2.22.0"
\pointAndClickOff

global = {
  \key d \minor
  \time 6/8
  \tempo "Lento"
  \repeat volta 2 {
    s2.*8
  }
  \repeat volta 2 {
    s2.*8
  }
}

violin = {
  a'8. _\mf  a'16  bes'8  a'8.  a'16 bes'8
  bes'16 (  a'16  bes'4 )  bes'16 ( a'16  bes'4 )
  a'16 ( _\<  bes'16  a'16  bes'16 a'16  bes'16 )  g'16 (  a'16  g'16 a'16  g'16  a'16 ) _\!
  f'16 ( _\>  g'16  f'16  g'16  f'16 g'16 )  f'4. _\!
  d''16 ( _\f  e''16  d''4 ) f''16 (  g''16  f''4 )
  f''8.  f''16  g''8  f''8. f''16  g''8
  e''2. \trill
  f''4 ~  f''16  f'16  f'4 r8
  e''4. _\mf  d''8.  a'8.
  bes'8.  e''16 (  d''16  c''16 ) a'8 (  bes'16 ) g'16 (  a'16 bes'16 )
  r8  a'4 -> r8  g'4 ->
  r8  g'4 -> r8  f'4 ->
  e''4 _\markup{ \italic {cresc.} }  f''8 ~ f''8  g''4
  d''8.  e''16 (  d''16  cis''16 )  d''8.  cis''16 (  d''16  e''16 )
  a''16 ( _\f  e''16  d''16 ) cis''8.  bes''16 (  e''16  d''16 ) cis''8.
  d''8. _\f  d'''16 _\p  d'''8 d'''4.
}
viola = {
  f'8 _\mf  f4  f'8  f4
  e'16  d'16  c'16  a16 c'16  d'16  e'4.
  cis'4. _\<  a4. _\!
  a16 ( _\>  bes16  a16  bes16  a16 bes16 )  a4._\!
  f'8. _\f  f'16 (  g'16  a'16 )  bes'16 (  a'16  g'16  f'16 a'16  bes'16 )
  a'4  g'8  a'4  bes'8
  bes'16 (  a'16  bes'4 )  bes'16 (  a'16  bes'4 )
  a'4 ~  a'16  a16  a4 r8
  r8  g'4 _\mf  g'8  f'4
  e'4  g'8  f'8 (  e'4 )
  cis'4 (  bes8 )  a4.
  r8  bes4 -> r8  bes4 ->
  bes'8 ( _\markup{ \italic {cresc.} }  a'8 ) bes'8  bes'8 (  a'8 )  bes'8
  f'8  f'4 ->  f'8  f'4 ->
  a'8. _\f  a'16 (  bes'16  a'16 )  g'8.  g'16 (  a'16  g'16 )
  f'8. _\f  d''16 _\p  d''8  d''4.
}

violoncello = {
  d4. _\mf  d16  e16  d16  c16 bes,16  a,16
  g,4.  g16  f16  e16  d16 c16  bes,16
  a,8. _\<  bes,8.  cis8.  cis8. _\!
  << {\stemDown d2.} \\{ s2_\> s8 s _\!} >>
  bes,16 ( _\f  c16  bes,16  a,16 bes,16  c16 )  d4.
  c16  a,16  f,16  c,16  f,16 a,16  c16  a,16  f,16  c,16 f,16  a,16
  c,8  c,8  c,8  c,8  c,8 c,8
  f,4 ~  f,16  f,16  f,4 r8
  r4  cis'8 _\mf  d'4  d8
  g,8.  e,8.  g,4.
  a,8.  a,8.  cis,8.  cis8.
  d4.  d,4.
  g,16 ( _\markup{ \italic {cresc.} }  a,16 bes,16  c16  d16  e16 )  g16 ( f16  e16  f16  g16 bes16 )
  a16 ( ->  bes16  a4 )  a16 ( -> bes16  a4 )
  a16 ( _\f  g16  e16  d16 cis16  b,16 )  a,8.  a,8.
  d8. _\f  d,16 _\p  d,8  d,4.
}

\bookpart {
  \header {
    dedication = \markup { \italic "de «Soy Legión»" }
    title = "Ana Carolina"
    subtitle = "(Trío de cuerdas)"
    subsubtitle = "Dados: [2, 3, 6, 4, 3, 6, 3, 3, 6, 5, 6, 6, 1, 4, 6, 5]"
    instrument = "Partitura general"
    composer = "Pablo Herrera"
    copyright = \markup {\with-url #"https://github.com/notacontranota/soylegion-fondo_ciudadano" {
      \center-column {
        \concat { \epsfile #0 #15 #"recursos/soyfondo.eps"
        "   "
        \epsfile #0 #15 #"recursos/soyncn.eps" }
        \bold {"Fondo Ciudadano de Desarrollo Cultural & Nota contra Nota"}
        "https://github.com/notacontranota/soylegion-fondo_ciudadano"
        \null
        }
      }
    }
    tagline = ""
  }

  \markup { \vspace #1 }
  #(set-global-staff-size 20)
  \score {
    \new StaffGroup <<
      \overrideTimeSignatureSettings 3/4 1/4 1,1,1 #'() %para dividir beats.
      \new Staff \with {
        instrumentName = \markup { \caps "Violín" }
        midiInstrument = "string ensemble 1"
        midiPanPosition = #-0.5
      }{
        \clef treble
        \accidentalStyle StaffGroup.modern-voice-cautionary
        << \global \compressMMRests {\violin} >>
      }
      \new Staff \with {
        instrumentName = \markup { \caps "Viola" }
        midiInstrument = "string ensemble 1"
        midiPanPosition = #0.5
      }{ 
        \clef alto 
        << \global \viola >>
      }
      \new Staff \with{
        instrumentName = \markup { \caps "Violoncello" }
        midiInstrument = "string ensemble 1"
        midiPanPosition = #0.0
      }{ 
        \clef bass
        << \global \violoncello >>
      }
    >>
    \layout {
      indent = 3\cm
      #(layout-set-staff-size 17 )
    }
    \midi {\tempo 4=60}
  }
}
%particellas
\bookpart {
  \header {
    dedication = \markup { \italic "de «Soy Legión»" }
    title = "Ana Carolina"
    subtitle = "(Trío de cuerdas)"
    instrument = "Violín, Flauta u Oboe"
    subsubtitle = "Dados: [2, 3, 6, 4, 3, 6, 3, 3, 6, 5, 6, 6, 1, 4, 6, 5]"
    composer = "Pablo Herrera"
    copyright = \markup {\with-url #"https://github.com/notacontranota/soylegion-fondo_ciudadano" {
      \center-column {
        \concat { \epsfile #0 #15 #"recursos/soyfondo.eps"
        "   "
        \epsfile #0 #15 #"recursos/soyncn.eps" }
        \bold {"Fondo Ciudadano de Desarrollo Cultural & Nota contra Nota"}
        "https://github.com/notacontranota/soylegion-fondo_ciudadano"
        \null
        }
      }
    }
    tagline = ""
  }

  \markup { \vspace #1 }
  \score {
    \new Staff {
      \overrideTimeSignatureSettings 3/4 1/4 1,1,1 #'() %para dividir beats.
      \accidentalStyle Staff.modern-cautionary
      \clef treble
      <<\global \compressMMRests{\violin}>>
    }
    \layout {
      indent = 0\cm
    }
  }
}

\bookpart {
  \header {
    dedication = \markup { \italic "de «Soy Legión»" }
    title = "Ana Carolina"
    subtitle = "(Trío de cuerdas)"
    instrument = \markup { \concat {"Viola o Clarinete en Si" \flat} }
    subsubtitle = "Dados: [2, 3, 6, 4, 3, 6, 3, 3, 6, 5, 6, 6, 1, 4, 6, 5]"
    composer = "Pablo Herrera"
    copyright = \markup {\with-url #"https://github.com/notacontranota/soylegion-fondo_ciudadano" {
      \center-column {
        \concat { \epsfile #0 #15 #"recursos/soyfondo.eps"
        "   "
        \epsfile #0 #15 #"recursos/soyncn.eps" }
        \bold {"Fondo Ciudadano de Desarrollo Cultural & Nota contra Nota"}
        "https://github.com/notacontranota/soylegion-fondo_ciudadano"
        \null
        }
      }
    }
    tagline = ""
  }

  \markup { \vspace #1 }
  \score {
    \new Staff {
      \overrideTimeSignatureSettings 3/4 1/4 1,1,1 #'() %para dividir beats.
      \accidentalStyle Staff.modern-cautionary
      \clef alto
      <<\global \compressMMRests{\viola}>>
    }
    \layout {
      indent = 0\cm
    }
  }

  \markup { \vspace #8 }
  \score {
    \new Staff {
      \overrideTimeSignatureSettings 3/4 1/4 1,1,1 #'() %para dividir beats.
      \accidentalStyle Staff.modern-cautionary
      \clef treble
      \transpose c d <<\global \compressMMRests{\viola}>>
    }
    \layout {
      indent = 0\cm
    }
  }
}

\bookpart {
  \header {
    dedication = \markup { \italic "de «Soy Legión»" }
    title = "Ana Carolina"
    subtitle = "(Trío de cuerdas)"
    instrument = "Violoncello o Fagot"
    subsubtitle = "Dados: [2, 3, 6, 4, 3, 6, 3, 3, 6, 5, 6, 6, 1, 4, 6, 5]"
    composer = "Pablo Herrera"
    copyright = \markup {\with-url #"https://github.com/notacontranota/soylegion-fondo_ciudadano" {
      \center-column {
        \concat { \epsfile #0 #15 #"recursos/soyfondo.eps"
        "   "
        \epsfile #0 #15 #"recursos/soyncn.eps" }
        \bold {"Fondo Ciudadano de Desarrollo Cultural & Nota contra Nota"}
        "https://github.com/notacontranota/soylegion-fondo_ciudadano"
        \null
        }
      }
    }
    tagline = ""
  }

  \markup { \vspace #1 }
  \score {
    \new Staff {
      \overrideTimeSignatureSettings 3/4 1/4 1,1,1 #'() %para dividir beats.
      \accidentalStyle Staff.modern-cautionary
      \clef bass
      <<\global \compressMMRests{\violoncello}>>
    }
    \layout {
      indent = 0\cm
    }
  }
}
      
