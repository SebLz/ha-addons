ARG BUILD_FROM
FROM $BUILD_FROM

COPY rootfs /
RUN pip3 install -r /requirements.txt && rm requirements.txt && chmod +x run.sh

CMD ["/run.sh"]
# test