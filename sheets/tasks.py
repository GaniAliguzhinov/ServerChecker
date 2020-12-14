from __future__ import absolute_import
from query.models import Query
from ServerChecker.celery import app


@app.task
def process(urls):
    """
    Task for processing a lot of queries via multithreading.
    Run with celery.
    """
    # pool = Pool(cpu_count())
    # pool.map(process_query, urls)
    for url in urls:
        process_single(url)


@app.task
def process_single(url):
    query = Query(url=url)
    query.save()
