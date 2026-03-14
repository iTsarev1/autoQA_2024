FROM python 3.12

WORKDIR /the/workdir/path

COPY .. /

RUN pip install -r requirements 

CMD pytest tests / --alluredir=allure-result