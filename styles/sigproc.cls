\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{sigproc}[2022/04/29 sigproc class]

\newif\ifebook
\ebookfalse
\DeclareOption{ebook}{\ebooktrue}
\ProcessOptions

\ifebook\else
\PassOptionsToClass{twoside,gutter=20mm}{jlreq}
\fi

\newcommand{\jlreqkanjiskip}{0pt plus 0.1\zw minus 0.01\zw}
\newcommand{\jlreqxkanjiskip}{0.25em plus 0.15em minus 0.06em}
\LoadClass[disablejfam,book,paper=a5,fontsize=9bp,head_space=20mm,line_length=112mm,number_of_lines=32,headfoot_verticalposition=11bp]{jlreq}

\ifebook\else
\RequirePackage{jlreq-trimmarks}
\fi

\RequirePackage[math-style=ISO,warnings-off={mathtools-colon}]{unicode-math}
\RequirePackage[no-math,match,deluxe,sourcehan-jp,jfm_yoko=jlreq]{luatexja-preset}
\RequirePackage{etoolbox}
\RequirePackage{titletoc}
\RequirePackage{appendix}
\RequirePackage{multicol}

% フォント
\ltjsetparameter{jacharrange={-2,-9},alxspmode={`‐,0}}
\ltjsetparameter{yalbaselineshift=0.03\zh}
\setmathfont{STIX Two Math}[Scale=1.1]
\setmainfont{STIX Two Text}[Ligatures=TeX,Scale=1.1]
\setsansfont{Liberation Sans}[Ligatures=TeX,Scale=1.1]
\setmonofont{HackGen}[Ligatures=TeX]
\setmonojfont{HackGen}

% 版面
\jlreqsetup{
  caption_font=\small,
  caption_label_font=\sffamily\bfseries\small
}

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

\jlreqsetup{
  frontmatter_pagestyle=frontmatter,
  backmatter_pagebreak=clearpage
}

% 目次・補遺
\patchcmd{\tableofcontents}{\@starttoc}{\thispagestyle{empty}\@starttoc}{}{}
\titlecontents{chapter}[0\zw]{\addvspace{1\zh}\sffamily\bfseries}{\makebox[4\zw][l]{\thecontentslabel}}{}{\hfill\contentspage}
\titlecontents{section}[1.5\zw]{}{\makebox[2.5\zw][l]{\thecontentslabel}}{\hspace{2.5\zw}}{\space\titlerule*[0.5\zw]{.}\contentspage}
\titlecontents*{subsection}[4\zw]{\small}{}{}{}[／]
\renewcommand{\appendixname}{補遺}

% 索引
\renewenvironment{theindex}{%
  \jlreq@oldfontcommand@enable%
  \setlength{\columnseprule}{0pt}%
  \setlength{\columnsep}{2\zw}%
  \setlength{\multicolsep}{0pt}%
  \clearpage%
  \phantomsection%
  \addcontentsline{toc}{chapter}{\indexname}%
  \begin{multicols}{3}[\section*{\indexname}]%
  \@mkboth{\indexname}{\indexname}%
  \jlreq@theindex@pagestyle%
  \footnotesize%
  \setlength{\parindent}{0pt}%
  \setlength{\parskip}{0pt plus 0.03\zh}%
  \let\item\@idxitem
}{%
  \end{multicols}%
  \ifx\jlreq@theindex@savedpagestyle\@undefined\else\expandafter\pagestyle\expandafter{\jlreq@theindex@savedpagestyle}\fi%
  \let\jlreq@theindex@savedpagestyle\@undefined%
  \clearpage%
  \jlreq@oldfontcommand@disable%
}

\renewcommand{\@idxitem}{\par\setlength{\hangindent}{3\zw}}
\renewcommand{\subitem}{\@idxitem\hspace*{1\zw}}
\renewcommand{\subsubitem}{\@idxitem\hspace*{2\zw}}

% narrowbaselines
\newif{\ifnbl@narrowbaselines}
\newlength{\nbl@adskip}
\newlength{\nbl@asskip}
\newlength{\nbl@bdskip}
\newlength{\nbl@bsskip}

\newcommand{\narrowbaselines}{%
  \nbl@narrowbaselinestrue%
  \setlength{\nbl@adskip}{\abovedisplayskip}%
  \setlength{\nbl@asskip}{\abovedisplayshortskip}%
  \setlength{\nbl@bdskip}{\belowdisplayskip}%
  \setlength{\nbl@bsskip}{\belowdisplayshortskip}%
  \DeclareCommandCopy{\nbl@nomath}{\@nomath}%
  \RenewCommandCopy{\@nomath}{\@gobble}%
  \@currsize\selectfont%
  \RenewCommandCopy{\@nomath}{\nbl@nomath}%
  \setlength{\abovedisplayskip}{\nbl@adskip}%
  \setlength{\abovedisplayshortskip}{\nbl@asskip}%
  \setlength{\belowdisplayskip}{\nbl@bdskip}%
  \setlength{\belowdisplayshortskip}{\nbl@bsskip}%
}

\everydisplay=\expandafter{\the\everydisplay \narrowbaselines}
\preto{\normalsize}{\ifnbl@narrowbaselines\setlength{\jlreq@baselineskip}{1.2\jlreq@fontsize}\fi}
\preto{\small}{\ifnbl@narrowbaselines\setlength{\jlreq@baselineskip}{1.1\jlreq@fontsize}\fi}
