FROM debian:bullseye-slim AS build
ENV PATH /usr/local/bin/texlive:$PATH
WORKDIR /tmp
RUN apt-get update
RUN apt-get install --yes perl wget xz-utils fontconfig
COPY ./texlive.profile ./
RUN wget --no-verbose https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
RUN tar --extract --gzip --file ./install-tl-unx.tar.gz --strip-components=1
RUN ./install-tl --profile=texlive.profile
RUN ln -sf /usr/local/texlive/*/bin/* /usr/local/bin/texlive
RUN tlmgr install appendix cleveref comment diffcoeff environ light-latex-make subfiles tcolorbox thmtools titlesec

FROM python:3.10-slim-bullseye
ENV PATH /usr/local/bin/texlive:$PATH
ENV PYTHONPATH /python_modules/:$PYTHONPATH
ENV MPLCONFIGDIR /python_modules/
ENV MPLBACKEND pgf
WORKDIR /workdir
RUN apt-get update
RUN apt-get install --yes perl wget xz-utils fontconfig
COPY --from=build /usr/local/texlive /usr/local/texlive
RUN ln -sf /usr/local/texlive/*/bin/* /usr/local/bin/texlive
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./src/Pipfile ./
RUN pipenv install --dev
VOLUME ["/usr/local/texlive/.texlive2022/texmf-var/luatex-cache"]
CMD ["bash"]
