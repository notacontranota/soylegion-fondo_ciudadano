\version "2.21.80"

violin = {
  \clef "treble" \key c \major \time 3/4
  %compás 1
  c''4 (  b'8  g'8 )  d''4
  g'8. (  a'16  b'8.  c''16 ) d''8. (  c''16 )
  c'4 \acciaccatura {  d'8  e'8  f'8 } e'4 r4
  g''4 ( -\p \acciaccatura {  e''8  f''8 } e''4 )  c''4
  %compás 5
  g'8 ( -\markup{ \small\italic {cresc.} }  a'16 b'16  c''16  d''16  e''16 f''16 )  fis''8 (  g''8 )
  c''4 -\f  c'4 -\p r4
  c''4 ( -\markup{ \small\italic {cresc.} }  e''4 ) \acciaccatura {  a''8  g''8  f''8 }  g''4
  g'2  a'8 (  b'8 )
  a'4 -\p  a'16 (  b'16  a'16  b'16 \acciaccatura {  c''8  d''8 }  c''4 )
  %compás 10
  f'4 ( \acciaccatura {  a'8  b'8 }  a'4 ) \acciaccatura {  a'8  b'8 }  a'4
  d''8. (  a'16  f'8  a'8 ) \acciaccatura {  d''8  e''8 }  d''4
  c''4  c''4 \acciaccatura { c''8  d''8 }  c''4
  g'8 ( -\markup{ \small\italic {cresc.} }  a'16 b'16  c''16  d''16  e''16 f''16 )  fis''8 (  g''8 )
  g'4 \acciaccatura {  a'8  g'8  f'8 } g'4 r4
  %compás 15
  c'8 (  d'16  e'16  f'16  g'16 a'16  b'16 ) \acciaccatura { c''8  d''8 }  c''4
  c''4 -\f  c'4 -\p r4
  c''8. (  b'16  d'8.  g'16 ) d''8. (  c''16 )
  c''4 (  b'16  c''16  b'16 c''16 )  d''8 (  c''8 )
  c''4 -\f  c'4 -\p r4
  %compás 20
  g'8. ( -\markup{ \small\italic {cresc.} }  a'16 g'4 ) \acciaccatura { d''8  e''8  f''8 }  g''4
  f'4 (  g'16  a'16  g'16  a'16 ) \acciaccatura {  a'8  b'8 }  a'4
  f'8. ( -\<  g'16  a'8.  b'16 ) \acciaccatura {  c''8 (  d''8 }  c''8. d''16 ) -\!
  c'8. (  e'16 ) \acciaccatura {  g'8  a'8 }  g'4 r4
  c''4 -\f  c'4 -\p r4
  %compás 25
  g'4 ( -\markup{ \small\italic {cresc.} }  c''4 )  g''4
  e'4. ( -\p  d'8 )  e'8. (  f'16 )
  f'8. (  a'16  g'8  f'8 ) \acciaccatura {  e'8 (  f'8 }  e'8  d'8 )
  f'8. ( -\<  g'16 \acciaccatura { a'8 b'8 }  a'8  c''8 )  b'8.\trill (  a'32 b'32 ) -\!
  c''4 -\f  c'4 -\p r4
  %compás 30
  f'4 (  f''4 ) \acciaccatura { f''8 g''8 }  f''4
  a'8. ( -\p  c''16  b'8  a'8 ) \acciaccatura {  g'8 (  a'8 }  g'8  f'8 )
  c''4 -\f  c'4 -\p r4
  f'4. (  a'8 ) \acciaccatura { g'8 ( a'8 }  g'8.  f'16 )
  e'2 -\p  f'8 (  fis'8 )
  %compás 35
  c''4 -\f  c'4 -\p r4
  a''4 ( -\p \acciaccatura {  f''8  g''8 } f''4 )  c''4
  c''4  c''4  c''4
  e'4 ( -\p  d'16  e'16  d'16  e'16 )  f'8 (  fis'8 )
  \acciaccatura {  f''8 (  g''8 }  f''8. -\< e''16  d''8  c''8 )  b'8.\trill ( a'32  b'32 ) -\!
  %compás 40
  g'4. (  b8 )  d'8 (  g'8 )
  f''8 ( -\<  b'16  c''16 \acciaccatura { d''8  e''8 }  d''8.  c''16 ) b'8.\trill (  a'32  b'32 ) -\!
  g'8. ( -\markup{ \small\italic {cresc.} }  a'16  b'8  c''8 )  d''8 (  e''8 )
  c''8. ( -\p  g'16 )  e'4 r4
  f'4 (  a'8  d''8 ) \acciaccatura { f''8  g''8 }  f''4
  %compás 45
  g'4. (  b'8 )  d''8 (  g''8 )
  c''4 -\f  c'4 -\p r4
  d''4  a'16 (  b'16  a'16  b'16 \acciaccatura {  a'8  b'8 }  a'4 )
  e'4 -\p  e'4  e'4
  g'4 \acciaccatura {  a'8  g'8  f'8 } g'4 r4
  %compás 50
  a'8. ( -\p  c''16  f''8  e''8 ) \acciaccatura {  d''8 (  e''8 }  d''8 c''8 )
  g'8.  g'16  g'4 r4
  f''8 ( -\<  e''16  d''16  c''4 )  b'8.\trill (  a'32  b'32 ) -\!
  f''4. ( -\<  d''8 ) \acciaccatura { e''8 (  f''8 }  e''8  d''8 ) -\!
  f'4 (  a'4 ) \acciaccatura { c''8  d''8 }  c''4
  %compás 55
  c''4 -\f  c'4 -\p r4
  a'4. ( -\p  c''8 )  b'8. (  a'16 )
  \acciaccatura {  c''8  d''8 }  c''4  c''8  c''8  c''8  c''8
  g'8. (  b'16 ) \acciaccatura { g''8  a''8 }  g''4 r4
  g'4 ( -\markup{ \small\italic {cresc.} }  c''8  e''8 ) \acciaccatura {  g''8  a''8 }  g''4
  %compás 60
  f'8. (  g'16  a'4 ) \acciaccatura { f''8  e''8  d''8 }  c''4
  c''4 ( -\markup{ \small\italic {cresc.} }  g'4 ) \acciaccatura {  g''8  a''8 }  g''4
  c''4 -\f  c'4 -\p r4
  f'8. ( -\<  g'16 \acciaccatura { a'8 b'8 }  a'8  c''8 )  b'8.\trill (  a'32  b'32 ) -\!
  g'8. (  a'16  b'8.  c''16 ) d''8. (  e''16 )
  %compás 65
  \acciaccatura {  f''8 (  g''8 }  f''8. -\< e''16  d''8  c''8 )  b'8.\trill ( a'32  b'32 ) -\!
  a'4 -\p  a'4  a'4
  f'4  d''16 (  e''16  d''16 e''16 \acciaccatura {  f''8  g''8 } f''4 )
  d''4 (  a'4 ) \acciaccatura { f'8 g'8 }  f'4
  c''8 (  g'16  a'16  b'16 c''16  d''16  e''16 ) \acciaccatura { f''8 g''8 }  f''4
  %compás 70
  d''4 (  a'4 ) \acciaccatura { f'8 g'8 }  f'4
  c''4 (  c'4 ) \acciaccatura { a'8 b'8 }  a'4
  f'4  f'4  f'4
  c''8. ( -\markup{ \small\italic {cresc.} }  b'16 g'4 ) \acciaccatura { a''8  g''8  f''8 }  g''4
  c''4 -\f  c'4 -\p r4
  %compás 75
  \acciaccatura {  c''8  d''8 }  c''4 b'8  b'8  d''8 (  g''8 )
  f''4 ( -\< \acciaccatura {  d''8  e''8 } d''4 )  b'8.\trill (  a'32  b'32 ) -\!
  g'8. (  b'16 )  e''4 r4
  g'4 ( -\markup{ \small\italic {cresc.} }  e''4 ) g''4
  d''4 (  f''4 ) \acciaccatura { a''8 b''8 }  a''4
  %compás 80
  f''4 ( -\<  d''16  e''16  d''16 e''16 ) \acciaccatura {  d''8 (  e''8 } d''8  b'8 ) -\!
  c''4 \acciaccatura { c''8  b'8  a'8 }  g'4 r4
  c''4. (  d''8 )  f''8 (  a''8 )
  f'4 (  a'4 ) \acciaccatura { a'8  b'8 }  a'4
  f''8. ( -\<  g''16 \acciaccatura { f''8 g''8 }  f''4 )  b'8.\trill (  a'32 b'32 ) -\!
  %compás 85
  f''8. ( -\<  e''16 \acciaccatura { d''8 e''8 }  d''8.  c''16 )  b'8.\trill ( a'32  b'32 ) -\!
  g'4 \acciaccatura {  a'8  g'8  f'8 } g'4 r4
  g'8. (  b'16 ) \acciaccatura { e''8 f''8 }  e''4 r4
  c''8. ( -\markup{ \small\italic {cresc.} }  b'16 g'4 ) \acciaccatura { a''8  g''8  f''8 }  g''4
  g'4 \acciaccatura {  c''8  d''8 } c''2
  %compás 90
  g'4 (  b'4 )  e''4
  f'4 (  a'4 ) \acciaccatura { f'8  g'8 }  f'4
  c'4 (  a'4 )  c''4
  g'8. ( -\markup{ \small\italic {cresc.} }  a'16 g'4 )  g''4
  c''8. (  b'16 ) \acciaccatura { b'8 c''8 }  b'4 r4
  %compás 95
  f'8. (  g'16  a'8  b'8 ) \acciaccatura {  c''8 (  d''8 }  c''8  d''8 )
  c''4 -\f  c'4 -\p r4
}
