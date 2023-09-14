\version "2.21.80"

viola = {
  \clef "alto" \key c \major \time 3/4
  %compás 1
  d'8.  d'16  d'8.  d'16 \acciaccatura {  c'8  d'8 }  c'8.  b16
  e'4 \acciaccatura {  g8  a8 }  g4 r4
  a4  c'4 r4
  e'4 ( -\p  c'4 )  e'4
  %compás 5
  c'8. ( -\markup{ \small\italic {cresc.} }  d'16 e'8.  d'16 )  e'4
  e'4 -\f  e4 -\p r4
  g8. ( -\markup{ \small\italic {cresc.} }  d'16 c'8.  d'16 )  e'4
  d'8. (  c'16 \acciaccatura { b8 c'8 }  b4 )  d'4
  c'4 -\p  c'16 (  d'16  c'16 d'16  c'4 )
  %compás 10
  a4 (  c'4 )  c'8 (  d'8 )
  a2  a4
  f'2.
  c'8. ( -\markup{ \small\italic {cresc.} }  d'16 e'8.  d'16 )  c'4
  d'4  b4 r4
  %compás 15
  a2.
  << { \textLengthOn \parenthesize e'4_\f^\markup { \italic \magnify #0.6 "cercana a la anterior"}^\markup { \italic \magnify #0.6 "Tocar la nota más" } } \\ { \parenthesize e4 } >> c_\p r
  d'4  b4 r4
  f'4 (  g'16  a'16  g'16 a'16 )  f'8 (  e'8 )
  e'4 -\f  e4 -\p r4
  %compás 20
  c'4 ( -\markup{ \small\italic {cresc.} }  e'8. d'16 )  e'4
  a4 (  b16  c'16  b16  c'16 ) c'8. (  d'16 )
  a8. ( -\<  g16  f4 )  g4 -\!
  c'4  e'4 r4
  e'4 -\f  e4 -\p r4
  %compás 25
  c'8. ( -\markup{ \small\italic {cresc.} }  d'16 \acciaccatura {  e'8  f'8 }  e'8  f'8 )  e'4
  g4. ( -\p  b8 )  c'8. (  d'16 )
  a2  a4
  a8. ( -\<  g16  f4 )  g4 -\!
  e'4 -\f  e4 -\p r4
  %compás 30
  a8. (  b16  c'8.  b16 )  c'8. (  d'16 )
  c'2 -\p  c'4
  e'4 -\f  e4 -\p r4
  a8. (  b16  c'4 )  b4
  c'4 -\p  d'2
  %compás 35
  << { \textLengthOn \parenthesize e'4_\f^\markup { \italic \magnify #0.6 "cercana a la anterior"}^\markup { \italic \magnify #0.6 "Tocar la nota más" } } \\ { \parenthesize e4 } >> c_\p r
  a4 ( -\p  c'4 )  f'4
  c'4 (  e'4 ) \acciaccatura { e'8 f'8 }  e'4
  c'4 ( -\p  b16  c'16  b16  c'16 )  d'4
  d'8. -\<  b16  b8.  b16 d'4 -\!
  %compás 40
  d'4  e'4 r4
  d'4 ( -\<  b4 )  d'4 -\!
  c'4 -\markup{ \small\italic {cresc.} }  c'2
  e'2 -\p r4
  d'8. (  e'16  d'8  c'8 ) b8 (  a8 )
  %compás 45
  d'4  b4 r4
  e'4 -\f  e4 -\p r4
  a4  f'16 (  g'16  f'16 g'16  f'4 )
  c'2 -\p  e'4
  c'4  b4 r4
  %compás 50
  c'2. -\p
  d'8.  c'16 \acciaccatura { b8  c'8 }  b4 r4
  d'4 ( -\<  c'8  d'16  e'16 ) d'4 -\!
  b8. ( -\<  c'16  d'8.  c'16 ) b8 (  c'16  d'16 ) -\!
  a8 (  b8 ) \acciaccatura {  c'8  d'8 } c'2
  %compás 55
  << { \textLengthOn \parenthesize e'4_\f^\markup { \italic \magnify #0.6 "cercana a la anterior"}^\markup { \italic \magnify #0.6 "Tocar la nota más" } } \\ { \parenthesize e4 } >> c_\p r
  c'4. ( -\p  a8 )  b8. (  c'16 )
  f'8. (  e'16  d'4 )  e'4
  d'2 r4
  c'8. ( -\markup{ \small\italic {cresc.} }  d'16 c'8  b8 )  a8 (  g8 )
  %compás 60
  a4  a4 (  c'4 )
  c'8. ( -\markup{ \small\italic {cresc.} }  d'16  e'8.  d'16 )  c'4
  << { \textLengthOn \parenthesize e'4_\f^\markup { \italic \magnify #0.6 "cercana a la anterior"}^\markup { \italic \magnify #0.6 "Tocar la nota más" } } \\ { \parenthesize e4 } >> c_\p r
  d'8. ( -\<  c'16  b8.  c'16 ) d'8.\trill (  c'32  d'32 ) -\!
  d'4 \acciaccatura {  g8  a8 }  g4 r4
  %compás 65
  b8. -\<  b16  b8.  b16  d'4 -\!
  c'4 -\p  c'4  c'4
  a4 (  f4 )  a8 (  b8 )
  a4 (  f'4 )  d'4
  d'2.
  %compás 70
  a8 (  b8 ) \acciaccatura {  c'8  d'8 } c'2
  f'4 (  f4 )  f'4
  a4  a4  a4
  c'4 -\markup{ \small\italic {cresc.} }  e'2
  << { \textLengthOn \parenthesize e'4_\f^\markup { \italic \magnify #0.6 "cercana a la anterior"}^\markup { \italic \magnify #0.6 "Tocar la nota más" } } \\ { \parenthesize e4 } >> c_\p r
  %compás 75
  d'8. (  b16  g8.  f'16 ) \acciaccatura {  e'8 (  f'8 }  e'8. d'16 )
  b4 -\<  b4 (  d'4 ) -\!
  c'8. (  d'16 ) \acciaccatura { b8 c'8 }  b4 r4
  c'8 ( -\markup{ \small\italic {cresc.} }  d'8 \acciaccatura {  c'8  d'8 }  c'8  d'8 )  e'4
  a8. (  b16  c'8.  b16 )  c'8. ( a16 )
  %compás 80
  b4 ( ~ -\<  b16  c'16  b16  c'16 )  b8 (  d'8 ) -\!
  d'4  d'4 r4
  f'8. (  e'16  d'4 )  c'4
  a4 (  f4 )  f4
  b8. ( -\<  c'16  d'8.  e'16 ) f'8. (  g'16 ) -\!
  %compás 85
  b8. ( -\<  c'16  b8.  c'16 ) d'4 -\!
  c'4  c'4 r4
  e'2 r4
  c'4 -\markup{ \small\italic {cresc.} }  c'4 ( e'4 )
  c'8. (  b16  a8.  f'16 ) \acciaccatura {  e'8 (  f'8 }  e'8. c'16 )
  %compás 90
  e'8. (  b16 ) \acciaccatura { g8 a8 }  g4 r4
  a2.
  c'8. (  a16 ) \acciaccatura { c'8  d'8 }  c'4 r4
  c'4 ( -\markup{ \small\italic {cresc.} }  e'8. d'16 )  e'8. (  c'16 )
  d'4  d'4 r4
  %compás 95
  a2  c'4
  << { \textLengthOn \parenthesize e'4_\f^\markup { \italic \magnify #0.6 "cercana a la anterior"}^\markup { \italic \magnify #0.6 "Tocar la nota más" } } \\ { \parenthesize e4 } >> c_\p r
}
