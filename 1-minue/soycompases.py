#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#módulo música de Ana Carolina
violin = [
  #compás 1
  "c''4 (  b'8  g'8 )  d''4",
  "g'8. (  a'16  b'8.  c''16 ) d''8. (  c''16 )",
  "c'4 \\acciaccatura {  d'8  e'8  f'8 } e'4 r4",
  "g''4 ( -\\p \\acciaccatura {  e''8  f''8 } e''4 )  c''4",
  #compás 5
  "g'8 ( -\\markup{ \\small\\italic {cresc.} }  a'16 b'16  c''16  d''16  e''16 f''16 )  fis''8 (  g''8 )",
  "c''4 -\\f  c'4 -\\p r4",
  "c''4 ( -\\markup{ \\small\\italic {cresc.} }  e''4 ) \\acciaccatura {  a''8  g''8  f''8 }  g''4",
  "g'2  a'8 (  b'8 )",
  "a'4 -\\p  a'16 (  b'16  a'16  b'16 \\acciaccatura {  c''8  d''8 }  c''4 )",
  #compás 10
  "f'4 ( \\acciaccatura {  a'8  b'8 }  a'4 ) \\acciaccatura {  a'8  b'8 }  a'4",
  "d''8. (  a'16  f'8  a'8 ) \\acciaccatura {  d''8  e''8 }  d''4",
  "c''4  c''4 \\acciaccatura { c''8  d''8 }  c''4",
  "g'8 ( -\\markup{ \\small\\italic {cresc.} }  a'16 b'16  c''16  d''16  e''16 f''16 )  fis''8 (  g''8 )",
  "g'4 \\acciaccatura {  a'8  g'8  f'8 } g'4 r4",
  #compás 15
  "c'8 (  d'16  e'16  f'16  g'16 a'16  b'16 ) \\acciaccatura { c''8  d''8 }  c''4",
  "c''4 -\\f  c'4 -\\p r4",
  "c''8. (  b'16  d'8.  g'16 ) d''8. (  c''16 )",
  "c''4 (  b'16  c''16  b'16 c''16 )  d''8 (  c''8 )",
  "c''4 -\\f  c'4 -\\p r4",
  #compás 20
  "g'8. ( -\\markup{ \\small\\italic {cresc.} }  a'16 g'4 ) \\acciaccatura { d''8  e''8  f''8 }  g''4",
  "f'4 (  g'16  a'16  g'16  a'16 ) \\acciaccatura {  a'8  b'8 }  a'4",
  "f'8. ( -\\<  g'16  a'8.  b'16 ) \\acciaccatura {  c''8 (  d''8 }  c''8. d''16 ) -\\!",
  "c'8. (  e'16 ) \\acciaccatura {  g'8  a'8 }  g'4 r4",
  "c''4 -\\f  c'4 -\\p r4",
  #compás 25
  "g'4 ( -\\markup{ \\small\\italic {cresc.} }  c''4 )  g''4",
  "e'4. ( -\\p  d'8 )  e'8. (  f'16 )",
  "f'8. (  a'16  g'8  f'8 ) \\acciaccatura {  e'8 (  f'8 }  e'8  d'8 )",
  "f'8. ( -\\<  g'16 \\acciaccatura { a'8 b'8 }  a'8  c''8 )  b'8.\\trill (  a'32 b'32 ) -\\!",
  "c''4 -\\f  c'4 -\\p r4",
  #compás 30
  "f'4 (  f''4 ) \\acciaccatura { f''8 g''8 }  f''4",
  "a'8. ( -\\p  c''16  b'8  a'8 ) \\acciaccatura {  g'8 (  a'8 }  g'8  f'8 )",
  "c''4 -\\f  c'4 -\\p r4",
  "f'4. (  a'8 ) \\acciaccatura { g'8 ( a'8 }  g'8.  f'16 )",
  "e'2 -\\p  f'8 (  fis'8 )",
  #compás 35
  "c''4 -\\f  c'4 -\\p r4",
  "a''4 ( -\\p \\acciaccatura {  f''8  g''8 } f''4 )  c''4",
  "c''4  c''4  c''4",
  "e'4 ( -\\p  d'16  e'16  d'16  e'16 )  f'8 (  fis'8 )",
  "\\acciaccatura {  f''8 (  g''8 }  f''8. -\\< e''16  d''8  c''8 )  b'8.\\trill ( a'32  b'32 ) -\\!",
  #compás 40
  "g'4. (  b8 )  d'8 (  g'8 )",
  "f''8 ( -\\<  b'16  c''16 \\acciaccatura { d''8  e''8 }  d''8.  c''16 ) b'8.\\trill (  a'32  b'32 ) -\\!",
  "g'8. ( -\\markup{ \\small\\italic {cresc.} }  a'16  b'8  c''8 )  d''8 (  e''8 )",
  "c''8. ( -\\p  g'16 )  e'4 r4",
  "f'4 (  a'8  d''8 ) \\acciaccatura { f''8  g''8 }  f''4",
  #compás 45
  "g'4. (  b'8 )  d''8 (  g''8 )",
  "c''4 -\\f  c'4 -\\p r4",
  "d''4  a'16 (  b'16  a'16  b'16 \\acciaccatura {  a'8  b'8 }  a'4 )",
  "e'4 -\\p  e'4  e'4",
  "g'4 \\acciaccatura {  a'8  g'8  f'8 } g'4 r4",
  #compás 50
  "a'8. ( -\\p  c''16  f''8  e''8 ) \\acciaccatura {  d''8 (  e''8 }  d''8 c''8 )",
  "g'8.  g'16  g'4 r4",
  "f''8 ( -\\<  e''16  d''16  c''4 )  b'8.\\trill (  a'32  b'32 ) -\\!",
  "f''4. ( -\\<  d''8 ) \\acciaccatura { e''8 (  f''8 }  e''8  d''8 ) -\\!",
  "f'4 (  a'4 ) \\acciaccatura { c''8  d''8 }  c''4",
  #compás 55
  "c''4 -\\f  c'4 -\\p r4",
  "a'4. ( -\\p  c''8 )  b'8. (  a'16 )",
  "\\acciaccatura {  c''8  d''8 }  c''4  c''8  c''8  c''8  c''8",
  "g'8. (  b'16 ) \\acciaccatura { g''8  a''8 }  g''4 r4",
  "g'4 ( -\\markup{ \\small\\italic {cresc.} }  c''8  e''8 ) \\acciaccatura {  g''8  a''8 }  g''4",
  #compás 60
  "f'8. (  g'16  a'4 ) \\acciaccatura { f''8  e''8  d''8 }  c''4",
  "c''4 ( -\\markup{ \\small\\italic {cresc.} }  g'4 ) \\acciaccatura {  g''8  a''8 }  g''4",
  "c''4 -\\f  c'4 -\\p r4",
  "f'8. ( -\\<  g'16 \\acciaccatura { a'8 b'8 }  a'8  c''8 )  b'8.\\trill (  a'32  b'32 ) -\\!",
  "g'8. (  a'16  b'8.  c''16 ) d''8. (  e''16 )",
  #compás 65
  "\\acciaccatura {  f''8 (  g''8 }  f''8. -\\< e''16  d''8  c''8 )  b'8.\\trill ( a'32  b'32 ) -\\!",
  "a'4 -\\p  a'4  a'4",
  "f'4  d''16 (  e''16  d''16 e''16 \\acciaccatura {  f''8  g''8 } f''4 )",
  "d''4 (  a'4 ) \\acciaccatura { f'8 g'8 }  f'4",
  "c''8 (  g'16  a'16  b'16 c''16  d''16  e''16 ) \\acciaccatura { f''8 g''8 }  f''4",
  #compás 70
  "d''4 (  a'4 ) \\acciaccatura { f'8 g'8 }  f'4",
  "c''4 (  c'4 ) \\acciaccatura { a'8 b'8 }  a'4",
  "f'4  f'4  f'4",
  "c''8. ( -\\markup{ \\small\\italic {cresc.} }  b'16 g'4 ) \\acciaccatura { a''8  g''8  f''8 }  g''4",
  "c''4 -\\f  c'4 -\\p r4",
  #compás 75
  "\\acciaccatura {  c''8  d''8 }  c''4 b'8  b'8  d''8 (  g''8 )",
  "f''4 ( -\\< \\acciaccatura {  d''8  e''8 } d''4 )  b'8.\\trill (  a'32  b'32 ) -\\!",
  "g'8. (  b'16 )  e''4 r4",
  "g'4 ( -\\markup{ \\small\\italic {cresc.} }  e''4 ) g''4",
  "d''4 (  f''4 ) \\acciaccatura { a''8 b''8 }  a''4",
  #compás 80
  "f''4 ( -\\<  d''16  e''16  d''16 e''16 ) \\acciaccatura {  d''8 (  e''8 } d''8  b'8 ) -\\!",
  "c''4 \\acciaccatura { c''8  b'8  a'8 }  g'4 r4",
  "c''4. (  d''8 )  f''8 (  a''8 )",
  "f'4 (  a'4 ) \\acciaccatura { a'8  b'8 }  a'4",
  "f''8. ( -\\<  g''16 \\acciaccatura { f''8 g''8 }  f''4 )  b'8.\\trill (  a'32 b'32 ) -\\!",
  #compás 85
  "f''8. ( -\\<  e''16 \\acciaccatura { d''8 e''8 }  d''8.  c''16 )  b'8.\\trill ( a'32  b'32 ) -\\!",
  "g'4 \\acciaccatura {  a'8  g'8  f'8 } g'4 r4",
  "g'8. (  b'16 ) \\acciaccatura { e''8 f''8 }  e''4 r4",
  "c''8. ( -\\markup{ \\small\\italic {cresc.} }  b'16 g'4 ) \\acciaccatura { a''8  g''8  f''8 }  g''4",
  "g'4 \\acciaccatura {  c''8  d''8 } c''2",
  #compás 90
  "g'4 (  b'4 )  e''4",
  "f'4 (  a'4 ) \\acciaccatura { f'8  g'8 }  f'4",
  "c'4 (  a'4 )  c''4",
  "g'8. ( -\\markup{ \\small\\italic {cresc.} }  a'16 g'4 )  g''4",
  "c''8. (  b'16 ) \\acciaccatura { b'8 c''8 }  b'4 r4",
  #compás 95
  "f'8. (  g'16  a'8  b'8 ) \\acciaccatura {  c''8 (  d''8 }  c''8  d''8 )",
  "c''4 -\\f  c'4 -\\p r4"
]
viola = [
  #compás 1
  "d'8.  d'16  d'8.  d'16 \\acciaccatura {  c'8  d'8 }  c'8.  b16",
  "e'4 \\acciaccatura {  g8  a8 }  g4 r4",
  "a4  c'4 r4",
  "e'4 ( -\\p  c'4 )  e'4",
  #compás 5
  "c'8. ( -\\markup{ \\small\\italic {cresc.} }  d'16 e'8.  d'16 )  e'4",
  "e'4 -\\f  e4 -\\p r4",
  "g8. ( -\\markup{ \\small\\italic {cresc.} }  d'16 c'8.  d'16 )  e'4",
  "d'8. (  c'16 \\acciaccatura { b8 c'8 }  b4 )  d'4",
  "c'4 -\\p  c'16 (  d'16  c'16 d'16  c'4 )",
  #compás 10
  "a4 (  c'4 )  c'8 (  d'8 )",
  "a2  a4",
  "f'2.",
  "c'8. ( -\\markup{ \\small\\italic {cresc.} }  d'16 e'8.  d'16 )  c'4",
  "d'4  b4 r4",
  #compás 15
  "a2.",
  "<< { \\textLengthOn \\parenthesize e'4_\\f^\\markup { \\italic \\magnify #0.6 \"cercana a la anterior\"}^\\markup { \\italic \\magnify #0.6 \"Tocar la nota más\" } } \\\\ { \\parenthesize e4 } >> c_\\p r",
  "d'4  b4 r4",
  "f'4 (  g'16  a'16  g'16 a'16 )  f'8 (  e'8 )",
  "e'4 -\\f  e4 -\\p r4",
  #compás 20
  "c'4 ( -\\markup{ \\small\\italic {cresc.} }  e'8. d'16 )  e'4",
  "a4 (  b16  c'16  b16  c'16 ) c'8. (  d'16 )",
  "a8. ( -\\<  g16  f4 )  g4 -\\!",
  "c'4  e'4 r4",
  "e'4 -\\f  e4 -\\p r4",
  #compás 25
  "c'8. ( -\\markup{ \\small\\italic {cresc.} }  d'16 \\acciaccatura {  e'8  f'8 }  e'8  f'8 )  e'4",
  "g4. ( -\\p  b8 )  c'8. (  d'16 )",
  "a2  a4",
  "a8. ( -\\<  g16  f4 )  g4 -\\!",
  "e'4 -\\f  e4 -\\p r4",
  #compás 30
  "a8. (  b16  c'8.  b16 )  c'8. (  d'16 )",
  "c'2 -\\p  c'4",
  "e'4 -\\f  e4 -\\p r4",
  "a8. (  b16  c'4 )  b4",
  "c'4 -\\p  d'2",
  #compás 35
  "<< { \\textLengthOn \\parenthesize e'4_\\f^\\markup { \\italic \\magnify #0.6 \"cercana a la anterior\"}^\\markup { \\italic \\magnify #0.6 \"Tocar la nota más\" } } \\\\ { \\parenthesize e4 } >> c_\\p r",
  "a4 ( -\\p  c'4 )  f'4",
  "c'4 (  e'4 ) \\acciaccatura { e'8 f'8 }  e'4",
  "c'4 ( -\\p  b16  c'16  b16  c'16 )  d'4",
  "d'8. -\\<  b16  b8.  b16 d'4 -\\!",
  #compás 40
  "d'4  e'4 r4",
  "d'4 ( -\\<  b4 )  d'4 -\\!",
  "c'4 -\\markup{ \\small\\italic {cresc.} }  c'2",
  "e'2 -\\p r4",
  "d'8. (  e'16  d'8  c'8 ) b8 (  a8 )",
  #compás 45
  "d'4  b4 r4",
  "e'4 -\\f  e4 -\\p r4",
  "a4  f'16 (  g'16  f'16 g'16  f'4 )",
  "c'2 -\\p  e'4",
  "c'4  b4 r4",
  #compás 50
  "c'2. -\\p",
  "d'8.  c'16 \\acciaccatura { b8  c'8 }  b4 r4",
  "d'4 ( -\\<  c'8  d'16  e'16 ) d'4 -\\!",
  "b8. ( -\\<  c'16  d'8.  c'16 ) b8 (  c'16  d'16 ) -\\!",
  "a8 (  b8 ) \\acciaccatura {  c'8  d'8 } c'2",
  #compás 55
  "<< { \\textLengthOn \\parenthesize e'4_\\f^\\markup { \\italic \\magnify #0.6 \"cercana a la anterior\"}^\\markup { \\italic \\magnify #0.6 \"Tocar la nota más\" } } \\\\ { \\parenthesize e4 } >> c_\\p r",
  "c'4. ( -\\p  a8 )  b8. (  c'16 )",
  "f'8. (  e'16  d'4 )  e'4",
  "d'2 r4",
  "c'8. ( -\\markup{ \\small\\italic {cresc.} }  d'16 c'8  b8 )  a8 (  g8 )",
  #compás 60
  "a4  a4 (  c'4 )",
  "c'8. ( -\\markup{ \\small\\italic {cresc.} }  d'16  e'8.  d'16 )  c'4",
  "<< { \\textLengthOn \\parenthesize e'4_\\f^\\markup { \\italic \\magnify #0.6 \"cercana a la anterior\"}^\\markup { \\italic \\magnify #0.6 \"Tocar la nota más\" } } \\\\ { \\parenthesize e4 } >> c_\\p r",
  "d'8. ( -\\<  c'16  b8.  c'16 ) d'8.\\trill (  c'32  d'32 ) -\\!",
  "d'4 \\acciaccatura {  g8  a8 }  g4 r4",
  #compás 65
  "b8. -\\<  b16  b8.  b16  d'4 -\\!",
  "c'4 -\\p  c'4  c'4",
  "a4 (  f4 )  a8 (  b8 )",
  "a4 (  f'4 )  d'4",
  "d'2.",
  #compás 70
  "a8 (  b8 ) \\acciaccatura {  c'8  d'8 } c'2",
  "f'4 (  f4 )  f'4",
  "a4  a4  a4",
  "c'4 -\\markup{ \\small\\italic {cresc.} }  e'2",
  "<< { \\textLengthOn \\parenthesize e'4_\\f^\\markup { \\italic \\magnify #0.6 \"cercana a la anterior\"}^\\markup { \\italic \\magnify #0.6 \"Tocar la nota más\" } } \\\\ { \\parenthesize e4 } >> c_\\p r",
  #compás 75
  "d'8. (  b16  g8.  f'16 ) \\acciaccatura {  e'8 (  f'8 }  e'8. d'16 )",
  "b4 -\\<  b4 (  d'4 ) -\\!",
  "c'8. (  d'16 ) \\acciaccatura { b8 c'8 }  b4 r4",
  "c'8 ( -\\markup{ \\small\\italic {cresc.} }  d'8 \\acciaccatura {  c'8  d'8 }  c'8  d'8 )  e'4",
  "a8. (  b16  c'8.  b16 )  c'8. ( a16 )",
  #compás 80
  "b4 ( ~ -\\<  b16  c'16  b16  c'16 )  b8 (  d'8 ) -\\!",
  "d'4  d'4 r4",
  "f'8. (  e'16  d'4 )  c'4",
  "a4 (  f4 )  f4",
  "b8. ( -\\<  c'16  d'8.  e'16 ) f'8. (  g'16 ) -\\!",
  #compás 85
  "b8. ( -\\<  c'16  b8.  c'16 ) d'4 -\\!",
  "c'4  c'4 r4",
  "e'2 r4",
  "c'4 -\\markup{ \\small\\italic {cresc.} }  c'4 ( e'4 )",
  "c'8. (  b16  a8.  f'16 ) \\acciaccatura {  e'8 (  f'8 }  e'8. c'16 )",
  #compás 90
  "e'8. (  b16 ) \\acciaccatura { g8 a8 }  g4 r4",
  "a2.",
  "c'8. (  a16 ) \\acciaccatura { c'8  d'8 }  c'4 r4",
  "c'4 ( -\\markup{ \\small\\italic {cresc.} }  e'8. d'16 )  e'8. (  c'16 )",
  "d'4  d'4 r4",
  #compás 95
  "a2  c'4",
  "<< { \\textLengthOn \\parenthesize e'4_\\f^\\markup { \\italic \\magnify #0.6 \"cercana a la anterior\"}^\\markup { \\italic \\magnify #0.6 \"Tocar la nota más\" } } \\\\ { \\parenthesize e4 } >> c_\\p r",
]
violoncello = [
  #compás 1
  "g4 (  d4 )  g,4",
  "e4  e,4 r4",
  "e4  e,4 r4",
  "c,4 ( -\\p  e,4 )  g,4",
  #compás 5
  "e4 ( -\\markup{ \\small\\italic {cresc.} }  c4 ) cis4",
  "c4 -\\f  c,4 -\\p r4",
  "e4 ( -\\markup{ \\small\\italic {cresc.} }  e,4 ) cis4",
  "e4 (  d8.  c16 )  b,4",
  "f2 -\\p  f4",
  #compás 10
  "f4 (  c4 )  a,4",
  "f4 (  c'8[ \\acciaccatura { b8  c'8 }  b8 ] )  a8 (  f8 )",
  "a2.",
  "e4 -\\markup{ \\small\\italic {cresc.} }  e,4 r4",
  "e4  e,4 r4",
  #compás 15
  "e2.",
  "c4 -\\f  c,4 -\\p r4",
  "g,4  g,4 r4",
  "a4 (  a,4 )  f,4",
  "c4 -\\f  c,4 -\\p r4",
  #compás 20
  "e4 ( -\\markup{ \\small\\italic {cresc.} }  c4 ) cis4",
  "f2  f4",
  "d4 ( -\\<  c4 )  b,4 -\\!",
  "e4  cis8 [ -.  d8 ] -.  dis8 -. e8 -.",
  "c4 -\\f  c,4 -\\p r4",
  #compás 25
  "e2 -\\markup{ \\small\\italic {cresc.} }  cis4",
  "c8. ( -\\p  b,16 )  c4 r4",
  "d4. (  a8 )  f4",
  "d4 -\\<  g,4 r4 -\\!",
  "c4 -\\f  c,4 -\\p r4",
  #compás 30
  "f4 (  c4 )  a,4",
  "f4. ( -\\p  c'8 )  a4",
  "c4 -\\f  c,4 -\\p r4",
  "d4  d,4 r4",
  "c'2 -\\p  b4",
  #compás 35
  "c4 -\\f  c,4 -\\p r4",
  "f,4 ( -\\p  a,4 )  c4",
  "a4 (  c4 )  f,4",
  "c2 -\\p  b,4",
  "d4 ( -\\<  b,4 )  g,4 -\\!",
  #compás 40
  "e8. (  f16 ) \\acciaccatura { g8  a8 }  g4 r4",
  "d4 -\\<  g,4 r4 -\\!",
  "e4 -\\markup{ \\small\\italic {cresc.} }  e,2",
  "c2 -\\p r4",
  "f2  f4",
  #compás 45
  "e8. (  f16 ) \\acciaccatura { g8  a8 }  g4 r4",
  "c4 -\\f  c,4 -\\p r4",
  "f2  d4",
  "c'4 ( -\\p  g4 )  c4",
  "e4  e,4 r4",
  #compás 50
  "f2. -\\p",
  "e4  f8 -.  fis8 -.  g8 -. gis8 -.",
  "d8 -. -\\<  dis8 -.  e8 -.  f,8 -. fis,8 -.  g,8 -. -\\!",
  "d4 ( -\\<  g,4 )  g4 -\\!",
  "f2.",
  #compás 55
  "c4 -\\f  c,4 -\\p r4",
  "f8. ( -\\p  e16 )  f4 r4",
  "a2  a,4",
  "e2 r4",
  "e2 -\\markup{ \\small\\italic {cresc.} }  cis4",
  #compás 60
  "f4 (  c'4 )  a4",
  "e4 -\\markup{ \\small\\italic {cresc.} }  e,4 r4",
  "c4 -\\f  c,4 -\\p r4",
  "d4 -\\<  g,4 r4 -\\!",
  "e4  e,4 r4",
  #compás 65
  "d4 ( -\\<  g4 )  g,4 -\\!",
  "f4 -\\p  f4  f4",
  "d4 (  a,4 )  d4",
  "f4 (  d4 )  a,4",
  "g2.",
  #compás 70
  "f2.",
  "a4 (  a,4 )  c4",
  "d4  d4  d4",
  "e4 ( ~ -\\markup{ \\small\\italic {cresc.} }  e8. d16 )  cis4",
  "c4 -\\f  c,4 -\\p r4",
  #compás 75
  "g4 (  d4 )  g,4",
  "d4 ( -\\<  b,4 )  g,4 -\\!",
  "e4  e,4 r4",
  "e2. -\\markup{ \\small\\italic {cresc.} }",
  "f4  d4 r4",
  #compás 80
  "d8 -. -\\<  dis8 -.  e8 -.  f8 -.  fis8 -.  g8 -. -\\!",
  "g,4  b,4 r4",
  "a2  a,4",
  "d4 (  a,4 )  d4",
  "d4 -\\<  g,4 r4 -\\!",
  #compás 85
  "d4 ( -\\<  b,4 )  g,4 -\\!",
  "e4  e,4 r4",
  "e2 r4",
  "e4 ( -\\markup{ \\small\\italic {cresc.} }  g4 ) c4",
  "e4 (  e,4 )  g4",
  #compás 90
  "e4  e,4 r4",
  "d2.",
  "e4  e,4 r4",
  "e4 -\\markup{ \\small\\italic {cresc.} }  c,4 r4",
  "g,4  cis8 -.  d8 -.  dis8 -. e8 -.",
  #compás 95
  "f2  a,4",
  "c4 -\\f  c,4 -\\p r4"
]

c01 = [43, 48, 38, 34, 4, 26 ]
c02 = [58, 14, 51, 8, 64, 45]
c03 = [12, 37, 18, 57, 71, 82]
c04 = [69, 81, 94, 1, 17, 75]
c05 = [54, 10, 21, 95, 60, 30]
c06 = [78, 93, 13, 42, 88, 61]
c07 = [65, 84, 80, 85, 76, 53]
c08 = [19, 24, 46, 29, 6, 32]
c09 = [50, 66, 9, 31, 36, 56]
c10 = [87, 49, 77, 90, 2, 40]
c11 = [91, 72, 67, 27, 83, 33]
c12 = [15, 3, 23, 92, 86, 89]
c13 = [70, 68, 47, 44, 11, 79]
c14 = [25, 20, 5, 59, 73, 7]
c15 = [39, 28, 52, 22, 41, 63]
c16 = [55, 35, 74, 96, 62, 16]
compases = [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15, c16]
