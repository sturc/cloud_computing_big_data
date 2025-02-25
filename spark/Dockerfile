
#  Author: Christoph Sturm
#
#
#  https://github.com/sturc/cloud_computing_big_data
#
#
FROM csturm/spark-py:v3.5.3

USER 0
COPY requirements.txt /opt/spark/work-dir/requirements.txt
RUN pip3 install -r /opt/spark/work-dir/requirements.txt

ARG spark_uid=185
USER ${spark_uid}

ADD ./exercises /opt/spark/work-dir/exercises
ADD ./data /opt/spark/work-dir/data

