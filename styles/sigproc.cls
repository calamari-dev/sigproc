\NeedsTeXFormat{LaTeX2e}
\RequirePackage{expl3}
\ProvidesExplClass{sigproc}{2023-02-04}{1.0}{sigproc class}
\ExplSyntaxOff

\newif\if@ebook
\@ebookfalse

\DeclareOption{ebook}{\@ebooktrue}
\ProcessOptions

\if@ebook
\else
  \PassOptionsToClass{twoside,gutter=20mm}{jlreq}
\fi

\newcommand{\jlreqkanjiskip}{\z@ \@plus .1\zw \@minus .01\zw}
\newcommand{\jlreqxkanjiskip}{.25em \@plus .15em \@minus .06em}
\LoadClass[disablejfam,book,paper=a5,fontsize=9bp,head_space=20mm,line_length=112mm,number_of_lines=32,headfoot_verticalposition=11bp]{jlreq}

\RequirePackage[math-style=ISO,warnings-off={mathtools-colon}]{unicode-math}
\RequirePackage[no-math,match,deluxe,sourcehan-jp,jfm_yoko=jlreq]{luatexja-preset}
\RequirePackage{luatexja-ruby}
\RequirePackage{etoolbox}
\RequirePackage{titletoc}
\RequirePackage{multicol}

% フォント
\ltjsetparameter{jacharrange={-2,-9},alxspmode={`‐,0}}
\ltjsetparameter{yalbaselineshift=.02\zh}
\ltjsetruby{fontcmd=\rmfamily\mcfamily\mdseries}
\setmathfont{STIX Two Math}[Scale=1.1]
\setmainfont{STIX Two Text}[Scale=1.1]
\setsansfont{Liberation Sans}[Scale=1.1]
\setmonofont{HackGen}
\setmonojfont{HackGen}

% 版面
\ModifyPageStyle{plain}{
  nombre_font=\small,
  nombre_position=top-fore-edge,
  running_head_font=\small,
  running_head_position=top-center,
  odd_running_head=_section,
  even_running_head=_chapter,
  mark_format={_chapter={第\thechapter 章\quad #1},_section={§\thesection\quad #1}}
}

\NewPageStyle{frontmatter}{
  nombre_font=\small,
  nombre_position=top-fore-edge,
  running_head_font=\small,
  running_head_position=top-center,
  odd_running_head=_chapter,
  even_running_head=_chapter,
  mark_format={_chapter={#1}}
}

\NewPageStyle{appendix}{
  nombre_font=\small,
  nombre_position=top-fore-edge,
  running_head_font=\small,
  running_head_position=top-center,
  odd_running_head=_section,
  even_running_head=_chapter,
  mark_format={_chapter={付録\thechapter\quad #1},_section={§\thesection\quad #1}}
}

\jlreqsetup{
  appendix_heading={chapter={label_format={付録{\bfseries\thechapter}}}},
  backmatter_pagebreak=clearpage,
  caption_font=\small,
  caption_label_font=\gtfamily\bfseries\small,
  frontmatter_pagestyle=frontmatter
}

% 見出し
\RenewBlockHeading{chapter}{0}{
  align=right,
  font={\Large},
  format={\jlreqHeadingLabel{#1\\{\normalsize\vspace{1\zh}}}{\huge\sffamily\gtfamily\bfseries #2}},
  label_format={第{\bfseries\thechapter}章},
  lines=6,
  pagebreak=begin_with_odd_page,
  pagestyle=empty
}

\ModifyHeading{section}{font={\Large\gtfamily\bfseries}}
\ModifyHeading{subsection}{font={\large\gtfamily\bfseries}}

% 目次・補遺
\patchcmd{\tableofcontents}{\@starttoc}{\thispagestyle{empty}\@starttoc}{}{}
\titlecontents{chapter}[0\zw]{\addvspace{1\zh}\gtfamily\bfseries}{\makebox[4\zw][l]{\thecontentslabel}}{}{\hfill\contentspage}
\titlecontents{section}[1\zw]{}{\makebox[3\zw][l]{\thecontentslabel}}{\hspace{3\zw}}{\space\titlerule*[.5\zw]{.}\contentspage}
\titlecontents*{subsection}[4\zw]{\small}{}{}{}[／]

% 索引
\newlength{\midx@columnseprule}
\newlength{\midx@columnsep}
\newlength{\midx@multicolsep}

\renewenvironment{theindex}{%
  \jlreq@oldfontcommand@enable%
  \setlength{\midx@columnseprule}{\columnseprule}%
  \setlength{\midx@columnsep}{\columnsep}%
  \setlength{\midx@multicolsep}{\multicolsep}%
  \setlength{\columnseprule}{.4\p@}%
  \setlength{\columnsep}{2\zw}%
  \setlength{\multicolsep}{\z@}%
  \clearpage%
  \phantomsection%
  \addcontentsline{toc}{chapter}{\indexname}%
  \begin{multicols}{3}[\section*{\indexname}]%
  \@mkboth{\indexname}{\indexname}%
  \jlreq@theindex@pagestyle%
  \small%
  \setlength{\parindent}{\z@}%
  \setlength{\parskip}{\z@ \@plus .03\zh}%
  \DeclareCommandCopy{\item}{\@idxitem}%
}{%
  \end{multicols}%
  \ifx\jlreq@theindex@savedpagestyle\@undefined
  \else
    \expandafter\pagestyle\expandafter{\jlreq@theindex@savedpagestyle}%
  \fi
  \let\jlreq@theindex@savedpagestyle\@undefined%
  \clearpage%
  \jlreq@oldfontcommand@disable%
  \setlength{\columnseprule}{\midx@columnseprule}%
  \setlength{\columnsep}{\midx@columnsep}%
  \setlength{\multicolsep}{\midx@multicolsep}%
}

\newcommand{\seename}{→}
\renewcommand{\@idxitem}{\par\setlength{\hangindent}{1\zw}}
\renewcommand{\subitem}{\@idxitem\hspace*{2\zw}}
\renewcommand{\subsubitem}{\@idxitem\hspace*{3\zw}}

% 数式
\setlength{\predisplaypenalty}{\z@}
\newmuskip\scriptthinmuskip \scriptthinmuskip=.7\thinmuskip

\ExplSyntaxOn
\cs_new:Nn{\sigproc_thinskip:}{
  \mode_if_math:TF{
    \int_compare:nNnTF{\mathstyle}>{\crampedtextstyle}{
      \mskip\scriptthinmuskip
    }{
      \mskip\thinmuskip
    }
  }{
    \kern.16667em
  }
}

\RenewDocumentCommand{\,}{}{\sigproc_thinskip:}
\RenewDocumentCommand{\thinspace}{}{\sigproc_thinskip:}
\ExplSyntaxOff
