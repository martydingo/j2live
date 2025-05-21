FROM python:3.13
RUN git clone https://github.com/martydingo/j2live.git app
RUN cd /app && pip3 install git+https://github.com/martydingo/j2live
CMD ["python3", "-m", "j2live"]