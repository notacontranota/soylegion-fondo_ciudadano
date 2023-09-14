\version "2.21.80"

violoncello = {
  \clef "bass" \key f \major \time 6/8
  %compás 1
  bes,4. _\f  bes,4.
  a,16 ( _\f  bes,16  a,16 )  a,16 ( bes,16  a,16 )  a,16 (  bes,16 a,16 )  a,16 (  bes,16  a,16 )
  bes,8. _\f  c8.  d4.
  c8  c,4  c8  c,4
  %compás 5
  d4. r4.
  g,4.  g,4.
  d,2. _\f
  g,4.  g16  f16  e16  d16 c16  bes,16
  d4 ~ _\mf  d16  d16  d4 ~ d16  g,16
  %compás 10
  a8  a,4  a8  g,4
  d4. _\mf  d8 (  cis8  d8 )
  a,4.  cis16 (  d16  e16 a16  g16  e16 )
  d4 _\>  a8  d4. _\!
  g8. _\markup{ \italic {cresc.} }  e8. e8.  g8.
  %compás 15
  a,4 _\<  bes,8  cis4. _\!
  f,4.  f,4.
  g,8.  e,8.  g,4.
  c16 (  d16  c16  d16  c16 d16 )  c16 (  d16  c16  d16 c16  d16 )
  c4.  c8.  c,8.
  %compás 20
  d4.  d'4.
  a16 ( _\f  g16  e16  d16 cis16  b,16 )  a,8.  a,8.
  d4 _\mf  d'8  d4  d'8
  r4  f8 _\mf  d4.
  a,4  bes,8  cis4.
  %compás 25
  a,8. _\<  bes,8.  cis8.  cis8. _\!
  c,2.
  g,16  f,16  g,16  a,16  bes,16 e16  g4.
  g8. _\markup{ \italic {cresc.} }  fis16 ( g16  a16 )  g8.  bes16 ( a16  g16 )
  a,16 ( _\f  bes,16  a,4 )  a,16 ( bes,16  a,4 )
  %compás 30
  f,8  a,8  c8  f4.
  d4.  d,4.
  a16 ( ->  bes16  a4 )  a16 ( -> bes16  a4 )
  r8  g,4 r8  g,4
  << {\stemDown d2.} \\{ s2_\> s8 s _\!} >>
  %compás 35
  a8  g,4  cis'8  cis4
  g4 ~ _\markup{ \italic {cresc.} }  g16 g16  g4.
  g8  g,4  g8  g,4
  <a, d>4 r8  <a, d>4 r8
  r8  <d a>4 _\mf r8  <d a>4
  %compás 40
  d4 _\mf  e8  f4  d8
  c,4 (  e,8 )  c,4 (  e,8 )
  d16 ( _\>  cis16  d16 )  e16 f16  a16  d'4. _\! _\p
  c,4.  c,4.
  r4  bes,8 _\f r4  bes,8
  %compás 45
  d2. _\f
  a,4 _\<  a,8  cis4  cis8 _\!
  d8 _\>  a,8  f,8  d,4. _\!
  a16 ( _\f  e16  d16  cis16 b,16  a,16 )  a16 (  e16 d16  cis16  b,16  a,16 )
  g,16 ( _\markup{ \italic {cresc.} }  a,16 bes,16  c16  d16  e16 )  g16 ( f16  e16  f16  g16 bes16 )
  %compás 50
  d4. _\mf  f,4.
  c2. \trill
  g,4.  g,16 (  a,16  bes,16  a,16 g,16  e,16 )
  a4  a,8 ~  a,8  a4
  d8. _\f  d,16 _\p  d,8  d,4.
  %compás 55
  d4. _\>  d16 (  cis16  d4 ) _\!
  a,8.  a,8.  cis8.  cis8.
  a,4. _\<  cis4. _\!
  d4.  d,4.
  a,4 _\<  e8  cis4  e8 _\!
  %compás 60
  d16 _\mf  f16  e16  d16 c16  bes,16  a,16  a16 g16  f16  e16  d16
  g,16  a,16  bes,16  c16  e16 d16  g16  f16  e16  d16 c16  bes,16
  f,2.
  bes,8. _\f  bes,16  c8  d8. c16  d8
  c8.  c,8.  c,8.  c8.
  %compás 65
  a,8. _\f  a,16  bes,8  a,8.  a,16 bes,8
  c,8  c,8  c,8  c,8  c,8 c,8
  d8. _\f  d8.  d,4.
  c8  c'4  c8  c'4
  a,8.  a,8.  cis,8.  cis8.
  %compás 70
  c16 (  bes,16  a,16  g16 f16  e16 )  d16 (  c16  bes,16 a,16  g,16  c,16 )
  g,8  g4  g,8  g4
  g16 ( _\markup{ \italic {cresc.} }  f16 e16  d16  bes,16  a,16 )  g,8. g8.
  r8  g,8  g,8 r8  g,8  g,8
  d,4. _\mf  f,8  a,8  d8
  %compás 75
  d2.
  d16 ( _\>  cis16  d16  e16 ) f16  a16  d'4. _\!
  bes,16 ( _\f  c16  bes,16  a,16 bes,16  c16 )  d4.
  a2. \trill
  d4. _\mf  d16  e16  d16  c16 bes,16  a,16
  %compás 80
  f,4 ~  f,16  f,16  f,4 r8
  a,4 _\<  e8  cis4  a,8 _\!
  f,4  f8  f,4.
  d4. _\f  d,4. _\p
  d16 ( _\mf  e16  d4 )  d16 ( e16  d4 )
  %compás 85
  g,4 ~  g,16  g,16  g,8.  e,8.
  g2. \trill _\markup{ \italic {cresc.} }
  f,4.  f,4.
  a,4 ~ _\f  a,16  a,16  a,4.
  a8.  a,16  a,8  a8. a,16  a,8
  %compás 90
  d8. ( _\>  d8. )  d4. _\!
  c16  a,16  f,16  c,16  f,16 a,16  c16  a,16  f,16  c,16 f,16  a,16
  d4.  d'4.
  g,8.  g,16  g8  g,8.  g,16 g8
  bes,4 _\f  a,8  bes,4.
  %compás 95
  a,16 (  bes,16  a,4 )  cis16 ( d16  cis4 )
  r4  cis'8 _\mf  d'4  d8
}
