# TeX Live をインストールする
FROM debian:bullseye-slim AS build
ENV PATH=/usr/local/bin/texlive:$PATH
RUN apt-get update
RUN apt-get install --yes fontconfig nkf perl wget xz-utils
WORKDIR /tmp
COPY texlive.profile .
RUN nkf -Lu --overwrite texlive.profile
RUN wget --no-verbose https://texlive.texjp.org/2022/tlnet/install-tl-unx.tar.gz
RUN tar --extract --gzip --file install-tl-unx.tar.gz --strip-components=1
RUN ./install-tl --profile=texlive.profile --repository https://texlive.texjp.org/2022/tlnet
RUN ln -sf /usr/local/texlive/*/bin/* /usr/local/bin/texlive
RUN tlmgr install light-latex-make tikz-cd

# TeX Live を build ステージからコピーする
FROM python:3.10-slim-bullseye
ENV PATH=/usr/local/bin/texlive:$PATH
RUN apt-get update
RUN apt-get install --yes fontconfig perl xz-utils
COPY --from=build /usr/local/texlive /usr/local/texlive
RUN ln -sf /usr/local/texlive/*/bin/* /usr/local/bin/texlive

# LuaTeX のキャッシュを永続化する
RUN mkdir /var/cache/texmf-cache/
RUN chmod 777 /var/cache/texmf-cache/
RUN tlmgr conf texmf TEXMFCACHE /var/cache/texmf-cache/

# 一般ユーザで Python の仮想環境を作る
RUN pip install --upgrade pip
RUN pip install pipenv
RUN useradd --shell /bin/bash --user-group --create-home anon
ENV PATH=/home/anon/.local/bin:$PATH WORKON_HOME=/home/anon/.local/share/virtualenvs
RUN mkdir --parents /home/anon/.local/share/virtualenvs/
RUN chmod 777 /home/anon/.local/share/virtualenvs/
WORKDIR /home/anon/src
ENTRYPOINT ["python", "init.py"]
CMD ["/bin/bash"]
