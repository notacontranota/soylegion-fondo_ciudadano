#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#módulo música de Ana Carolina
violin = [
  #compás 1
  "r8.  d''16 _\\f  d''16  d''16 d''8.  d''16  d''16  d''16",
  "a''8. _\\f  g''8.  e''8.  cis''8.",
  "d''8. _\\f  e''8.  f''4.",
  "e''8.  f''8.  g''8.  e''8.",
  #compás 5
  "f'4. r4.",
  "bes'4. ~  bes'16 (  e'16  f'16 g'16  a'16  bes'16 )",
  "d''2. _\\f",
  "bes'16 (  a'16  bes'4 )  bes'16 ( a'16  bes'4 )",
  "a'4 ~ _\\mf  a'16  a'16  a'4 ~ a'16  bes'16",
  #compás 10
  "d''4  d'''8 ~  d'''8  d''4",
  "a'8 ( _\\mf  bes'8  g'8 )  a'4.",
  "a'16 (  cis'16  d'16  e'16  bes'16 a'16 )  g'4 (  a'8 )",
  "g'16 ( _\\>  a'16  g'16  f'8. ) ~ f'4.\\!",
  "e''8. _\\markup{ \\italic {cresc.} }  g''8. g''8.  e''8.",
  #compás 15
  "bes''16 _\\<  a''16  g''16  e''16 cis''16  a'16  a''16  g''16 e''16  cis''16  a'16  g'16 _\\!",
  "f''4.  f'4.",
  "bes'8.  e''16 (  d''16  c''16 ) a'8 (  bes'16 ) g'16 (  a'16 bes'16 )",
  "f''8  g''8  a''8  f''8 g''8  a''8",
  "f''8.  f'8.  f''4.",
  #compás 20
  "f'8  bes'8  d''8  f''4.",
  "a''16 ( _\\f  e''16  d''16 ) cis''8.  bes''16 (  e''16  d''16 ) cis''8.",
  "a'4. _\\mf  a'8 (  g'8  a'8 )",
  "d'4. _\\mf  f'8  g'8  a'8",
  "a''8.  g''8.  a'8.  g'8.",
  #compás 25
  "a'16 ( _\\<  bes'16  a'16  bes'16 a'16  bes'16 )  g'16 (  a'16  g'16 a'16  g'16  a'16 ) _\\!",
  "e''16 (  d''16  e''4 )  e''16 (  d''16  e''4 )",
  "bes'16 (  a'16  bes'4 )  bes'16 (    a'16  bes'4 )",
  "e'''8 _\\markup{ \\italic {cresc.} }  e''4 e'''8  e''4",
  "cis''2.\\trill  _\\f",
  #compás 30
  "f''8  c''8  a'8  f'4.",
  "g'16  a'16  bes'16  c''16 d''16  e''16  f''4.",
  "d''8.  e''16 (  d''16  cis''16 )  d''8.  cis''16 (  d''16  e''16 )",
  "bes'8.  bes'16  a'8  bes'8. bes'16  a'8",
  "f'16 ( _\\>  g'16  f'16  g'16  f'16 g'16 )  f'4. _\\!",
  #compás 35
  "a'4  a''8  g'4  g''8",
  "e''2. \\trill _\\markup{ \\italic {cresc.} }",
  "bes'8.  c''16 (  d''16  e''16 ) e''8.  d''16 (  c''16  bes'16 )",
  "r8  d''4 -> r8  d''4 ->",
  "d''4 _\\mf  f''8  a'4  d''8",
  #compás 40
  "a''8. _\\mf  g''16 (  f''16  e''16 )  d''8.  c''16 (  bes'16  a'16 )",
  "e''8.  e''16  g''8  e''8. e''16  g''8",
  "d''8. _\\>  a'16  f'8  d'4. _\\! _\\p",
  "g''16 (  a''16  bes''16  a''16 g''16  f''16 )  e''16 (  d''16 c''16  d''16  e''16  g''16 )",
  "d''16 ( _\\f  e''16  d''4 )  d''16 (  e''16  d''4 )",
  #compás 45
  "d''2. _\\f",
  "a'16 ( _\\<  bes'16  a'4 )  g'16 ( a'16  g'4 ) _\\!",
  "g'4. ( _\\>  f'4. ) _\\!",
  "cis''16 ( _\\f  b'16  cis''4 ) cis''16 (  b'16  cis''4 )",
  "e''4 _\\markup{ \\italic {cresc.} }  f''8 ~ f''8  g''4",
  #compás 50
  "a''8.\\mf f''8. d''8. a'8.",
  "f''8  f''8  f''8  f''8 f''8  f''8",
  "bes'8.  bes''16  bes''8  bes'8. bes''16  bes''8",
  "r8  d''4 -> r8  d''4 ->",
  "d''8. _\\f  d'''16 _\\p  d'''8 d'''4.",
  #compás 55
  "f'16 ( _\\>  g'16  f'4 ) ~  f'4. _\\!",
  "a'4.  g'4. \\trill",
  "a'16 _\\<  e''16  d''16  cis''16 b'16  a'16  g'4. _\\!",
  "r8  g'4 -> r8  f'4 ->",
  "a'8. _\\<  a''8.  g''8.  g'8. _\\!",
  #compás 60
  "a'8. _\\mf  d''8.  f''8. a''8.",
  "bes'8 (  a'8  bes'8 )  c''8 bes'4",
  "f''2.",
  "d''4 _\\f  e''8  f''4  g''8",
  "f''8  f'4  f''8  f'4",
  #compás 65
  "bes''16 _\\f  a''16  g''16  f''16 e''16  d''16  cis''4.",
  "e''2. \\trill",
  "d''8. _\\f  d'8.  d'4.",
  "f''16  e''16  d''16  c''16 bes'16  b'16  c''16  cis''16 d''16  dis''16  e''16  f''16",
  "r8  a'4 -> r8  g'4 ->",
  #compás 70
  "e''16.  f''16.  g''16.  a''16. g''16.  f''16.  e''16.  g''16.",
  "<< { \\parenthesize bes''8.^\\markup { \\italic \\magnify #0.6 \"cercana a la anterior\" }^\\markup { \\italic \\magnify #0.6 \"Tocar la nota más\" }  g''8. e''8. bes'8. } \\\\ { \\parenthesize bes'8.  g''8. e''8. bes'8. } >>",
  "e''16 ( _\\markup{ \\italic {cresc.} }  d''16 e''4 )  e''16 (  d''16  e''4 )",
  "bes'8 (  e'8 )  g'8  bes'8 ( e''8 )  bes'8",
  "r4  a8 _\\mf  d'8  f'8  a'8",
  #compás 75
  "g'8.  f'16 (  a'16  g'16 )  f'4.",
  "g'16 ( _\\>  a'16  g'8 )  f'8 ~  f'4. _\\!",
  "d''16 ( _\\f  e''16  d''4 ) f''16 (  g''16  f''4 )",
  "d''4 ~  d''16  d''16  d''4.",
  "a'8. _\\mf  a'16  bes'8  a'8.  a'16 bes'8",
  #compás 80
  "f''4 ~  f''16  f'16  f'4 r8",
  "a'4. \\trill _\\<  g'4.\\trill _\\!",
  "f''8  c''8  a'8  f'4.",
  "d''4. _\\f  d'4. _\\p",
  "f''4 ( _\\mf  d''8 )  a'4 (  d''8 )",
  #compás 85
  "bes'4 ~  bes'16  bes'16  bes'8. e''16 (  d''16  bes'16 )",
  "e'''16 ( _\\markup{ \\italic {cresc.} }  bes''16 a''16  g''16  f''16  e''16 ) e'''16 (  bes''16  a''16  g''16 f''16  e''16 )",
  "f''4  f'8  f'4.",
  "cis''4 ~ _\\f  cis''16  cis''16 cis''4.",
  "d''2. \\trill",
  #compás 90
  "g'8. ( _\\>  a'8. )  f'4. _\\!",
  "f''8.  f''16  g''8  f''8. f''16  g''8",
  "f'8  a'8  d''8  f''4.",
  "bes'4 (  a'8 )  bes'4 (  a'8 )",
  "d''4 _\\f  es''8  d''4.",
  "a'8.  b'16 (  cis''16  d''16 ) e''16 (  d''16  cis''16  b'16 a'16  g'16 )",
  "e''4. _\\mf  d''8.  a'8."
]
viola = [
  #compás 1
  "r8  f'4 _\\f r8  f'4",
  "e'8. _\\f  bes'8.  a'8.  g'8.",
  "f'4. _\\f  bes8.  bes'8.",
  "g'4  a'8  bes'4  c''8",
  #compás 5
  "bes4. r4.",
  "e'16 (  bes16  c'16  d'16 e'16  f'16 )  e'4.",
  "fis'2. _\\f",
  "e'16  d'16  c'16  a16 c'16  d'16  e'4.",
  "f'4 ~ _\\mf  f'16  f'16  f'4 ~ f'16  e'16",
  #compás 10
  "f'8.  g'16 (  f'16  e'16 ) f'8.  e'16 (  f'16  g'16 )",
  "f'8 ( _\\mf  g'8  e'8 )  f'8 ( e'8  f'8 )",
  "cis'8 (  bes8  cis'8 )  a8 ( bes8  a8 )",
  "a8. _\\>  bes16 (  c'16  bes16  a4. ) _\\!",
  "bes'16 ( _\\markup{ \\italic {cresc.} }  a'16 bes'16 )  bes'16 (  a'16  bes'16 )  bes'16 (  a'16  bes'16 ) bes'16 (  a'16  bes'16 )",
  #compás 15
  "cis'8. _\\<  cis'16  bes8  a8.  a16 bes8 _\\!",
  "a'4.  a4.",
  "e'4  g'8  f'8 (  e'4 )",
  "a'8  g'8  f'8  a'8  g'8 f'8",
  "a'8.  a8.  a'4.",
  #compás 20
  "bes8.  d'8.  bes'4.",
  "a'8. _\\f  a'16 (  bes'16  a'16 )  g'8.  g'16 (  a'16  g'16 )",
  "f'8 _\\mf  a8  d'8  f'4.",
  "r8  a4 _\\mf  a8  d'8  f'8",
  "cis'16  d'16  e'16  f'16 g'16  a'16  a16  cis'16 e'16  d'16  cis'16  a16",
  #compás 25
  "cis'4. _\\<  a4. _\\!",
  "bes'16  a'16  g'16  f'16 e'16  d'16  c'16  e'16 f'16  g'16  a'16  bes'16",
  "e'4  e'16 (  f'16 )  e'4 e'16 (  d'16 )",
  "bes'8 ( _\\markup{ \\italic {cresc.} }  a'8 bes'8 )  bes'8 (  a'8  bes'8 )",
  "a'8. _\\f  bes'16 (  a'16  f'16 )  g'8.  a'16 (  g'16  e'16 )",
  #compás 30
  "a'8  f'8  c'8  a4.",
  "bes4 (  bes'8 )  a'4.",
  "f'8  f'4 ->  f'8  f'4 ->",
  "r8  e'4 r8  e'4",
  "a16 ( _\\>  bes16  a16  bes16  a16 bes16 )  a4._\\!",
  #compás 35
  "cis'8. cis'16  bes8  a8.  a16 bes8",
  "bes'4 ~ _\\markup{ \\italic {cresc.} }  bes'16 bes'16  bes'4.",
  "e'8.  e'16 (  f'16  g'16 ) g'8.  f'16 (  e'16  d'16 )",
  "r8  f'4 -> r8  f'4 ->",
  "f'4 _\\mf  a'8  d'4  f'8",
  #compás 40
  "f'8 _\\mf  f4  d'8  f'4",
  "bes'4 (  bes8 )  bes'4 (  bes8 )",
  "f'16 ( _\\>  e'16  f'4 )  f4. _\\! _\\p",
  "r8  <g' bes'>4 r8  <g' bes'>4",
  "f'4 _\\f  f8  f'4  f8",
  #compás 45
  "f'2. _\\f",
  "cis'8. _\\<  e'16  cis'8  a8. cis'16  a8_\\!",
  "a16 _\\>  bes16  c'16  d'16 c'16  bes16  a4. _\\!",
  "a'8. _\\f  a'16 (  g'16  f'16 )  e'4  g'8",
  "bes'8 ( _\\markup{ \\italic {cresc.} }  a'8 ) bes'8  bes'8 (  a'8 )  bes'8",
  #compás 50
  "f''8.\\mf d''8. a'8. f'8.",
  "a'8  a'8  a'8  a'8  a'8 a'8",
  "e'16 (  d'16 c'16  bes16 c'16  d'16 )  e'4.",
  "f'8.  f'8.  f'8.  f'8.",
  "f'8. _\\f  d''16 _\\p  d''8  d''4.",
  #compás 55
  "a16 ( _\\>  bes16  a4 )  a16 ( bes16  a4 ) _\\!",
  "cis'8.  e'16 (  d'16  cis'16 )  a8.  cis'16 (  bes16  a16 )",
  "cis'4. _\\<  a16  e'16  d'16 cis'16  b16  gis16 _\\!",
  "r8  bes4 -> r8  bes4 ->",
  "cis'8 _\\<  bes4  a8  bes4 _\\!",
  #compás 60
  "f'4 _\\mf  a'8  d''4  f'8",
  "e'4  e8  e'4  e8",
  "a'2.",
  "f'4 _\\f  a'8  bes'4  c''8",
  "a'16 (  g'16  a'4 )  a'16 ( g'16  a'4 )",
  #compás 65
  "r8  a'8 _\\f  bes'8  g'4. \\trill",
  "bes'16 (  a'16  bes'4 )  bes'16 (  a'16  bes'4 )",
  "f'8. _\\f  f8.  f4.",
  "a'4 (  g'8 )  a'4 (  g'8 )",
  "cis'4 (  bes8 )  a4.",
  #compás 70
  "g'16 (  f'16  g'4 )  bes'16 ( a'16  bes'4 )",
  "e'4  e8  e'4  e8",
  "bes'4 _\\markup{ \\italic {cresc.} }  bes8 ( a8 ) bes'4",
  "e'8 (  g8 )  bes8  e'8 (  g'8 )  e'8",
  "r8  f4 _\\mf  a8  d'8  f'8",
  #compás 75
  "bes2.",
  "a4. _\\>  a4. _\\!",
  "f'8. _\\f  f'16 (  g'16  a'16 )  bes'16 (  a'16  g'16  f'16 a'16  bes'16 )",
  "f'4 ~  f'16  f'16  f'4.",
  "f'8 _\\mf  f4  f'8  f4",
  #compás 80
  "a'4 ~  a'16  a16  a4 r8",
  "cis'8 ( _\\<  d'8  cis'8 )  a8 ( bes8  a8 ) _\\!",
  "a'4.  a4.",
  "f'4. _\\f  d4. _\\p",
  "a'4 ( _\\mf  f'8 )  f'4 (  a'8 )",
  #compás 85
  "e'4 ~  e'16  e'16  e'8. g'8.",
  "bes'8. _\\markup{ \\italic {cresc.} }  bes8. bes8.  bes'8.",
  "a'4  a8  a4.",
  "a'4. \\trill _\\f  g'4. \\trill",
  "f'16 (  e'16  d'16  a16  g16 f16 )  f'16 (  e'16  d'16  a16 g16  f16 )",
  #compás 90
  "a8. ( _\\>  f8. )  a4. _\\!",
  "a'4  g'8  a'4  bes'8",
  "a8.  d'8.  a'4.",
  "e'4.  e'4.",
  "f'4 _\\f  f'8  f'4  gis'8",
  "cis'8.  b8.  a8.  a8.",
  "r8  g'4 _\\mf  g'8  f'4",
]
violoncello = [
  #compás 1
  "bes,4. _\\f  bes,4.",
  "a,16 ( _\\f  bes,16  a,16 )  a,16 ( bes,16  a,16 )  a,16 (  bes,16 a,16 )  a,16 (  bes,16  a,16 )",
  "bes,8. _\\f  c8.  d4.",
  "c8  c,4  c8  c,4",
  #compás 5
  "d4. r4.",
  "g,4.  g,4.",
  "d,2. _\\f",
  "g,4.  g16  f16  e16  d16 c16  bes,16",
  "d4 ~ _\\mf  d16  d16  d4 ~ d16  g,16",
  #compás 10
  "a8  a,4  a8  g,4",
  "d4. _\\mf  d8 (  cis8  d8 )",
  "a,4.  cis16 (  d16  e16 a16  g16  e16 )",
  "d4 _\\>  a8  d4. _\\!",
  "g8. _\\markup{ \\italic {cresc.} }  e8. e8.  g8.",
  #compás 15
  "a,4 _\\<  bes,8  cis4. _\\!",
  "f,4.  f,4.",
  "g,8.  e,8.  g,4.",
  "c16 (  d16  c16  d16  c16 d16 )  c16 (  d16  c16  d16 c16  d16 )",
  "c4.  c8.  c,8.",
  #compás 20
  "d4.  d'4.",
  "a16 ( _\\f  g16  e16  d16 cis16  b,16 )  a,8.  a,8.",
  "d4 _\\mf  d'8  d4  d'8",
  "r4  f8 _\\mf  d4.",
  "a,4  bes,8  cis4.",
  #compás 25
  "a,8. _\\<  bes,8.  cis8.  cis8. _\\!",
  "c,2.",
  "g,16  f,16  g,16  a,16  bes,16 e16  g4.",
  "g8. _\\markup{ \\italic {cresc.} }  fis16 ( g16  a16 )  g8.  bes16 ( a16  g16 )",
  "a,16 ( _\\f  bes,16  a,4 )  a,16 ( bes,16  a,4 )",
  #compás 30
  "f,8  a,8  c8  f4.",
  "d4.  d,4.",
  "a16 ( ->  bes16  a4 )  a16 ( -> bes16  a4 )",
  "r8  g,4 r8  g,4",
  "<< {\\stemDown d2.} \\\\{ s2_\\> s8 s _\\!} >>",
  #compás 35
  "a8  g,4  cis'8  cis4",
  "g4 ~ _\\markup{ \\italic {cresc.} }  g16 g16  g4.",
  "g8  g,4  g8  g,4",
  "<a, d>4 r8  <a, d>4 r8",
  "r8  <d a>4 _\\mf r8  <d a>4",
  #compás 40
  "d4 _\\mf  e8  f4  d8",
  "c,4 (  e,8 )  c,4 (  e,8 )",
  "d16 ( _\\>  cis16  d16 )  e16 f16  a16  d'4. _\\! _\\p",
  "c,4.  c,4.",
  "r4  bes,8 _\\f r4  bes,8",
  #compás 45
  "d2. _\\f",
  "a,4 _\\<  a,8  cis4  cis8 _\\!",
  "d8 _\\>  a,8  f,8  d,4. _\\!",
  "a16 ( _\\f  e16  d16  cis16 b,16  a,16 )  a16 (  e16 d16  cis16  b,16  a,16 )",
  "g,16 ( _\\markup{ \\italic {cresc.} }  a,16 bes,16  c16  d16  e16 )  g16 ( f16  e16  f16  g16 bes16 )",
  #compás 50
  "d4. _\\mf  f,4.",
  "c2. \\trill",
  "g,4.  g,16 (  a,16  bes,16  a,16 g,16  e,16 )",
  "a4  a,8 ~  a,8  a4",
  "d8. _\\f  d,16 _\\p  d,8  d,4.",
  #compás 55
  "d4. _\\>  d16 (  cis16  d4 ) _\\!",
  "a,8.  a,8.  cis8.  cis8.",
  "a,4. _\\<  cis4. _\\!",
  "d4.  d,4.",
  "a,4 _\\<  e8  cis4  e8 _\\!",
  #compás 60
  "d16 _\\mf  f16  e16  d16 c16  bes,16  a,16  a16 g16  f16  e16  d16",
  "g,16  a,16  bes,16  c16  e16 d16  g16  f16  e16  d16 c16  bes,16",
  "f,2.",
  "bes,8. _\\f  bes,16  c8  d8. c16  d8",
  "c8.  c,8.  c,8.  c8.",
  #compás 65
  "a,8. _\\f  a,16  bes,8  a,8.  a,16 bes,8",
  "c,8  c,8  c,8  c,8  c,8 c,8",
  "d8. _\\f  d8.  d,4.",
  "c8  c'4  c8  c'4",
  "a,8.  a,8.  cis,8.  cis8.",
  #compás 70
  "c16 (  bes,16  a,16  g16 f16  e16 )  d16 (  c16  bes,16 a,16  g,16  c,16 )",
  "g,8  g4  g,8  g4",
  "g16 ( _\\markup{ \\italic {cresc.} }  f16 e16  d16  bes,16  a,16 )  g,8. g8.",
  "r8  g,8  g,8 r8  g,8  g,8",
  "d,4. _\\mf  f,8  a,8  d8",
  #compás 75
  "d2.",
  "d16 ( _\\>  cis16  d16  e16 ) f16  a16  d'4. _\\!",
  "bes,16 ( _\\f  c16  bes,16  a,16 bes,16  c16 )  d4.",
  "a2. \\trill",
  "d4. _\\mf  d16  e16  d16  c16 bes,16  a,16",
  #compás 80
  "f,4 ~  f,16  f,16  f,4 r8",
  "a,4 _\\<  e8  cis4  a,8 _\\!",
  "f,4  f8  f,4.",
  "d4. _\\f  d,4. _\\p",
  "d16 ( _\\mf  e16  d4 )  d16 ( e16  d4 )",
  #compás 85
  "g,4 ~  g,16  g,16  g,8.  e,8.",
  "g2. \\trill _\\markup{ \\italic {cresc.} }",
  "f,4.  f,4.",
  "a,4 ~ _\\f  a,16  a,16  a,4.",
  "a8.  a,16  a,8  a8. a,16  a,8",
  #compás 90
  "d8. ( _\\>  d8. )  d4. _\\!",
  "c16  a,16  f,16  c,16  f,16 a,16  c16  a,16  f,16  c,16 f,16  a,16",
  "d4.  d'4.",
  "g,8.  g,16  g8  g,8.  g,16 g8",
  "bes,4 _\\f  a,8  bes,4.",
  #compás 95
  "a,16 (  bes,16  a,4 )  cis16 ( d16  cis4 )",
  "r4  cis'8 _\\mf  d'4  d8",
]

c01 = [22, 79, 39, 50, 84, 11]
c02 = [61, 33, 8, 93, 37, 73]
c03 = [57, 46, 81, 15, 59, 25]
c04 = [13, 47, 90, 34, 76, 55]
c05 = [44, 1, 77, 94, 3, 63]
c06 = [68, 51, 19, 64, 18, 91]
c07 = [26, 41, 66, 4, 43, 70]
c08 = [82, 16, 80, 62, 87, 30]
c09 = [9, 60, 40, 23, 74, 96]
c10 = [71, 85, 27, 52, 17, 6]
c11 = [35, 24, 56, 12, 95, 69]
c12 = [20, 75, 5, 92, 31, 58]
c13 = [49, 72, 86, 28, 36, 14]
c14 = [53, 10, 89, 32, 78, 38]
c15 = [65, 29, 48, 88, 2, 21]
c16 = [7, 83, 42, 67, 54, 45]
compases = [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15, c16]
