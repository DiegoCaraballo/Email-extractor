ARG IMAGE

ARG VERSION

FROM $IMAGE:$VERSION

# IMPORTANT: remeber to declare ARG values AFTER FROM sentence....

MAINTAINER info@kedu.coop

ADD requirements.txt .

ADD EmailExtractor.py .

RUN pip install -r requirements.txt
