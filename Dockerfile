FROM python:3.13
RUN useradd --system --shell /usr/bin/false --home /app --no-create-home j2live 
RUN git clone https://github.com/martydingo/j2live.git app
RUN chown -R j2live:j2live /app
USER j2live
RUN cd /app && python3 -m venv .venv && /app/.venv/bin/pip3 install git+https://github.com/martydingo/j2live
WORKDIR /app
CMD ["/app/.venv/bin/python3", "-m", "j2live"]