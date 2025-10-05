FROM python:3
COPY index.html homez/index.html
EXPOSE 8000
CMD python3 -m http.server -d ./homez
# docker build -t chosen_name .    --  to build the image
# docker run -d -p 8000:8000 docker-trial -- for the port mapping! 