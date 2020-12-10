FROM node:15.3.0-alpine3.10

WORKDIR /frontend
COPY . /frontend
# RUN chown -R app:app $FRONTEND_CODE_HOME
# ARG API_URL
# ENV REACT_APP_HOST_IP_ADDRESS $API_URL
RUN yarn
RUN yarn build
# USER root