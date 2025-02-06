
#  Author: Christoph Sturm
#
#
#  https://github.com/sturc/cloud_computing_big_data
#
#
FROM tomcat:10.1

# Expose port 8080
EXPOSE 8080

ADD ./helloworld /usr/local/tomcat/webapps/helloworld

CMD ["catalina.sh", "run"]