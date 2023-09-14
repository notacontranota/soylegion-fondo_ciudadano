#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import soycompases

def partitura(dados):
  lily = []
  lily.append ("""%Generado automáticamente por 'soylegion.py'
%para el juego \"Ana Carolina\", de Pablo Herrera.
\\version \"2.22.0\"
\\pointAndClickOff

global = {
  \\key d \minor
  \\time 6/8
  \\tempo "Lento"
  \\repeat volta 2 {
    s2.*8
  }
  \\repeat volta 2 {
    s2.*8
  }
}\n\n""")
  #violín
  lily.append ("violin = {\n")
  for j in range(len(soycompases.compases)):
    compasVl = soycompases.violin[soycompases.compases[j][dados[j]-1]-1]
    lily.append ("  " + compasVl + "\n")
  lily.append ("}\n")
  #viola
  lily.append ("viola = {\n")
  for k in range(len(soycompases.compases)):
    compasVla = soycompases.viola[soycompases.compases[k][dados[k]-1]-1]
    lily.append ("  " + compasVla + "\n")
  lily.append ("}\n\n")
  #violoncello
  lily.append ("violoncello = {\n")
  cVc = []
  for l in range(len(soycompases.compases)):
    compasVc = soycompases.violoncello[soycompases.compases[l][dados[l]-1]-1]
    lily.append ("  " + compasVc + "\n")
  lily.append ("}\n\n")
  
  #partitura general
  lily.append ("""\\bookpart {
  \\header {
    dedication = \\markup { \\italic \"de «Soy Legión»\" }
    title = \"Ana Carolina\"
    subtitle = \"(Trío de cuerdas)\"\n""")
  lily.append ("    subsubtitle = \"Dados: " + repr(dados) + "\"\n")
  lily.append ("""    instrument = \"Partitura general\"
    composer = \"Pablo Herrera\"
    copyright = \\markup {\\with-url #\"https://github.com/notacontranota/soylegion-fondo_ciudadano\" {
      \\center-column {
        \\concat { \\epsfile #0 #15 #\"recursos/soyfondo.eps\"
        "   "
        \\epsfile #0 #15 #\"recursos/soyncn.eps\" }
        \\bold {\"Fondo Ciudadano de Desarrollo Cultural & Nota contra Nota\"}
        \"https://github.com/notacontranota/soylegion-fondo_ciudadano\"
        \\null
        }
      }
    }
    tagline = \"\"\n  }\n\n""")
  
  
  #sección \score{}
  lily.append("""  \\markup { \\vspace #1 }
  #(set-global-staff-size 20)
  \\score {
    \\new StaffGroup <<
      \\overrideTimeSignatureSettings 3/4 1/4 1,1,1 #'() %para dividir beats.
      \\new Staff \\with {
        instrumentName = \\markup { \\caps \"Violín\" }
        midiInstrument = \"string ensemble 1\"
        midiPanPosition = #-0.5
      }{
        \\clef treble
        \\accidentalStyle StaffGroup.modern-voice-cautionary
        << \\global \\compressMMRests {\\violin} >>
      }
      \\new Staff \\with {
        instrumentName = \\markup { \\caps \"Viola\" }
        midiInstrument = \"string ensemble 1\"
        midiPanPosition = #0.5
      }{ 
        \\clef alto 
        << \\global \\viola >>
      }
      \\new Staff \\with{
        instrumentName = \\markup { \\caps \"Violoncello\" }
        midiInstrument = \"string ensemble 1\"
        midiPanPosition = #0.0
      }{ 
        \\clef bass
        << \\global \\violoncello >>
      }
    >>
    \\layout {
      indent = 3\\cm
      #(layout-set-staff-size 17 )
    }
    \\midi {\\tempo 4=60}
  }
}
""")
  lily.append ("""%particellas
\\bookpart {
  \\header {
    dedication = \\markup { \\italic \"de «Soy Legión»\" }
    title = \"Ana Carolina\"
    subtitle = \"(Trío de cuerdas)\"
    instrument = \"Violín, Flauta u Oboe\"\n """)
  lily.append ("   subsubtitle = \"Dados: " + repr(dados) + "\"\n")
  lily.append ("""    composer = \"Pablo Herrera\"
    copyright = \\markup {\\with-url #\"https://github.com/notacontranota/soylegion-fondo_ciudadano\" {
      \\center-column {
        \\concat { \\epsfile #0 #15 #\"recursos/soyfondo.eps\"
        "   "
        \\epsfile #0 #15 #\"recursos/soyncn.eps\" }
        \\bold {\"Fondo Ciudadano de Desarrollo Cultural & Nota contra Nota\"}
        \"https://github.com/notacontranota/soylegion-fondo_ciudadano\"
        \\null
        }
      }
    }
    tagline = \"\"
  }

  \\markup { \\vspace #1 }
  \\score {
    \\new Staff {
      \\overrideTimeSignatureSettings 3/4 1/4 1,1,1 #'() %para dividir beats.
      \\accidentalStyle Staff.modern-cautionary
      \\clef treble
      <<\\global \\compressMMRests{\\violin}>>
    }
    \\layout {
      indent = 0\\cm
    }
  }
}

\\bookpart {
  \\header {
    dedication = \\markup { \\italic \"de «Soy Legión»\" }
    title = \"Ana Carolina\"
    subtitle = \"(Trío de cuerdas)\"
    instrument = \\markup { \\concat {\"Viola o Clarinete en Si\" \\flat} }\n """)
  lily.append ("   subsubtitle = \"Dados: " + repr(dados) + "\"\n")
  lily.append ("""    composer = \"Pablo Herrera\"
    copyright = \\markup {\\with-url #\"https://github.com/notacontranota/soylegion-fondo_ciudadano\" {
      \\center-column {
        \\concat { \\epsfile #0 #15 #\"recursos/soyfondo.eps\"
        "   "
        \\epsfile #0 #15 #\"recursos/soyncn.eps\" }
        \\bold {\"Fondo Ciudadano de Desarrollo Cultural & Nota contra Nota\"}
        \"https://github.com/notacontranota/soylegion-fondo_ciudadano\"
        \\null
        }
      }
    }
    tagline = \"\"
  }

  \\markup { \\vspace #1 }
  \\score {
    \\new Staff {
      \\overrideTimeSignatureSettings 3/4 1/4 1,1,1 #'() %para dividir beats.
      \\accidentalStyle Staff.modern-cautionary
      \\clef alto
      <<\\global \\compressMMRests{\\viola}>>
    }
    \\layout {
      indent = 0\\cm
    }
  }

  \\markup { \\vspace #8 }
  \\score {
    \\new Staff {
      \\overrideTimeSignatureSettings 3/4 1/4 1,1,1 #'() %para dividir beats.
      \\accidentalStyle Staff.modern-cautionary
      \\clef treble
      \\transpose c d <<\\global \\compressMMRests{\\viola}>>
    }
    \\layout {
      indent = 0\\cm
    }
  }
}

\\bookpart {
  \\header {
    dedication = \\markup { \\italic \"de «Soy Legión»\" }
    title = \"Ana Carolina\"
    subtitle = \"(Trío de cuerdas)\"
    instrument = \"Violoncello o Fagot\"\n """)
  lily.append ("   subsubtitle = \"Dados: " + repr(dados) + "\"\n")
  lily.append ("""    composer = \"Pablo Herrera\"
    copyright = \\markup {\\with-url #\"https://github.com/notacontranota/soylegion-fondo_ciudadano\" {
      \\center-column {
        \\concat { \\epsfile #0 #15 #\"recursos/soyfondo.eps\"
        "   "
        \\epsfile #0 #15 #\"recursos/soyncn.eps\" }
        \\bold {\"Fondo Ciudadano de Desarrollo Cultural & Nota contra Nota\"}
        \"https://github.com/notacontranota/soylegion-fondo_ciudadano\"
        \\null
        }
      }
    }
    tagline = \"\"
  }

  \\markup { \\vspace #1 }
  \\score {
    \\new Staff {
      \\overrideTimeSignatureSettings 3/4 1/4 1,1,1 #'() %para dividir beats.
      \\accidentalStyle Staff.modern-cautionary
      \\clef bass
      <<\\global \\compressMMRests{\\violoncello}>>
    }
    \\layout {
      indent = 0\\cm
    }
  }
}
      
""")
  return lily