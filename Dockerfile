FROM		tensorflow/tensorflow:1.15.2-py3
MAINTAINER	sah0322@naver.com

ENV DEBIAN_FRONTEND=noninteractive

RUN		apt-get -y update && apt-get -y install libsndfile1 libsndfile-dev python3-tk
RUN     ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

RUN		pip install --upgrade pip
RUN		pip install six==1.11.0 \
				matplotlib==2.0.2 \
				scikits.audiolab==0.11.0 \
				scipy==1.1.0 \
				scikit_learn==0.18.1 \
				tabulate==0.7.7 \
				theano==0.9.0 \
				xlwt==1.2.0 \
				librosa==0.5.1 \
				leven

#RUN     pip uninstall -y tensorflow

WORKDIR		/opt/project

ENV PYTHONPATH /usr/local/lib/python3.6/dist-packages:PYTHONPATH
