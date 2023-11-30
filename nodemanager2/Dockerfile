FROM bde2020/hadoop-base:2.0.0-hadoop3.2.1-java8

MAINTAINER Ivan Ermilov <ivan.s.ermilov@gmail.com>

HEALTHCHECK CMD curl -f http://localhost:8043/ || exit 1

ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 8043

CMD ["/run.sh"]
